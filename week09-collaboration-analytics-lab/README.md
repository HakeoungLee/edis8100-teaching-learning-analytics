# 🤝 Week 9: Collaboration Analytics Lab

Reading a group by its chat, in two settings, then deciding what a dashboard should refuse to show.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 28, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Learning Analytics for Understanding and Supporting Collaboration |
| **Guest speaker** | None this week. The 60-minute discussion block is entirely student led. |
| **In-class time on this notebook** | About 40 minutes, in the hands-on block (4:30 to 5:00). Section 6 is written to spill into the 5:00 discussion on purpose. |
| **Deliverable** | None from this notebook. It is a lab, not a graded submission. |
| **Due date** | The **Course Research Project Outline** is due this week via Canvas, submitted separately from this notebook, together with your AI interaction log and reflection. |
| **Notebook** | `week09_collaboration_analytics_lab.ipynb` |
| **Data used** | Two published, openly licensed datasets, downloaded by the notebook. `collab-chat/chat_logs.csv` (1,374 chat messages, 8 groups of 4 or 5 undergraduates, four days in February 2021; CC BY 4.0; Villa-Torrano, 2021, Zenodo 5150537) and the Week 6 JUSThink files `justhink/per_participant.csv` and `justhink/pehri_team_outcomes.csv` (78 children in 39 teams of two, 34 teams with an outcome; CC BY 4.0; Norman et al., 2021, Zenodo 4627104; Nasir et al., 2021, Zenodo 4633092). |
| **Libraries** | pandas, numpy, matplotlib, scipy |

## Objectives

By the end of this activity you will be able to:

1. **Open** a real, messy export, name each cleaning decision out loud, and state what the decision costs.
2. **Recognise** when a measure is reporting the instrument's resolution rather than anyone's behaviour, and retire the measure rather than caveat it.
3. **Compute** the unevenness of a group's recorded participation, read it against both its ceiling of (n - 1) / n and against what chance alone would produce at that group size and volume, and describe the spread across groups without over-testing it.
4. **Say precisely** why eight groups, two sittings each, will not support a group-level significance claim, and what nesting does to any interval you might print.
5. **Argue**, with evidence from two settings, what a collaboration dashboard should refuse to display, and to whom.

The through-line of the session: Week 6 measured collaboration with one set of instruments and found something. This week you point a different instrument at a different room, then ask the only question that matters for anything you would build. **Does the finding travel?** The parts that do not travel are not noise. They are the reason the last hour of class is an argument about what to build.

## What is in this folder

| File | What it is |
|---|---|
| `week09_collaboration_analytics_lab.ipynb` | The notebook. It downloads its own data from the course dataset repository and runs top to bottom untouched. |
| `README.md` | This file. |

You do not need to clone anything or download a CSV by hand. The first code cell fetches all three files. If your connection drops, that cell prints a plain message naming the repository rather than a traceback.

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

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository. Your Section 6 specification is worth keeping: Week 11's co-design studio starts from exactly that kind of artifact.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib and scipy, all of which ship with Anaconda, plus an internet connection for the three CSV files.

## The data, and where it came from

Nothing here was collected by this course. Both datasets are redistributed under the licence their authors chose, and both citations belong in your reference manager the moment you use anything from them.

**Villa-Torrano (2021), `collab-chat/chat_logs.csv`, CC BY 4.0.** 1,374 messages, four columns, from undergraduates in a computer networks course working through Moodle and a platform called CoTrackV2. Eight groups of four or five, each recorded on two days between 15 and 18 February 2021, online, in Spanish. Semicolon delimited, UTF-8 with a byte order mark, day-first dates.

> Villa-Torrano, C. (2021). *Dataset on an online collaborative learning situation in a computer networks course* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5150537

**JUSThink and PE-HRI (2021), `justhink/`, CC BY 4.0.** The Week 6 children: 78 nine to twelve year olds in 39 teams of two, building a minimum spanning tree with a robot in the room. Interface actions for all 78, speech for 20 of them, team level learning outcomes for 34 of the 39 teams.

