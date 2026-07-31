# 🤝 Week 9: Collaboration Analytics Lab

Reading a group by its chat, then deciding what a dashboard should refuse to show.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 28, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Learning Analytics for Understanding and Supporting Collaboration |
| **Guest speaker** | None this week. The 60-minute discussion block is entirely student led. |
| **In-class time on this notebook** | About 30 minutes, in the hands-on block (4:30 to 5:00). Section 5 is written to spill into the 5:00 discussion on purpose. |
| **Deliverable** | None from this notebook. It is a lab, not a graded submission. |
| **Due date** | The **Course Research Project Outline** is due this week via Canvas, submitted separately from this notebook, together with your AI interaction log and reflection. |
| **Notebook** | `week09_collaboration_analytics_lab.ipynb` |
| **Data used** | `students.csv`, `group_chat.csv`, `mmla_studio.csv`, `studio_artifacts.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib, networkx |

## Objectives

By the end of this activity you will be able to:

1. **Turn** a raw chat log into turn-taking measures: what counts as a turn, who follows whom, and how long a group waits before somebody else speaks, and show why two equally natural readings of that last phrase give answers a third apart.
2. **Compute** participation equity from chat and compare it directly against the speaking time equity you already computed in week 6, on the same 192 group-sessions.
3. **Build and read** a per-group sociogram in `networkx`, and say plainly what the picture shows, what it only appears to show, and what it cannot show at all.
4. **Argue**, with evidence from these data, what a collaboration dashboard should refuse to display, and to whom.

The through-line of the session: week 6 measured collaboration with microphones and found something. This week you point a second instrument at the same rooms and watch which findings survive the change of sensor. The ones that do not survive are not noise. They are the reason the last hour of class is an argument about what to build.

## What is in this folder

| File | What it is |
|---|---|
| `week09_collaboration_analytics_lab.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the four datasets into the runtime.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week09-collaboration-analytics-lab/week09_collaboration_analytics_lab.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week09-collaboration-analytics-lab/week09_collaboration_analytics_lab.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week09-collaboration-analytics-lab/week09_collaboration_analytics_lab.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository. Your Your turn 4 specification is worth keeping: week 11's co-design studio starts from exactly that kind of artifact.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and networkx, all of which ship with Anaconda.

## Step-by-step walkthrough

Total time is about 35 minutes if you keep moving, which is roughly the hands-on block. The four ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. You are not expected to write code from scratch today. You are expected to read output carefully and argue about what it means.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the chat log, the studio sensor table, the artifact scores, and the roster inside your runtime, so nothing has to be downloaded and no real student is ever recorded.

**⚙️ Load the libraries and the files (1 minute).** Four files, 6,379 chat messages, 960 student-sessions of sensor data, 192 artifact scores, 120 students. The markdown above the cell tells you what one row of each file means, which is the single most useful thing to know before touching any of them.

**📊 1. From a chat log to turns (4 minutes).** Three analyst decisions, written down so you can argue with them later: a turn is one message, a response is a message from a different person, and latency is the wall clock gap from a message to the one immediately after it, counted only when a different person sent it. Every gap is computed inside one group and one session, so no interval ever spans two sessions. Then the numbers: 77.8 percent of messages are a switch to a new speaker and 22.2 percent are the same person continuing. The raster plot shows one session (G07, studio_5) as marks on a timeline, where one member holds 38.2 percent of the messages and another posted exactly once, at 2.9 percent. The prompt about that single dot does not ask what the student was doing. It asks you to find a candidate explanation in the instrument, one in the setting, and one in the circumstances first, and only then to treat anything about the person as one hypothesis among several.

**✏️ Your turn 1: look at a different room (1 minute).** Change the group and session and rerun. Then find a session whose shape makes you want to ask a question about it, and write the sentence naming the standard you just applied. Whatever word arrived first, *uneven*, *quiet*, *unhealthy*, *fine*, is a construct you brought with you rather than something the raster measured. Section 5 holds you to that sentence, because it is the same sentence a dashboard writes on your behalf.

