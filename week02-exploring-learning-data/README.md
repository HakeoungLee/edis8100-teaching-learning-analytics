# 📊 Week 2: Exploring Learning Data

Finding out how far a column in a CSV is from a thing that matters.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 2, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Mapping the Learning Analytics Landscape and Theoretical Lenses |
| **Guest speaker** | None. Dr. Lee leads the discussion this week so that you can watch the facilitation moves you will be using from Week 3 onward. |
| **In-class time on this notebook** | About 35 minutes, in the hands-on block (4:35 to 5:10). The core path is built to fit that window. |
| **Deliverable** | None. Week 2 is in-class work only. |
| **Due date** | Not applicable. The first Canvas deliverable is Mini Project 1 in Week 4. |
| **Notebook** | `week02_exploring_learning_data.ipynb` |
| **Data used** | `students.csv`, `lms_clickstream.csv`, `gradebook.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib |
| **Prior coding experience needed** | None |

## Objectives

By the end of this activity you will be able to:

1. **Aggregate** 41,117 raw clickstream events down to one row per student with `groupby`, and **join** that table to the gradebook with `merge`, checking after every join that nobody silently disappeared.
2. **Read** a scatterplot of activity against achievement and say out loud what an `r` of 0.335 does and does not license you to claim.
3. **Use the claim ladder** (feature, indicator, construct) to name the distance between a number the system happened to record and a thing that theory says matters.
4. **Notice a temporal pattern** in when work gets submitted, and write one claim plus the evidence that would be needed to defend it.

The through-line of the session: **the claim ladder is a Week 2 idea and the whole semester leans on it.** A feature is arithmetic and free. An indicator is a feature you have argued stands in for something educational, and that argument is the work. A construct is the thing you actually care about, and no column contains it. Week 3 audits a model built on features that were promoted to indicators without an argument. Week 6 asks which sensor deserves the word "participation." Week 7 asks whether a loop rate reaches self-regulation. Every one of those weeks points back here, so it is worth being able to say the three rungs from memory.

## What is in this folder

| File | What it is |
|---|---|
| `week02_exploring_learning_data.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the three datasets into the runtime.

The data describe **EDUC 1010: Learning How to Learn**, an eight-week blended course at Blue Ridge University with 120 students. Neither the course nor the students exist. They are synthetic on purpose: learning analytics runs on records about people who rarely got a say in being measured, and a class exercise is a poor reason to touch a real student's file. The ask in return is that you treat these files as if they were real.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week02-exploring-learning-data/week02_exploring_learning_data.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week02-exploring-learning-data/week02_exploring_learning_data.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week02-exploring-learning-data/week02_exploring_learning_data.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda.

## Step-by-step walkthrough

Total time is about 35 minutes if you keep moving. The three ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. The reading is the work. The code is short.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the roster, the clickstream, and the gradebook inside your runtime so that nothing has to be downloaded and no real student data is ever involved.

**📊 1. Meet the tables (3 minutes).** Two files with two very different origins. `lms_clickstream.csv` is a **log**, 41,117 rows of exhaust from a system doing its job, and nobody designed it to answer a research question. `gradebook.csv` is a **measurement**, 1,080 rows produced on purpose by an instrument somebody built. Learning analytics almost always means putting the first kind of data next to the second kind and arguing about the pairing. Notice the grain of each file before you go on.

**📊 2. From 41,117 events to 120 students (4 minutes).** `groupby` is the tool that moves between grains, and this is where you meet it. The median student generated a little over 300 events, the busiest generated 1,144, and the quietest generated 25. The histogram makes the heavy tail obvious. Section 2b then splits by two keys at once, student and event type, because educational meaning usually lives in the breakdown rather than the total.

**💬 3. The claim ladder (5 minutes).** Stop here. This is the section the rest of the semester points back to. A three-row table lays out feature, indicator, and construct, with `total_events = 412` as the feature and engagement as the construct that no column contains. Then there is a text cell where you finish three sentences about your own work. Type in it. It takes two minutes and it is the only writing the notebook asks for.

**📊 4. The other table, then the join (3 minutes).** Two defensible judgment calls are hiding in three lines of code: we keep the eight quizzes and drop the final project, and we take the mean of a student's quiz scores. A mean hides growth, which Week 7 comes back for. Then `merge` on `student_id`, with the row count printed before and after, because an inner join is where students quietly vanish from an analysis.

**📊 5. Does activity buy achievement? (5 minutes).** The plot that launched a thousand dashboards: effort on the x axis, outcome on the y axis. Write your prediction down before you run it. The correlation comes back at `r = 0.335`, so `r` squared is 0.112, which means about 89 percent of the variation in quiz scores is doing something other than tracking click volume. Sit with that before you move on.

**📊 5b. Look at the students the line gets wrong (4 minutes).** Two views. First a tercile table: mean scores climb from 72.4 to 79.5 across the three activity groups, but the spread inside any one group is far wider than the distance between groups, and 32 percent of the low-activity third beat the median of the high-activity third. Then the map: 8 students sit in the low-activity, high-score corner, several near the top of the class on roughly a third of their peers' clicks. Week 3 builds the model that would flag every one of them.

**✏️ Your turn 1: build a different feature (2 minutes).** `total_events` counts logins, page views, video plays and pauses, forum views, assignment views, and submissions. Change the list, re-run, and watch a number that a dashboard would report about a student move because you changed a definition rather than because anything happened to the student.