> Norman, U., Dinkar, T., Nasir, J., Bruno, B., Clavel, C., & Dillenbourg, P. (2021). *JUSThink dialogue and actions corpus* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4627104
>
> Nasir, J., Norman, U., Bruno, B., Chetouani, M., & Dillenbourg, P. (2021). *PE-HRI: A multimodal dataset for the study of productive engagement in a robot mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4633092

Neither dataset carries a name, an age band for the chat students, a gender, a language background, a prior grade, or in the chat data any measure at all of what a group produced. Those absences shape the whole week, and the notebook names each one where it bites rather than working around it quietly.

## Step-by-step walkthrough

Total time is about 40 minutes if you keep moving, which is roughly the hands-on block. The five ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. You are not expected to write code from scratch today. You are expected to read output carefully and argue about what it means.

**⚙️ Setup (2 minutes).** One cell: `%matplotlib inline`, the imports, a colourblind safe palette, and a loader that fetches three CSVs and, if the network is down, says so in English and names the repository. It confirms 1,374 chat messages by 4 columns, 78 children by 12, and 34 teams by 6.

**🧹 1. The file as it arrived (6 minutes).** Three ordinary problems, each shown going wrong before it goes right. A default `pd.read_csv` returns **one** column, because the file is semicolon delimited. Reaching for `encoding="latin-1"`, the reflex for a file full of Spanish accents, produces a first column named `ï»¿timestamp` and mangles the accents in 185 messages; the three bytes in front are `EF BB BF`, a byte order mark, and `encoding="utf-8-sig"` is the honest name for what the file is. Month-first date parsing raises `ValueError`, because there is no month 15. Then the inventory: 1,374 messages, zero missing values, 8 groups, 34 authorids, 4 or 5 authors per group, nobody writing in two groups, four calendar days, and every group recorded on exactly two of them.

Four decisions go into a table with their price tags. The one worth the argument: **there is no roster**, so the only people visible are the people who typed. Three member-sessions do show somebody typing on one of their group's two days and not the other, and those get filled in as zeros. Anyone silent across all four days leaves no trace, which makes every unevenness number in the notebook a **lower bound**. The figure maps all sixteen sessions on a clock: groups 1 and 2 in the afternoon of 15 and 17 February, groups 3 to 8 after ten at night on 16 and 18 February, sessions running 13 to 35 minutes with a median of 17.5.

**✏️ Your turn 1: read a room (2 minutes).** Print the opening of any session with authors relabelled `P1` to `P5` **within that session, ordered by message count**. The prompt names that relabelling as a decision, because it builds a ranking into the labels and makes every group look like it has a leading contributor.

**⏱️ 2. The clock the platform kept (7 minutes).** The section that decides what the rest of the week can measure. **97.0 percent of messages (1,333 of 1,374) share a minute stamp with another message in the same session.** The file has 283 occupied minutes holding 4.9 messages each on average and 22 in the busiest. **80.3 percent of consecutive within-session gaps are exactly 0 seconds**, every gap is a whole number of minutes, and the smallest non-zero gap anywhere is 60 seconds. So the tile the section came to build, median seconds until somebody else posts, reads **0.0 seconds in 16 of 16 sessions**. That number is about the export format.

The decision is stated and priced: **retire the tile**, do not caveat it. What that costs is no responsiveness measure, no uptake speed, and no burst structure finer than a minute. What survives is co-presence at minute grain, 222 of 283 occupied minutes (78.4 percent) holding two or more writers, printed with counts beside every rate.

**✏️ Your turn 2: where does one stretch of talk end? (2 minutes).** With latency retired, the temporal question gets coarser. At the default 2 minute idle rule the file holds 25 stretches and 11 of 16 sessions are a single unbroken one; at 1 minute it fragments to 38, at 5 minutes it collapses to 18. The rule is a claim, not a fact, and the appendix says so.