**📊 2. Response latency, and a cautionary tale about metrics (5 minutes).** Median seconds until somebody else replies, computed honestly and then tested. Across all group-sessions the median is 108 seconds, the fastest is 46 and the slowest 319. Then the uncomfortable panel: the correlation between a session's message count and its median latency is **-0.72** (Spearman -0.76). The cell prints the arithmetic underneath it. A studio session's messages span about 82 minutes almost regardless of group, so the median gap is close to that span divided by the number of gaps in it, and that purely mechanical quantity tracks the measured latency at r = 0.77. This tile would separate busy rooms from quiet ones even if nobody in either room were listening. The cell also computes the second reading of the same definition, the gap to the next message by anybody else rather than to the next message: 143 seconds against 108. Same English sentence, one third apart. This is the first candidate for the refusal list.

**📊 3. Participation equity in a second channel (6 minutes).** The Gini coefficient from week 6, re-pointed at chat message counts, and carrying week 6's ceiling with it: for a group of five the maximum Gini is **0.8**, not 1.0, so every number here is read against 0.8. The boring step that matters most: a member who sent zero messages does not appear in the chat log at all, so the roster is rebuilt from the sensor table first and the silent members are filled in as zeros. Nine member-sessions out of 960 would otherwise have vanished. Then two findings arrive back to back. First, the two channels barely agree: r = -0.03 with a 95 percent interval of [-0.17, +0.11], which rules out even a moderate association rather than merely failing to find one, and 106 of 192 group-sessions (55 percent) land on opposite sides of the two medians against the 50 percent chance would give. Second, week 6's result does not transfer. Measured by speaking time, the most balanced third of sessions averages 7.05 on the artifact rubric against 6.09 for the most dominated third. Measured by chat messages, the three bands are 6.62, 6.74, and 6.57, which is to say indistinguishable. The cell also repeats both relationships on the 24 group means, where speaking time equity strengthens to -0.52, matching what week 6 reported.

**✏️ Your turn 2: swap in a better chat measure (1 minute).** Change one string to compute equity on human-coded substantive contributions instead of raw message counts. Raw message equity correlates +0.02 with artifact score and coded ideas -0.08. Neither is distinguishable from zero, so the honest sentence is that both chat-based equity measures are silent about this outcome, and both are far from speaking time equity at -0.33.

**📊 4. Sociograms: the shape of a conversation (4 minutes).** A Gini says how lopsided a group was. It cannot say what the lopsidedness looked like. So the notebook draws two extremes side by side: the most evenly shared chat in the dataset (G06, studio_1, chat Gini 0.04, five members within one message of each other) and the most concentrated (G14, studio_2, chat Gini 0.43, where one member sent 59.5 percent of the messages). Read the arrows honestly. In an unthreaded chat, "B posted soon after A" is not "B replied to A."

**✏️ Your turn 3: the window is an argument (1 minute).** The 120-second reply window is your claim about how long a conversational thread stays open, not a fact about the group. At 30 seconds quiet groups look disconnected when they are only slow. At 600 seconds every group looks equally connected.

**📊 5. Which group signals actually move with the product (4 minutes).** Every candidate indicator lined up against the same outcome across all 192 sessions, with the number printed on each bar. Speaking time equity is the strongest at -0.331 and coded idea units the strongest positive at +0.300. Doc edits reach +0.184 and chat volume +0.125. Chat message equity sits at +0.021 and total speaking time at -0.013.

Then the correction that governs how any of it may be read. **Those 192 rows are not 192 independent observations.** They are eight sessions from each of the same 24 groups, and how evenly a group shares its floor is largely a property of the group: 61 percent of the variance in speaking time equity sits between groups rather than within them, which makes 192 sessions worth about 37 independent observations. The cell prints the intraclass correlation and effective sample size for every indicator alongside the same correlations recomputed on the 24 group means, where the bar for conventional significance moves from |0.14| to about |0.40|. The ranking reshuffles: speaking time equity strengthens to -0.52, coded idea units to +0.45, total chat messages to +0.41, and total interruptions falls to -0.11. Nothing about the groups changed. Only the question did.

