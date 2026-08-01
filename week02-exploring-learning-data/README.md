# 📊 Week 2: Exploring Learning Data

Finding out how far a column in a CSV is from a thing that matters, using records from a course that actually ran.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 2, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Mapping the Learning Analytics Landscape and Theoretical Lenses |
| **Guest speaker** | None. Dr. Lee leads the discussion this week so that you can watch the facilitation moves you will be using from Week 3 onward. |
| **In-class time on this notebook** | About 35 minutes, in the hands-on block (4:35 to 5:10). The core path is built to fit that window; Section 7b is the designated cut if it does not. |
| **Deliverable** | None. Week 2 is in-class work only. |
| **Due date** | Not applicable. The first Canvas deliverable is Mini Project 1 in Week 4. |
| **Notebook** | `week02_exploring_learning_data.ipynb` |
| **Data used** | **Real.** The Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J. Six files, 922,449 rows, downloaded by the notebook from the course dataset repository. CC BY 4.0. |
| **Citation** | Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Libraries** | pandas, numpy, matplotlib |
| **Prior coding experience needed** | None |

## Something changed this week

Week 1 ran on invented students. From Week 2 the data is real: enrollment records and daily click counts from a UK distance-teaching university, describing people who actually studied, some of whom passed and many of whom left.

That switch is the point, not a convenience. Students in this seminar should know where real data comes from, what it cost somebody to publish it, and that real data does not arrange itself into a clean lesson. Section 2 of the notebook is built entirely around what an institutional export looks like when it arrives.

## Objectives

By the end of this activity you will be able to:

1. **Aggregate** 452,638 clickstream rows down to one row per student with `groupby`, and **join** that table to assessment scores with `merge`, saying after every step who disappeared and what that costs.
2. **Read** a scatterplot of activity against achievement and say out loud what an `r` of 0.26 does and does not license you to claim.
3. **Use the claim ladder** (feature, indicator, construct) to name the distance between a number the system happened to record and a thing that theory says matters.
4. **Defend a data preparation decision**, including the choice of axis scale, as an argument rather than a formatting preference.

The through-line of the session: **the claim ladder is a Week 2 idea and the whole semester leans on it.** A feature is arithmetic and free. An indicator is a feature you have argued stands in for something educational, and that argument is the work. A construct is the thing you actually care about, and no column contains it. Week 3 audits a model built on features that were promoted to indicators without an argument. Week 6 asks which sensor deserves the word "participation." Week 7 asks whether a loop rate reaches self-regulation. Every one of those weeks points back here, so it is worth being able to say the three rungs from memory.

Real data adds a rung below the ladder that synthetic data hid: before a number is even a feature, somebody decided it existed. The notebook names that rung explicitly.

## What is in this folder

| File | What it is |
|---|---|
| `week02_exploring_learning_data.ipynb` | The notebook. It downloads its own data from a public URL and runs top to bottom untouched. |
| `README.md` | This file. |

You do not need to clone anything, download a CSV, or create an account. The first code cell fetches six files over plain HTTPS in a couple of seconds and prints what arrived. If the download fails, the cell prints a plain-English message naming the repository rather than a wall of red.

## Where the data comes from

**Dataset.** The Open University Learning Analytics Dataset, restricted to module **BBB** and its two presentations, **2013J** and **2014J**. A *presentation* is one running of a module, the way EDIS 8100 Fall 2026 is one running of EDIS 8100.

**Who collected it.** The Open University is a UK distance-teaching university where almost all instruction happens inside an online Virtual Learning Environment, so its own systems recorded every enrollment, every resource click, and every assignment score as a by-product of teaching. Its analytics team anonymized seven modules' worth of those records and published them so that researchers with no access to a live student system could work on real learning data.

**License.** CC BY 4.0. Use, share, and adapt it, including commercially, provided you give credit. If your course project uses it, cite Kuzilek, Hlosta, and Zdrahal (2017) and say which module and presentation you used. "OULAD" alone is not a citation.

**What it cost to get here.** Names are gone; students are integers. Calendar dates are gone; every date is a day number counted from the first day of the module, which is why the notebook shows you negative dates. Home addresses are gone; in their place sits `imd_band`, the decile of the UK Index of Multiple Deprivation for the small area a student lives in, an area-level measure that describes a neighborhood and not a person. Each substitution protects somebody and costs the analyst something, and the notebook makes students say what.

**The files the notebook reads** (from `HakeoungLee/edis8100-datasets`, folder `oulad-bbb`):

