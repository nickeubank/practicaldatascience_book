"""Generate the class schedule CSVs that the course .rst pages render.

The Excel workbooks (``ids*_specific/class_schedule_*_xlsx.xlsx``) are the
single source of truth. The ``class_schedule_*.generated.csv`` files beside
them are build artifacts -- do not edit them by hand, your changes will be
overwritten on the next build.

A ``jupyter-book build`` regenerates them automatically (this module is wired
in as a local extension in ``_config.yml``). To regenerate without building::

    python _ext/schedule_tables.py

In-class exercise links are published on the morning of the class they belong
to: a row's exercise cell is emptied until that class date arrives, so the
links are absent from the built HTML rather than merely hidden. The nightly
GitHub Action (``.github/workflows/daily_build.yml``) rebuilds the site so
this happens without you doing anything.

Class dates
-----------
The schedules write dates as ``Tues, Aug 26`` or ``Mon Jan 12`` -- no year --
so the year is inferred from the weekday: ``Aug 26`` is only a Tuesday in
2025, and so on. That inference doubles as a staleness check. If a workbook's
dates resolve to a semester that already ended, it has not been rolled forward
yet, and regenerating it would dump every exercise onto the live site at once.
So the schedule is left alone and the build warns instead.

To roll a schedule forward, update its date column to the new semester's
dates. Nothing else needs to change.

To see a future class day rendered, set ``SCHEDULE_AS_OF=YYYY-MM-DD`` when you
build; see ``AS_OF_ENV`` below.
"""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import os
import re
import sys
from pathlib import Path
from typing import NamedTuple
from zoneinfo import ZoneInfo

import pandas as pd

#: Workbooks are found with this glob, relative to the book root.
WORKBOOK_GLOB = "ids*_specific/class_schedule_*_xlsx.xlsx"

#: Column holding the exercise links that get gated by date.
EXERCISE_COLUMN = "In-Class Exercise"

#: Classes are scheduled in Durham, so "today" is Eastern, not UTC. Without
#: this a build running at 01:00 UTC would publish a day early.
CAMPUS_TZ = ZoneInfo("America/New_York")

#: How long after its last class a schedule stays eligible for regeneration.
#: Past this, the workbook is assumed to be last year's, not this year's.
STALE_AFTER = dt.timedelta(days=45)

#: Set to ``YYYY-MM-DD`` to build the site as if it were that date, so you can
#: look at a future class day rendered. The build has to be told, not just the
#: CLI: this extension regenerates the CSVs at ``builder-inited``, so a build
#: that didn't know the date would overwrite them with today's schedule before
#: Sphinx ever read them. Unset everywhere that matters (the nightly Action),
#: so real builds always use the real today.
AS_OF_ENV = "SCHEDULE_AS_OF"

_WEEKDAYS = {name.lower()[:3]: i for i, name in enumerate(calendar.day_name)}
_MONTHS = {name.lower()[:3]: i for i, name in enumerate(calendar.month_name) if name}


def find_workbooks(root: Path) -> list[Path]:
    return sorted(root.glob(WORKBOOK_GLOB))


def output_path(workbook: Path) -> Path:
    """``class_schedule_540_xlsx.xlsx`` -> ``class_schedule_540.generated.csv``."""
    return workbook.with_name(workbook.stem.removesuffix("_xlsx") + ".generated.csv")


def today_on_campus() -> dt.date:
    return dt.datetime.now(CAMPUS_TZ).date()


def as_of_from_env() -> dt.date | None:
    """The ``SCHEDULE_AS_OF`` override, or None for a normal build."""
    raw = os.environ.get(AS_OF_ENV, "").strip()
    if not raw:
        return None
    try:
        return dt.date.fromisoformat(raw)
    except ValueError:
        raise ValueError(
            f"{AS_OF_ENV}={raw!r} is not a date -- expected YYYY-MM-DD."
        ) from None


# -- Dates -------------------------------------------------------------------


def parse_day(text: str) -> tuple[int, int, int] | None:
    """``"Tues, Oct 14 (Break)"`` -> ``(weekday, month, day)``.

    Returns None for anything that isn't a recognizable class date, which is
    how blank rows and free-text rows ("Final Project Due") opt out.
    """
    cleaned = re.sub(r"\([^)]*\)", " ", str(text)).replace(",", " ")
    tokens = re.findall(r"[A-Za-z]+|\d+", cleaned)

    weekday = month = day = None
    for token in tokens:
        key = token.lower()[:3]
        if token.isdigit():
            if day is None and 1 <= int(token) <= 31:
                day = int(token)
        elif month is None and key in _MONTHS and weekday is not None:
            month = _MONTHS[key]
        elif weekday is None and key in _WEEKDAYS:
            weekday = _WEEKDAYS[key]
        elif month is None and key in _MONTHS:
            month = _MONTHS[key]

    if month is None or day is None:
        return None
    return weekday, month, day