**📊 3. Who the log recorded, and how evenly (6 minutes).** The Gini coefficient is defined here rather than recalled, since Week 6 works in pairs and a Gini on two people carries no information the larger share does not already carry. The part dashboards get wrong is stated plainly: the ceiling is **(n - 1) / n**, so **0.75** for the six four-person groups and **0.80** for the two five-person ones. The measure is named for what it is, unevenness of *recorded messages*, and the stacked bar figure marks where an even split would fall for each group. **Gini runs from 0.092 (Group 6) to 0.306 (Group 8), a ratio of 3.32, while group size is nearly constant, so the spread is not a size artifact.** Group 8's most recorded member holds 44 percent of 106 messages, 2.22 times an even share; Group 1's holds 1.18 times.

**🎲 4. How much is chance, how much is the group, how much is the day (8 minutes).** Three questions before that spread counts as a finding.

*Chance, and the null model most people get wrong.* Twenty thousand simulated draws per group give each group its own floor, and the floor is not zero and not constant. The obvious null treats each of the 1,374 messages as an independent draw, and it is **wrong**, because people type in runs: the file's 1,374 messages arrive in 982 runs, averaging 1.40 messages and reaching 7. Independent draws are smoother than bursty ones, so that null puts the floor too low and flatters every group. The notebook simulates both and prints them side by side. The honest floor, which resamples **turns** with run lengths drawn from that group's own runs, sits about **35 percent higher** than the naive one on average and nearly half again as high for Group 8: **0.077 for Group 5 with 260 messages, 0.143 for Group 8 with 106 messages and five members**, against 0.053 and 0.098 naive. Six of the eight groups are still more uneven than 95 percent of their own simulations, and **Groups 1 and 6 are still not distinguishable from chance at all**, so the verdict survives the correction. The distances do not, which is the transferable lesson: a distance from a floor is only as good as the floor. The two rankings still disagree at the top: the most uneven group by raw Gini is Group 8, the most uneven above its own floor is Group 5.

*The day.* Every group was recorded twice, and the figure plots both sittings beside the pooled value. **Group 7 reads 0.064 on one day and 0.446 on the other, a swing of 0.382, which is larger than the entire spread of 0.214 across all eight groups.** Any dashboard labelling a group after one session is labelling a Tuesday.

*The units.* The nesting is written out: 1,374 messages inside 34 people inside 8 groups, each seen twice. Group-level claims have **eight** units. The section then asks whether groups that send more messages spread them more evenly, and answers with the interval rather than the estimate: Spearman +0.26 with a bootstrap interval of **[-0.59, +1.00]** over 4,000 resamples of the eight groups. "This file cannot tell" is presented as a complete answer. The scatter draws the chance floor as a curve rather than subtracting it, because subtracting a floor that falls with volume builds a correlation with volume into the statistic by construction.

**✏️ Your turn 3: change what counts as a contribution (2 minutes).** Real text allows what a message count cannot reach: count characters or words rather than messages. Ranking the eight groups by characters agrees with ranking them by messages at Spearman **+0.929**, and words the same. The prompt refuses to call that reassuring: both measures count typing, 28.5 percent of messages are two words or fewer, and neither measure sees the student who solved the problem on a voice call.

**🌍 5. Does any of this travel? (7 minutes).** Everything so far describes eight groups of undergraduates typing Spanish in February 2021. So the notebook changes almost every variable at once and looks again at the Week 6 children: 78 of them, in 39 teams of **two**, with a robot, in a different country, language, medium and age band. The dyad ceiling is **0.5**, which is why the cross-setting comparison uses the busiest member's share as a multiple of an even split, defined identically at any group size, with the chance floor drawn beside each strip. Two honesty notes travel with that figure. The chat floor keeps the burst structure; the two JUSThink floors cannot, because those files record totals and not sequences, so they are lower bounds and the gap above them is an upper bound. And the speech floor is computed on speaking **turns** while the plotted statistic is a share of **seconds**, which pushes the same way: seconds arrive in unequal lumps, so the real floor for seconds is higher than the one drawn.