| File | Rows | Grain (one row is) |
|---|---|---|
| `studentInfo.csv` | 4,529 | one enrollment: who signed up, and how it ended |
| `studentVle.csv.gz` | 891,062 | one student, one resource, one day: the clickstream |
| `studentAssessment.csv` | 21,783 | one submitted assessment: the score |
| `assessments.csv` | 18 | one assessment: its type, due day, and weight |
| `studentRegistration.csv` | 4,529 | one enrollment: when they registered, when they left |
| `vle.csv` | 528 | one resource in the course website |

**The stance we take.** In Week 1 the data were invented precisely so that nobody could be harmed by our practice. This data is real. The people in it studied a real module, and none of them are in the room to correct you. The ask is the same one as Week 1, only sharper: say who could be harmed by a claim before you make it.

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

The **dataset** repository is public, so the notebook's download works from any runtime, including a fresh Colab with no GitHub authorization at all.

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda, plus an internet connection for the first cell.

## Step-by-step walkthrough

The core path is about 35 minutes if you keep moving, which is the 4:35 to 5:10 block. The per-section estimates below sum to more than that on purpose: they assume you stop and argue at every 💬 prompt, and the arguing continues in the 5:10 discussion block. If the room is running behind, **Section 7b is the one to read aloud rather than run**, because it is the only section whose numbers are all printed in the walkthrough above. The three ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. The reading is the work. The code is short.

**⚙️ Setup (1 minute).** Run the first code cell. It downloads six files and prints a table of what arrived: 922,449 rows in total, module BBB, presentations 2013J and 2014J. Read the "Where this data came from" cell above it before you run anything. You should never analyze data whose origin you cannot state.

**📊 1. Meet the tables (3 minutes).** Three files with three genuinely different origins. `studentVle` is a **log**, exhaust from a website doing its job, and nobody designed it to answer a research question. `studentAssessment` is a **measurement**, produced on purpose by an instrument somebody built. `studentInfo` is an **administrative record**, assembled by a registry for funding and compliance. Learning analytics almost always means putting those kinds of data next to each other and arguing about the pairing. Notice the grain of each file before you go on.

**📊 2. What an export actually looks like when it arrives (8 minutes).** The section Week 1 could not teach. Four messes, each one met, decided in front of you, and costed.

- **2a, two courses wearing the same name.** 4,529 enrollment rows but only 4,482 distinct students: 47 people sat the module twice, once in each presentation. Student 151917 failed 2013J with 909 clicks and passed 2014J with 713. A `groupby` on `id_student` alone reports one imaginary person with 1,622 clicks who both failed and passed. The decision: the unit of analysis is the **enrollment**, keyed on `(id_student, code_presentation)`. The section also says where the dependency does and does not bite: 589 of the 4,529 rows record a previous attempt at this module in `num_of_prev_attempts`, only 47 of those repeats are visible here as a duplicated person, and scoping to one presentation in 2e removes the duplication entirely. Your turn 2 pools the years and puts 25 of them back.
- **2b, activity before the course starts.** `date` runs from -23 to 268, and 46,884 rows (5.3 percent) sit before day 0. Those are not corrupt; they are 2,739 people looking at the site before it opens. The decision: keep them, because the most voluntary engagement in the file should not be deleted. The cost: total clicks is not a rate, so students had unequal windows in which to accumulate them. The section is careful about the size of that inequality: registration runs from 198 days early to 44 days late, but the 2013J log holds no row before day -23 and the 2014J log none before day -9, so the extra pre-start opportunity is capped at about three weeks, not six months.
- **2c, a blank column and one label typed out of pattern.** `imd_band` has ten deciles and 29 blanks. Nine deciles carry a percent sign; the band `10-20` does not. There is no duplicate category and no error to catch, which is what makes it dangerous: write the ten labels out by hand the sensible way and 586 rows (12.9 percent) fail to match, 557 of them real enrollments (550 distinct people) from a single deprivation band, silently. Week 3 wants this column.
- **2d, enrollments with no activity at all.** 738 of 4,529 enrollments (16.3 percent, about one in six) never registered a single click, and 30.8 percent of the cohort ends in `Withdrawn`. The students who most concern an early-warning system are exactly the students who leave the least data behind.
- **2e, the scoping decision.** Analyze **2013J only**, and say so every time. 2013J ran six tutor-marked and five computer-marked assignments; 2014J ran five tutor-marked assignments, no computer-marked ones, and the first of the five weighted zero. Pooling two grading regimes and calling the result a finding is the error this section refuses.

