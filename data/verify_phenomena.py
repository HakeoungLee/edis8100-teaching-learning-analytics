"""
EDIS 8100: statistical verification of the planted phenomena P1 to P9.

This is the instructor's regression test for the synthetic data universe. Every
notebook in the course depends on a specific pattern being present in the CSVs,
discoverable by a beginner, and noisy enough to argue about. If someone edits
generate_all_data.py, this script says whether the course still works.

Run it after regenerating:
    python generate_all_data.py
    python verify_phenomena.py

Prints one PASS or FAIL line per phenomenon and exits nonzero if anything failed.
Only numpy and pandas are required. The generator module is imported so that the
two latent facts a data analyst could not know (which four students were built as
network connectors, and which conversational cluster each student belongs to) can
be checked against what the forum data actually produced.
"""

from __future__ import annotations

import argparse
import sys
from collections import deque
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_all_data as gen  # noqa: E402

DEFAULT_DATADIR = Path(__file__).resolve().parent

RESULTS = []


def check(label: str, ok: bool, detail: str) -> None:
    RESULTS.append((label, bool(ok), detail))


def cohens_d(a, b) -> float:
    """Standardized mean difference, a minus b, pooled standard deviation."""
    a = np.asarray(a, dtype="float64")
    b = np.asarray(b, dtype="float64")
    na, nb = a.size, b.size
    if na < 2 or nb < 2:
        return float("nan")
    sp = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    if sp <= 0:
        return float("nan")
    return float((a.mean() - b.mean()) / sp)


def pearson(x, y) -> float:
    x = np.asarray(x, dtype="float64")
    y = np.asarray(y, dtype="float64")
    if x.size < 3 or x.std() == 0 or y.std() == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def ols_slope(x, y) -> float:
    x = np.asarray(x, dtype="float64")
    y = np.asarray(y, dtype="float64")
    xc = x - x.mean()
    denom = float((xc ** 2).sum())
    return float((xc * (y - y.mean())).sum() / denom) if denom > 0 else float("nan")


def logistic_fit(X, y, l2: float = 0.2, iters: int = 60):
    """Newton fitted logistic regression on standardized features."""
    X = np.asarray(X, dtype="float64")
    y = np.asarray(y, dtype="float64")
    mu, sd = X.mean(0), X.std(0)
    sd = np.where(sd > 0, sd, 1.0)
    Xs = np.column_stack([np.ones(len(X)), (X - mu) / sd])
    w = np.zeros(Xs.shape[1])
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-(Xs @ w)))
        wts = np.clip(p * (1 - p), 1e-6, None)
        H = Xs.T @ (Xs * wts[:, None]) + l2 * np.eye(Xs.shape[1])
        g = Xs.T @ (y - p) - l2 * w
        step = np.linalg.solve(H, g)
        w = w + step
        if np.max(np.abs(step)) < 1e-8:
            break
    return 1.0 / (1.0 + np.exp(-(Xs @ w)))


def fpr(y_true, y_pred, mask) -> float:
    neg = mask & (y_true == 0)
    if neg.sum() == 0:
        return float("nan")
    return float(y_pred[neg].mean())


