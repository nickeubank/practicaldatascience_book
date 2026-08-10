# Practical Data Science

The files here are hosted at the domain [here](https://nickeubank.github.io/practicaldatascience_book/intro.html).

## Installs

To be able to run (for building — this doesn't cover exercise libraries), install:

```
conda install jupyter-book=1
pip install sphinx_markdown_tables
conda install pandas openpyxl
```

(`pandas` and `openpyxl` are what read the Excel class schedules during the build — see [Class Schedules](#class-schedules).)

(Jupyter-book has a version 2.0, but it's not feature-complete, so this is all still building off jupyter `1.0.4.post1`)

## Organization

This repo is primarily organized around the "notebooks" directory — which is home to all the instructional readings, three `ids[course number]_specific` directories with things like class schedules, and an `exercises` directory with course exercises.

Note that the contents of the exercises directory are just for local hosting — the MASTER version of all exercises is in a private `solutions_and_quizzes` repo. Email me if you need access for some reason.

How notebooks are built into the site is determined by the `_toc.yml` table-of-contents file.

You can complete ignore `_build` — that's where builds of the site land — and `docs`, which is where they need to be copied for github pages to serve up the actual website. But you shouldn't edit anything there yourself.

`_ext` holds local Sphinx extensions that run during the build (currently just the class schedule generator, described below).

## Building Book

- set `cd` to this repo
- run `jupyter-book build .` By default only changed pages. Use `jupyter-book build --all .` to force full build.
- Copy into docs (where github pages looks): `cp -R _build/html/* docs`
- Push to github and it'll update online shortly!
- You can also open `_build/index.html` (just double click!) and it'll open in your browser locally.

The site *also* rebuilds itself every morning via GitHub Actions, to release class exercises on schedule — see [Class Schedules](#class-schedules). That means `main` can pick up commits you didn't make, so `git pull` before editing.

For copy-paste ease:

If you didn't change the table of contents/course organization:

```bash
jupyter-book build .; cp -R _build/html/* docs; git add .; git commit; git push
```

If you changed the table of contents/want a slower but full site build:

```bash
jupyter-book build --all .; cp -R _build/html/* docs; git add .; git commit; git push
```

## Class Schedules

Each `ids[course number]_specific` directory has three schedule files, but **you only ever edit the Excel one**:

- `class_schedule_[num]_xlsx.xlsx` — the master schedule, and the only file you should edit. Excel keeps the formatting and is easy to rearrange by hand.
- `class_schedule_[num].generated.csv` — built from the xlsx. **Do not edit this**, your changes get overwritten on the next build. It's committed so schedule changes show up as readable diffs (the xlsx is binary, so `git diff` on it tells you nothing).
- `class_schedule_[num].rst` — the actual webpage. Everything above the table (office hours, syllabus link, etc.) lives here and is edited by hand; the table itself is just a `csv-table` pointed at the generated CSV.

`jupyter-book build .` regenerates the CSVs before building, so the normal build commands above already do the right thing. To regenerate without building:

```bash
python _ext/schedule_tables.py
```

### Exercises appear on the day of class

You don't reveal exercises by hand. Each row's **In-Class Exercise** cell is emptied in the generated CSV until that class date arrives, so unreleased links aren't in the built HTML at all — not merely hidden with CSS.

A GitHub Action (`.github/workflows/daily_build.yml`) rebuilds the site every morning at 6am ET and pushes to `docs/`, so the day's exercise goes up whether or not you build anything. You can also trigger it by hand from the Actions tab. Note that it commits to `main`, so **`git pull` before you start editing** or your next `jbp` will conflict.

### Testing before a date arrives

`--as-of` builds the schedule as if it were any date you name. It **only prints** — no files are touched — so it's safe to run any time:

```bash
python _ext/schedule_tables.py --as-of 2026-10-06
```

```text
If the site were built on Tuesday, October 06, 2026:

  class_schedule_540_xlsx.xlsx  (2026)
    11 of 22 exercises visible  |  next class: Thu Oct 08  |  CHANGES the published CSV
      + Thu Aug 27: - `Legos <../exercises/10_lego_algorithm.html>`_
      + Tue Sep 01: - Using VS Code - `Max <../exercises/20_max.html>`_ ...
```

Each `+` line is an exercise that would be public on that date. That's usually all you need — to check whether an exercise goes up on the right day, name the day.

If you want to *look at the rendered page* as it will appear on some future date, add `--write` and build:

```bash
python _ext/schedule_tables.py --as-of 2026-10-06 --write
jupyter-book build .          # now open _build/html/... and look at it
python _ext/schedule_tables.py   # IMPORTANT: restores today's schedule
```

Between those commands your working copy holds a schedule from the future, so don't run `jbp` or commit until you've restored it. The last command puts things back (`git checkout ids*_specific/*.generated.csv` also works).

To rehearse the Action itself, trigger it by hand from the Actions tab — on a day when nothing is due to change it should report "Site unchanged today; nothing to commit."

### Class dates and rolling a schedule forward

The schedules write dates as `Tues, Aug 26` or `Mon Jan 12`, with no year, so the year is inferred from the weekday — `Aug 26` only falls on a Tuesday in 2025, and so on. **To roll a schedule forward to a new semester, just update the date column.** Nothing else needs changing.

That inference is also the safety net. If a workbook's dates resolve to a semester that already ended (i.e. you haven't rolled it forward yet), then every class is "in the past" and a naive rebuild would dump the whole semester's exercises onto the live site at once. So the build **skips that schedule entirely** and warns:

```text
WARNING: class_schedule_540_xlsx.xlsx: skipped -- its dates resolve to a
semester that ended Dec 10, 2025. Roll the date column forward ...
```

The published CSV is left exactly as it was, so nothing leaks. Update the dates and the warning stops on its own. The build also warns when a weekday doesn't match its date (`'Wed Dec 12' is a Friday in 2025`), which is a handy typo check when you're building a new schedule.

## Syntax

Jupyter books basically use Markdown + some extra features for things like note boxes, or danger boxes, etc.
[Cheatsheet here](https://jupyterbook.org/en/stable/reference/cheatsheet.html)

Here's footnotes: <https://jupyterbook.org/en/stable/content/content-blocks.html#footnotes>
Notes and warnings: <https://jupyterbook.org/en/stable/content/content-blocks.html#notes-warnings-and-other-admonitions>