**📊 3. From 452,638 rows to one row per student (4 minutes).** `groupby` is the tool that moves between grains. Two features at once: `total_clicks` (how much) and `active_days` (how spread out). 1,870 students appear; the median generated 386 clicks and the busiest generated 16,440, roughly 43 times the median. Two histograms side by side, raw and log10, plant the axis question that Section 7 detonates. The printed line underneath is the important one: 367 enrollments appear on neither chart, because a `groupby` can only tell you about people who left rows.

**📊 3b. The enrollments with no recorded activity (3 minutes).** Not a rounding error and not spread evenly across the cohort. Of 644 withdrawn enrollments in 2013J, 318 (49.4 percent) have no click recorded at all. Of 896 passes and 176 distinctions, zero do. The chart is a fact about the record, not about the people in it, and the interpretation prompt walks the instrument, the setting, and these adults' circumstances before it allows a candidate explanation about a student. Students are also asked to predict which final results are about to vanish from the analysis before the join happens.

**💬 4. The claim ladder (5 minutes).** Stop here. This is the section the rest of the semester points back to. A three-row table lays out feature, indicator, and construct, with `total_clicks = 909` for student 151917 as the feature and engagement as the construct that no column contains. Real data adds a rung below the ladder: before a number is even a feature, somebody decided it existed. Then a text cell where you finish three sentences about your own work. Type in it. It takes two minutes and it is the only writing the notebook asks for.

**📊 5. The other table, then the join (5 minutes).** `studentAssessment` has no presentation column, so the first move is a lookup join against `assessments`. Three judgment calls are visible in a few lines: 10 blank scores are dropped rather than zeroed, the mean is unweighted (the real module weighted one tutor-marked assignment at 5 percent, five at 18 percent each, and five computer-marked ones at 1 percent apiece), and **the final exam has no submission rows anywhere**, so every claim today is about coursework and not final attainment.

**📊 5b. Merge, and an honest count of who left (4 minutes).** From 2,237 enrollments to a panel of 1,697: 540 set aside, 24.1 percent. Then the chart that matters most and is not about learning at all. Of the 540 set aside, 441 withdrew and 99 failed, and **not one passed**. Withdrawn is 28.8 percent of the cohort and 12.0 percent of the panel. An inner join is the correct operation and the distortion is real anyway.

**📊 6. Does activity buy achievement? (4 minutes).** Recorded activity on x, outcome on y, which is the plot that launched a thousand dashboards and which quietly invites a reader to call the x axis effort. Write your prediction down first. Two correlations are reported, not one, because click counts are heavy tailed and a single Pearson number cannot tell "barely related" from "related, but not in a straight line." Pearson `r = 0.258` with a 95 percent interval of [0.224, 0.296], so a straight line in raw clicks tracks about 7 percent of the variation in coursework scores. Spearman's rho on the same points is 0.466, interval [0.425, 0.504]. The disagreement between them is the finding. Both intervals come from a percentile bootstrap the notebook writes out in four lines, so that students see uncertainty as something you compute rather than something you cite.

**📊 7. The same two variables, a different axis, a different answer (6 minutes).** The teaching gift of this dataset. A decile table first shows why a log is arguable at all: from decile 1 to decile 5, +342 clicks buys +11.6 score points; from decile 5 to decile 10, +2,198 clicks buys +6.5, about 6.4 times the extra clicking for roughly half the payoff. Then the same students on a log x axis: `r` goes from 0.258 to 0.473 [0.429, 0.511], 1.83 times larger, and the variance explained goes from 7 percent to 22 percent, 3.3 times larger. The notebook also puts an interval on the difference itself, 0.214 [0.173, 0.251], by resampling the same enrollments into both correlations at once, and then spends a paragraph on why that interval is not permission to call the relationship stronger. Nobody clicked more. No score moved. Both sentences are true about the same 1,697 people. The section's argument: the log version is defensible, the raw version is defensible, and what is **not** defensible is choosing between them after seeing which gives the bigger number.

**📊 7b. What is that 0.47 made of? (2 minutes).** Two ingredients sit inside the headline number and neither is about how hard anybody worked. First, length of stay: the number of scored submissions correlates 0.604 with log clicks and 0.416 with score, and holding it fixed drops the 0.473 to 0.305, so roughly a third of the association is shared with how many assessments an enrollment lived long enough to sit. Second, what counts as achievement: computer-marked assessments average 88.1 and tutor-marked ones 71.5, so an unweighted mean lets the mix a student happened to sit move their score, and rebuilding it with the module's own weights takes the log Pearson to 0.399 and the Spearman to 0.414. This is the section that keeps Section 7's argument from ending at "the axis changed the number." The definition of the outcome changes it too, and length of stay is a fact about a calendar before it is a fact about a person.