def betweenness(adj: dict) -> dict:
    """Brandes betweenness centrality for an unweighted undirected graph."""
    nodes = list(adj)
    cb = {v: 0.0 for v in nodes}
    for s in nodes:
        stack, preds = [], {v: [] for v in nodes}
        sigma = {v: 0.0 for v in nodes}
        dist = {v: -1 for v in nodes}
        sigma[s], dist[s] = 1.0, 0
        q = deque([s])
        while q:
            v = q.popleft()
            stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    preds[w].append(v)
        delta = {v: 0.0 for v in nodes}
        while stack:
            w = stack.pop()
            for v in preds[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                cb[w] += delta[w]
    n = len(nodes)
    scale = 2.0 / ((n - 1) * (n - 2)) if n > 2 else 1.0
    return {v: c * scale for v, c in cb.items()}


# ---------------------------------------------------------------------------


def load(datadir: Path) -> dict:
    names = [
        "students", "lms_clickstream", "gradebook", "forum_posts", "group_chat",
        "mmla_studio", "studio_artifacts", "srl_traces", "game_players",
        "game_telemetry", "game_emotion",
    ]
    data = {}
    missing = []
    for name in names:
        path = datadir / f"{name}.csv"
        if not path.exists():
            missing.append(path.name)
            continue
        data[name] = pd.read_csv(path, keep_default_na=True)
    if missing:
        print("Missing CSV files: " + ", ".join(missing))
        print("Run: python generate_all_data.py")
        sys.exit(2)
    return data


def per_student_activity(clicks: pd.DataFrame) -> pd.DataFrame:
    clicks = clicks.copy()
    clicks["day"] = pd.to_datetime(clicks["timestamp"]).dt.date
    agg = clicks.groupby("student_id").agg(
        total_events=("event_id", "count"),
        active_days=("day", "nunique"),
    )
    wide = (
        clicks.pivot_table(index="student_id", columns="event_type", values="event_id", aggfunc="count")
        .fillna(0)
    )
    for col in ["video_play", "forum_view", "submit", "page_view"]:
        if col not in wide.columns:
            wide[col] = 0
    return agg.join(wide[["video_play", "forum_view", "submit", "page_view"]])


def quiz_frame(gradebook: pd.DataFrame) -> pd.DataFrame:
    q = gradebook[gradebook["assessment"].str.startswith("quiz_")].copy()
    q["quiz_no"] = q["assessment"].str.replace("quiz_", "", regex=False).astype(int)
    q["submitted_at"] = pd.to_datetime(q["submitted_at"])
    q["deadline"] = pd.to_datetime(q["deadline"])
    q["hours_before_deadline"] = (q["deadline"] - q["submitted_at"]).dt.total_seconds() / 3600.0
    return q


# ---------------------------------------------------------------------------
# Phenomenon checks
# ---------------------------------------------------------------------------


def check_p1(data):
    act = per_student_activity(data["lms_clickstream"])
    q = quiz_frame(data["gradebook"])
    score = q.groupby("student_id")["score"].mean()
    df = act.join(score.rename("mean_quiz")).dropna()

    r = pearson(df["total_events"], df["mean_quiz"])
    low_cut = df["total_events"].quantile(1 / 3)
    high_cut = df["mean_quiz"].quantile(0.75)
    efficient = df[(df["total_events"] <= low_cut) & (df["mean_quiz"] >= high_cut)]
    lift = float(efficient["mean_quiz"].mean() - df["mean_quiz"].mean())

    ok = (0.15 <= r <= 0.50) and len(efficient) >= 8
    check(
        "P1 activity volume relates only weakly to achievement; an efficient low-volume cluster exists",
        ok,
        f"r(total_events, mean_quiz) = {r:.3f} (target 0.15 to 0.50); "
        f"low-volume high-score cluster n = {len(efficient)} (target >= 8), "
        f"scoring {lift:+.1f} points above the class mean on a fraction of the clicks",
    )


def check_p2(data):
    students = data["students"].set_index("student_id")
    act = per_student_activity(data["lms_clickstream"])
    q = quiz_frame(data["gradebook"])
    mean_quiz = q.groupby("student_id")["score"].mean()

    df = students.join(act).join(mean_quiz.rename("mean_quiz"))
    y = (df["mean_quiz"] < 70).astype(int).to_numpy()
    group = ((df["first_gen"] == 1) & (df["work_hours_per_week"] >= 15)).to_numpy()

    naive_X = df[["total_events", "active_days", "video_play", "forum_view"]].to_numpy()
    p_naive = logistic_fit(naive_X, y)
    pred_naive = (p_naive > 0.5).astype(int)
    acc_naive = float((pred_naive == y).mean())
    fpr_group = fpr(y, pred_naive, group)
    fpr_rest = fpr(y, pred_naive, ~group)
    gap_naive = fpr_group - fpr_rest

    fair_X = df[["prior_gpa"]].to_numpy()
    p_fair = logistic_fit(fair_X, y)
    pred_fair = (p_fair > 0.5).astype(int)
    acc_fair = float((pred_fair == y).mean())
    gap_fair = fpr(y, pred_fair, group) - fpr(y, pred_fair, ~group)

    n_neg_group = int(((y == 0) & group).sum())
    ok = (
        gap_naive >= 0.12
        and n_neg_group >= 8
        and abs(gap_fair) <= 0.12
        and gap_fair <= gap_naive - 0.06
        and acc_naive >= 0.65
    )
    check(
        "P2 activity-only at-risk model over-flags first-generation students working 15+ hours; a prior-GPA model does not",
        ok,
        f"activity model accuracy {acc_naive:.2f}, FPR {fpr_group:.2f} in group (n negatives = {n_neg_group}) "
        f"vs {fpr_rest:.2f} elsewhere, gap = {gap_naive:+.2f} (target >= +0.12); "
        f"prior_gpa model accuracy {acc_fair:.2f}, FPR gap = {gap_fair:+.2f} (target within +/-0.12)",
    )


def check_p3(data):
    q = quiz_frame(data["gradebook"])
    last_minute = q["hours_before_deadline"] < 6
    d = cohens_d(q.loc[~last_minute, "score"], q.loc[last_minute, "score"])
    share = float(last_minute.mean())
    r = pearson(
        np.log1p(np.clip(q["hours_before_deadline"], 0, None)), q["score"]
    )
    ok = (0.35 <= d <= 1.10) and (0.10 <= share <= 0.50)
    check(
        "P3 submitting within 6 hours of the deadline goes with lower quiz scores",
        ok,
        f"d(earlier minus last 6 hours) = {d:.2f} (target 0.35 to 1.10); "
        f"{share:.0%} of submissions are last minute; r(log hours before, score) = {r:.3f}",
    )


def check_p4(data):
    latents = gen.make_students(write=False).set_index("student_id")
    posts = data["forum_posts"]
    by_id = posts.set_index("post_id")["student_id"].to_dict()

    replies = posts[posts["parent_post_id"].notna()]
    edges = set()
    cross_same = [0, 0]
    community = latents["community"].to_dict()
    for child, parent in zip(replies["student_id"], replies["parent_post_id"]):
        p_author = by_id.get(parent)
        if p_author is None or p_author == child:
            continue
        edges.add(tuple(sorted((child, p_author))))
        if community[child] == community[p_author]:
            cross_same[1] += 1
        else:
            cross_same[0] += 1

    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)

    # Work on the largest connected component so betweenness is well defined.
    seen, comps = set(), []
    for node in adj:
        if node in seen:
            continue
        stack, comp = [node], []
        seen.add(node)
        while stack:
            v = stack.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        comps.append(comp)
    giant = max(comps, key=len)
    sub = {v: adj[v] & set(giant) for v in giant}

    bt = betweenness(sub)
    deg = {v: len(sub[v]) for v in giant}
    bt_rank = sorted(bt, key=lambda v: -bt[v])
    deg_series = pd.Series(deg)
    deg_pct = deg_series.rank(pct=True)

    connectors = list(latents.index[latents["connector"] == 1])
    in_graph = [c for c in connectors if c in bt]
    top8 = set(bt_rank[:8])
    n_top = sum(1 for c in in_graph if c in top8)
    mean_deg_pct = float(np.mean([deg_pct[c] for c in in_graph])) if in_graph else float("nan")
    within_share = cross_same[1] / max(1, sum(cross_same))

    ok = (n_top >= 4) and (mean_deg_pct <= 0.90) and (within_share >= 0.70)
    check(
        "P4 forum replies form three loose clusters bridged by four connectors with high betweenness and middling degree",
        ok,
        f"{n_top} of {len(in_graph)} planted connectors are in the top 8 by betweenness (target 4); "
        f"their mean degree percentile = {mean_deg_pct:.2f} (target <= 0.90); "
        f"{within_share:.0%} of reply edges stay inside a cluster (target >= 70%)",
    )