**📊 The equity check you should run before shipping any of this (3 minutes).** Twenty-four students on this roster use more than one language day to day. A dashboard defining participation as speaking time reports them at 0.70 times their peers, bootstrap interval [0.51, 0.92]. Defining it as coded ideas in chat reports them at 1.26, interval [1.03, 1.53]. Same students, same sessions, opposite conclusion. The raw chat message ratio is 1.10 with an interval straddling 1.0, which is the fourth channel and the one you cannot yet tell apart from parity: an example of a number that would have looked like a finding on a slide. The prompt asks which dashboard is wrong, and then asks you to trace three steps forward from a teacher using the speaking time version to decide who to call on.

**✏️ Your turn 4: write the dashboard's refusal list (4 minutes, and then the rest of the hour).** Ten tiles, four possible audiences each: `teacher`, `group`, `student`, or `nobody`. You assign every tile, and the cell checks your specification against a short list of design hazards drawn from the findings above and prints a review. Change at least three defaults and be ready to defend the changes. **This is the heart of the week.** The specific slots matter less than the principle underneath them: a measure may be shown to an audience only if that audience can act on it in a way that helps, and only if being wrong about a person costs less than staying silent.

**💬 Reflection.** Five prompts, tied to this week's three readings and to your own project outline. Bring at least one answer to the 5:00 discussion block, because the discussion opens on the refusal list.

**✅ Submission checklist.** This notebook is not submitted. What is due this week is the Course Research Project Outline, and the checklist tells you exactly what goes with it.

## What this connects to in the readings

- **Chen and Teasley (2022)**, *Learning analytics for understanding and supporting collaboration*: specify the construct before you specify the sensor. This notebook is a live demonstration of skipping that step. Speaking time equity relates to product quality, chat message equity does not, and the two are perfectly capable of being described with the same word.
- **Praharaj, Scheffel, Drachsler, and Specht (2021)**, *Literature review on co-located collaboration modeling using multimodal learning analytics: Can we go the whole nine yards?*: the chain from sensing to feedback and the places it breaks. Section 5 hands you a tangle worth separating in writing. The strongest positive signal is human-coded idea units, which is also the one a school cannot afford to collect at scale. The strongest signal of any sign is the group-level inequality of speaking time, which comes free with the microphones. And the equity check found that the *per student* version of that same microphone channel records multilingual students at about 0.7 times their peers while three other channels record them at or above parity. Those are two claims about one sensor at two different grains, and only the second is an equity finding. What tempts people into the cost story, and what Your turn 2 refutes, is that `num_turns` comes off the same microphones, costs nothing extra, and lands at -0.33 with speaking time. What separates the indicators here is the channel, not the price.
- **Martinez-Maldonado, Kay, Buckingham Shum, and Yacef (2019)**, *Collocated collaboration analytics: Principles and dilemmas for mining multimodal interaction data*: the dilemmas are not abstract here. Your turn 4 makes you resolve one of them per tile, ten times, and write down who sees the result.

