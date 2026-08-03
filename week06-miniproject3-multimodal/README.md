# 🎙️ Week 6: Mini Project 3, Multimodal Participation

Thirty-nine pairs of children, two independent ledgers of the same forty minutes, and one deceptively simple question: who participated?

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 30, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Multimodal Learning Analytics |
| **Guest speaker** | None. Dr. Lee leads the interactive lecture, and the student-led discussion runs from 5:00. |
| **In-class time on this notebook** | About 30 minutes, launched in the hands-on studio block (4:30 to 5:00). That gets you through Section 4. The rest, including the memo, is finished outside class. |
| **Deliverable** | **Mini Project 3**, submitted through Canvas: the completed notebook, the inclusive participation memo, and the AI interaction log plus reflection. |
| **Due date** | This week, per the Canvas due date. The **Mid-Semester Check-In** is also due this week, so start early. |
| **Notebook** | `week06_miniproject3_multimodal_participation.ipynb` |
| **Data used** | **Real, published, openly licensed.** The **JUSThink Dialogue and Actions Corpus** and its **PE-HRI** companions, from the CHILI lab at EPFL: `per_participant.csv` (78 children), `participant_with_team_channels.csv` (68 children joined to team channels), `pehri_team_outcomes.csv` (34 teams), `pehri_temporal.csv.gz` (4,676 ten-second windows). Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`. **CC BY 4.0.** |
| **Citation** | Norman, U., Dinkar, T., Nasir, J., Bruno, B., Clavel, C., & Dillenbourg, P. (2021). *JUSThink Dialogue and Actions Corpus* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4627104 <br> Nasir, J., Norman, U., Bruno, B., Chetouani, M., & Dillenbourg, P. (2021). *PE-HRI: A multimodal dataset for the study of productive engagement in a robot-mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4633092 <br> Nasir, J., Bruno, B., & Dillenbourg, P. (2024). *PE-HRI-temporal: A multimodal temporal dataset in a robot mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.13834073 |
| **Libraries** | pandas, numpy, matplotlib, scipy |
| **Estimated total time** | 30 minutes to launch in class, 2 to 3 hours to finish including the memo |

## What the data is

Thirty-nine pairs of children aged 9 to 12, in Switzerland, each pair at two screens with a humanoid robot between them, solving a **minimum spanning tree** problem: connect every town on a map of Swiss railways using the cheapest set of tracks. A logger recorded every edge each child added and removed and every button they pressed. Each child took a **10-item test** of the underlying idea before and after, so `gain` runs from -10 to +10 and in practice from -3 to +3.

For **10 of the 39 pairs**, the sessions were also transcribed, giving speech seconds, speaking turns, and word counts per child.

So for **20 children** there are two independent ledgers of the same forty minutes: what they said, and what they did. The whole project is what happens when those two ledgers are laid side by side.

Two companion releases describe the same activity at the level of the **team**: PE-HRI (34 teams, gaze and affect and speech-activity summaries plus learning outcomes) and PE-HRI-temporal (32 teams re-described in 10-second windows, 4,676 rows, about 13 hours of interaction).

Both corpora are **CC BY 4.0**. You may download, adapt, and redistribute them, including commercially, as long as you give credit. Section 7 of the notebook explains why that fact deserves a paragraph of its own.

## Objectives

By the end of this project you will be able to:

1. **Read** a real multimodal corpus at its true grain, including the part most published analyses skip: which children have which channels, and what it costs to keep only the ones who have both.
2. **Compare** two channels of participation on the same children, and state with an interval, not a point estimate, how much one tells you about the other.
3. **Recognise and correctly handle** non-independence when rows nest inside pairs, including the case where two rows are mathematically forced to mirror each other.
4. **Separate** a between-team association from a within-team one, and explain why an individual participation grade needs the second and this corpus only supplies the first.
5. **Audit** a dataset for what it does not record, and argue about what that absence does to an equity question.

The through-line of the session: **participation is not a thing in the data, it is a thing you decide to measure, and the sensor you choose decides who looks engaged.** In this corpus the microphone and the event log disagree about the same children, and both of them are "the data".

Two notes on where this sits in the semester. First, this is the week the claim ladder from Week 2 gets its hardest test: `speech_secs` is a feature, "participation" is a construct, and the whole memo is an argument about the rung in between. Second, this is the week the course stops treating **sample size and nesting** as a caveat and starts treating them as the subject. Week 9 assumes you can tell a between-group claim from a within-group one, so do not skip Section 5.2.

## What is in this folder

| File | What it is |
|---|---|
| `week06_miniproject3_multimodal_participation.ipynb` | The notebook. Downloads its four data files from the course dataset repository in the first code cell. Runs top to bottom untouched in about a minute. |
| `README.md` | This file. |
| `data/` | Not used this week. The notebook reads directly from the dataset repository over the network. |

You do not need to clone anything or download a CSV by hand. The first code cell fetches all four files. If your network blocks `raw.githubusercontent.com`, the cell prints a plain four-step message naming `github.com/HakeoungLee/edis8100-datasets` rather than a traceback.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week06-miniproject3-multimodal/week06_miniproject3_multimodal_participation.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week06-miniproject3-multimodal/week06_miniproject3_multimodal_participation.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week06-miniproject3-multimodal/week06_miniproject3_multimodal_participation.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository. For a graded project this matters more than usual: the copy in Drive is what you will download and submit.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and scipy, all of which ship with Anaconda.

## Step-by-step walkthrough

The studio block gets you through Section 4, which is where the central case lands. Sections 5 through 8 and the memo are yours to finish. The four ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything.

**⚙️ Setup (2 minutes).** A markdown cell states the dataset, who collected it, the licence, and the citation, **before** anything is loaded. Then one code cell: `%matplotlib inline`, the imports, the four downloads wrapped so a network failure prints instructions instead of a traceback, and a confirmation of what arrived.

**📊 1. Four files, four grains (5 minutes).** Know what one row of each file means before you compute anything. `children` is one row per child. `joined` is one row per child with that team's channel summary repeated on both rows, so two children in the same pair carry identical gaze and affect values that are not about either of them. `team_out` is one row per team. `temporal` is one row per team per window. The notebook then **checks the window size rather than trusting a README**: the gap between consecutive rows of a team is 10 seconds, in every team, with no other value. Sessions run 10.7 to 36.0 minutes, median 23.2, and 13.0 hours in total. And the temporal file has no `who` column, which becomes Section 8.

**📊 1.1 The mess, in front of you (6 minutes).** Fifty-eight of seventy-eight children have no speech record, and the gaps are not scattered: **10 whole teams were transcribed and 29 were not**. A two-panel figure shows the channel counts and all 39 teams as a labelled grid. The notebook then makes the decision in front of you and prices it: analyse the 20 children with both channels, accept that ten pairs is a small study, accept that nothing in the released files says how those ten were chosen, and recompute on all 78 children wherever that is possible. The interpretation prompt asks for a reason the transcribed teams look the way they do that has nothing to do with the children.

**📊 2. Two ledgers of the same forty minutes (10 minutes).** Each child gets their **share of their own pair** on each channel, because one pair talked for fifteen minutes and another for twenty-five and raw seconds mostly compare sessions. Then **Section 2.1, which is the methodological heart of the week**: within a pair the two shares must sum to exactly 1, so the second row of every pair carries no information the first did not, and a correlation across twenty children has ten observations in it wearing a costume. The notebook **proves** this rather than asserting it, recomputing the correlation from the ten pair deviations alone and checking it matches to six decimal places. Every interval from here on is a cluster bootstrap that resamples whole pairs. The result: speech share against action share is **r = +0.208, 95% CI [-0.262, +0.697]**; word share against edge-add share is **r = +0.015, 95% CI [-0.659, +0.784]**. ✏️ **Your turn 1** points the same machinery at any two channels, and the default, turns against seconds, returns **r = +0.966** as a calibration point for what agreement actually looks like.

**📊 3. Half the pairs swap places (8 minutes).** Counting, done correctly. A swap is a property of the **pair**, not the child: if A is above 0.5 on speech and below on actions, B is necessarily the mirror. So counting children double counts. **5 of 10 pairs swap, 95% CI [24%, 76%]**; the tempting child-level version gives the same 50% with an interval **24% narrower** than it should be, and the notebook prints both side by side. A slopegraph draws every child's line from speech share to action share, orange and solid where it crosses the line. ✏️ **Your turn 2** replaces the arbitrary 0.50 threshold with a question about the **size** of the gap: 6 of 10 pairs disagree by at least 0.05, 4 by at least 0.10, 3 by at least 0.15, 2 by at least 0.20, none by 0.30.

**📊 4. Team 47 belongs on a slide (6 minutes).** One pair, twenty minutes. Child A produced **505 seconds of speech against child B's 163**, which is **75.6% of the pair's speech** and **78.4% of its words**. On the map child A made **84 moves against child B's 99**, which is **45.9% of the pair's interface actions**. Both children scored one point lower after the session than before. Two panels: the split by channel, and the raw seconds against the raw clicks on two axes because seconds and clicks are not comparable numbers. The interpretation prompt asks which child you would have written down as the active participant, which channel you were using, and then requires three explanations of the pattern with at least two of them about the situation rather than the children.

**📊 5. The question the memo turns on (12 minutes).** Look at the outcome before correlating anything with it. Mean gain is **+0.10 items on a 10-item test, 95% CI [-0.24, +0.44]**, an interval containing zero: this activity produced no detectable average improvement on this instrument. Thirty-one children scored higher, 24 the same, 23 lower. Then the comparison, all with cluster-bootstrap intervals and Spearman beside Pearson: **speech seconds vs gain r = +0.015 [-0.36, +0.35]**, speech share vs gain **r = -0.089**, **interface actions vs gain r = +0.404 [-0.13, +0.79]**, and on all 78 children **+0.170 [-0.09, +0.39]**. The headline: **the channel an instructor would instinctively grade is the one carrying no signal.**

**📊 5.2 The +0.40 is about pairs, not about children (12 minutes).** This is the section that makes the finding correct rather than merely striking. Children in a pair worked on the same map for the same length of time, so their counts are related before anyone looks: the **ICC of interface actions is +0.53**, against **+0.00 for pre-test score**. The child-level correlation is then decomposed. **Between pairs, across all 39: r = +0.289, 95% CI [-0.029, +0.554].** **Within pairs, across all 78 children: r = -0.059.** The busier child of a pair did not gain more. So: speech carries no signal about who learned, interface actions carry a signal about **the pair**, and nothing in this corpus carries a signal about **which child of a pair** learned more. ✏️ **Your turn 3** runs the decomposition on any channel and warns you when the ICC is so high that the channel cannot tell two children apart at all.

**📊 6. How fragile is a number built on ten pairs? (8 minutes).** Two checks small studies should publish and rarely do. **Leave one pair out**: drop team 10 and the speech-versus-actions correlation falls from **+0.21 to -0.02**; the actions-versus-gain correlation swings from **+0.30 to +0.57** depending which single pair you remove. **The same number in two files**: `per_participant.csv` has 20 children with both channels, `participant_with_team_channels.csv` has 18 because team 11 is absent from the PE-HRI release, and that one absent pair moves the headline from **+0.404 to +0.332**. Nothing errors. Nothing warns you.

**🔍 7. The column that is not there (15 minutes).** The section where the equity analysis is attempted and fails. `children.groupby('first_language')` raises a `KeyError`, caught and printed plainly. Then a systematic audit of all **125 columns across the four files** against a list of person-attribute patterns: **zero matches**. A classification of every column shows 41 for interface actions, 24 for speech, 16 for gaze, 13 for affect, 13 for bookkeeping, 11 for outcomes, 7 for shares, and **0 for attributes of the child**. The corpus records the age range and nothing else. The study ran in Switzerland, in an activity conducted in English, so linguistic variation was in the room and went unrecorded, and the channel most likely to be unequal is the one present for a quarter of the sample. **Section 7.1 corrects a claim this course has been making**: multimodal data is mostly gated, the corpora at Oulu and Monash among them, and **this one is not**, because one lab did the work of releasing derived features under CC BY 4.0. Gating is a choice, not a law of nature. ✏️ **Your turn 4** is not a code cell: pick another open corpus, fill in a seven-row audit table, and bring it to class.

**📊 8. The finest-grained file dissolves the individual (8 minutes).** The temporal file at 10-second resolution, checked rather than trusted: `T_action_inc` is a running total, `T_speech_activity_inc` is a running mean, and both claims are verified in code. The derived team file is checked against the raw child file, and `T_LG_absolute` turns out to equal the pair's mean gain divided by 10 to within 1e-16, so reporting both would be reporting one thing twice. Then a real inconsistency that is not explained away: team action totals differ across files, agreeing exactly in **2 of 32 teams**, differing by **-13 to +30 actions**, a mean absolute gap of **8.1 actions or 4.4% of the team total**. The notebook names the decision (per-child counts for per-child questions, team counts for team questions, never divide one by the other) and its cost. The figure plots team 47 across 117 windows, and the point of it is that there is one green line where Section 4 showed a 76-to-24 split.

**💬 9. Reflection (20 minutes).** Six prompts, four tied to this week's readings by author and one addressed to the people who released the data. Two to four sentences each. Do them before the memo rather than after.

**📝 10. The inclusive participation memo (45 to 60 minutes).** The deliverable. About 500 to 700 words to a colleague who asks whether logged clicks plus a microphone can support an individual participation grade. The memo must report real numbers **with intervals**, name the measurement problem in plain language, take a position on the nesting, make a recommendation, and state the limits including the one that is an absence. **A clear refusal, well argued, earns full credit.**

**✅ 11. Submission checklist.** Includes the one that catches people this week: **every number in your memo carries its interval or its sample size.** A bare correlation from ten pairs is the one thing this week is designed to make you unable to write.

## Mini Project rubric

Mini Project 3 is worth 100 points. Five criteria, 20 points each.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Thoughtfully completes data, preparation, analysis, and interpretation with coherence. | Completes most stages clearly. | Some stages incomplete or weakly connected. | Workflow is minimal or fragmented. |
| **Data Preparation and Technical Care** | Careful, transparent, and well-documented preparation decisions. | Appropriate preparation with documentation. | Partial or uneven preparation. | Minimal or unclear preparation. |
| **Analysis and Visualization Choices** | Methods and visuals are well-justified and aligned with the questions. | Analyses and visuals are appropriate. | Partial misalignment or clarity issues. | Inappropriate or missing analyses. |
| **Interpretation and Educational Meaning** | Interpretation connects findings to learning, teaching, or decision-making. | Interpretation is reasonable and evidence-based. | Interpretation is tentative or weak. | Minimal or absent interpretation. |
| **Critical Reflection: Limits, Ethics, Equity** | Thoughtfully addresses limitations and ethical and equity implications. | Identifies key considerations. | Mentions considerations superficially. | Does not address considerations. |

What this means in practice for Week 6. **Data Preparation and Technical Care** is earned in Sections 1.1 and 2.1: say out loud why you kept 20 children out of 78 and what that cost, and say why the intervals resample pairs rather than children. **Analysis and Visualization Choices** is the decomposition in Section 5.2 and the choice to show a scatter rather than quote a threshold count. **Interpretation and Educational Meaning** and **Critical Reflection** live in the memo, and the fifth criterion is not a paragraph you add at the end: Section 7 is a finding about the field, and the memo that treats the missing column as a limitation rather than as evidence has understood the week backwards.

## What this connects to in the readings

- **Ochoa (2022)**, *Multimodal learning analytics: Rationale, process, examples, and direction*: the pipeline from physical signal to sensor to feature to interpretation, and the insistence that every stage is a modelling choice that throws information away. Section 1 and Section 8 are that argument in code, including the moment where a 10-second window and a per-child count turn out not to add up.
- **Worsley, Martinez-Maldonado, and D'Angelo (2021)**, *A new era in multimodal learning analytics: Twelve core commitments to ground and grow MMLA*: the case that MMLA is accountable to the people it senses. Section 7 is the test case, and the reflection asks you to name a real trade-off rather than pick a side: releasing the missing columns would have strained a different commitment than omitting them did.
- **Lee, Sung, Celedón-Pattichis, and Pattichis (2026)**, *Toward an inclusive understanding of collaborative learning using MMLA: Exploring multimodal participation dynamics by gender and linguistic diversity*: the analysis you cannot replicate this week, which is why it is assigned this week. The reflection asks precisely which part of their argument this corpus can still speak to.
- **Mohammadi and colleagues (2025)**, *Artificial intelligence in multimodal learning analytics: A systematic literature review*: a map of how AI is being used across MMLA. Given Section 5.2, where the only reliable signal was about pairs, what would you require of an automated system before it produced a number attached to an individual child's name?
- **Norman, Dinkar, Nasir, Bruno, Clavel, and Dillenbourg (2021)** and **Nasir, Norman, Bruno, Chetouani, and Dillenbourg (2021)**, the data papers. Read the Zenodo records. They are short, and reading the documentation of a corpus you are about to criticise is the minimum standard for criticising it.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **The gaze and affect channels.** `participant_with_team_channels.csv` carries `at_partner`, `at_robot`, `screen_left`, `screen_right`, `positive_valence`, `negative_valence`, `arousal`, and `smile_count`. Every one of them is a **team** value repeated on both of the pair's rows. Verify that, then write two sentences on what it means that a file with one row per child contains eight columns that cannot vary between children. Then check whether the five gaze percentages sum to 100 in the temporal file. They do not, in 92% of rows. Decide what that permits you to say about gaze and what it does not.
2. **Rebuild Section 5 as a proper mixed model.** The notebook decomposes by hand, which is transparent and slightly crude. Fit `gain ~ actions + (1 | team)` with `statsmodels` and compare the fixed effect to the within-pair correlation. Report whether the conclusion changes and, more usefully, whether the interval does.
3. **Use the temporal file for a temporal question.** Section 8 uses it only as an illustration. Compute, per team, the correlation between speech activity and action rate across windows, then ask whether teams whose talk and work rise and fall together had different outcomes. Work at 32 teams, not 4,676 windows, and say why in a comment.
4. **The transcription selection.** Compare the 10 transcribed teams against the other 29 on everything the complete files record: actions, adds, presses, pre-test, gain. If they differ systematically, the 20-child analysis has a selection problem you should name in the memo. If they do not, say what that does and does not rule out, and give the comparison an interval.
5. **Write the missing data statement.** Draft the paragraph the original authors could have published: what person-level variables would have made an equity analysis possible, what protections each would have required for children aged 9 to 12, and what you would have released. One page. This is the stretch goal most likely to end up in a dissertation chapter.

## Troubleshooting

**"The data did not download."** The first code cell prints a four-step check. Work through it in order. The most common cause is a campus, school, or hospital network blocking `raw.githubusercontent.com`. Running the notebook in Google Colab almost always fixes it. Do not spend twenty minutes alone with this; post on Canvas with a screenshot.

**"NameError: name 'both' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart session and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**My charts do not appear.** Make sure you ran the first code cell, which begins with `%matplotlib inline`. Without that line the notebook stores no figures at all. If they still do not appear, restart and run all.

**"KeyError: 'first_language'".** That one is deliberate. It is Section 7, and the error is the point. Keep going.

**My `speech_secs` column is mostly empty.** It is supposed to be. Only 10 of the 39 teams were transcribed. Section 1.1 is about exactly that, and dropping those rows silently is the mistake the section exists to prevent.

**My numbers do not match the ones in this README.** If you changed a ✏️ **Your turn** cell, that is expected and good, and you should report your numbers rather than these. If you did not, restart and run all. The bootstraps are seeded with `SEED = 8100`, so a clean run reproduces the same intervals every time. If a number still differs, tell the instructor: the dataset repository may have been updated, and that is worth knowing.

**"Why is the correlation different when I use the other file?"** Because it is a different set of children. That is Section 6, and noticing it unprompted is worth more than most of the rest of the assignment.

**My interval looks impossibly narrow.** Check what you resampled. If you resampled children rather than pairs, you broke the pair structure and invented confidence. Use `pair_bootstrap_r`, which resamples whole teams, and read Section 2.1 again.

**Cohen's d, Gini, and the other Week 6 tools I was expecting are not here.** They are not in this version. Every team in this corpus has exactly two children, and a Gini coefficient on two people has a ceiling of 0.5 and carries no information that the larger child's share does not already carry, so **share of the pair** is the two-person special case and the notebook uses that instead. There are also no recorded groups of children to compare, so there is nothing for an effect size to stand between. Section 5.2's within-and-between decomposition does the work Cohen's *d* used to do here, and does it more correctly.

> **Note for the instructor.** The Week 9 notebook currently opens its unevenness section with "Week 6 introduced the **Gini coefficient** properly, so one sentence of recall is enough." That sentence needs changing: this notebook no longer introduces it. Week 9 is close to self-contained already, since it states the ceiling formula and the dyad ceiling itself, so the fix is a short paragraph rather than a new section.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**The notebook will not download as `.ipynb`.** In Colab use **File > Download > Download .ipynb**. Do not submit a `.py` export or a PDF: the graders need to see the outputs, which is why the checklist asks you to run it top to bottom one last time before downloading.

## A reminder about documenting AI use

Mini Project 3 has a Canvas **AI Reflection** submission alongside the project itself, and it has two parts that go in two different places. Getting them the right way round matters.

1. **The conversation record goes in a Word file, attached to the AI Reflection submission.** Ask your AI tool to copy out only the back-and-forth messages between you and it, in full, with no summarizing and no system or tool messages. Paste that into a Word document and attach the document. Do not paste your interactions into the Canvas text box.
2. **The reflection goes in the Canvas text box, not in the Word file.** Copy the four questions into your reply and answer each one:
   1. How did you use it?
   2. Did AI help you with your work this week? If so, how?
   3. Did it make your work more challenging in any way? If so, how?
   4. What new lessons, if any, could you share with a friend or the class that summarize what you learned about AI through this week's work?

Two things worth checking specifically this week, because both are common failure modes rather than hypotheticals. First, if an AI tool computed or interpreted a correlation for you, did it mention that the rows are children nested inside pairs? Most will not unless you tell them. Say what you had to add to the prompt to get a correct answer. Second, if you asked a tool about the equity implications of this dataset, check whether it **invented a demographic variable**. There is no such column anywhere in the 125, and a confident answer that assumes one is the exact failure Section 7 is built to catch.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use is normal scholarly practice, and in a course about analytics it is also a data point about your own learning process.

## Data credit

This project is built entirely on other people's work, released openly so that it could be.

> Norman, U., Dinkar, T., Nasir, J., Bruno, B., Clavel, C., & Dillenbourg, P. (2021). *JUSThink Dialogue and Actions Corpus* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4627104

> Nasir, J., Norman, U., Bruno, B., Chetouani, M., & Dillenbourg, P. (2021). *PE-HRI: A multimodal dataset for the study of productive engagement in a robot mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4633092

> Nasir, J., Bruno, B., & Dillenbourg, P. (2024). *PE-HRI-temporal: A multimodal temporal dataset in a robot mediated collaborative educational setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.13834073

CHILI lab, École Polytechnique Fédérale de Lausanne. All three **CC BY 4.0**. The licence requires attribution, and so does the fact that seventy-eight nine-to-twelve-year-olds and their families agreed to be recorded.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