def check_p5(data):
    students = data["students"]
    mmla = data["mmla_studio"].merge(students[["student_id", "multilingual"]], on="student_id")
    per = mmla.groupby(["student_id", "multilingual"]).mean(numeric_only=True).reset_index()
    ml = per[per["multilingual"] == 1]
    other = per[per["multilingual"] == 0]

    d_speak = cohens_d(ml["speaking_time_s"], other["speaking_time_s"])
    d_idea = cohens_d(ml["idea_units_chat"], other["idea_units_chat"])
    d_chat = cohens_d(ml["chat_messages"], other["chat_messages"])
    d_doc = cohens_d(ml["doc_edits"], other["doc_edits"])

    ok = (d_speak <= -0.35) and (d_idea >= 0.25) and (d_chat >= 0.10) and (d_doc >= 0.10)
    check(
        "P5 multilingual students speak less in studio but contribute as much or more through chat, ideas, and document edits",
        ok,
        f"d(multilingual minus rest): speaking_time {d_speak:+.2f} (target <= -0.35), "
        f"idea_units_chat {d_idea:+.2f} (target >= +0.25), chat_messages {d_chat:+.2f}, doc_edits {d_doc:+.2f}",
    )


def check_p6(data):
    srl = data["srl_traces"].copy()
    srl["timestamp"] = pd.to_datetime(srl["timestamp"])
    srl = srl.sort_values(["student_id", "session_id", "timestamp"])

    loops, spam_bursts = {}, {}
    for (sid, _sess), sub in srl.groupby(["student_id", "session_id"], sort=False):
        actions = sub["action"].tolist()
        times = sub["timestamp"].tolist()
        has_loop = 0
        if "set_goal" in actions and "reflect" in actions:
            if actions.index("reflect") > actions.index("set_goal"):
                has_loop = 1
        rec = loops.setdefault(sid, [0, 0])
        rec[0] += has_loop
        rec[1] += 1
        rapid = 0
        for i in range(1, len(actions)):
            if actions[i] == "request_hint" and actions[i - 1] == "request_hint":
                if (times[i] - times[i - 1]).total_seconds() < 8:
                    rapid += 1
        spam_bursts[sid] = spam_bursts.get(sid, 0) + rapid

    loop_rate = pd.Series({s: v[0] / v[1] for s, v in loops.items()}, name="loop_rate")
    rapid_hints = pd.Series(spam_bursts, name="rapid_hints")

    q = quiz_frame(data["gradebook"])
    slope = q.groupby("student_id").apply(
        lambda g: ols_slope(g["quiz_no"], g["score"]), include_groups=False
    ).rename("slope")

    df = pd.concat([loop_rate, rapid_hints, slope], axis=1).dropna()
    r = pearson(df["loop_rate"], df["slope"])

    spammers = df[df["rapid_hints"] >= 15]
    rest = df[df["rapid_hints"] < 15]
    d_spam = cohens_d(spammers["slope"], rest["slope"])

    loopers = rest[rest["loop_rate"] >= 0.6]
    middle = rest[rest["loop_rate"] < 0.6]
    order_ok = (
        len(spammers) >= 8
        and spammers["slope"].mean() < middle["slope"].mean() < loopers["slope"].mean()
    )

    ok = (0.25 <= r <= 0.65) and (d_spam <= -0.40) and order_ok
    check(
        "P6 complete SRL loops go with steeper quiz-to-quiz growth; the hint-spam subgroup grows least",
        ok,
        f"r(loop_rate, quiz slope) = {r:.3f} (target 0.25 to 0.65); "
        f"hint-spam students (n = {len(spammers)}) d = {d_spam:+.2f} (target <= -0.40); "
        f"mean slope spam {spammers['slope'].mean():+.2f} < middle {middle['slope'].mean():+.2f} < loopers {loopers['slope'].mean():+.2f}",
    )


