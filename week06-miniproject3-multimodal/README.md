# 🎙️ Week 6: Mini Project 3, Multimodal Participation

Twenty-four studio groups, seven sensor streams, and one deceptively simple question: who participated?

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
| **Data used** | `students.csv`, `mmla_studio.csv`, `studio_artifacts.csv`, `group_chat.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib |
| **Estimated total time** | 30 minutes to launch in class, 2 to 3 hours to finish including the memo |

## Objectives

By the end of this project you will be able to:

1. **Build** per-student participation profiles across audio, video, and digital modalities, and explain why raw units (seconds, counts, percentages) have to be put on a common scale before anyone compares them.
2. **Compute** the Gini coefficient of speaking time for a small group, interpret it against the ceiling that actually applies to a group of five, and say what it hides.
3. **Disaggregate** a multimodal participation measure by student background using Cohen's *d*, and say precisely what a single-modality measure would have gotten wrong and about whom.
4. **Link** participation structure to a group product, and state in writing the limits of that link before anyone builds an alert on it.

The through-line of the session: **participation is not a thing in the data, it is a thing you decide to measure, and the sensor you choose decides who looks engaged.** In this class the audio stream and the digital stream disagree about the same students, and both of them are "the data."

Two notes on where this sits in the semester. First, the **Gini coefficient is introduced properly here**, with a worked intuition, a Lorenz curve, and its ceiling, because Week 9 treats it as established and goes straight to using it on chat turn-taking. If you skip Section 6 you will be behind in four weeks. Second, this is the week where the claim ladder from Week 2 gets its hardest test: `speaking_time_s` is a feature, "participation" is a construct, and the whole memo is an argument about the rung in between.

## What is in this folder

| File | What it is |
|---|---|
| `week06_miniproject3_multimodal_participation.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the four datasets into the runtime.

Every student, every second of speaking time, and every chat message in these files is **synthetic**. We invented this course precisely so that we can practice reading participation data without surveilling a single real person. The ask in return is that you treat the data as if they were real, because the habits you build here are the habits you will carry into a room with actual students in it.

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

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda.

## Step-by-step walkthrough

The studio block gets you through Section 4, which is where the central finding lands. Sections 5 through 8 and the memo are yours to finish. The four ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long and it is meant to be collapsed. It builds the roster, the multimodal studio file, the artifact scores, and the group chat inside your runtime.

**📊 1. Four files, four grains (4 minutes).** Know what one row of each file means before you compute anything. `mmla_studio.csv` has 960 rows, one per student per session, because 120 students met 8 times. `studio_artifacts.csv` has 192, one per group per session. Getting the grain wrong is the most common way a multimodal analysis goes quietly wrong: it is very easy to average an average and end up describing nobody. Section 1.1 then names the sensor stream behind each of the seven columns and what a careless reader would assume it means. Speaking time runs to 2,581 seconds and idea units rarely pass 10, which is why nothing can be compared until it is rescaled.

**📊 2. From raw sensors to comparable profiles (6 minutes).** Average each student's eight sessions, then convert every modality to a percentile rank within the class. Section 2.1 introduces the week's central case, two members of group G01. Across eight sessions Mikael held the floor for 136 minutes and left 8 substantive ideas in the chat; Solveig spoke for 9 minutes and left 40. The radar chart puts all seven modalities on one picture: Solveig sits at the 2.5th percentile on speaking time and the 95th on idea units, and Mikael is very nearly the mirror image. ✏️ **Your turn 1** repeats the exercise on any two students you like.

**📊 3. A whole group at once (6 minutes).** A radar chart is comfortable for two students and unreadable for five, so groups get a parallel coordinates plot instead: one vertical axis per modality, one line per student. Crossing lines are the signal, because they mean the ranking of students reorganizes depending on which sensor you consult. Multilingual students are drawn with dashed lines as well as their own color so the distinction survives a black-and-white printout. ✏️ **Your turn 2** points the same function at any group from G01 to G24.

**📊 4. Who flips? The whole class at once (8 minutes).** Two students and one group are anecdotes. Now plot all 120 by two percentiles, speaking time against idea units, with the region that should not exist shaded: quiet on audio, top third on ideas. Sixteen students live there. Multilingual students are 20 percent of this class and 56 percent of that group, which is 2.8 times their base rate. This is the finding the memo has to deal with, and the question the notebook asks is whether it is a story about those students or a story about the microphone.

**📊 5. Disaggregating: the same class, seven measures, two stories (8 minutes).** Recompute every modality separately for multilingual and non-multilingual students, standardized as Cohen's *d* so that seconds and counts can sit in the same chart. Speaking time comes back at *d* = -0.59 and turns at -0.58. Idea units come back at +0.52 and doc edits at +0.41. The audio and video streams point one way, the digital stream points the other, and a single-modality report would have confidently published half of that. ✏️ **Your turn 3** switches the grouping column to `first_gen`, where the effects are much smaller and do not point consistently in any direction. Reporting a null honestly is part of the job.