**📊 8. Look at the students the line gets wrong (4 minutes).** A tercile table: mean scores climb from 70.5 to 82.1 across the three activity groups, but the standard deviation inside the low group alone is 12.4 points, wider than the 11.6-point gap between the extremes. Then the map: 60 enrollments sit in the low-clicks, high-score corner on a median of 145 clicks against the panel's 439, against the roughly 141 you would expect there if clicks and scores were unrelated. Nine earned distinctions, 21 passed, 17 failed, and 13 withdrew, one of the 13 carrying a coursework average above 95. That withdrawal share is 21.7 percent against 12.0 percent for the panel, with a 95 percent interval of [11.7, 33.3] that reaches down to the panel rate, so the notebook says plainly that 60 enrollments are enough to show the corner exists and not enough to describe the people in it. Week 3 builds the model that would flag every one of them.

**✏️ Your turn 1: three cleaning decisions, and what they cost (4 minutes).** The first Your turn of the semester is a data-cleaning decision with consequences, not a plotting tweak. Three switches: keep pre-start clicks or not, require 1 or 3 or more scored submissions, keep withdrawn enrollments or not. Nobody's behavior changes; only who counts changes. Requiring three submissions costs 185 rows and takes the log Pearson from 0.473 to 0.382 and the Spearman from 0.466 to 0.396, moving the estimate outside its own interval, which is how you can tell it changed the sample rather than the fit. Dropping withdrawn enrollments costs 203 rows and moves nothing by more than the interval is wide. This is a sensitivity analysis, and it is what separates a finding from a coincidence.

**📊 9. When does the work happen? (4 minutes).** Time, finally. Clicks per day from day -23 to day 268, with every assignment due day marked, beside a weekly count of distinct students still active. The left panel has a shape you could set a clock by. The right panel starts at 1,372 students in week 0 and ends at 381 in week 37, but it goes **up** in 14 of its 37 steps, and three of the five biggest rebounds land exactly on a tutor-marked deadline week. It stops at week 37 on purpose: the log runs three days into week 38, and plotting a three-day bucket beside seven-day buckets would draw a final plunge that is entirely an artifact of where the file ends. Attrition here is a sawtooth, not a slide, and the question is whether those students are returning to the course or to the assignment.

**✏️ Your turn 2: the other year.** Set `WHICH_PRESENTATION = '2014J'` and find out how much the answer depended on which year you happened to pick. It depends a lot: `r` on log clicks is 0.473 in 2013J and 0.195 in 2014J, a difference of 0.278 with a 95 percent interval of [0.205, 0.348], and the Spearman gap is wider still, 0.466 against 0.106, difference 0.360 [0.299, 0.422]. The years really do differ, and the interval is silent about why, because the assessment structure changed at the same time as the year. Pool them and you get 0.218, a number that describes neither year and rests on 3,485 rows of which 25 are somebody the other year already counted.

**✏️ Your turn 3: which clicks count as engagement?** `vle.csv` labels every resource with an `activity_type`. Narrow the definition and watch three numbers move: the Pearson correlation, the Spearman correlation, and how many enrollments vanish because they have no recorded click on the thing you chose. Restricting to `oucontent`, the actual course material, erases 201 enrollments. The cell prints the all-types correlation twice, once on the full panel and once recomputed on whoever survived your definition, because comparing a narrowed feature against the full-panel number confuses the feature change with the sample change. On the honest comparison no single activity type beats counting everything. Pearson and Spearman also rank the candidate features differently, which is worth a minute on its own.

**💬 10. Reflection.** Five prompts tied to this week's readings by author name, including one that asks you to sketch the same next step twice, once as educational data mining and once as learning analytics. Bring your answers to the 5:10 discussion block.

**✅ 11. Wrap up.** A short checklist, a reminder about citing CC BY 4.0 data, and a preview of Week 3.

**Appendix.** Worked solutions and expected numbers for all three ✏️ Your turn cells.

## What this connects to in the readings