There is no guest this week, which means the full hour belongs to your discussion leaders. The closing question is the one worth bringing them: **what should a collaboration dashboard refuse to show, and to whom?**

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Build a fairer composite index.** Standardize speaking time, coded idea units, and document edits, average them into one participation score per student-session, and recompute the Gini on that composite. Does its relationship to artifact score look more like the talk version or the chat version? Then say what you smuggled in when you chose equal weights, because equal weighting is a claim about what counts, not a neutral default.
2. **Turn taking beyond chance.** In a group where one member sends 40 percent of the messages, that member will appear in roughly 40 percent of the follow edges by arithmetic alone. Compute the expected edge weights under a null model where turn order is independent of who spoke last, subtract them from the observed weights, and redraw the sociogram from what is left. Which ties survive, and does the hub in G14 still look like a hub?
3. **Strip the chattiness out of latency.** Regress each session's median latency on its message count, keep the residuals, and test those residuals against artifact score. If the residual carries no signal, you have converted an intuition ("this metric is really volume") into the evidence you would need to keep the tile off a dashboard.
4. **Trajectories, not snapshots.** Plot each group's chat Gini across `studio_1` through `studio_8`. Do groups settle into a pattern or does the pattern move? Then answer the design question: what would a dashboard showing session 3 alone have said about the groups that changed, and how long would that label have followed them?
5. **Interrogate the silence.** Nine member-sessions had zero chat messages. Pull those same students' speaking time, gaze, and document edits for those exact sessions and describe what they were actually doing. Then write the sentence a chat-only dashboard would have generated about them.
6. **Check whether group composition could explain the speaking Gini.** The obvious rival explanation for the speaking time result is composition: if multilingual students hold the floor less, groups with more of them would show higher Gini for reasons that have nothing to do with how the group works. Test it, and notice what you find. `students.csv` deals the 24 multilingual students round robin, so **every one of the 24 groups contains exactly one**. There is no variation to correlate with anything, and the rival explanation cannot be tested in this dataset at all. Write the two sentences you would put in a limitations section, then say what you would have had to change about the group assignment procedure to make the question answerable. A design that makes a question unaskable is a finding about the design.
7. **The nested structure, properly.** Section 5 handles the 24-groups-by-8-sessions structure by aggregating to group means. Do it the other way instead: fit a mixed effects model of artifact score on speaking time Gini with a random intercept for group, and compare the fixed effect against both the 192-row and the 24-row correlations. Then decide which of the three you would report, and to whom.

## Troubleshooting

**"NameError: name 'equity' is not defined".** You skipped ahead. `equity` is built in section 3, and several later cells (including the appendix solution for Your turn 1) need it. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/group_chat.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the library cell right after the setup cell, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**"KeyError" or an empty chart after I changed the group and session.** Group ids run `G01` to `G24` and session ids run `studio_1` to `studio_8`, both as strings in quotes. `"G7"` and `"studio1"` are not valid. A session with very little chat can also produce a nearly empty raster, which is a real result rather than an error.

**My sociogram has almost no arrows.** Check `MY_WINDOW_S`. At 30 seconds you are keeping only rapid-fire exchanges, and a slow, thoughtful group will lose nearly all of its edges. That is the point of the exercise: the window is your claim, not the group's property.

**"ModuleNotFoundError: No module named 'networkx'".** You are running locally without networkx installed. In a terminal: `conda install networkx` or `pip install networkx`. In Colab this cannot happen, networkx is already there.

**The Your turn 4 review says "No hazard on the list was triggered" and I expected a warning.** Read the next line, which is the important one: the hazard list only contains problems this notebook happened to surface. A clean review is not a safe dashboard, and treating it as one is the exact failure mode the section is about.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all: the notebook is seeded, so a clean run reproduces the same numbers every time.

**My refusal list is completely different from my partner's.** Good. There is no answer key in section 5, only better and worse arguments. Compare the principles you each used, not the slots you each chose.

## A reminder about documenting AI use

This notebook is not a graded submission, but something is due this week: the **Course Research Project Outline**, uploaded to Canvas separately from anything here.

If you used an AI assistant while drafting that outline, or while working through this notebook, the course AI policy requires two things, and they go in two different places in the **AI Reflection** submission on Canvas:

- **The conversation record goes in an attached Word file.** Copy the actual exchanges into a `.docx` and attach it. Prompts, responses, the record itself, not a summary of it.
- **The four reflection questions are answered in the Canvas text box**, directly, not inside the attachment: what you asked for, what you accepted, what you rejected, and how you verified anything you kept.

If you used no AI at all, one line in the text box saying so is a complete and acceptable submission.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use costs you nothing.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