**📊 6. Measuring balance: the Gini coefficient, carefully (12 minutes).** The unit of analysis changes here, from the student to the group in one session. The section walks the intuition (line five people up from least talk to most, and watch how fast the accumulated share climbs), draws Lorenz curves for four invented groups so that a number like 0.45 acquires a feel, and states the formula. It also states the detail most dashboards get wrong: **in a group of five the maximum possible Gini is 0.8**, not 1.0. Then it computes the number for all 192 real sessions. The mean is 0.348, the most balanced session is 0.070, and the most dominated is 0.681, a session in which one student took 80 percent of the floor and one took none.

**📊 7. Does balanced talk go with a better group product? (10 minutes).** Two ways of asking, because one way is never enough. Across 192 sessions the correlation between talk Gini and artifact score is -0.33; aggregated to 24 groups it is -0.52. The most balanced third of sessions average 7.05 on the rubric and the most dominated third average 6.09, a difference of 0.96 rubric points and a Cohen's *d* of +0.69. Then read the warning underneath, because the scatter is a cloud and the tercile bars overlap by a full standard deviation, and somebody is about to propose an alert that fires at Gini 0.5. ✏️ **Your turn 4** runs the same Gini analysis on a different modality, and one of the three suggested columns behaves very differently from the others.

**✏️ 8. Stretch: build a fairer participation index and defend it (15 minutes, optional).** Everything above this is the core path. Here you combine modalities into a weighted composite and re-rank the class. With voice alone, 11 of the 24 multilingual students land in the flagged bottom quarter, which is 46 percent of them. With an equal-weight composite of voice, ideas, and document work, 5 do, which is 21 percent. The section is explicit that this is not automatically fairer: it is harder to explain to a student, it assumes chat and speech are interchangeable evidence, and the weights are a value judgment rather than a statistical finding.

**💬 9. Reflection (20 minutes).** Five prompts, four of them tied to this week's readings by author. Two to four sentences each. These are the notes you will draw on for the memo, so do them before you write it rather than after.

**📝 10. The inclusive participation memo (45 to 60 minutes).** The deliverable. About 500 to 700 words addressed to the instructor of EDUC 1010, who has asked a plain question: can the studio sensor data be used to give a participation grade? The memo must report actual numbers from at least two named figures or tables, name the measurement problem in language a colleague without statistics can follow, take a position on the group-level finding including one alternative explanation, make a recommendation you can live with, and state the limits. **A clear refusal, well argued, earns full credit.**

**✅ 11. Submission checklist.** Work through it before you upload. It includes the one that catches people: the numbers quoted in your memo must match the numbers printed in your notebook.

## Mini Project rubric

Mini Project 3 is worth 100 points. Five criteria, 20 points each.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Thoughtfully completes data, preparation, analysis, and interpretation with coherence. | Completes most stages clearly. | Some stages incomplete or weakly connected. | Workflow is minimal or fragmented. |
| **Data Preparation and Technical Care** | Careful, transparent, and well-documented preparation decisions. | Appropriate preparation with documentation. | Partial or uneven preparation. | Minimal or unclear preparation. |
| **Analysis and Visualization Choices** | Methods and visuals are well-justified and aligned with the questions. | Analyses and visuals are appropriate. | Partial misalignment or clarity issues. | Inappropriate or missing analyses. |
| **Interpretation and Educational Meaning** | Interpretation connects findings to learning, teaching, or decision-making. | Interpretation is reasonable and evidence-based. | Interpretation is tentative or weak. | Minimal or absent interpretation. |
| **Critical Reflection: Limits, Ethics, Equity** | Thoughtfully addresses limitations and ethical and equity implications. | Identifies key considerations. | Mentions considerations superficially. | Does not address considerations. |

What this means in practice for Week 6. The percentile normalization in Section 2 and the grain checks in Section 1 are where **Data Preparation and Technical Care** is earned or lost, so say out loud in a markdown cell why you rescaled and what rescaling threw away. The choice between the radar, the parallel coordinates plot, and the Cohen's *d* bar chart is **Analysis and Visualization Choices**, and each one is defensible for a different audience. The memo is where **Interpretation and Educational Meaning** and **Critical Reflection** live, and the fifth criterion is not a paragraph you add at the end: naming who the 16 quiet contributors are, and what a voice-only measure would have done to them, is the substance of the project rather than a caveat on it.

## What this connects to in the readings