- **Baker and Inventado (2014)**, *Educational data mining and learning analytics*: two research traditions that handle the gap between a feature and a construct differently. Educational data mining tends to work bottom up from features toward automated discovery; learning analytics tends to keep a human holding the construct and asking whether the indicator deserves the name it was given. Section 10 asks you to sketch your own next step both ways and then say which one your course project is closer to.
- **Reich (2022)**, *Learning analytics and learning at scale*: what it means to study learning through whatever traces a platform happens to keep. Read it against Sections 7 and 9. The weekly rhythm is at least as much a trace of the deadline calendar the institution imposed as it is a trace of the students, and Section 7 adds a clause Reich does not: and through whatever transformations the analyst happens to apply.
- **Nathan and Sawyer (2014)**, *Foundations of the learning sciences*: the top rung of the ladder, and the reason it is out of reach. Their account of learning as deep conceptual understanding built through activity in context refuses to let learning be defined by whatever is easy to capture, which is precisely what `total_clicks` is.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Take the weighted score further.** Section 7b already rebuilds achievement with the module's own weights and reports what happens, 0.473 to 0.399 on the log Pearson. Push it: rebuild the decile table and the low-clicks, high-score corner on the weighted score, and see whether the same 60 enrollments are in the corner. A finding that survives a change in the outcome definition is a different kind of finding from one that does not.
2. **Build regularity, not just volume.** `active_days` is already computed and then barely used. Add the longest gap in days between a student's consecutive active days, correlate both against `mean_score`, and compare them to the 0.473 that log clicks gets. If regularity beats volume, you have found the argument Week 3's bias audit turns on.
3. **Repair `imd_band` and look.** Fix the `10-20` label, decide out loud what to do with the 29 blanks, then compare click volume and coursework score across deprivation deciles. Write down what you find, and then write down what an area-level measure of a neighborhood can and cannot tell you about a person. Bring both sentences to Week 3.
4. **Let the correlation move through the module.** Compute Pearson `r` and Spearman rho between clicks in module week *k* and the score on the next assignment due, separately for each assignment. A relationship that only appears late is a different finding from one that is stable, and a per-window view is the only way to tell them apart.
5. **Model the withdrawal, not the score.** Everything in this notebook conditions on students who submitted something. Turn the question around: using `studentRegistration.csv`, which has `date_unregistration`, predict *whether* someone withdraws from their first two weeks of clicks. Then say honestly what the 318 withdrawn students with zero clicks do to your model, since they have no first two weeks at all.
6. **Check the second presentation properly.** Your turn 2 gives you one number for 2014J. Rebuild the whole notebook's analysis for it: the messes, the join losses, the corner. Does 2014J tell the same story with a weaker correlation, or a different story? Its Spearman rho is 0.106 against 0.466 in 2013J, which is a bigger gap than the Pearson numbers alone suggest.

## Troubleshooting

**"The data did not download."** The setup cell prints this in plain English, along with the repository it was trying to reach. The usual cause is no internet connection in the runtime. Check your connection and use `Runtime > Restart and run all`. If the repository itself is unreachable, send Dr. Lee the URL the message prints.

**"NameError: name 'panel' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**The download is slow.** `studentVle.csv.gz` is the big one, 891,062 rows, and it is compressed for exactly that reason. On a normal connection all six files take a couple of seconds. It is not stuck.

**My charts do not appear.** Make sure you ran the first code cell, which contains `%matplotlib inline` along with the imports. If they still do not appear, restart and run all.

**"I cannot type in the claim ladder cell."** It is a markdown cell, not a code cell. Double click it and it becomes editable. Press Shift + Enter when you are done to render it again.

**The panel has 1,697 rows and I expected 2,237.** That is correct and it is the point of Section 5b. 540 enrollments have no click record, no scored submission, or neither. The notebook prints exactly who they were: 441 withdrew, 99 failed, none passed.

**My `r` is not 0.258.** If you edited a ✏️ **Your turn** cell, that is expected and it is the entire point of the exercise. If you did not, restart and run all. The dataset is fixed and published, so a clean run reproduces the same numbers every time, on any machine, for everyone in the room.

**Section 3's log histogram has fewer people than the raw one.** No, it has the same 1,870. What both are missing is the 367 enrollments with no recorded clicks. You cannot take the log of zero, so the log panel has no place to put a count of zero, and neither panel can say whether those enrollments studied off the platform, never opened it, or opened it in a way this log does not record.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox. Note that this affects opening the *notebook*, not the data download: the dataset repository is public.

**I got a different answer than my neighbor.** Compare your ✏️ **Your turn** settings first. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload for Week 2. Even so, if you used an AI assistant while working through this notebook, to explain what `groupby` does, to check your reading of the scatterplot, or to help you draft a reflection, save that exchange now.

Starting with Mini Project 1 in Week 4, the course AI policy requires you to upload your **AI interaction log plus a short reflection** alongside your notebook, in the Canvas "AI Reflection" submission. AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation.

Building the habit this week, when nothing is being graded, is much easier than starting it under a deadline.

## Data credit

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. Licensed CC BY 4.0. This folder uses module BBB, presentations 2013J and 2014J, redistributed unmodified in the course dataset repository `HakeoungLee/edis8100-datasets`.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