def check_p7(data):
    tel = data["game_telemetry"]
    players = data["game_players"].set_index("player_id")
    gain = (players["post_score"] - players["pre_score"]).rename("gain")

    per_level = tel.groupby(["player_id", "level"]).agg(
        attempts=("attempt", "max"), errors=("errors", "sum")
    ).reset_index()
    early = per_level[per_level["level"] <= 3].groupby("player_id")["errors"].mean().rename("early_errors")
    retries = per_level.groupby("player_id")["attempts"].mean().rename("mean_attempts")
    reach = per_level.groupby("player_id")["level"].max().rename("max_level")
    prof = pd.concat([early, retries, reach, gain], axis=1).dropna()

    e_lo, e_hi = prof["early_errors"].quantile([0.30, 0.80])
    a_lo, a_hi = prof["mean_attempts"].quantile([0.40, 0.55])
    strugglers = prof[
        (prof["early_errors"] >= e_lo) & (prof["early_errors"] <= e_hi)
        & (prof["mean_attempts"] >= a_hi) & (prof["max_level"] >= 4)
    ]
    speedrunners = prof[(prof["early_errors"] < e_lo) & (prof["mean_attempts"] <= a_lo)]
    d_gain = cohens_d(strugglers["gain"], speedrunners["gain"])

    lvl = tel.groupby("level").agg(
        mean_errors=("errors", "mean"),
        mean_attempts=("attempt", "mean"),
        completion=("completed", "mean"),
        players=("player_id", "nunique"),
    )
    cliff_err = lvl.loc[4, "mean_errors"] / ((lvl.loc[3, "mean_errors"] + lvl.loc[5, "mean_errors"]) / 2)
    cliff_att = lvl.loc[4, "mean_attempts"] > max(lvl.loc[3, "mean_attempts"], lvl.loc[5, "mean_attempts"])
    cliff_comp = lvl.loc[4, "completion"] < min(lvl.loc[3, "completion"], lvl.loc[5, "completion"])

    ok = (
        d_gain >= 0.40
        and len(strugglers) >= 20
        and len(speedrunners) >= 20
        and cliff_err >= 1.30
        and cliff_att
        and cliff_comp
    )
    check(
        "P7 productive strugglers gain more than error-free fast finishers, and level 4 is a difficulty cliff",
        ok,
        f"d(strugglers n={len(strugglers)} minus fast finishers n={len(speedrunners)}) = {d_gain:+.2f} (target >= +0.40); "
        f"level 4 errors are {cliff_err:.2f}x the level 3 and 5 average (target >= 1.30), "
        f"attempts peak at level 4 = {cliff_att}, completion dips at level 4 = {cliff_comp}",
    )