Missingness is reported, not absorbed: 34 of 39 teams have an outcome row, teams 11, 33, 34, 35 and 36 do not, 10 teams have speech, 9 have both. A cross-file check confirms `T_LG_absolute` equals the pair's mean test change divided by 10 to within 0.000000, which is how you learn what a derived column actually means. Base rates come before any comparison: pre-test mean 5.85 of 10, post-test 5.95, with 17 teams rising, 8 unchanged and 14 falling.

Then the question the chat data cannot ask, because it records no outcome at all. Across 34 teams, unevenness of interface actions against absolute learning gain gives Spearman **-0.008, interval [-0.37, +0.36]**; against final task error, **-0.183, interval [-0.50, +0.18]**. Across the 10 teams with both channels, action unevenness against speech unevenness gives **-0.200, interval [-0.80, +0.63]**, and the prompt insists on the difference between "the channels disagree" and "ten teams cannot tell us whether they agree." Three comparisons are reported as three, not as the best of three.

**🎛️ 6. The design question (5 minutes, and then the rest of the hour).** ✏️ **Your turn 4** gives you ten tiles and four possible audiences each: `teacher`, `group`, `student`, `nobody`. You assign every tile and the cell checks your specification against hazards **drawn only from what this notebook found**, then prints a review. Change at least three defaults and be ready to defend them. **This is the heart of the week.** The principle underneath: a measure may be shown to an audience only if that audience can act on it in a way that helps, and only if being wrong about a person costs less than staying silent. ✏️ **Your turn 5** then asks for one sentence, written out: what should this dashboard refuse to show, to whom, and who decided. The appendix shows one worked refusal and names the test it has to pass, which is that every clause of the "because" describes the instrument rather than a student.

**💬 Reflection.** Six prompts, tied to the three readings, to your own outline, and to the two research teams whose open data made the week possible.

**✅ Submission checklist.** This notebook is not submitted. What is due is the Course Research Project Outline, and the checklist says exactly what goes with it.

## What this connects to in the readings

- **Chen and Teasley (2022)**, *Learning analytics for understanding and supporting collaboration*: specify the construct before you specify the sensor. This notebook deliberately runs the other way, taking the sensor it was handed and asking which construct survives it. Section 2 is what happens when the sensor's resolution and the construct's definition never meet: "how fast does this group answer each other" is a perfectly good construct that this instrument cannot express, and no amount of analysis repairs that.
- **Praharaj, Scheffel, Drachsler, and Specht (2021)**, *Literature review on co-located collaboration modeling using multimodal learning analytics: Can we go the whole nine yards?*: the chain from sensing to feedback and the places it breaks. Here the chain breaks at the first link for one measure and holds for another, and the section that separates them is worth the discussion. Note also which channel turned out to be affordable: in the JUSThink data the interface log is complete for all 39 teams and unrelated to the outcome, while the speech transcript exists for 10 teams and cannot be evaluated at that size. Neither cost nor completeness rescued the finding.
- **Martinez-Maldonado, Kay, Buckingham Shum, and Yacef (2019)**, *Collocated collaboration analytics: Principles and dilemmas for mining multimodal interaction data*: the dilemmas are concrete in Section 6. You resolve one per tile, ten times, and write down who sees the result. The sharpest one this year is the roster: the notebook's participation shares have a denominator that cannot be observed, and a tile displaying them to a group presents a lower bound as if it were a fact about people.

