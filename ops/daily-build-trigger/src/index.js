/**
 * Triggers the "Daily site rebuild" workflow in
 * nickeubank/practicaldatascience_book, because GitHub's own `schedule` event
 * does not run on time. Measured on that repo over 21 consecutive days, a
 * "0 10 * * *" cron fired a median of 5.1 hours late (max 9.1h) and never once
 * within an hour of its slot -- useless for a build that has to beat 7:30am.
 *
 * Cloudflare fires its Cron Triggers on time, so this Worker turns the
 * schedule into something that can actually hold a deadline.
 *
 * Behaviour on each tick (slots are in wrangler.toml):
 *
 *   1. Work out today's date in Durham -- the campus date is what the book's
 *      exercise gating keys off, so it is the only date that matters here.
 *   2. Ask GitHub what that workflow has already done today.
 *   3. Skip if a run already succeeded (the normal case: the 05:10 slot does
 *      the work and the 07:10 one costs a single API call and goes home).
 *      Skip too if one is queued or still running, so attempts never stack.
 *   4. Otherwise dispatch a fresh run.
 *
 * So the second slot is a retry, not a second build: the day's build happens
 * once, and 07:10 only does anything if 05:10 failed or never fired.
 *
 * The dispatch passes force=false, which leaves the workflow's own 7:30am ET
 * gate armed. That gate, not this Worker, is what actually enforces the
 * cutoff -- if Cloudflare were ever badly delayed, the late dispatch gets
 * dropped on GitHub's side rather than pushing into the workday.
 *
 * Secret required:  GITHUB_TOKEN
 *   Fine-grained PAT, repo nickeubank/practicaldatascience_book only,
 *   Actions: Read and write.  Set with:
 *     npx wrangler secret put GITHUB_TOKEN
 */

const OWNER = "nickeubank";
const REPO = "practicaldatascience_book";
const WORKFLOW = "daily_build.yml";
const BRANCH = "main";
const CAMPUS_TZ = "America/New_York";
const UA = "pds-daily-build-trigger";

/** Date in Durham as YYYY-MM-DD. "en-CA" is the trick: it formats ISO-style. */
function campusDate(when = new Date()) {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: CAMPUS_TZ,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(when);
}

function github(path, env, init = {}) {
  return fetch(`https://api.github.com${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": UA,
      ...(init.body ? { "Content-Type": "application/json" } : {}),
    },
  });
}

/**
 * Today's runs, newest first. The `created` filter keeps the response small,
 * which matters: the free plan allows 10ms of CPU per cron invocation, and
 * parsing a full page of run objects is not free. Waiting on the network
 * costs no CPU, but JSON.parse does.
 *
 * `created` filters on the UTC date while we want the Durham date, so the
 * result is re-filtered below. The two only disagree for runs created between
 * midnight and ~05:00 UTC, which is outside every slot in wrangler.toml.
 */
async function runsToday(env, today) {
  const query = `created=${encodeURIComponent(">=" + today)}&per_page=10&exclude_pull_requests=true`;
  const res = await github(
    `/repos/${OWNER}/${REPO}/actions/workflows/${WORKFLOW}/runs?${query}`,
    env,
  );
  if (!res.ok) {
    throw new Error(`listing runs failed: ${res.status} ${await res.text()}`);
  }
  const body = await res.json();
  return (body.workflow_runs || []).filter(
    (run) => campusDate(new Date(run.created_at)) === today,
  );
}

async function dispatch(env) {
  const res = await github(
    `/repos/${OWNER}/${REPO}/actions/workflows/${WORKFLOW}/dispatches`,
    env,
    {
      method: "POST",
      // force=false leaves the workflow's 7:30am ET gate in charge.
      body: JSON.stringify({ ref: BRANCH, inputs: { force: "false" } }),
    },
  );
  // A successful dispatch is 204 No Content.
  if (res.status !== 204) {
    throw new Error(`dispatch failed: ${res.status} ${await res.text()}`);
  }
}

async function tick(env) {
  if (!env.GITHUB_TOKEN) {
    throw new Error("GITHUB_TOKEN secret is not set on this Worker.");
  }

  const today = campusDate();
  const runs = await runsToday(env, today);

  if (runs.some((r) => r.conclusion === "success")) {
    return { date: today, action: "skip", reason: "already built successfully today" };
  }
  if (runs.some((r) => r.status === "queued" || r.status === "in_progress")) {
    return { date: today, action: "skip", reason: "a run is already in flight" };
  }

  await dispatch(env);
  const failed = runs.filter((r) => r.conclusion && r.conclusion !== "success").length;
  return {
    date: today,
    action: "dispatched",
    reason: failed ? `retrying after ${failed} failed attempt(s) today` : "first attempt of the day",
  };
}

export default {
  async scheduled(event, env, ctx) {
    ctx.waitUntil(
      tick(env).then(
        (result) => console.log(JSON.stringify({ cron: event.cron, ...result })),
        // Thrown, not swallowed, so the failure is visible in `wrangler tail`
        // and in the Worker's error rate. The next slot retries anyway.
        (err) => {
          console.error(JSON.stringify({ cron: event.cron, error: String(err) }));
          throw err;
        },
      ),
    );
  },

  /**
   * Read-only status, for eyeballing what the Worker thinks is going on.
   * Deliberately cannot trigger a build: the workers.dev URL is public, and
   * this only ever reports on a repo that is public anyway.
   */
  async fetch(request, env) {
    const today = campusDate();
    try {
      const runs = await runsToday(env, today);
      return Response.json({
        campus_date: today,
        runs_today: runs.map((r) => ({
          started: r.created_at,
          status: r.status,
          conclusion: r.conclusion,
          event: r.event,
          url: r.html_url,
        })),
      });
    } catch (err) {
      return Response.json({ campus_date: today, error: String(err) }, { status: 502 });
    }
  },
};
