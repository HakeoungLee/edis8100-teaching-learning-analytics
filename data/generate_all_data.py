"""
EDIS 8100: Teaching and Learning Analytics (Fall 2026)
Synthetic data universe generator.

Two fictional settings are generated here:

  1. "EDUC 1010: Learning How to Learn" at Blue Ridge University.
     A simulated 8-week blended undergraduate course with 120 students, an LMS,
     a discussion forum, 24 weekly studio groups of 5, and an adaptive practice tutor.

  2. "FractionQuest", a middle school fractions game with 200 players,
     used in the week 10 game and emotional analytics lab.

Everything is synthetic. No real student was observed, recorded, or scored to
make these files. That is the point: we practice on data that behaves like
student data so that we can rehearse our judgment without surveilling anyone.

Design contract for this module
-------------------------------
* One master seed, 8100. Each dataset function seeds its own generator with
  8100 plus a fixed offset, so any single file can be regenerated on its own
  and will be byte-identical every time.
* make_students() computes every latent trait for the 120 students
  (ability, engagement, srl_skill, procrastination, and friends). Latents are
  returned in the DataFrame but are NOT written to students.csv. They exist so
  that every other dataset can be generated independently and still agree with
  the others about who each student is.
* make_game_players() plays the same role for the FractionQuest universe.
* Every make_* function is independently callable, takes an output directory,
  and writes exactly one CSV.
* Pure numpy and pandas. Nothing else beyond the standard library.

Run it:
    python generate_all_data.py                # writes CSVs next to this file
    python generate_all_data.py --outdir ./out # writes CSVs somewhere else

Then check the planted phenomena:
    python verify_phenomena.py
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Seeds and constants
# ---------------------------------------------------------------------------

SEED = 8100

SEED_STUDENTS = SEED + 0
SEED_CLICKSTREAM = SEED + 1
SEED_GRADEBOOK = SEED + 2
SEED_FORUM = SEED + 3
SEED_GROUP_CHAT = SEED + 4
SEED_MMLA = SEED + 5
SEED_ARTIFACTS = SEED + 6
SEED_SRL = SEED + 7
SEED_GAME_PLAYERS = SEED + 10
SEED_GAME_TELEMETRY = SEED + 11
SEED_GAME_EMOTION = SEED + 12
# Shared helper stream: studio chat volume is drawn once and reused by both
# make_group_chat (which writes the messages) and make_mmla (which counts them),
# so the two files always agree.
SEED_STUDIO_CHAT = SEED + 20

DEFAULT_OUTDIR = Path(__file__).resolve().parent

N_STUDENTS = 120
N_GROUPS = 24
GROUP_SIZE = 5
N_WEEKS = 8
N_PLAYERS = 200
N_LEVELS = 8

# Course clock. Week 1 starts Monday 2026-09-07; week 8 ends Sunday 2026-11-01.
COURSE_START = np.datetime64("2026-09-07T00:00:00")
DAY_S = 86400
# Quiz k is due 23:59 on the Tuesday after week k closes.
QUIZ_DEADLINE_DAY = {k: 7 * k + 1 for k in range(1, N_WEEKS + 1)}
FINAL_PROJECT_DEADLINE_DAY = 64  # Tuesday 2026-11-10

WEEK_TOPICS = {
    1: "memory",
    2: "spacing",
    3: "metacognition",
    4: "motivation",
    5: "collaboration",
    6: "note-taking",
    7: "sleep",
    8: "test anxiety",
}

STUDENT_COLS = [
    "student_id",
    "first_name",
    "last_name",
    "gender",
    "first_gen",
    "multilingual",
    "work_hours_per_week",
    "prior_gpa",
    "major_area",
]

# ---------------------------------------------------------------------------
# Small utilities
# ---------------------------------------------------------------------------


def _outpath(outdir, filename: str) -> Path:
    path = Path(outdir).expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path / filename


def _ts(seconds_from_start) -> np.ndarray:
    """Seconds since COURSE_START to datetime64[s]."""
    secs = np.asarray(seconds_from_start, dtype="float64")
    return COURSE_START + np.round(secs).astype("int64").astype("timedelta64[s]")


def _iso(dt64) -> pd.Series:
    """Format datetime64 values as ISO 8601 strings without fractional seconds."""
    return pd.Series(pd.to_datetime(np.asarray(dt64))).dt.strftime("%Y-%m-%dT%H:%M:%S")


def _z(x) -> np.ndarray:
    x = np.asarray(x, dtype="float64")
    sd = x.std()
    return (x - x.mean()) / (sd if sd > 0 else 1.0)


def _sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.asarray(x, dtype="float64")))


def gini(values) -> float:
    """Gini coefficient of a nonnegative vector. 0 means perfectly equal."""
    v = np.sort(np.asarray(values, dtype="float64"))
    v = np.clip(v, 0, None)
    n = v.size
    total = v.sum()
    if n == 0 or total <= 0:
        return 0.0
    idx = np.arange(1, n + 1)
    return float((2.0 * np.sum(idx * v)) / (n * total) - (n + 1.0) / n)


def _correlated(rng, base: np.ndarray, r: float) -> np.ndarray:
    """A standard normal vector correlated with `base` at approximately r."""
    noise = rng.normal(0, 1, base.size)
    return r * base + np.sqrt(max(0.0, 1.0 - r * r)) * noise


# ---------------------------------------------------------------------------
# Name banks
# ---------------------------------------------------------------------------

FIRST_NAMES_WOMAN = [
    "Aaliyah", "Sofia", "Mei", "Priya", "Emma", "Zara", "Isabella", "Hana",
    "Grace", "Amara", "Leila", "Camila", "Nia", "Yuki", "Ruth", "Elena",
    "Tanvi", "Noor", "Bridget", "Maya", "Ines", "Anika", "Kaia", "Rosa",
    "Delphine", "Simone", "Adaeze", "Lucia", "Hafsa", "Marta", "Thandiwe",
    "Colette", "Fatima", "Beatriz", "Solveig", "Imani",
]
FIRST_NAMES_MAN = [
    "Elijah", "Diego", "Ravi", "Omar", "Noah", "Tobias", "Malik", "Kenji",
    "Andre", "Samuel", "Hugo", "Nikhil", "Ivan", "Caleb", "Mateo", "Youssef",
    "Liam", "Dmitri", "Jonas", "Tariq", "Peter", "Wen", "Ezra", "Rafael",
    "Bilal", "Soren", "Kwame", "Julian", "Arun", "Felix", "Mikael", "Hector",
    "Devon", "Idris", "Lorenzo", "Emeka",
]
FIRST_NAMES_NONBINARY = [
    "Avery", "Rowan", "Quinn", "Sasha", "Jules", "Kai", "Ari", "Reese",
    "Emery", "Noel", "Marlowe", "Sage",
]
LAST_NAMES = [
    "Alvarez", "Nakamura", "Okoro", "Bennett", "Silva", "Petrov", "Haddad",
    "Nguyen", "Kowalski", "O'Neill", "Rahman", "Fitzgerald", "Mbeki", "Larsen",
    "Duarte", "Chowdhury", "Vasquez", "Kim", "Delgado", "Whitfield", "Osei",
    "Ramirez", "Baptiste", "Lindqvist", "Serrano", "Tran", "Abebe", "Moreau",
    "Castillo", "Yamada", "Hollis", "Bright", "Novak", "Iyer", "Sandoval",
    "Keller", "Adeyemi", "Marchetti", "Villanueva", "Sokolov", "Barros",
    "Ferreira", "Nwosu", "Hassan", "Blackwell", "Mendoza", "Park", "Rossi",
    "Grant", "Solano", "Achebe", "Bauer", "Cruz", "Dawson", "Egan", "Farrell",
]

MAJOR_AREAS = [
    "education", "psychology", "data science", "nursing", "engineering", "humanities",
]
MAJOR_PROBS = [0.30, 0.22, 0.12, 0.15, 0.09, 0.12]


# ---------------------------------------------------------------------------
# 1. Students and their latent traits
# ---------------------------------------------------------------------------


def make_students(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Build the 120 students of EDUC 1010 and their latent traits.

    Writes students.csv (the nine documented columns only). The returned frame
    also carries the latent traits that every other generator needs. Latents are
    never written to disk: students in the course are supposed to discover the
    planted structure, not read it off a column.
    """
    rng = np.random.default_rng(SEED_STUDENTS)
    n = N_STUDENTS

    student_id = np.array([f"S{i + 1:03d}" for i in range(n)])

    # Core latent traits.
    ability = rng.normal(0, 1, n)                       # what the assessments track
    engagement = _correlated(rng, ability, 0.20)        # how much they click
    srl_skill = _correlated(rng, ability, 0.35)         # planning, monitoring, reflecting
    procrastination = -0.42 * srl_skill + np.sqrt(1 - 0.42**2) * rng.normal(0, 1, n)
    # Regularity is how many separate days a student touches the course. It helps
    # learning, and it is also the feature the naive at-risk model leans on.
    regularity = 0.35 * engagement + 0.30 * srl_skill + 0.85 * rng.normal(0, 1, n)
    talkativeness = rng.normal(0, 1, n)                 # studio floor time
    chat_propensity = 0.30 * talkativeness + 0.95 * rng.normal(0, 1, n)
    doc_propensity = rng.normal(0, 1, n)
    forum_propensity = 0.30 * engagement + np.sqrt(1 - 0.30**2) * rng.normal(0, 1, n)

    # Demographics.
    gender = rng.choice(["woman", "man", "nonbinary"], size=n, p=[0.61, 0.34, 0.05])
    first_gen = (rng.random(n) < 0.30).astype(int)
    multilingual = (rng.random(n) < 0.24).astype(int)
    major_area = rng.choice(MAJOR_AREAS, size=n, p=MAJOR_PROBS)

    prior_gpa = np.clip(3.16 + 0.42 * ability + rng.normal(0, 0.17, n), 2.0, 4.0)
    prior_gpa = np.round(prior_gpa, 2)

    # Paid work. First generation students in this cohort work more hours, which
    # is what makes the naive at-risk model in week 3 go wrong.
    work_raw = rng.gamma(1.9, 4.3, n) + first_gen * rng.uniform(5.0, 14.0, n)
    work_hours = np.clip(np.round(work_raw), 0, 30).astype(int)

    # P2 group: works 15+ hours, first generation, studies in concentrated bursts.
    burst_worker = ((first_gen == 1) & (work_hours >= 15)).astype(int)

    # P1 group: high ability, low clickstream volume. The "efficient" cluster.
    efficient = np.zeros(n, dtype=int)
    eligible = np.where((ability > 0.28) & (burst_worker == 0))[0]
    efficient[rng.choice(eligible, size=min(18, eligible.size), replace=False)] = 1

    # P6 group: requests hints in rapid bursts instead of working the problem.
    hint_spam = np.zeros(n, dtype=int)
    eligible = np.where(srl_skill < 0.15)[0]
    hint_spam[rng.choice(eligible, size=min(18, eligible.size), replace=False)] = 1

    # Forum structure for P4: three loose clusters plus four bridge builders.
    community = np.tile(np.arange(3), int(np.ceil(n / 3)))[:n]
    rng.shuffle(community)

    silent_forum = (forum_propensity < np.quantile(forum_propensity, 0.18)).astype(int)

    fp_rank = forum_propensity.argsort().argsort() / (n - 1)
    connector = np.zeros(n, dtype=int)
    conn_pool = np.where((fp_rank > 0.45) & (fp_rank < 0.74) & (silent_forum == 0))[0]
    chosen = []
    for comm in [0, 1, 2]:
        opts = [i for i in conn_pool if community[i] == comm]
        if opts:
            chosen.append(int(rng.choice(opts)))
    remaining = [i for i in conn_pool if i not in chosen]
    while len(chosen) < 4 and remaining:
        pick = int(rng.choice(remaining))
        chosen.append(pick)
        remaining.remove(pick)
    connector[np.array(chosen, dtype=int)] = 1

    # Studio groups of five. Multilingual students are dealt round robin so that
    # no group ends up as an artifact of the assignment procedure.
    order = np.lexsort((rng.random(n), -multilingual))
    group_index = np.empty(n, dtype=int)
    group_index[order] = np.arange(n) % N_GROUPS
    group_id = np.array([f"G{g + 1:02d}" for g in group_index])

    # Names. Keep full names unique so student_id is never ambiguous in class.
    first_name = np.empty(n, dtype=object)
    last_name = np.empty(n, dtype=object)
    used = set()
    for i in range(n):
        if gender[i] == "woman":
            bank = FIRST_NAMES_WOMAN
        elif gender[i] == "man":
            bank = FIRST_NAMES_MAN
        else:
            bank = FIRST_NAMES_NONBINARY
        for _ in range(400):
            fn = str(rng.choice(bank))
            ln = str(rng.choice(LAST_NAMES))
            if (fn, ln) not in used:
                break
        used.add((fn, ln))
        first_name[i] = fn
        last_name[i] = ln

    df = pd.DataFrame(
        {
            "student_id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "first_gen": first_gen,
            "multilingual": multilingual,
            "work_hours_per_week": work_hours,
            "prior_gpa": prior_gpa,
            "major_area": major_area,
            # latent traits below this line, never written to CSV
            "ability": ability,
            "engagement": engagement,
            "srl_skill": srl_skill,
            "procrastination": procrastination,
            "regularity": regularity,
            "talkativeness": talkativeness,
            "chat_propensity": chat_propensity,
            "doc_propensity": doc_propensity,
            "forum_propensity": forum_propensity,
            "efficient": efficient,
            "burst_worker": burst_worker,
            "hint_spam": hint_spam,
            "community": community,
            "connector": connector,
            "silent_forum": silent_forum,
            "group_id": group_id,
        }
    )

    if write:
        df[STUDENT_COLS].to_csv(_outpath(outdir, "students.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 2. LMS clickstream
# ---------------------------------------------------------------------------

EVENT_TYPES = [
    "login", "page_view", "video_play", "video_pause",
    "forum_view", "assignment_view", "submit",
]
EVENT_BASE_P = np.array([0.12, 0.32, 0.16, 0.11, 0.13, 0.11, 0.05])


def make_clickstream(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """LMS event log for the eight course weeks.

    Two things vary across students and they are not the same thing. Volume is how
    many events a student generates, and it is heavy tailed. Regularity is how many
    separate days they show up at all. The week also has a rhythm: Monday and
    Tuesday spike ahead of the Tuesday night quiz deadline.

    Two subgroups break the "more clicks means more learning" story. Efficient
    students generate few events and score well (P1). First generation students
    working 15+ hours can only touch the course on a handful of days, so their
    regularity looks terrible even though their learning does not (P2).
    """
    rng = np.random.default_rng(SEED_CLICKSTREAM)
    students = make_students(write=False)
    n = len(students)

    ability = students["ability"].to_numpy()
    engagement = students["engagement"].to_numpy()
    procrast = students["procrastination"].to_numpy()
    regularity_z = _z(students["regularity"].to_numpy())
    efficient = students["efficient"].to_numpy()
    burst = students["burst_worker"].to_numpy()

    # Expected event count per student, lognormal so the tail is heavy.
    log_mu = (
        5.78
        + 0.40 * engagement
        + 0.05 * ability
        + 0.10 * regularity_z
        + np.log(np.where(efficient == 1, 0.30, 1.0))
        + np.log(np.where(burst == 1, 0.95, 1.0))
    )
    n_events = np.clip(
        np.round(np.exp(log_mu + rng.normal(0, 0.18, n))), 25, 4000
    ).astype(int)

    n_days = N_WEEKS * 7
    day_index = np.arange(n_days)
    weekday = (day_index + 0) % 7  # 0 = Monday, because 2026-09-07 is a Monday
    weekday_weight = np.array([1.45, 1.60, 1.10, 1.00, 0.75, 0.60, 1.05])
    weekday_rel = weekday_weight / weekday_weight.mean()
    week_of = day_index // 7
    week_weight = 1.0 - 0.022 * week_of  # attention fades a little across the term
    base_day_w = weekday_weight[weekday] * week_weight

    # Probability that a given student touches the course on a given day.
    p_active = _sigmoid(0.45 + 0.95 * regularity_z)
    # Working 15+ hours compresses the week into a couple of long evenings.
    p_active = np.where(burst == 1, p_active * 0.18, p_active)

    # Submit events crowd into the 48 hours before each Tuesday deadline.
    submit_day_w = np.where(np.isin(weekday, [0, 1]), 5.0, 0.70) * week_weight

    rows_student, rows_day, rows_type = [], [], []
    rows_hour = []

    for i in range(n):
        k = int(n_events[i])
        day_p = np.clip(p_active[i] * weekday_rel[weekday] * week_weight, 0.01, 0.97)
        active = rng.random(n_days) < day_p
        if active.sum() < 4:
            active[rng.choice(n_days, size=4, replace=False)] = True

        w = base_day_w * active * (0.55 + rng.gamma(3.0, 1.0 / 3.0, n_days))
        w = w / w.sum()
        sw = submit_day_w * active
        sw = sw / sw.sum()

        # Per-student taste for videos versus pages versus the forum.
        p_types = rng.dirichlet(EVENT_BASE_P * 55.0)
        types = rng.choice(len(EVENT_TYPES), size=k, p=p_types)

        days = rng.choice(n_days, size=k, p=w)
        is_submit = types == EVENT_TYPES.index("submit")
        if is_submit.any():
            days[is_submit] = rng.choice(n_days, size=int(is_submit.sum()), p=sw)

        # Time of day: three loose study sessions, later for procrastinators.
        centers = rng.choice(
            [9.6, 14.2, 20.8], size=k, p=[0.27, 0.33, 0.40]
        ) + 1.05 * procrast[i] * rng.random(k)
        hours = centers + rng.normal(0, 0.85, k)
        hours = np.clip(hours, 0.02, 23.97)

        rows_student.append(np.full(k, i))
        rows_day.append(days)
        rows_type.append(types)
        rows_hour.append(hours)

    student_idx = np.concatenate(rows_student)
    days = np.concatenate(rows_day)
    types = np.concatenate(rows_type)
    hours = np.concatenate(rows_hour)

    seconds = days * DAY_S + hours * 3600.0
    order = np.argsort(seconds, kind="stable")
    student_idx, days, types, seconds = (
        student_idx[order], days[order], types[order], seconds[order]
    )

    week = (days // 7 + 1).astype(int)
    type_names = np.array(EVENT_TYPES)[types]

    # Plausible resource ids per event type.
    resource = np.empty(seconds.size, dtype=object)
    page_no = rng.integers(1, 9, seconds.size)
    video_no = rng.integers(1, 5, seconds.size)
    thread_no = rng.integers(1, 61, seconds.size)
    for t, name in enumerate(EVENT_TYPES):
        mask = types == t
        if not mask.any():
            continue
        if name == "login":
            resource[mask] = "lms_home"
        elif name == "page_view":
            resource[mask] = [
                f"w{w}_page_{p:02d}" for w, p in zip(week[mask], page_no[mask])
            ]
        elif name in ("video_play", "video_pause"):
            resource[mask] = [
                f"w{w}_video_{v:02d}" for w, v in zip(week[mask], video_no[mask])
            ]
        elif name == "forum_view":
            resource[mask] = [f"thread_{t3:03d}" for t3 in thread_no[mask]]
        else:  # assignment_view and submit both point at the next quiz due
            deadline_days = np.array([QUIZ_DEADLINE_DAY[k] for k in range(1, N_WEEKS + 1)])
            next_quiz = np.clip(
                1 + np.searchsorted(deadline_days, days[mask], side="left"), 1, N_WEEKS
            )
            resource[mask] = [f"quiz_{k}" for k in next_quiz]

    df = pd.DataFrame(
        {
            "event_id": [f"E{i + 1:06d}" for i in range(seconds.size)],
            "student_id": students["student_id"].to_numpy()[student_idx],
            "timestamp": _iso(_ts(seconds)),
            "week": week,
            "event_type": type_names,
            "resource_id": resource,
        }
    )
    if write:
        df.to_csv(_outpath(outdir, "lms_clickstream.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 3. Gradebook
# ---------------------------------------------------------------------------

QUIZ_DIFFICULTY = np.array([2.2, 0.4, -3.1, -0.8, 1.1, -2.4, 0.2, 1.4])


def make_gradebook(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Eight quizzes plus a final project, with submission and deadline stamps.

    Two planted structures live here. Quiz to quiz improvement tracks self
    regulated learning skill and is flattest for the hint spam subgroup (P6,
    completed by srl_traces.csv). Submission timing tracks procrastination, which
    also drags scores down, so last minute submissions score lower (P3). The link
    is correlational by construction: nothing about submitting late causes the
    lower score, which is exactly the inference students should have to argue about.
    """
    rng = np.random.default_rng(SEED_GRADEBOOK)
    students = make_students(write=False)
    n = len(students)

    ability = students["ability"].to_numpy()
    engagement = students["engagement"].to_numpy()
    srl = students["srl_skill"].to_numpy()
    procrast = students["procrastination"].to_numpy()
    hint_spam = students["hint_spam"].to_numpy()
    burst = students["burst_worker"].to_numpy()
    sid = students["student_id"].to_numpy()

    srl_z = _z(srl)
    procrast_z = _z(procrast)
    regularity_z = _z(students["regularity"].to_numpy())

    base = (
        76.0
        + 7.2 * ability
        + 1.9 * srl_z
        + 0.3 * engagement
        + 4.2 * regularity_z
        - 4.1 * procrast_z
        - 0.6 * burst
        + rng.normal(0, 2.0, n)
    )
    # Growth across the term: SRL loops pay off, hint spamming does not.
    slope = 0.68 * srl_z - 0.62 * hint_spam + 0.12 * ability + rng.normal(0, 0.35, n)

    rows = []
    for k in range(1, N_WEEKS + 1):
        raw = (
            base
            + slope * (k - 4.5)
            + QUIZ_DIFFICULTY[k - 1]
            + rng.normal(0, 6.0, n)
        )
        score = np.round(np.clip(raw, 32.0, 100.0), 1)

        deadline_s = QUIZ_DEADLINE_DAY[k] * DAY_S + 23 * 3600 + 59 * 60
        # Hours before the deadline: procrastinators cut it close.
        mu = 3.25 - 1.35 * procrast_z
        hours_before = np.exp(mu + rng.normal(0, 0.85, n))
        # A quiz cannot be submitted before it exists. It opens with its own
        # week, so the earliest possible submission is that week's first moment.
        # Saturating against that window leaves the last minute tail exactly as
        # drawn (1 - exp(-x) is x for small x) and only bends the early tail, so
        # nobody stacks up on the release instant.
        open_s = (k - 1) * 7 * DAY_S
        max_hours = (deadline_s - open_s) / 3600.0
        hours_before = max_hours * (1.0 - np.exp(-hours_before / max_hours))
        hours_before = np.clip(hours_before, 0.03, max_hours)
        # A few submissions land after the bell.
        late = rng.random(n) < (0.02 + 0.035 * _sigmoid(1.4 * procrast_z))
        hours_before = np.where(late, -rng.uniform(0.2, 11.0, n), hours_before)
        submit_s = deadline_s - hours_before * 3600.0

        rows.append(
            pd.DataFrame(
                {
                    "student_id": sid,
                    "assessment": f"quiz_{k}",
                    "score": score,
                    "submitted_at": _iso(_ts(submit_s)),
                    "deadline": _iso(_ts(np.full(n, deadline_s))),
                }
            )
        )

    quizzes = pd.concat(rows, ignore_index=True)

    mean_quiz = quizzes.groupby("student_id")["score"].mean().reindex(sid).to_numpy()
    fp_raw = 0.55 * mean_quiz + 0.45 * (77.0 + 7.0 * ability + 2.0 * srl_z) + rng.normal(0, 4.6, n)
    fp_score = np.round(np.clip(fp_raw, 40.0, 100.0), 1)
    fp_deadline_s = FINAL_PROJECT_DEADLINE_DAY * DAY_S + 23 * 3600 + 59 * 60
    fp_hours = np.clip(np.exp(3.05 - 1.2 * procrast_z + rng.normal(0, 0.8, n)), 0.05, 14 * 24)
    final_project = pd.DataFrame(
        {
            "student_id": sid,
            "assessment": "final_project",
            "score": fp_score,
            "submitted_at": _iso(_ts(fp_deadline_s - fp_hours * 3600.0)),
            "deadline": _iso(_ts(np.full(n, fp_deadline_s))),
        }
    )

    df = pd.concat([quizzes, final_project], ignore_index=True)
    df = df.sort_values(["student_id", "assessment"], kind="stable").reset_index(drop=True)
    if write:
        df.to_csv(_outpath(outdir, "gradebook.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 4. Forum text banks and composer
# ---------------------------------------------------------------------------

TOPIC_BANKS = {
    "memory": {
        "concepts": [
            "retrieval practice", "the forgetting curve", "encoding versus retrieval",
            "chunking", "the testing effect", "elaborative interrogation",
            "cue dependent forgetting", "the difference between recall and recognition",
        ],
        "claims": [
            "recognizing material is not the same as being able to recall it",
            "retrieval practice does more for me than rereading ever did",
            "the effort that feels unproductive is often the effort that works",
            "working memory limits explain why cramming feels productive and then fails",
            "expert memory is mostly organized knowledge rather than raw capacity",
            "how we encode something decides what cues will bring it back later",
        ],
        "practices": [
            "closing the book and writing down everything I could recall",
            "drawing the diagram from memory before checking my notes",
            "quizzing myself on the vocabulary instead of highlighting it",
            "explaining the model out loud to my roommate",
            "starting each session with five minutes of blank page recall",
            "turning the section headings into questions and answering them",
        ],
        "outcomes": [
            "the gaps in my understanding showed up immediately",
            "I was surprised by how much I had already lost",
            "it took longer but it stuck for the whole week",
            "I could rebuild the structure but not the specific numbers",
            "my confidence dropped and my actual scores went up",
            "the second attempt was noticeably easier than the first",
        ],
        "contexts": [
            "my anatomy course", "a statistics class I took last year",
            "the certification exam I am studying for", "my seminar readings",
            "an intro chemistry sequence", "the language class I am taking",
        ],
        "qualifiers": [
            "most of the studies used word lists rather than course material",
            "the effect might be smaller when the material is genuinely new to you",
            "students who already know the content have less to retrieve",
            "the discomfort makes it hard to keep doing on a busy week",
            "we never see how long the advantage lasts past a semester",
            "the classroom studies had far messier results than the lab ones",
        ],
        "questions": [
            "Does anyone else find retrieval practice uncomfortable at first?",
            "How do you use recall for conceptual material rather than definitions?",
            "Has anyone tried this with a partner instead of alone?",
            "Is there a point where self testing starts giving you false confidence?",
            "What do you do when you cannot recall anything at all?",
            "Would this work the same way for skills rather than facts?",
        ],
    },
    "spacing": {
        "concepts": [
            "distributed practice", "the spacing effect", "interleaving",
            "massed practice", "review scheduling", "desirable difficulty",
            "the lag effect", "retention interval",
        ],
        "claims": [
            "spacing wins even when total study time is held constant",
            "cramming buys performance today and borrows it from next month",
            "interleaving feels worse during practice and better on the test",
            "the optimal gap depends on how long you need to hold the material",
            "our sense of how well we are learning is a poor guide to scheduling",
            "spacing is less about willpower and more about calendar design",
        ],
        "practices": [
            "spreading my review over four short sessions instead of one long one",
            "mixing problem types in a single set instead of blocking them",
            "scheduling a ten minute review the morning after each lecture",
            "putting review blocks in my calendar the way I schedule classes",
            "revisiting week one material during week four",
            "keeping a running list of topics due for another pass",
        ],
        "outcomes": [
            "the material felt less familiar each time and I retained more",
            "my week stopped ending in panic",
            "the fourth pass took almost no time at all",
            "I noticed which topics kept slipping and could target them",
            "it felt inefficient and the quiz said otherwise",
            "I stopped rereading things I already knew cold",
        ],
        "contexts": [
            "a summer course that moved very fast", "my licensure exam prep",
            "the two courses I am taking back to back", "a research methods class",
            "my part time job schedule", "a course with weekly quizzes",
        ],
        "qualifiers": [
            "spacing assumes you have control over your own schedule",
            "students working long hours cannot always choose their gaps",
            "the studies rarely say what to do when the exam is in three days",
            "interleaving needs enough material to interleave in the first place",
            "the recommended gaps in the literature vary quite a lot",
            "it is hard to separate spacing from simply studying more often",
        ],
        "questions": [
            "How far apart do your review sessions actually end up being?",
            "Does interleaving still help when the problem types look identical?",
            "What do you do when the schedule collapses in a heavy week?",
            "Has anyone found a way to make spacing feel less pointless early on?",
            "Do you space by topic or by course?",
            "Is there a version of this that works for writing rather than problem sets?",
        ],
    },
    "metacognition": {
        "concepts": [
            "judgments of learning", "calibration", "monitoring and control",
            "the illusion of fluency", "self explanation", "planning and reflection",
            "overconfidence in familiar material", "the study plan nobody follows",
        ],
        "claims": [
            "we are confident about exactly the things we have not learned",
            "monitoring is worthless if it never changes what you do next",
            "fluency during reading gets mistaken for knowing the material",
            "asking why after each paragraph changes what you notice",
            "good learners are not smarter so much as better calibrated",
            "reflection has to be specific enough to point at a next action",
        ],
        "practices": [
            "predicting my quiz score before submitting and checking it after",
            "writing one sentence about what confused me at the end of each session",
            "rating my confidence on each problem before looking at the answer",
            "asking myself why a step works before moving on",
            "keeping a short log of what I planned and what I actually did",
            "stopping every ten minutes to summarize without looking",
        ],
        "outcomes": [
            "my predictions were about eight points too generous every time",
            "the reflection took two minutes and changed my next session",
            "I found out I was confident and wrong in the same places",
            "the log made my avoidance patterns embarrassingly visible",
            "I started catching confusion earlier instead of at the exam",
            "my confidence ratings slowly became more accurate",
        ],
        "contexts": [
            "a course where I had no background", "my thesis writing",
            "a coding class", "the statistics unit", "an online module",
            "a lab section with weekly reports",
        ],
        "qualifiers": [
            "self report is exactly the measure we are trying to improve",
            "reflection prompts get gamed once students know they are graded",
            "calibration studies usually use short retention intervals",
            "some of this may just be conscientiousness under another name",
            "it is unclear how much of this transfers across subjects",
            "the effect could be a byproduct of spending more time overall",
        ],
        "questions": [
            "How accurate are your own predictions of your performance?",
            "Does reflection help if nobody ever reads it?",
            "What is the smallest monitoring habit that has worked for you?",
            "Can a dashboard support calibration or does it replace it?",
            "How do you tell useful confusion from unproductive confusion?",
            "Should reflection be graded at all?",
        ],
    },
    "motivation": {
        "concepts": [
            "expectancy value theory", "self efficacy", "mastery goals",
            "autonomy support", "interest development", "cost appraisals",
            "attribution after a bad grade", "the difference between interest and utility",
        ],
        "claims": [
            "cost is the part of the motivation equation we ignore most",
            "self efficacy is built from experience and not from encouragement",
            "performance goals help until the first bad grade arrives",
            "interest can be developed and is not only something you arrive with",
            "autonomy matters more when the task is genuinely difficult",
            "telling a student to try harder tells them nothing about how",
        ],
        "practices": [
            "writing down why the unit connects to work I actually care about",
            "breaking the assignment into pieces small enough to start",
            "tracking my wins for a week instead of my failures",
            "choosing the paper topic myself instead of taking the default",
            "asking my instructor what a strong answer looks like",
            "starting with the part of the problem set I can already do",
        ],
        "outcomes": [
            "the assignment stopped feeling like one giant block",
            "I noticed how much of my avoidance was about cost and not interest",
            "my first draft finally happened",
            "the connection was thin but it was enough to start",
            "I felt more in control even though the work was the same",
            "the small wins mattered more than I expected",
        ],
        "contexts": [
            "a required course outside my field", "an early morning section",
            "a class where I felt behind from week one", "my capstone project",
            "a course with only two grades all semester", "the online section",
        ],
        "qualifiers": [
            "motivation research often measures intentions rather than behavior",
            "structural constraints get relabeled as motivation problems",
            "a student working thirty hours a week is not lacking grit",
            "the interventions that work in one course often fail in another",
            "self report measures are collected right after the intervention",
            "we rarely see what happens to motivation a year later",
        ],
        "questions": [
            "Where do you see cost showing up in your own courses?",
            "Can an analytics dashboard support motivation without shaming anyone?",
            "How do you rebuild self efficacy after a bad exam?",
            "What does autonomy support look like in a large lecture?",
            "Is interest something a course can actually design for?",
            "Do mastery goals survive contact with a curve?",
        ],
    },
    "collaboration": {
        "concepts": [
            "transactive discussion", "group regulation", "productive friction",
            "free riding", "role assignment", "shared mental models",
            "socially shared regulation", "who gets listened to in a group",
        ],
        "claims": [
            "groups get smarter when disagreement is about ideas and not people",
            "equal talk time is not the same thing as equal contribution",
            "the group that plans first usually finishes with less rework",
            "roles help until they become an excuse to stop listening",
            "one dominant voice can hide four people who understood more",
            "building on someone else's idea is a skill that has to be taught",
        ],
        "practices": [
            "starting our session with two minutes of silent individual writing",
            "assigning a rotating facilitator each week",
            "restating the previous person's point before adding mine",
            "putting our disagreements in the shared doc instead of resolving them fast",
            "asking the quietest person for their read before we decided",
            "leaving the first ten minutes for planning rather than drafting",
        ],
        "outcomes": [
            "our artifact was better and the session felt slower",
            "two people who had said nothing turned out to have the key objection",
            "we stopped redoing each other's work",
            "the conversation got sharper once we wrote first",
            "we finished early and the quality did not suffer",
            "the disagreement turned out to be about definitions",
        ],
        "contexts": [
            "our studio group", "a lab team of four", "a semester long design project",
            "a class where groups were assigned randomly", "an online group",
            "a group where two of us knew each other already",
        ],
        "qualifiers": [
            "talk time is easy to measure and easy to overinterpret",
            "quiet does not mean disengaged in every culture or every group",
            "our data cannot see who did the thinking between sessions",
            "group grades hide enormous variation inside the group",
            "the same group behaves differently on a task they care about",
            "a single session is a very thin slice of a collaboration",
        ],
        "questions": [
            "How would you measure contribution without privileging talk?",
            "What should a collaboration dashboard refuse to show the group?",
            "Has role assignment ever backfired in your experience?",
            "How do you surface a quiet objection without putting someone on the spot?",
            "Is productive friction something you can design for?",
            "What counts as an idea unit if the idea arrives in three fragments?",
        ],
    },
    "note-taking": {
        "concepts": [
            "generative note-taking", "verbatim transcription", "the encoding function",
            "the storage function", "concept mapping", "revision passes",
            "selectivity while listening", "what notes are actually for",
        ],
        "claims": [
            "notes that are complete are often notes that were never processed",
            "the encoding benefit happens while you write and not while you read",
            "reviewing notes without transforming them does very little",
            "handwriting helps mainly because it forces you to be selective",
            "the best notes are the ones you rewrite badly and then fix",
            "note structure should mirror the structure of the argument",
        ],
        "practices": [
            "leaving a wide margin for questions I write after class",
            "rewriting my lecture notes as a concept map that evening",
            "limiting myself to one page per lecture on purpose",
            "writing a three sentence summary at the bottom of each page",
            "coding my notes for claims, evidence, and open questions",
            "comparing my notes with a classmate the next day",
        ],
        "outcomes": [
            "my notes got shorter and much more useful",
            "the summary was where I discovered what I had missed",
            "I stopped transcribing and started listening",
            "the map showed two ideas I had recorded as unrelated",
            "the margin questions became my study guide",
            "our two versions disagreed in an informative way",
        ],
        "contexts": [
            "a fast lecture course", "a seminar with dense readings",
            "a class where slides were posted afterward", "my methods course",
            "a course taught mostly through examples", "an online asynchronous class",
        ],
        "qualifiers": [
            "the laptop versus longhand studies have not replicated cleanly",
            "the right strategy depends on whether slides are available",
            "students with accommodations may need transcription and that is fine",
            "note quality is hard to score reliably",
            "most studies look at one lecture rather than a semester",
            "we cannot see what students do with notes after the study ends",
        ],
        "questions": [
            "What does your revision pass actually look like?",
            "Does concept mapping help you or slow you down?",
            "How do you take notes on a reading that is already well organized?",
            "Do posted slides change what you should write?",
            "Has anyone found a note system that survives a heavy week?",
            "Should we teach note-taking explicitly in first year courses?",
        ],
    },
    "sleep": {
        "concepts": [
            "memory consolidation", "sleep debt", "circadian timing",
            "slow wave sleep", "social jetlag", "attention lapses",
            "the tradeoff between one more hour and one more cycle", "sleep as a study strategy",
        ],
        "claims": [
            "the last two hours of studying are often worth less than the sleep they cost",
            "consolidation is part of learning and not a break from it",
            "sleep debt shows up as attention lapses long before it feels like fatigue",
            "an early class schedule fights the circadian rhythm of most undergraduates",
            "napping helps but does not repay a week of short nights",
            "we treat sleep as a lifestyle choice when it is a study strategy",
        ],
        "practices": [
            "moving my last study block an hour earlier for two weeks",
            "putting my phone across the room after eleven",
            "protecting seven hours on the nights before quizzes",
            "reviewing the hardest material right before sleeping",
            "keeping a fixed wake time even on weekends",
            "trading my late night session for an early morning one",
        ],
        "outcomes": [
            "my afternoon focus improved more than my evening focus did",
            "I lost an hour of studying and gained a much better quiz",
            "the first week was rough and the second was clearly better",
            "I stopped rereading the same paragraph four times",
            "my weekend recovery sleep stopped wrecking Monday",
            "the difference was smaller than I hoped but it was real",
        ],
        "contexts": [
            "a semester with two early classes", "my night shift job",
            "finals week", "a course with Tuesday deadlines",
            "the weeks I was commuting", "a stretch when I had a newborn at home",
        ],
        "qualifiers": [
            "sleep advice assumes a schedule that many students do not control",
            "the correlational studies cannot separate sleep from stress",
            "self reported sleep is not very accurate",
            "caregiving and shift work make fixed schedules impossible",
            "the lab studies use young adults with no other obligations",
            "telling a working student to sleep more can land as a judgment",
        ],
        "questions": [
            "How do you protect sleep in a week with three deadlines?",
            "Has anyone actually shifted their schedule and kept it?",
            "Should a learning analytics system ever collect sleep data?",
            "What would you do with sleep data if you had it?",
            "Is the tradeoff different for problem sets versus writing?",
            "How do you talk about sleep without moralizing about it?",
        ],
    },
    "test anxiety": {
        "concepts": [
            "worry versus emotionality", "working memory load", "stereotype threat",
            "expressive writing", "reappraisal", "practice testing under pressure",
            "what a single high stakes exam measures", "arousal as information",
        ],
        "claims": [
            "anxiety consumes the working memory the test is trying to measure",
            "the worry component predicts performance more than the physical symptoms",
            "reappraising arousal as readiness changes performance without changing the feeling",
            "low stakes practice testing lowers the stakes of the real thing",
            "test anxiety is partly a signal about how the assessment is designed",
            "students who feel underprepared and students who are underprepared are different groups",
        ],
        "practices": [
            "writing about my worries for ten minutes before the exam",
            "taking a full practice test under timed conditions",
            "reframing my racing heart as my body getting ready",
            "arriving early enough to stop rushing",
            "starting with the question I know I can answer",
            "planning what I would do if I blanked on the first page",
        ],
        "outcomes": [
            "the writing did not calm me down but my score went up",
            "the practice test was awful and the real one was manageable",
            "I stopped spiraling after the first hard question",
            "my hands still shook and I finished the exam",
            "the plan mattered more than the calm",
            "it helped less than I hoped but it did help",
        ],
        "contexts": [
            "a high stakes licensure exam", "my first graduate statistics midterm",
            "a course where one exam was sixty percent of the grade",
            "an oral exam", "a timed coding assessment", "the final in my methods course",
        ],
        "qualifiers": [
            "some of these interventions were tested only in single sessions",
            "the effects are much smaller outside psychology labs",
            "an anxious student in a badly designed assessment is responding rationally",
            "we should probably fix the assessment before fixing the student",
            "expressive writing has had mixed replication results",
            "anxiety measures are collected right after a stressful event",
        ],
        "questions": [
            "Where does test anxiety come from in the courses you have taught?",
            "Would more frequent low stakes quizzes help or add pressure?",
            "Has reappraisal worked for anyone here?",
            "How should an early warning system talk to an anxious student?",
            "Is anxiety a student problem or an assessment design problem?",
            "What would you change about the assessment itself?",
        ],
    },
}

OPENERS_ROOT = [
    "I have been thinking about {concept} since the reading.",
    "This week's material on {concept} landed differently than I expected.",
    "I want to open a thread on {concept}.",
    "Something about {concept} has been nagging at me all week.",
    "I came into this week fairly skeptical about {concept}.",
    "The section on {concept} was the part I understood least.",
    "Quick question for the group about {concept}.",
    "Reading about {concept} made me rethink how I study.",
    "I keep circling back to the discussion of {concept}.",
]

OPENERS_REPLY = [
    "I agree with the earlier point about {concept}, but I want to push on one piece.",
    "This thread is helping me see {concept} more clearly.",
    "Building on the post above, I think {concept} is doing a lot of work here.",
    "I read that section on {concept} differently.",
    "Adding a small counterexample to what has been said about {concept}.",
    "Yes to all of this, and I want to add one thing about {concept}.",
    "I am not sure I follow the argument about {concept} yet.",
    "Coming back to an earlier comment on {concept}.",
    "This framing of {concept} lines up with my own experience.",
    "I had the opposite reaction to the claim about {concept}.",
    "Thank you for naming what bothered me about {concept}.",
    "I want to sit with the point about {concept} for a second.",
    "Two people above have said something useful about {concept}.",
    "I will take the other side on {concept}, mostly to see what happens.",
]

CLAIM_FRAMES = [
    "My takeaway is that {claim}.",
    "The reading argues that {claim}, and I think that is right.",
    "What seems clear to me is that {claim}.",
    "I keep coming back to the idea that {claim}.",
    "If I followed the chapter, {claim}.",
    "The part that convinced me is that {claim}.",
    "I would say {claim}, at least for the kind of material we work with.",
    "It looks like {claim}, though the evidence is not airtight.",
    "The strongest version of the argument is that {claim}.",
    "What I did not expect was the claim that {claim}.",
    "The authors seem to be saying that {claim}.",
    "Stated plainly, {claim}.",
]

EVIDENCE_FRAMES = [
    "Last week I tried {practice}, and {outcome}.",
    "When I started {practice}, {outcome}.",
    "I tested this on myself by {practice}, and {outcome}.",
    "In {context} I have been {practice}, and {outcome}.",
    "I gave {practice} an honest try, and {outcome}.",
    "The first time I tried {practice} it felt slow, but {outcome}.",
    "During {context} I ended up {practice}, and {outcome}.",
    "I spent two weeks {practice}, and {outcome}.",
    "Something similar happened in {context} when I was {practice}, since {outcome}.",
]

QUALIFIER_FRAMES = [
    "That said, {qualifier}.",
    "The caveat for me is that {qualifier}.",
    "One limit worth naming is that {qualifier}.",
    "I am holding this loosely, because {qualifier}.",
    "It is worth remembering that {qualifier}.",
    "Where I get stuck is that {qualifier}.",
    "I would want to know more before generalizing, since {qualifier}.",
    "My hesitation is that {qualifier}.",
    "This is probably context dependent, given that {qualifier}.",
]

GENERIC_QUESTION_FRAMES = [
    "How would you explain {concept} to a first year student?",
    "Where does {concept} break down in your experience?",
    "Would you design a course around {concept}?",
    "What would change your mind about {concept}?",
    "How would you even measure {concept} in a real classroom?",
    "Does {concept} look different in an online course?",
    "Who benefits when we take {concept} seriously, and who does not?",
    "What would you want to see before you trusted {concept}?",
]

POSITIVE_TAILS = [
    "Honestly, this was the most useful reading of the semester so far.",
    "I appreciated how concrete the examples were.",
    "This one actually changed something about my week, which is rare.",
    "Great thread, everyone.",
    "I am excited to try this in my own teaching.",
    "This clarified something I had been confused about for years.",
    "I liked that the authors admitted what they could not explain.",
    "This is the first reading that felt written for practitioners.",
    "Really glad this was assigned.",
    "I have already sent this one to a colleague.",
    "The examples were the best part for me.",
    "I finished this feeling more hopeful than I expected.",
    "Thanks to whoever picked this reading.",
    "This gave me language for something I had only felt.",
]
NEGATIVE_TAILS = [
    "I found this reading frustrating and a little discouraging.",
    "I am struggling to see how any of this survives a real classroom.",
    "This felt disconnected from the students I actually work with.",
    "I am worried we are asking students to fix a system problem.",
    "I left this reading more confused than when I started.",
    "The tone bothered me, even if the findings hold up.",
    "I wanted the authors to say what they would actually do on Monday.",
    "The sample felt too narrow for the size of the claim.",
    "This one wore me out, to be honest.",
    "I kept waiting for the part about resources and it never came.",
    "I am skeptical, and I am open to being talked out of it.",
    "The writing made a simple idea feel complicated.",
    "This landed as advice for students who already have time.",
    "I finished this a little annoyed, which may be my own week talking.",
]


def _compose_post(rng, topic: str, is_reply: bool) -> str:
    bank = TOPIC_BANKS[topic]
    parts = []

    def a_question() -> str:
        if rng.random() < 0.45:
            return str(rng.choice(GENERIC_QUESTION_FRAMES)).format(
                concept=str(rng.choice(bank["concepts"]))
            )
        return str(rng.choice(bank["questions"]))

    opener_bank = OPENERS_REPLY if is_reply else OPENERS_ROOT
    if is_reply or rng.random() < 0.85:
        parts.append(str(rng.choice(opener_bank)).format(concept=str(rng.choice(bank["concepts"]))))

    parts.append(str(rng.choice(CLAIM_FRAMES)).format(claim=str(rng.choice(bank["claims"]))))

    if rng.random() < 0.62:
        parts.append(
            str(rng.choice(EVIDENCE_FRAMES)).format(
                practice=str(rng.choice(bank["practices"])),
                outcome=str(rng.choice(bank["outcomes"])),
                context=str(rng.choice(bank["contexts"])),
            )
        )
    if rng.random() < 0.48:
        parts.append(
            str(rng.choice(QUALIFIER_FRAMES)).format(qualifier=str(rng.choice(bank["qualifiers"])))
        )
    if rng.random() < 0.55:
        parts.append(a_question())

    tail_roll = rng.random()
    if tail_roll < 0.13:
        parts.append(str(rng.choice(POSITIVE_TAILS)))
    elif tail_roll < 0.22:
        parts.append(str(rng.choice(NEGATIVE_TAILS)))

    if len(parts) < 2:
        parts.append(a_question())
    return " ".join(parts[:6])


# ---------------------------------------------------------------------------
# 5. Forum posts
# ---------------------------------------------------------------------------


def make_forum(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Threaded discussion forum, one topic per course week.

    The reply structure is the point (P4). Students belong to one of three loose
    conversational clusters and almost always reply inside their own cluster.
    Four students reply across clusters far more often. Those four end up with
    high betweenness and only middling degree, which is exactly the pattern the
    week 8 network lab asks students to find and interpret.
    """
    rng = np.random.default_rng(SEED_FORUM)
    students = make_students(write=False)
    n = len(students)

    sid = students["student_id"].to_numpy()
    community = students["community"].to_numpy()
    connector = students["connector"].to_numpy()
    silent = students["silent_forum"].to_numpy()
    fprop = students["forum_propensity"].to_numpy()

    # Posting propensity. Silent students are close to invisible on the forum,
    # which is the missingness students will have to reckon with.
    weight = np.exp(0.72 * fprop)
    weight = np.where(silent == 1, weight * 0.05, weight)
    # Connectors post a steady, unremarkable two replies a week. Their influence
    # comes from who they answer, not from how loud they are.
    weight = np.where(connector == 1, 0.0, weight)
    weight = weight / weight.sum()

    cross_p = np.where(connector == 1, 0.90, 0.010)

    conn_idx = np.where(connector == 1)[0]
    # Each connector keeps up a friendship with a few people in the other two
    # clusters. Those repeated ties are the bridges the whole network runs on.
    bridge_partners = {}
    for c in conn_idx:
        pool = np.where((community != community[c]) & (silent == 0) & (connector == 0))[0]
        bridge_partners[int(c)] = set(int(x) for x in rng.choice(pool, size=3, replace=False))

    posts = []
    thread_counter = 0
    post_counter = 0

    for week in range(1, N_WEEKS + 1):
        topic = WEEK_TOPICS[week]
        n_posts = int(rng.integers(165, 205))
        n_threads = int(rng.integers(6, 10))

        week_posts = []  # (post_id, thread_id, author_idx, seconds)
        week_start_s = (week - 1) * 7 * DAY_S

        reply_authors = [int(c) for c in conn_idx for _ in range(2)]
        n_replies = n_posts - n_threads
        reply_authors += list(
            rng.choice(n, size=max(0, n_replies - len(reply_authors)), p=weight)
        )
        rng.shuffle(reply_authors)

        for t in range(n_threads):
            author = int(rng.choice(n, p=weight))
            thread_counter += 1
            post_counter += 1
            thread_id = f"TH{thread_counter:03d}"
            post_id = f"F{post_counter:04d}"
            day = float(rng.uniform(0.2, 2.6))
            hour = float(np.clip(rng.normal(15.0, 3.2), 7.5, 23.5))
            secs = week_start_s + day * DAY_S + hour * 3600.0
            posts.append(
                {
                    "post_id": post_id,
                    "thread_id": thread_id,
                    "parent_post_id": "",
                    "student_id": sid[author],
                    "week": week,
                    "_secs": secs,
                    "text": _compose_post(rng, topic, is_reply=False),
                }
            )
            week_posts.append((post_id, thread_id, author, secs))

        for author in reply_authors:
            same_comm = rng.random() >= cross_p[author]
            candidates = [
                p for p in week_posts
                if p[2] != author
                and ((community[p[2]] == community[author]) == same_comm)
            ]
            if not candidates:
                candidates = [p for p in week_posts if p[2] != author]
            if not candidates:
                continue
            # Prefer recent posts, which produces plausible thread growth.
            ages = np.array([week_posts[-1][3] - c[3] for c in candidates])
            w = np.exp(-ages / (1.6 * DAY_S)) + 0.08
            if author in bridge_partners and not same_comm:
                boost = np.array(
                    [40.0 if c[2] in bridge_partners[author] else 1.0 for c in candidates]
                )
                w = w * boost
            else:
                # Connectors spend their time answering other people rather than
                # collecting answers, so fewer replies land on their posts.
                w = w * np.array([0.30 if connector[c[2]] == 1 else 1.0 for c in candidates])
            w = w / w.sum()
            parent = candidates[int(rng.choice(len(candidates), p=w))]

            post_counter += 1
            post_id = f"F{post_counter:04d}"
            gap = float(rng.gamma(1.6, 5.5)) * 3600.0
            # Keep the thread inside its own week without letting late replies
            # pile up on the closing instant. Saturating the gap against the
            # room that is left leaves short gaps untouched (1 - exp(-x) is x
            # for small x) and squeezes only the long tail, so a reply always
            # lands strictly after the post it answers.
            room = week_start_s + 6.9 * DAY_S - parent[3]
            if room > 1.0:
                gap = room * (1.0 - float(np.exp(-gap / room)))
                # 1 - exp(-x) saturates to exactly 1.0 in float64, so hold a
                # second back to keep room for whoever replies next.
                gap = min(gap, room - 1.0)
            else:
                gap = 1.0
            secs = parent[3] + gap
            hour_of_day = (secs % DAY_S) / 3600.0
            if hour_of_day < 7.0:
                secs += (8.0 - hour_of_day) * 3600.0
            posts.append(
                {
                    "post_id": post_id,
                    "thread_id": parent[1],
                    "parent_post_id": parent[0],
                    "student_id": sid[author],
                    "week": week,
                    "_secs": secs,
                    "text": _compose_post(rng, topic, is_reply=True),
                }
            )
            week_posts.append((post_id, parent[1], author, secs))

    # Timestamps are written to whole seconds, so a very short gap could still
    # round a reply onto its parent. Walk the posts in creation order (a parent
    # is always created before its replies) and push any collision one second
    # out. The nudge is at most a second per post, well inside the week.
    at_secs = {}
    for p in posts:
        p["_secs"] = float(np.round(p["_secs"]))
        parent_id = p["parent_post_id"]
        if parent_id:
            p["_secs"] = max(p["_secs"], at_secs[parent_id] + 1.0)
        at_secs[p["post_id"]] = p["_secs"]

    df = pd.DataFrame(posts)
    df["timestamp"] = _iso(_ts(df["_secs"].to_numpy()))
    df = df[["post_id", "thread_id", "parent_post_id", "student_id", "week", "timestamp", "text"]]
    if write:
        df.to_csv(_outpath(outdir, "forum_posts.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 6. Studio chat volume (shared between group_chat and mmla)
# ---------------------------------------------------------------------------


def _studio_chat_counts(students: pd.DataFrame):
    """Messages and substantive idea units per student per studio session.

    Drawn once from a dedicated stream so that group_chat.csv and mmla_studio.csv
    tell the same story about who typed what. Multilingual students send at least
    as many messages and a higher share of substantive ones, which is half of P5.
    """
    rng = np.random.default_rng(SEED_STUDIO_CHAT)
    n = len(students)
    chat_prop = _z(students["chat_propensity"].to_numpy())
    multilingual = students["multilingual"].to_numpy()
    ability = students["ability"].to_numpy()

    lam = np.exp(1.72 + 0.38 * chat_prop + 0.19 * multilingual)
    p_sub = np.clip(0.34 + 0.055 * multilingual + 0.05 * ability, 0.10, 0.85)

    n_msgs = np.zeros((n, N_WEEKS), dtype=int)
    n_sub = np.zeros((n, N_WEEKS), dtype=int)
    for s in range(N_WEEKS):
        session_factor = float(rng.uniform(0.82, 1.22))
        msgs = rng.poisson(lam * session_factor)
        n_msgs[:, s] = msgs
        n_sub[:, s] = rng.binomial(msgs, p_sub)
    return n_msgs, n_sub


# ---------------------------------------------------------------------------
# 7. Group chat
# ---------------------------------------------------------------------------

# Chat is generated compositionally: a lead, a template with slots, and sometimes
# a trailing tag. Chat register on purpose (lowercase, clipped), so that week 5 can
# contrast it against the longer and more formal forum posts.
CHAT_LEADS = ["", "", "", "ok ", "alright ", "so ", "hey ", "wait ", "yeah ", "hmm ", "right ", "oh "]
CHAT_TAGS = [
    "", "", "", "", "?", " right", " does that track", " if that works for everyone",
    " what do you think", " or am i off", " lol", " sorry if that is obvious",
]
CHAT_PARTS = [
    "part 1", "part 2", "part 3", "the intro", "the summary", "the second question",
    "the examples", "the last section", "the wrap up", "the definitions", "the counterargument",
]
CHAT_THINGS = [
    "the rubric", "the prompt", "the reading", "the doc link", "the slide", "our notes",
    "the question", "the example", "the table", "the handout", "the transcript",
]
CHAT_VERBS = ["start", "open", "share", "set up", "clean up", "reorganize"]
CHAT_NUMS = ["two", "three", "four", "five", "ten", "fifteen", "twenty"]

CHAT_COORDINATION = [
    "{lead}who is taking notes today{tag}",
    "{lead}i can {verb} the doc{tag}",
    "{lead}i'll take {part}{tag}",
    "{lead}can someone paste {thing}{tag}",
    "{lead}we have {num} minutes left{tag}",
    "{lead}let's split this {num} ways{tag}",
    "{lead}i'm adding {thing} to the doc{tag}",
    "{lead}who wants to present back{tag}",
    "{lead}should we outline first{tag}",
    "{lead}let's timebox this to {num} minutes{tag}",
    "{lead}i'll write up {part}{tag}",
    "{lead}moving {thing} into the doc now{tag}",
    "{lead}does everyone have {thing} open{tag}",
    "{lead}i can present if nobody else wants to{tag}",
    "{lead}putting {thing} at the top of the doc{tag}",
    "{lead}can we come back to {part} in a sec{tag}",
    "{lead}i lost {thing} again sorry{tag}",
    "{lead}sharing my screen now{tag}",
    "{lead}let's each take {num} minutes to write first{tag}",
    "{lead}someone should own {part}{tag}",
]
CHAT_SOCIAL = [
    "{lead}good point{tag}", "{lead}yes exactly{tag}", "{lead}that makes sense{tag}",
    "{lead}agreed{tag}", "{lead}oh interesting{tag}", "{lead}really{tag}",
    "{lead}that is a great way to put it{tag}", "{lead}same here honestly{tag}",
    "{lead}you two are on a roll{tag}", "{lead}my wifi dropped sorry{tag}",
    "{lead}i'm back{tag}", "{lead}thanks for waiting{tag}", "{lead}this is fun actually{tag}",
    "{lead}i'm following now{tag}", "{lead}no worries{tag}", "{lead}brb one sec{tag}",
    "{lead}that made me laugh{tag}", "{lead}i'm convinced{tag}",
    "{lead}hi all{tag}", "{lead}running two minutes late{tag}",
    "{lead}nice{tag}", "{lead}fair enough{tag}", "{lead}love that{tag}",
]
CHAT_CLARIFY = [
    "{lead}which {thing} are we on{tag}",
    "{lead}can you say more about that{tag}",
    "{lead}sorry can you repeat that{tag}",
    "{lead}i'm not sure i follow{tag}",
    "{lead}can you give an example{tag}",
    "{lead}do you mean {thing} or the other one{tag}",
    "{lead}hold on let me reread {thing}{tag}",
    "{lead}what does that term mean again{tag}",
    "{lead}are we answering question {num} or the next one{tag}",
    "{lead}is that the same as what we said before{tag}",
    "{lead}i missed that last bit{tag}",
    "{lead}where is that in {thing}{tag}",
]
CHAT_HEDGES = [
    "", "", "", "i think ", "maybe ", "honestly ", "so ", "not sure, but ",
    "from the reading, ", "for the doc, ", "my read is ", "counterpoint, ",
]
CHAT_SUBSTANTIVE = {
    "memory": [
        "i think recall beats rereading for us because the exam is all application",
        "the forgetting curve thing only worked for me when i spaced it out",
        "recognizing it in the notes is not the same as producing it",
        "our example should be the blank page recall one",
        "chunking is basically why the experts in the study looked faster",
        "maybe we say encoding decides which cues work later",
        "the testing effect showed up even in the ungraded condition which is the interesting part",
        "cues matter as much as effort when you are trying to bring something back",
        "we could open with the difference between recognizing and producing",
    ],
    "spacing": [
        "four short sessions beat one long one even at equal time",
        "interleaving felt terrible and my scores went up",
        "cramming is borrowing from next month",
        "we should say the optimal gap depends on the retention interval",
        "our counterexample is the student who cannot control their schedule",
        "the calendar is the intervention honestly",
        "blocked practice makes you feel fluent and that is the trap",
        "the lag effect is the part i did not know before this week",
        "how long you need to remember it should set the gap",
    ],
    "metacognition": [
        "my confidence ratings were about eight points too high every time",
        "monitoring only matters if it changes the next action",
        "the illusion of fluency is the whole problem with rereading",
        "we could ask students to predict their score before submitting",
        "reflection has to point at something you will actually do",
        "calibration is the word we want in the summary",
        "self report is the measure and also the thing we are trying to fix",
        "overconfidence is worst on the material that feels familiar",
        "a study plan nobody follows is not a plan",
    ],
    "motivation": [
        "cost is the piece everyone skips in expectancy value",
        "self efficacy comes from mastery experiences not pep talks",
        "a student working thirty hours is not lacking grit",
        "we should distinguish interest you arrive with from interest you develop",
        "performance goals hold up until the first bad grade",
        "autonomy matters most when the task is hard",
        "our design should let students pick the topic",
        "attribution after a bad grade is where self efficacy gets decided",
        "utility value and interest are not the same thing",
    ],
    "collaboration": [
        "equal talk time is not equal contribution",
        "we should write silently first then discuss",
        "the quietest person had the key objection last week",
        "transactive means building on the previous turn not just adding",
        "roles help until people stop listening outside their role",
        "our dashboard should not rank individuals in the group",
        "group grades hide huge variation inside the group",
        "socially shared regulation is the term for what our group does badly",
        "who gets listened to is a design question not a personality one",
    ],
    "note-taking": [
        "complete notes usually mean unprocessed notes",
        "the encoding benefit happens while you write",
        "the margin questions became my whole study guide",
        "one page per lecture forced me to choose",
        "the concept map showed two ideas i had kept separate",
        "we should recommend a revision pass not just a format",
        "if slides are posted the note strategy should change",
        "selectivity while listening is the actual skill",
        "we should ask what the notes are for before we recommend a format",
    ],
    "sleep": [
        "the last two hours of studying cost more than they return",
        "consolidation is part of learning not a break from it",
        "attention lapses show up before you feel tired",
        "we should be careful about collecting sleep data at all",
        "fixed wake time helped me more than total hours did",
        "an eight am class fights most undergrad circadian rhythms",
        "sleep advice assumes a schedule many students do not control",
        "one more hour of studying versus one more sleep cycle is the real tradeoff",
        "framing sleep as a study strategy landed better with my students",
    ],
    "test anxiety": [
        "worry eats the working memory the test is measuring",
        "reappraisal did not calm me down but it helped my score",
        "low stakes practice testing lowers the stakes of the real one",
        "maybe the assessment design is the problem not the student",
        "the worry component predicts scores better than the physical symptoms",
        "we should say frequent low stakes quizzes carefully",
        "an early warning email to an anxious student could backfire",
        "one high stakes exam measures composure as much as knowledge",
        "treating arousal as information is the reappraisal move",
    ],
}


def _compose_chat(rng, topic: str, kind: str) -> str:
    """One short chat message. Slots keep the register natural without repeating."""
    lead = str(rng.choice(CHAT_LEADS))
    tag = str(rng.choice(CHAT_TAGS))
    if kind == "substantive":
        body = str(rng.choice(CHAT_SUBSTANTIVE[topic]))
        hedge = str(rng.choice(CHAT_HEDGES))
        return (lead + hedge + body + tag).strip()

    roll = rng.random()
    if roll < 0.42:
        template = str(rng.choice(CHAT_COORDINATION))
    elif roll < 0.76:
        template = str(rng.choice(CHAT_SOCIAL))
    else:
        template = str(rng.choice(CHAT_CLARIFY))
    if roll >= 0.42 and roll < 0.76 and rng.random() < 0.65:
        tag = ""  # short reactions rarely carry a trailing tag
    return template.format(
        lead=lead,
        tag=tag,
        part=str(rng.choice(CHAT_PARTS)),
        thing=str(rng.choice(CHAT_THINGS)),
        verb=str(rng.choice(CHAT_VERBS)),
        num=str(rng.choice(CHAT_NUMS)),
    ).strip()


def make_group_chat(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Backchannel chat from the eight weekly studio sessions.

    Short chat register on purpose, so week 5 can contrast it with the longer,
    more formal forum posts. Message counts match mmla_studio.csv exactly.
    """
    rng = np.random.default_rng(SEED_GROUP_CHAT)
    students = make_students(write=False)
    n_msgs, n_sub = _studio_chat_counts(students)

    sid = students["student_id"].to_numpy()
    gid = students["group_id"].to_numpy()

    rows = []
    counter = 0
    for s in range(N_WEEKS):
        week = s + 1
        topic = WEEK_TOPICS[week]
        # Studio meets Thursday of each course week, 4:00 to 5:30 PM.
        session_start_s = ((week - 1) * 7 + 3) * DAY_S + 16 * 3600
        for i in range(len(students)):
            total = int(n_msgs[i, s])
            if total == 0:
                continue
            subs = int(n_sub[i, s])
            kinds = ["substantive"] * subs + ["other"] * (total - subs)
            rng.shuffle(kinds)
            offsets = np.sort(rng.uniform(60, 88 * 60, total))
            for kind, off in zip(kinds, offsets):
                text = _compose_chat(rng, topic, kind)
                counter += 1
                rows.append(
                    {
                        "group_id": gid[i],
                        "session_id": f"studio_{week}",
                        "student_id": sid[i],
                        "_secs": session_start_s + float(off),
                        "text": text,
                    }
                )

    df = pd.DataFrame(rows).sort_values("_secs", kind="stable").reset_index(drop=True)
    df["message_id"] = [f"M{i + 1:05d}" for i in range(len(df))]
    df["timestamp"] = _iso(_ts(df["_secs"].to_numpy()))
    df = df[["message_id", "group_id", "session_id", "student_id", "timestamp", "text"]]
    if write:
        df.to_csv(_outpath(outdir, "group_chat.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 8. Multimodal studio traces
# ---------------------------------------------------------------------------


def make_mmla(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """One row per student per studio session, across five modalities.

    P5 lives here: multilingual students hold the floor less, and contribute at
    least as much through chat, idea units, and document edits. Anyone who reads
    only speaking_time_s will misdescribe them.

    P9 also starts here: groups differ in how evenly speaking time is spread, and
    studio_artifacts.csv scores the products those groups made.
    """
    rng = np.random.default_rng(SEED_MMLA)
    students = make_students(write=False)
    n_msgs, n_sub = _studio_chat_counts(students)

    sid = students["student_id"].to_numpy()
    gid = students["group_id"].to_numpy()
    talk = students["talkativeness"].to_numpy()
    multilingual = students["multilingual"].to_numpy()
    doc_prop = _z(students["doc_propensity"].to_numpy())

    group_names = [f"G{g + 1:02d}" for g in range(N_GROUPS)]
    members = {g: np.where(gid == g)[0] for g in group_names}

    # How evenly the floor is shared in each group. Low alpha means one or two
    # people dominate every session.
    group_alpha = np.exp(rng.normal(1.30, 0.62, N_GROUPS))
    group_alpha = np.clip(group_alpha, 0.8, 14.0)

    rows = []
    for s in range(N_WEEKS):
        session_id = f"studio_{s + 1}"
        for g_i, g in enumerate(group_names):
            idx = members[g]
            w = np.exp(0.55 * talk[idx] - 0.26 * multilingual[idx])
            alpha = group_alpha[g_i] * w / w.mean()
            shares = rng.dirichlet(np.clip(alpha, 0.15, None))

            total_speech = float(rng.normal(3050, 260))
            total_turns = int(rng.integers(150, 260))

            # Even a student who barely speaks says something, so nobody is a flat zero.
            speaking = np.round(np.maximum(shares * total_speech, rng.uniform(3, 22, len(idx))), 1)
            turns = np.maximum(1, rng.poisson(np.clip(shares * total_turns, 0.7, None)))
            avg_turn = np.round(speaking / turns, 1)
            interruptions = rng.poisson(np.clip(0.6 + 9.0 * shares, 0.05, None))
            gaze_peer = np.clip(
                rng.normal(38 + 26 * (shares - 0.2) + 3.0 * multilingual[idx], 6.0), 8, 72
            )
            gaze_material = np.clip(rng.normal(74 - gaze_peer * 0.55, 7.0), 10, 70)
            over = np.maximum(0.0, gaze_peer + gaze_material - 94.0)
            gaze_material = gaze_material - over
            gestures = rng.poisson(np.clip(5 + 42 * shares, 0.5, None))
            doc_edits = rng.poisson(
                np.clip(3.4 + 2.4 * doc_prop[idx] + 1.2 * multilingual[idx], 0.4, None)
            )

            for j, i in enumerate(idx):
                rows.append(
                    {
                        "session_id": session_id,
                        "group_id": g,
                        "student_id": sid[i],
                        "speaking_time_s": float(speaking[j]),
                        "num_turns": int(turns[j]),
                        "interruptions": int(interruptions[j]),
                        "avg_turn_length_s": float(avg_turn[j]),
                        "gaze_peer_pct": round(float(gaze_peer[j]), 1),
                        "gaze_material_pct": round(float(gaze_material[j]), 1),
                        "gesture_count": int(gestures[j]),
                        "chat_messages": int(n_msgs[i, s]),
                        "doc_edits": int(doc_edits[j]),
                        "idea_units_chat": int(n_sub[i, s]),
                    }
                )

    df = pd.DataFrame(rows)
    df = df.sort_values(["session_id", "group_id", "student_id"], kind="stable").reset_index(drop=True)
    if write:
        df.to_csv(_outpath(outdir, "mmla_studio.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 9. Studio artifacts
# ---------------------------------------------------------------------------


def make_studio_artifacts(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Rubric score, 1 to 10, for the product each group made in each session.

    P9: groups whose speaking time is spread evenly (low Gini) produce better
    rated artifacts than groups where one or two voices dominate. Group ability
    and the amount of substantive chat also matter, so the relationship is real
    but never clean.
    """
    rng = np.random.default_rng(SEED_ARTIFACTS)
    students = make_students(write=False)
    mmla = make_mmla(write=False)

    group_ability = (
        students.assign(a=students["ability"]).groupby("group_id")["a"].mean().to_dict()
    )

    grouped = mmla.groupby(["group_id", "session_id"])
    rows = []
    for (g, s), sub in grouped:
        g_ini = gini(sub["speaking_time_s"].to_numpy())
        idea = float(sub["idea_units_chat"].sum())
        rows.append({"group_id": g, "session_id": s, "gini": g_ini, "idea": idea, "ga": group_ability[g]})

    frame = pd.DataFrame(rows)
    idea_z = _z(frame["idea"].to_numpy())
    gini_c = frame["gini"].to_numpy() - frame["gini"].mean()

    raw = (
        6.5
        - 5.0 * gini_c
        + 0.62 * frame["ga"].to_numpy()
        + 0.42 * idea_z
        + rng.normal(0, 1.15, len(frame))
    )
    frame["artifact_score"] = np.round(np.clip(raw, 1.0, 10.0), 1)

    df = frame[["group_id", "session_id", "artifact_score"]].copy()
    df["_k"] = df["session_id"].str.replace("studio_", "", regex=False).astype(int)
    df = df.sort_values(["_k", "group_id"], kind="stable").drop(columns="_k").reset_index(drop=True)
    if write:
        df.to_csv(_outpath(outdir, "studio_artifacts.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 10. Adaptive tutor SRL traces
# ---------------------------------------------------------------------------


def make_srl(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Action level traces from the adaptive practice tutor.

    P6 lives here. Students high in srl_skill open a session with set_goal, often
    view_plan, and close it with reflect. Those complete loops are the behavioral
    marker that lines up with the quiz to quiz growth in gradebook.csv. A hint
    spam subgroup fires request_hint several times within a few seconds and gains
    the least across the term.
    """
    rng = np.random.default_rng(SEED_SRL)
    students = make_students(write=False)
    n = len(students)

    sid = students["student_id"].to_numpy()
    ability = students["ability"].to_numpy()
    srl_z = _z(students["srl_skill"].to_numpy())
    engagement = students["engagement"].to_numpy()
    hint_spam = students["hint_spam"].to_numpy()

    p_goal = _sigmoid(1.55 * srl_z + 0.15 - 1.1 * hint_spam)
    p_reflect = _sigmoid(1.60 * srl_z - 0.10 - 1.3 * hint_spam)
    p_attend = np.clip(0.86 + 0.07 * engagement, 0.55, 0.99)

    rows = []
    counter = 0
    for week in range(1, N_WEEKS + 1):
        session_id = f"tutor_{week}"
        # Tutor work happens Wednesday through Monday before the Tuesday deadline.
        base_day = (week - 1) * 7 + 2
        for i in range(n):
            if rng.random() > p_attend[i]:
                continue
            day_off = float(rng.uniform(0, 5.4))
            hour = float(np.clip(rng.normal(19.0, 3.0), 7.0, 23.4))
            t = (base_day + day_off) * DAY_S + hour * 3600.0

            def emit(action, item_id="", correct="NA"):
                nonlocal counter, t
                counter += 1
                rows.append(
                    {
                        "trace_id": f"T{counter:05d}",
                        "student_id": sid[i],
                        "session_id": session_id,
                        "_secs": t,
                        "action": action,
                        "item_id": item_id,
                        "correct": correct,
                    }
                )

            opened_goal = rng.random() < p_goal[i]
            if opened_goal:
                emit("set_goal")
                t += float(rng.uniform(8, 40))
                if rng.random() < 0.62 + 0.15 * srl_z[i]:
                    emit("view_plan")
                    t += float(rng.uniform(10, 55))

            n_items = int(rng.integers(4, 10))
            for j in range(1, n_items + 1):
                item_id = f"w{week}_item_{j:02d}"
                difficulty = float(rng.uniform(-0.4, 1.1))
                solved = False
                for attempt in range(1, 4):
                    if hint_spam[i] == 1 and rng.random() < 0.68:
                        # Rapid fire hint requests, seconds apart.
                        for _ in range(int(rng.integers(3, 8))):
                            emit("request_hint", item_id)
                            t += float(rng.uniform(1.5, 6.0))
                    elif rng.random() < _sigmoid(0.7 * difficulty - 0.5 * ability[i] - 0.4):
                        emit("request_hint", item_id)
                        t += float(rng.uniform(12, 60))

                    p_correct = _sigmoid(1.25 * ability[i] - 1.5 * difficulty + 0.55 * (attempt - 1) + 0.35)
                    correct = int(rng.random() < p_correct)
                    emit("attempt", item_id, str(correct))
                    t += float(rng.uniform(15, 95))

                    if rng.random() < 0.72:
                        emit("check_answer", item_id, str(correct))
                        t += float(rng.uniform(4, 22))
                    if correct == 0 and rng.random() < 0.55 + 0.2 * srl_z[i]:
                        emit("review_feedback", item_id)
                        t += float(rng.uniform(10, 70))
                    if correct == 1:
                        solved = True
                        break
                if not solved and rng.random() < 0.3:
                    emit("review_feedback", item_id)
                    t += float(rng.uniform(10, 50))

            if rng.random() < p_reflect[i]:
                emit("reflect")

    df = pd.DataFrame(rows)
    df["timestamp"] = _iso(_ts(df["_secs"].to_numpy()))
    df = df[["trace_id", "student_id", "session_id", "timestamp", "action", "item_id", "correct"]]
    if write:
        df.to_csv(_outpath(outdir, "srl_traces.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 11. FractionQuest players
# ---------------------------------------------------------------------------

GAME_START = np.datetime64("2026-10-05T08:00:00")

PROFILES = ["fast_finisher", "productive_struggler", "disengaged", "steady"]
PROFILE_P = [0.24, 0.34, 0.20, 0.22]


def make_game_players(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """The 200 FractionQuest players, with pre and post fractions assessments.

    Latent play profiles are set here so that telemetry and emotion pings can be
    generated independently and still describe the same 200 children.

    P7: productive strugglers, who make moderate early errors and keep retrying,
    gain the most from pre to post, more than the error free fast finishers who
    were already near the top of the scale.
    """
    rng = np.random.default_rng(SEED_GAME_PLAYERS)
    n = N_PLAYERS

    player_id = np.array([f"P{i + 1:03d}" for i in range(n)])
    grade_level = rng.choice([6, 7], size=n, p=[0.5, 0.5])
    profile = rng.choice(PROFILES, size=n, p=PROFILE_P)

    ability = rng.normal(0, 1, n)
    persistence = rng.normal(0, 1, n)
    ability += np.select(
        [profile == "fast_finisher", profile == "productive_struggler",
         profile == "disengaged", profile == "steady"],
        [0.85, 0.00, -0.45, 0.20],
    )
    persistence += np.select(
        [profile == "fast_finisher", profile == "productive_struggler",
         profile == "disengaged", profile == "steady"],
        [0.25, 1.05, -1.15, 0.25],
    )
    ability = ability * 0.85
    error_tendency = np.select(
        [profile == "fast_finisher", profile == "productive_struggler",
         profile == "disengaged", profile == "steady"],
        [-0.70, 0.35, 0.55, -0.15],
    ) + rng.normal(0, 0.35, n)

    confusion_resolves = (rng.random(n) < _sigmoid(0.95 * persistence + 0.35 * ability + 0.15)).astype(int)

    pre_score = np.clip(np.round(10.0 + 3.1 * ability + rng.normal(0, 1.9, n)), 0, 20).astype(int)

    gain_base = np.select(
        [profile == "fast_finisher", profile == "productive_struggler",
         profile == "disengaged", profile == "steady"],
        [2.55, 3.75, 1.45, 2.85],
    )
    gain = (
        gain_base
        - 0.24 * (pre_score - 10.0)          # ceiling: less room at the top
        + 1.05 * confusion_resolves
        + 0.30 * persistence
        + rng.normal(0, 2.25, n)
    )
    post_score = np.clip(np.round(pre_score + gain), 0, 20).astype(int)

    df = pd.DataFrame(
        {
            "player_id": player_id,
            "grade_level": grade_level,
            "pre_score": pre_score,
            "post_score": post_score,
            # latent traits, not written to CSV
            "profile": profile,
            "ability": ability,
            "persistence": persistence,
            "error_tendency": error_tendency,
            "confusion_resolves": confusion_resolves,
        }
    )
    if write:
        df[["player_id", "grade_level", "pre_score", "post_score"]].to_csv(
            _outpath(outdir, "game_players.csv"), index=False
        )
    return df


# ---------------------------------------------------------------------------
# 12. FractionQuest telemetry
# ---------------------------------------------------------------------------

# Level 4 introduces unlike denominators. It is a cliff on purpose.
LEVEL_DIFFICULTY = np.array([0.28, 0.40, 0.52, 1.02, 0.60, 0.70, 0.80, 0.90])


def make_game_telemetry(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """Attempt level telemetry for the eight FractionQuest levels.

    P7 continues here: errors, attempts, and time all spike at level 4, and the
    players who keep retrying through it are the ones who gain the most.
    Players who run out of patience simply stop appearing in the log, which is
    the kind of missingness a game analyst has to notice on their own.
    """
    rng = np.random.default_rng(SEED_GAME_TELEMETRY)
    players = make_game_players(write=False)

    rows = []
    for _, p in players.iterrows():
        ability = float(p["ability"])
        persistence = float(p["persistence"])
        err_t = float(p["error_tendency"])
        resolves = int(p["confusion_resolves"])
        fast = p["profile"] == "fast_finisher"

        t = (
            GAME_START
            + np.timedelta64(int(rng.integers(0, 9)), "D")
            + np.timedelta64(int(rng.integers(0, 7 * 3600)), "s")
        )
        for level in range(1, N_LEVELS + 1):
            diff = float(LEVEL_DIFFICULTY[level - 1])
            patience = 1 + rng.poisson(max(0.30, 1.70 + 1.20 * persistence + 0.6 * diff))
            patience = int(np.clip(patience, 1, 8))
            completed_level = False

            for attempt in range(1, patience + 1):
                p_success = _sigmoid(
                    1.40 * ability - 3.00 * (diff - 0.30) + 0.60 * (attempt - 1) + 1.55
                )
                success = rng.random() < p_success
                err_lam = np.clip(
                    0.7 + 5.2 * diff * (1.0 - 0.28 * ability) + 0.9 * err_t - 0.55 * (attempt - 1),
                    0.15, None,
                )
                errors = int(rng.poisson(err_lam))
                if success:
                    errors = int(max(0, errors - rng.integers(0, 2)))
                hints = int(rng.poisson(np.clip(
                    0.35 + 1.9 * diff * (1.0 - 0.3 * ability) - (0.55 if fast else 0.0), 0.05, None
                )))
                time_s = float(np.round(np.exp(
                    3.55 + 0.85 * diff - 0.18 * ability + 0.045 * errors
                    - (0.28 if fast else 0.0) + rng.normal(0, 0.32)
                ), 1))

                rows.append(
                    {
                        "player_id": p["player_id"],
                        "grade_level": int(p["grade_level"]),
                        "level": level,
                        "attempt": attempt,
                        "time_s": time_s,
                        "errors": errors,
                        "hints_used": hints,
                        "completed": int(success),
                        "_ts": t,
                    }
                )
                t = t + np.timedelta64(int(time_s) + int(rng.integers(20, 200)), "s")
                if success:
                    completed_level = True
                    break

            if not completed_level:
                break  # ran out of patience and stopped playing

            # Between levels, some players simply do not come back.
            p_quit = _sigmoid(
                -3.20 - 0.85 * persistence + 1.15 * float(LEVEL_DIFFICULTY[min(level, N_LEVELS - 1)])
                - 0.70 * resolves
            )
            if level < N_LEVELS and rng.random() < p_quit:
                break
            if rng.random() < 0.45:
                t = t + np.timedelta64(int(rng.integers(6, 40)) * 3600, "s")

    df = pd.DataFrame(rows)
    df["timestamp"] = _iso(df["_ts"].to_numpy())
    df = df[["player_id", "grade_level", "level", "attempt", "time_s", "errors",
             "hints_used", "completed", "timestamp"]]
    if write:
        df.to_csv(_outpath(outdir, "game_telemetry.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# 13. FractionQuest emotion pings
# ---------------------------------------------------------------------------

EMOTIONS = ["interest", "confusion", "frustration", "boredom"]


def make_game_emotion(outdir=DEFAULT_OUTDIR, write: bool = True) -> pd.DataFrame:
    """In game emotion self reports, sampled while each level is being played.

    P8: for players whose confusion resolves within about two levels, confusion
    is a productive signal and they gain. For players whose confusion never
    resolves, it keeps escalating and their last ping comes shortly before they
    stop playing altogether.
    """
    rng = np.random.default_rng(SEED_GAME_EMOTION)
    players = make_game_players(write=False)
    telemetry = make_game_telemetry(write=False)

    latents = players.set_index("player_id")
    tel = telemetry.copy()
    tel["ts"] = pd.to_datetime(tel["timestamp"])

    rows = []
    counter = 0
    for pid, sub in tel.groupby("player_id", sort=True):
        lat = latents.loc[pid]
        ability = float(lat["ability"])
        persistence = float(lat["persistence"])
        resolves = int(lat["confusion_resolves"])
        fast = lat["profile"] == "fast_finisher"

        levels = sorted(sub["level"].unique())
        max_level = max(levels)
        first_confusion = None

        for level in levels:
            lvl_rows = sub[sub["level"] == level]
            diff = float(LEVEL_DIFFICULTY[level - 1])
            attempts = int(lvl_rows["attempt"].max())
            mean_err = float(lvl_rows["errors"].mean())
            t0 = lvl_rows["ts"].min()
            t1 = lvl_rows["ts"].max()

            n_pings = int(rng.integers(1, 4))
            for _ in range(n_pings):
                w_interest = np.exp(0.85 + 0.45 * ability - 1.05 * diff + 0.25 * persistence)
                w_confusion = np.exp(-0.35 + 1.65 * diff - 0.55 * ability + 0.16 * mean_err)
                w_frustration = np.exp(-1.15 + 1.25 * diff + 0.30 * (attempts - 1) - 0.45 * persistence)
                w_boredom = np.exp(-0.85 - 1.35 * diff + (0.95 if fast else 0.0) - 0.25 * ability)

                # The P8 mechanism: resolved confusion fades after a level or two,
                # unresolved confusion keeps building and precedes quitting.
                if first_confusion is not None:
                    since = level - first_confusion
                    if resolves == 1 and since >= 1:
                        w_confusion *= 0.14
                        w_interest *= 1.55
                    elif resolves == 0:
                        w_confusion *= 1.9 + 0.5 * since
                        w_frustration *= 1.7 + 0.4 * since

                w = np.array([w_interest, w_confusion, w_frustration, w_boredom])
                w = w / w.sum()
                emotion = EMOTIONS[int(rng.choice(4, p=w))]
                if emotion == "confusion" and first_confusion is None:
                    first_confusion = level

                if emotion == "interest":
                    intensity = int(np.clip(rng.normal(3.5, 0.95), 1, 5))
                elif emotion == "confusion":
                    intensity = int(np.clip(rng.normal(3.0 + 0.55 * diff + 0.4 * (1 - resolves), 0.9), 1, 5))
                elif emotion == "frustration":
                    intensity = int(np.clip(rng.normal(3.1 + 0.6 * diff, 1.0), 1, 5))
                else:
                    intensity = int(np.clip(rng.normal(2.6, 0.95), 1, 5))

                span = max(60.0, (t1 - t0).total_seconds())
                ts = t0 + pd.Timedelta(seconds=float(rng.uniform(0, span)))
                counter += 1
                rows.append(
                    {
                        "player_id": pid,
                        "level": int(level),
                        "emotion": emotion,
                        "intensity": intensity,
                        "_ts": ts,
                    }
                )

        # Unresolved confusion right before a player disappears from the log.
        if first_confusion is not None and resolves == 0 and max_level < N_LEVELS:
            last = sub[sub["level"] == max_level]["ts"].max()
            counter += 1
            rows.append(
                {
                    "player_id": pid,
                    "level": int(max_level),
                    "emotion": "confusion",
                    "intensity": int(np.clip(rng.normal(4.2, 0.7), 1, 5)),
                    "_ts": last + pd.Timedelta(seconds=float(rng.uniform(5, 90))),
                }
            )

    df = pd.DataFrame(rows).sort_values(["_ts"], kind="stable").reset_index(drop=True)
    df["ping_id"] = [f"PG{i + 1:05d}" for i in range(len(df))]
    df["timestamp"] = pd.Series(df["_ts"]).dt.strftime("%Y-%m-%dT%H:%M:%S")
    df = df[["ping_id", "player_id", "level", "emotion", "intensity", "timestamp"]]
    if write:
        df.to_csv(_outpath(outdir, "game_emotion.csv"), index=False)
    return df


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

GENERATORS = [
    ("students.csv", make_students),
    ("lms_clickstream.csv", make_clickstream),
    ("gradebook.csv", make_gradebook),
    ("forum_posts.csv", make_forum),
    ("group_chat.csv", make_group_chat),
    ("mmla_studio.csv", make_mmla),
    ("studio_artifacts.csv", make_studio_artifacts),
    ("srl_traces.csv", make_srl),
    ("game_players.csv", make_game_players),
    ("game_telemetry.csv", make_game_telemetry),
    ("game_emotion.csv", make_game_emotion),
]


def generate_all(outdir=DEFAULT_OUTDIR, verbose: bool = True) -> dict:
    """Write every CSV in the data universe. Returns {filename: row count}."""
    counts = {}
    for filename, fn in GENERATORS:
        t0 = time.time()
        df = fn(outdir=outdir, write=True)
        counts[filename] = len(df)
        if verbose:
            print(f"  {filename:24s} {len(df):>7,} rows   ({time.time() - t0:.1f}s)")
    return counts


def main():
    parser = argparse.ArgumentParser(description="Generate the EDIS 8100 synthetic data universe.")
    parser.add_argument(
        "--outdir",
        default=str(DEFAULT_OUTDIR),
        help="Directory to write CSVs into (default: the folder holding this script).",
    )
    args = parser.parse_args()

    print(f"EDIS 8100 data universe, master seed {SEED}")
    print(f"Writing to {Path(args.outdir).resolve()}")
    t0 = time.time()
    generate_all(args.outdir)
    print(f"Done in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