There is no guest this week, which means the full hour belongs to your discussion leaders. The closing question is the one worth bringing them: **what should a collaboration dashboard refuse to show, and to whom?**

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **The roster you cannot see.** Every unevenness number is a lower bound because a student who never typed is missing from the denominator. Recompute each group's Gini assuming one, then two, additional silent members, and plot how far the numbers move. Then write the limitations sentence for a denominator you cannot observe.
2. **Minute-grain interaction structure.** The clock cannot support latency but it can support a graph: an edge between two people whenever both wrote inside the same minute. Build it per group and compare its density against a null that shuffles authorship within each minute. Which groups still look connected once the shuffle has had its say?
3. **Message length at the level of the person.** Your turn 3 found that characters and messages rank the eight *groups* almost identically. Do it for individuals instead. Is there anyone here for whom the two channels disagree sharply, and what would a dashboard built on each have said about them?
4. **Cluster the day, not the group.** Treat all 16 sessions as the unit and ask whether 16 February looks systematically different from 18 February. If it does, you have found a day effect that a group-level dashboard would have charged to teams.
5. **Do the nesting properly.** Fit a model of session Gini with a random intercept for group and report the intraclass correlation *with its uncertainty*. With eight groups the estimate will be unstable, and reporting the instability rather than the estimate is the exercise. Then say what sample size the question would actually need.
6. **Sensitivity of the session rule.** We defined a session as a group-day. Rebuild it with the idle rule from Your turn 2 and check whether anything in Sections 3 or 4 changes. A conclusion that survives both definitions is worth more than one that needs the right definition.
7. **The full Villa-Torrano release.** The original Zenodo record also holds document edit logs, Moodle logs and questionnaires for these same students. Download it and ask what this extract cannot: how much of the recorded unevenness in chat is offset by the same students' work in the shared document?
8. **The chance floor, in general.** Section 4 simulates a floor for the Gini under equal propensities. Derive or simulate the same floor for a measure you plan to use in your own project, and report your observed value beside it. Most published participation numbers have never been read against their floor.

## Troubleshooting

**"Could not download: collab-chat/chat_logs.csv".** The notebook could not reach the internet. The files live at `github.com/HakeoungLee/edis8100-datasets`. Check your connection and run the first cell again. Nothing else in the notebook will work until that cell prints "All three files loaded."

**"NameError: name 'groups' is not defined".** You skipped ahead. `groups` is built in Section 3 and Sections 4 and 5 both need it. Use **Runtime > Restart and run all** in Colab, or **Kernel > Restart & Run All** in Jupyter. This fixes the large majority of problems.

**"KeyError: 'timestamp'".** You are reading the file without `encoding="utf-8-sig"` on a pandas version that does not strip the byte order mark, or you guessed `latin-1`. Section 1 shows exactly this happening on purpose.

**My charts do not appear.** The very first line of the first code cell is `%matplotlib inline`. If that cell did not run, no figure will render. Restart and run all.

**"ValueError: time data ... does not match format".** You changed the date format string. The file is day first: `%d/%m/%Y %H:%M`.

**Your turn 1 prints nothing.** You asked for a group and day that do not go together. Groups 1 and 2 met on `2021-02-15` and `2021-02-17`. Groups 3 to 8 met on `2021-02-16` and `2021-02-18`. The dates are strings in quotes.

**The messages are in Spanish and I do not read Spanish.** That is expected and it is the honest cost of using this dataset. Every measure in the notebook is built from metadata: who wrote, when, and how much. Nothing asks you to interpret content. The notebook says plainly that giving up content is a large thing to give up in a week about collaboration.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all. The simulations and bootstraps are seeded, so a clean run reproduces the same numbers every time.

**The design review flagged fewer tiles than I expected.** Read the line underneath, which is the important one: the hazard list holds only the problems this notebook happened to surface, from eight groups over four days. A clean review is not a safe dashboard, and treating it as one is the exact failure mode Section 6 is about.

**My refusal list is completely different from my partner's.** Good. There is no answer key in Section 6, only better and worse arguments. Compare the principles you each used, not the slots you each chose.

## A reminder about documenting AI use

This notebook is not a graded submission, but something is due this week: the **Course Research Project Outline**, uploaded to Canvas separately from anything here.

If you used an AI assistant while drafting that outline, or while working through this notebook, the course AI policy requires two things, and they go in two different places in the **AI Reflection** submission on Canvas:

- **The conversation record goes in an attached Word file.** Copy the actual exchanges into a `.docx` and attach it. Prompts, responses, the record itself, not a summary of it.
- **The four reflection questions from the syllabus are answered in the Canvas text box**, directly, not inside the attachment. Copy them in and answer each one: how you used it; whether it helped and how; whether it made your work more challenging in any way; and what lesson about AI from this week you would pass on to a friend or the class.

If you used no AI at all, one line in the text box saying so is a complete and acceptable submission.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use costs you nothing.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