#: Share of weekday names that must match for a candidate year to be believed.
#: Not 100%: a single typo ("Wed Dec 12" on a Friday) shouldn't veto a whole
#: schedule, but a wholesale mismatch means we picked the wrong year.
WEEKDAY_AGREEMENT = 0.8


def resolve_dates(
    date_texts: list[str], today: dt.date
) -> tuple[list[dt.date | None], int, list[int]] | None:
    """Attach a year to a schedule's dates using their weekday names.

    Returns ``(dates, year, mismatched_rows)``, where ``dates`` lines up with
    ``date_texts`` and holds None for rows that aren't class dates, and
    ``mismatched_rows`` flags rows whose weekday disagrees with the resolved
    date -- typos worth fixing. Returns None when no candidate year comes
    close, which usually means a schedule half-edited into a new semester.
    """
    parsed = [parse_day(text) for text in date_texts]
    if not any(parsed):
        return None

    best = None
    for year in range(today.year - 1, today.year + 2):
        dates: list[dt.date | None] = []
        mismatched: list[int] = []
        usable = True

        for position, entry in enumerate(parsed):
            if entry is None:
                dates.append(None)
                continue
            weekday, month, day = entry
            try:
                date = dt.date(year, month, day)
            except ValueError:  # e.g. Feb 29 in a non-leap year
                usable = False
                break
            # A schedule that runs into January belongs to the next year.
            if previous := next((d for d in reversed(dates) if d), None):
                if date < previous:
                    date = dt.date(year + 1, month, day)
            if weekday is not None and date.weekday() != weekday:
                mismatched.append(position)
            dates.append(date)

        if not usable:
            continue
        dated = [d for d in dates if d]
        checkable = sum(1 for entry in parsed if entry and entry[0] is not None)
        if checkable and (checkable - len(mismatched)) / checkable < WEEKDAY_AGREEMENT:
            continue

        # Prefer the best weekday agreement, then the semester nearest today.
        distance = min(abs((d - today).days) for d in dated)
        score = (len(mismatched), distance)
        if best is None or score < best[0]:
            best = (score, dates, year, mismatched)

    return (best[1], best[2], best[3]) if best else None


# -- Building ----------------------------------------------------------------


def read_workbook(workbook: Path) -> pd.DataFrame:
    frame = pd.read_excel(workbook).fillna("")
    frame = frame.map(lambda cell: str(cell).strip() if cell != "" else "")
    # Excel exports often carry a few trailing blank rows.
    return frame[frame.ne("").any(axis=1)].reset_index(drop=True)


def gate_exercises(
    frame: pd.DataFrame, dates: list[dt.date | None], today: dt.date
) -> tuple[pd.DataFrame, int]:
    """Empty the exercise cell of every class that hasn't happened yet."""
    if EXERCISE_COLUMN not in frame.columns:
        return frame, 0

    frame = frame.copy()
    held_back = 0
    current: dt.date | None = None
    for position, date in enumerate(dates):
        # Rows without their own date (continuations) follow the row above.
        current = date or current
        if current is not None and current <= today:
            continue
        if str(frame.at[position, EXERCISE_COLUMN]).strip():
            frame.at[position, EXERCISE_COLUMN] = ""
            held_back += 1
    return frame, held_back


class Plan(NamedTuple):
    """What one schedule would look like if it were rebuilt on a given day."""

    workbook: Path
    csv_path: Path
    frame: pd.DataFrame  # already gated
    dates: list[dt.date | None]
    year: int
    held_back: int

    @property
    def csv_text(self) -> str:
        return self.frame.to_csv(index=False, lineterminator="\n")

    @property
    def is_current(self) -> bool:
        return (
            self.csv_path.exists()
            and self.csv_path.read_text(encoding="utf-8") == self.csv_text
        )