**📊 6. When does the work happen? (4 minutes).** So far time has been squashed flat. Now count events per calendar day with the eight Tuesday deadlines marked. Monday and Tuesday together carry more events than Wednesday through Sunday combined. The chart has a shape you could set a clock by, and the question is whether that is a finding about students or a finding about the course calendar.

**📊 7. A closer look at the deadline (4 minutes).** For every quiz submission, compute the hours between the submission and its deadline. Submissions landing in the last 6 hours average 68.2 points; submissions more than 3 days early average 83.3. That 15-point gap is a much stronger pattern than the activity story, which is exactly why the notebook treats it as the dangerous one and walks you through the leap from "these students score lower" to "nudging them earlier would raise their scores."

**✏️ Your turn 2 and 3.** Move the two arbitrary cutoffs that defined the corner and see whether the group survives a stricter definition, then zoom the rhythm chart into a single week. Try `FOCUS_WEEK = 8` second: the clickstream ends November 1 and quiz 8 is not due until November 3, so the line runs out before the deadline line does. Every real LMS export has an edge like that.

**💬 8. Reflection.** Four prompts tied to this week's readings, including one that asks you to sketch the same next step twice, once as educational data mining and once as learning analytics. Bring your answers to the 5:10 discussion block.

**✅ 9. Wrap up.** A short checklist, and a preview of Week 3.

## What this connects to in the readings

- **Baker and Inventado (2014)**, *Educational data mining and learning analytics*: two research traditions that handle the gap between a feature and a construct differently. Educational data mining tends to work bottom up from features toward automated discovery; learning analytics tends to keep a human holding the construct and asking whether the indicator deserves the name it was given. Section 8 asks you to sketch your own next step both ways and then say which one your course project is closer to.
- **Reich (2022)**, *Learning analytics and learning at scale*: what it means to study learning through whatever traces a platform happens to keep. Read it against Section 6. The weekly rhythm in that chart is at least as much a trace of the deadline calendar the platform imposes as it is a trace of the students.
- **Nathan and Sawyer (2014)**, *Foundations of the learning sciences*: the top rung of the ladder, and the reason it is out of reach. Their account of learning as deep conceptual understanding built through activity in context refuses to let learning be defined by whatever is easy to capture, which is precisely what `total_events` is.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Replace the mean with growth.** Section 4 deliberately throws away the shape of a student's trajectory by averaging their eight quizzes. Fit a straight line through each student's quiz scores instead and keep the slope, then re-run the Section 5 scatter against slope rather than mean. Does the correlation with activity get stronger or weaker, and what does your answer say about which outcome a dashboard should be built on?
2. **Let the correlation move through the term.** Compute `r` between week *k* activity and quiz *k* score separately for each of the eight weeks, then plot the eight values against week number. A relationship that only appears late in the term is a different finding from one that is stable, and a per-week view is the only way to tell them apart. Remember what Your turn 3 showed you about week 8 being a partial week.
3. **Volume against regularity.** Build two more features from the clickstream: `active_days` (the number of distinct calendar days on which a student generated at least one event) and the largest gap in days between consecutive active days. Correlate each with mean quiz score and compare against the 0.335 that `total_events` gets. If regularity beats volume, you have just found the argument that Week 3's bias audit turns on.
4. **Reconstruct sessions.** Sort each student's events by timestamp and cut a new session whenever more than 30 minutes passes between consecutive events. Now compute sessions per student and mean session length, and ask whether many short sessions or few long ones tracks scores better. This is the spacing question the course readings care about, asked with clickstream data.
5. **Ask who the eight corner students are.** `students.csv` is loaded in Section 1 and then never used. Merge the roster onto the corner group and look at `work_hours_per_week`, `first_gen`, `multilingual`, and `prior_gpa`. Write down what you find, then write down honestly what eight students can and cannot support as evidence. Bring both sentences to Week 3, where a model gets trained on exactly these features.

## Troubleshooting

**"NameError: name 'panel' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/lms_clickstream.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the first code cell of Section 1, which contains `%matplotlib inline` along with the imports. If they still do not appear, restart and run all.

**"I cannot type in the claim ladder cell."** It is a markdown cell, not a code cell. Double click it and it becomes editable. Press Shift + Enter when you are done to render it again.

**The merge printed fewer than 120 rows.** On a clean run it prints 120 before and 120 after, and the notebook says "nobody was dropped" for exactly this reason. If your number moved, you filtered something upstream, most likely in a ✏️ **Your turn** cell. Restart and run all to get back to the baseline.

**My `r` is not 0.335.** If you edited the `EVENT_TYPES` list in Your turn 1, that is expected and it is the entire point of the exercise. If you did not, restart and run all: the data generator is seeded, so a clean run reproduces the same numbers every time.

**Your turn 3 draws a line that stops before the deadline marker.** That is not a bug and you have found the thing the section is about. The clickstream export ends November 1 and quiz 8 is due November 3, so week 8 is a partial week. Any per-week comparison that includes it without saying so is comparing a partial week against seven complete ones.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**I got a different answer than my neighbor.** Compare the cutoffs and the event type lists first. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload for Week 2. Even so, if you used an AI assistant while working through this notebook, to explain what `groupby` does, to check your reading of the scatterplot, or to help you draft a reflection, save that exchange now.

Starting with Mini Project 1 in Week 4, the course AI policy requires you to upload your **AI interaction log plus a short reflection** alongside your notebook, in the Canvas "AI Reflection" submission. AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation.

Building the habit this week, when nothing is being graded, is much easier than starting it under a deadline.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