- **Ochoa (2022)**, *Multimodal learning analytics: Rationale, process, examples, and direction*: the pipeline from physical signal to sensor to feature to interpretation, and the insistence that every stage is a modeling choice that throws information away. The sensor table in Section 1.1 is built directly on that argument, which is why its third column names what each number is carelessly read as rather than what it is.
- **Worsley, Martinez-Maldonado, and D'Angelo (2021)**, *A new era in multimodal learning analytics: Twelve core commitments to ground and grow MMLA*: the case that MMLA is accountable to the people being sensed and not only to the sensors. Section 4 is the test case. Sixteen students are misrepresented by the microphone, and the reflection asks which of the twelve commitments your own analysis strained the most and what you would have to change about the study design, not the code, to meet it.
- **Lee, Sung, Celedón-Pattichis, and Pattichis (2026)**, *Toward an inclusive understanding of collaborative learning using MMLA: Exploring multimodal participation dynamics by gender and linguistic diversity*: the argument that Section 5 is designed to let you meet on your own data. Read it before you write the memo, and be honest about where your findings echo it and where the data stayed silent.
- **Mohammadi and colleagues (2025)**, *Artificial intelligence in multimodal learning analytics: A systematic literature review*: a map of how AI is currently being used across MMLA. The reflection question is the practical one: given what a single modality did to a fifth of this class, what would you require of an automated multimodal participation system before you let it inform a grade?

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Session-level instability.** Everything in Section 2 averages a student's eight sessions before ranking them. Compute each student's speaking-time percentile separately per session and plot the range. How many students move more than 30 percentile points across the term, and would a measure that unstable survive being shown to the student it describes?
2. **Group composition, not group balance.** The Gini result says balanced groups make better artifacts. Test the rival explanation. Compute, per group, the number of multilingual members and the mean prior GPA from `students.csv`, and regress artifact score on Gini plus those two. Does the Gini coefficient still carry its weight, or was it standing in for who happened to be in the room?
3. **Use the chat text, not just the counts.** `group_chat.csv` has the actual messages. Compute median message length and the share of messages containing a question mark, per student, and add them as two more modalities to the composite index. Then ask the harder question the notebook does not: does `idea_units_chat` agree with anything you can compute from the raw text, and what would you do if it did not?
4. **A defensible ceiling correction.** The notebook notes that the maximum Gini for a group of five is 0.8. Rescale every session's Gini by that ceiling so the measure runs from 0 to 1, re-run the correlation with artifact score, and write two sentences on whether the rescaling changed any conclusion. Then decide whether a dashboard should report the raw or the corrected number, and to whom.
5. **Cross-modality agreement as its own measure.** For each student compute the spread of their seven percentile ranks, for example the gap between their highest and lowest. Students with a large spread are the ones any single-sensor measure will misrepresent. Rank the class by that spread, check who is at the top, and argue for or against putting that number on a teacher's dashboard as a "read this student carefully" flag.

## Troubleshooting

**"NameError: name 'profile' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart session and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/mmla_studio.csv".** The setup cell did not run, or the runtime disconnected and you skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the first code cell of Section 1, which contains the imports and `%matplotlib inline`. If they still do not appear, restart and run all.

**"KeyError: 'S121'" in a Your turn cell.** The roster runs from `S001` to `S120`, and group IDs run from `G01` to `G24`. Both are zero-padded, so `S15` and `G1` will not match anything either.

**The radar chart looks like a triangle with one enormous spike.** You are probably plotting raw values rather than percentiles. The radar function expects the percentile table built in Section 2. If you changed the input, change it back and re-run from Section 2.

**My Gini is above 0.8 and I thought that was the maximum.** For a group of five it is. A value above it means the group in your slice does not have five members, most likely because you filtered or merged something upstream. Print the row count per group and session before you compute anything else.

**Cohen's *d* came out negative and I expected positive.** The sign is a direction, not a verdict. In Section 5 a positive *d* means multilingual students score higher on that modality. Read the column header before you read the number, and say the direction out loud in the memo rather than reporting a magnitude on its own.

**My colors are hard to tell apart.** The multilingual lines in Section 3 are dashed as well as colored, on purpose. If you are adding your own figures, do the same: never let a distinction live in color alone, and never let it live in red against green.

**My numbers do not match the ones in this README.** If you changed a ✏️ **Your turn** cell or the composite weights, that is expected and good, and you should report your numbers rather than these. If you did not, restart and run all: the data generator is seeded, so a clean run reproduces the same numbers every time.

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

If you used a chatbot or coding assistant for any part of this project, including debugging a chart, checking your understanding of the Gini coefficient, or tightening the wording of the memo, it belongs in the log. Say what you accepted, what you rejected, and how you verified it. If an AI tool told you something about Gini coefficients or effect sizes, say how you checked it, because this is a week where a confident wrong answer about a ceiling value would have quietly broken your interpretation.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use is normal scholarly practice, and in a course about analytics it is also a data point about your own learning process.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