def plan_schedules(root: Path, today: dt.date, warn=print) -> list[Plan]:
    """Work out what every schedule should contain on ``today``.

    Pure: reads workbooks and decides, but writes nothing. ``generate`` writes
    the result; ``preview`` prints it.
    """
    plans = []
    for workbook in find_workbooks(root):
        csv_path = output_path(workbook)
        frame = read_workbook(workbook)

        resolved = resolve_dates(list(frame[frame.columns[0]]), today)
        if resolved is None:
            warn(
                f"{workbook.name}: skipped -- could not read class dates from "
                f"the '{frame.columns[0]}' column, so there is no safe way to "
                f"tell which exercises should be public. {csv_path.name} was "
                f"left as it is."
            )
            continue

        dates, year, mismatched = resolved
        for position in mismatched:
            stated = frame.at[position, frame.columns[0]]
            warn(
                f"{workbook.name}: '{stated}' is a "
                f"{dates[position]:%A} in {year} -- check the date."
            )

        last_class = max(d for d in dates if d)
        if last_class < today - STALE_AFTER:
            warn(
                f"{workbook.name}: skipped -- its dates resolve to a semester "
                f"that ended {last_class:%b %d, %Y}. Roll the date column "
                f"forward to this semester; until then {csv_path.name} is left "
                f"as it is, so no exercises are published early."
            )
            continue

        gated, held_back = gate_exercises(frame, dates, today)
        plans.append(Plan(workbook, csv_path, gated, dates, year, held_back))
    return plans


def generate(root: Path, warn=print, today: dt.date | None = None) -> list[Path]:
    """Regenerate every schedule CSV. Returns the paths actually rewritten."""
    today = today or today_on_campus()
    written = []
    for plan in plan_schedules(root, today, warn):
        if plan.is_current:
            continue  # Unchanged; leave mtime alone so Sphinx skips the page.
        plan.csv_path.write_text(plan.csv_text, encoding="utf-8")
        written.append(plan.csv_path)
        print(
            f"[schedule_tables] {plan.csv_path.name}: {plan.year} schedule, "
            f"{plan.held_back} exercise(s) still held back"
        )
    return written


def preview(root: Path, today: dt.date, warn=print) -> None:
    """Report what a build on ``today`` would publish, without writing."""
    print(f"If the site were built on {today:%A, %B %d, %Y}:\n")
    for plan in plan_schedules(root, today, warn):
        published = (
            pd.read_csv(plan.csv_path).fillna("")
            if plan.csv_path.exists()
            else pd.DataFrame()
        )
        was_live = set()
        if EXERCISE_COLUMN in getattr(published, "columns", []):
            was_live = {
                i
                for i, cell in enumerate(published[EXERCISE_COLUMN])
                if str(cell).strip()
            }

        exercises = plan.frame[EXERCISE_COLUMN]
        live = {i for i, cell in enumerate(exercises) if str(cell).strip()}
        total_available = len(live) + plan.held_back

        upcoming = [d for d in plan.dates if d and d > today]
        next_class = f"{min(upcoming):%a %b %d}" if upcoming else "semester over"

        print(
            f"  {plan.workbook.name}  ({plan.year})\n"
            f"    {len(live)} of {total_available} exercises visible"
            f"  |  next class: {next_class}"
            f"{'' if plan.is_current else '  |  CHANGES the published CSV'}"
        )
        for position in sorted(live - was_live):
            date = plan.dates[position]
            label = f"{date:%a %b %d}" if date else "?"
            text = " ".join(str(exercises.iloc[position]).split())
            print(f"      + {label}: {text[:64]}")
        for position in sorted(was_live - live):
            print(f"      - row {position + 2} would be withdrawn")
    print()


# -- Sphinx plumbing ---------------------------------------------------------


def _on_builder_inited(app):
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    as_of = as_of_from_env()
    if as_of is not None:
        logger.warning(
            f"[schedule_tables] {AS_OF_ENV}={as_of:%Y-%m-%d}: building the "
            f"schedules as if it were that date. The generated CSVs are now a "
            f"schedule from another day -- run `python _ext/schedule_tables.py` "
            f"to restore them before you commit or copy into docs/."
        )
    for path in generate(Path(app.srcdir), warn=logger.warning, today=as_of):
        logger.info(f"[schedule_tables] regenerated {path.name}")


def setup(app):
    app.connect("builder-inited", _on_builder_inited)
    return {
        "version": "2.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Regenerate the class schedule CSVs from the Excel "
        "workbooks, publishing each class's exercises on its class date."
    )
    parser.add_argument(
        "--as-of",
        metavar="YYYY-MM-DD",
        type=dt.date.fromisoformat,
        help="print what a build on this date would publish. Nothing is "
        f"written. To see that date rendered, build with {AS_OF_ENV}=YYYY-MM-DD "
        "set instead",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    problems: list[str] = []

    if args.as_of:
        preview(root, args.as_of, warn=problems.append)
        for message in problems:
            print(f"WARNING: {message}", file=sys.stderr)
        sys.exit(1 if problems else 0)

    written = generate(root, warn=problems.append)

    for path in written:
        print(f"wrote {path.relative_to(root)}")
    for message in problems:
        print(f"WARNING: {message}", file=sys.stderr)
    if not written and not problems:
        print("all schedule CSVs already up to date")
    sys.exit(1 if problems else 0)