def check_p8(data):
    em = data["game_emotion"]
    tel = data["game_telemetry"]
    players = data["game_players"].set_index("player_id")
    gain = (players["post_score"] - players["pre_score"])
    max_level = tel.groupby("player_id")["level"].max()
    finished = tel[tel["level"] == gen.N_LEVELS].groupby("player_id")["completed"].max()

    conf = em[em["emotion"] == "confusion"]
    conf_levels = conf.groupby("player_id")["level"].apply(lambda s: sorted(set(s)))
    played = tel.groupby("player_id")["level"].apply(lambda s: sorted(set(s)))

    rows = []
    for pid, levels in conf_levels.items():
        first = levels[0]
        after = [l for l in played[pid] if l > first]
        if not after:
            resolved = 0
        else:
            window = [l for l in levels if first < l <= first + 2]
            resolved = 0 if window else 1
        quit_early = int(max_level.get(pid, 0) < gen.N_LEVELS or finished.get(pid, 0) == 0)
        rows.append({"player_id": pid, "resolved": resolved, "gain": gain[pid], "quit": quit_early})

    df = pd.DataFrame(rows)
    res = df[df["resolved"] == 1]
    unres = df[df["resolved"] == 0]
    d_gain = cohens_d(res["gain"], unres["gain"])
    quit_gap = float(unres["quit"].mean() - res["quit"].mean())

    ok = (
        d_gain >= 0.40
        and quit_gap >= 0.25
        and len(res) >= 25
        and len(unres) >= 25
    )
    check(
        "P8 confusion that resolves within two levels goes with gains; unresolved confusion precedes quitting",
        ok,
        f"d(resolved n={len(res)} minus unresolved n={len(unres)}) on pre-to-post gain = {d_gain:+.2f} (target >= +0.40); "
        f"quit rate {unres['quit'].mean():.0%} unresolved vs {res['quit'].mean():.0%} resolved, gap = {quit_gap:+.2f} (target >= +0.25)",
    )


def check_p9(data):
    mmla = data["mmla_studio"]
    arts = data["studio_artifacts"]
    g = (
        mmla.groupby(["group_id", "session_id"])["speaking_time_s"]
        .apply(gen.gini)
        .rename("speaking_gini")
        .reset_index()
    )
    df = g.merge(arts, on=["group_id", "session_id"])
    r = pearson(df["speaking_gini"], df["artifact_score"])

    lo, hi = df["speaking_gini"].quantile([1 / 3, 2 / 3])
    balanced = df[df["speaking_gini"] <= lo]["artifact_score"]
    dominated = df[df["speaking_gini"] >= hi]["artifact_score"]
    d = cohens_d(balanced, dominated)

    ok = (-0.60 <= r <= -0.25) and (d >= 0.40)
    check(
        "P9 groups with balanced talk produce higher rated artifacts than dominated groups",
        ok,
        f"r(speaking-time Gini, artifact_score) = {r:.3f} (target -0.25 to -0.60); "
        f"d(balanced third minus dominated third) = {d:+.2f} (target >= +0.40)",
    )


# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Verify the planted phenomena P1 to P9.")
    parser.add_argument("--datadir", default=str(DEFAULT_DATADIR), help="Directory holding the CSVs.")
    args = parser.parse_args()

    datadir = Path(args.datadir).expanduser().resolve()
    data = load(datadir)

    print(f"EDIS 8100 planted phenomena check, data in {datadir}")
    print("=" * 78)

    for fn in [check_p1, check_p2, check_p3, check_p4, check_p5,
               check_p6, check_p7, check_p8, check_p9]:
        fn(data)

    failures = 0
    for label, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(f"[{status}] {label}")
        print(f"        {detail}")

    print("=" * 78)
    print(f"{len(RESULTS) - failures} of {len(RESULTS)} phenomena verified.")
    if failures:
        print("At least one planted phenomenon is missing or out of range.")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
