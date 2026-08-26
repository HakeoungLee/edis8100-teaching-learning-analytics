# Week 2: Exploring Learning Data

This is the second hands-on session of EDIS 8100. Together we will open an institutional export
from a real university, aggregate a clickstream down to one row per student, join it to assessment
scores, and spend most of our attention on what happens to the people who fall out of the tables
along the way.

If you have never written a line of code, this notebook was written with you in mind. Nothing in it
asks you to write code from scratch, today or in any later week. You run cells, read what comes out,
and change a few clearly marked values to see how a cleaning decision moves a headline number.
Questions are welcome at any point, including questions about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 2, Wednesday, September 2, 2026, Ridley Hall 137 |
| **Topic** | Mapping the Learning Analytics Landscape and Theoretical Lenses |
| **Notebook portion** | Approximately 4:50 to 5:50 PM, after the student-led discussion hour and the break. We work through it together, instructor-guided. |
| **Notebook** | `week02_exploring_learning_data.ipynb` |
| **Data** | **Real, published, openly licensed.** The Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J: six files, 922,449 rows, from a UK distance-teaching university. CC BY 4.0. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `oulad-bbb` |
| **Citation** | Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Libraries** | pandas, numpy, matplotlib |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | None. This is in-class work, and nothing from the notebook goes to Canvas. |
| **Due** | Nothing this week. The first Canvas deliverable is Mini Project 1 in Week 4. |
| **Discussion leadership** | Weeks 2 to 11 are student-led. Each of the four of you leads **two** of those weeks, from the sign-up sheet completed in Week 1. |
| **Prior coding experience needed** | None |

## What I hope you leave with

1. A sense of how `groupby` moves a clickstream from one grain to another, and how `merge` puts two
   tables side by side.
2. The habit of saying, after each step, who is no longer in the table and what that costs.
3. A way of reading a scatterplot of activity against achievement that separates what the points
   show from what they are often taken to show.
4. The claim ladder, feature to indicator to construct, as a way of naming the distance between a
   column in a file and a thing that theory says matters.
5. A sense of why a data preparation decision, including the choice of axis scale, is an argument
   rather than a formatting preference.

None of these is a coding objective. Coding skill is not what is assessed anywhere in this course.

## The claim ladder

The claim ladder is introduced this week and used for the rest of the semester. A feature is
arithmetic and free. An indicator is a feature somebody has argued stands in for something
educational, and that argument is the work. A construct is the thing you actually care about, and no
column contains it. Week 3 audits a model built on features that were promoted to indicators without
an argument. Week 6 asks which sensor deserves the word "participation." Week 7 asks whether a loop
rate reaches self-regulation. Each of those weeks points back here.

An institutional export adds a rung below the ladder: before a number is even a feature, somebody
decided to record it, in a format somebody chose, for a purpose that was not research. The notebook
names that rung explicitly.

## What changes from Week 1

Week 1 was one flat file of 395 students in two Portuguese schools, and you could read a row out
loud as a sentence. This week is an institutional export: six files, 922,449 rows, enrollment
records and daily click counts from a UK distance-teaching university, describing people who
studied, some of whom passed and many of whom left. Both are real. What changes is the scale and the
raggedness.

The switch is deliberate. It is worth knowing what an institutional export looks like when it
arrives, what it cost somebody to publish it, and that real data does not arrange itself into a
clean lesson. Section 2 of the notebook is built around that.

## What is in this folder

| File | What it is |
|---|---|
| `week02_exploring_learning_data.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is nothing to download by hand and nothing to upload. The first code cell fetches six files
over plain HTTPS in a couple of seconds and prints what arrived. If the download fails, the cell
prints a plain-English message naming the repository it was trying to reach rather than a long error
trace.

## Where the data comes from

**Dataset.** The Open University Learning Analytics Dataset, restricted to module **BBB** and its
two presentations, **2013J** and **2014J**. A *presentation* is one running of a module, the way
EDIS 8100 Fall 2026 is one running of EDIS 8100.

**Who collected it.** The Open University is a UK distance-teaching university where almost all
instruction happens inside an online Virtual Learning Environment, so its own systems recorded every
enrollment, every resource click, and every assignment score as a by-product of teaching. Its
analytics team anonymized seven modules' worth of those records and published them so that
researchers with no access to a live student system could work on real learning data.

**License.** CC BY 4.0. Use, share, and adapt it, including commercially, provided you give credit.
If your course project uses it, cite Kuzilek, Hlosta, and Zdrahal (2017) and say which module and
presentation you used. "OULAD" alone is not a citation.

**What it cost to get here.** Names are gone; students are integers. Calendar dates are gone; every
date is a day number counted from the first day of the module, which is why the notebook shows
negative dates. Home addresses are gone; in their place the file carries `imd_band`, the decile of
the UK Index of Multiple Deprivation for the small area a student lives in, an area-level measure
that describes a neighborhood and not a person. Each substitution protects somebody and costs the
analyst something, and the notebook asks what.

**The files the notebook reads** (from `HakeoungLee/edis8100-datasets`, folder `oulad-bbb`):

| File | Rows | Grain (one row is) |
|---|---|---|
| `studentInfo.csv` | 4,529 | one enrollment: who signed up, and how it ended |
| `studentVle.csv.gz` | 891,062 | one student, one resource, one day: the clickstream |
| `studentAssessment.csv` | 21,783 | one submitted assessment: the score |
| `assessments.csv` | 18 | one assessment: its type, due day, and weight |
| `studentRegistration.csv` | 4,529 | one enrollment: when they registered, when they left |
| `vle.csv` | 528 | one resource in the course website |

**The stance we take.** The people in this file studied a real module, and none of them can correct
us. The ask is the same one as Week 1, and it matters more each week as the files get larger and the
people recorded in them are further away: it is worth asking who could be harmed by a claim before
making it, and saying what was measured rather than what a person is.

## Opening it in Colab

This repository is public, so you need only a Google account and a browser. There is nothing to
accept or authorize.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week02-exploring-learning-data/week02_exploring_learning_data.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week02-exploring-learning-data/week02_exploring_learning_data.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, and enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`. Then select
`week02-exploring-learning-data/week02_exploring_learning_data.ipynb`.

The **dataset** repository is public too, so the notebook's download works from any runtime,
including a fresh Colab with no GitHub authorization at all.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Nothing is lost if you forget:
the dataset is a fixed published file, so re-running the notebook from the top reproduces the same
numbers on any machine.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and
matplotlib, all of which ship with Anaconda, plus an internet connection for the first cell.

## Walkthrough

We will move through this together in class. The order below is a guide rather than a target, and it
is fine if we spend longer somewhere and leave something for later. The three **Your turn** cells
already contain working values, so the notebook runs start to finish without anyone typing anything.
Most of the work is in the reading; the code is short.

**Setup.** Run the first code cell. It downloads six files and prints a table of what arrived:
922,449 rows in total, module BBB, presentations 2013J and 2014J. The "Where this data came from"
cell above it is worth reading before anything runs.

**1. Meet the tables.** The three files that matter have genuinely different origins. `studentVle`
is a **log**, a by-product of a website's ordinary operation, and nobody designed it to answer a
research question. `studentAssessment` is a **measurement**, produced on purpose by an instrument
somebody built. `studentInfo` is an **administrative record**, assembled by a registry for funding
and compliance. Learning analytics almost always means putting those kinds of data next to each
other and arguing about the pairing. The grain of each file comes first.

**2. What an export actually looks like when it arrives.** This is the section Week 1 could not
teach. The notebook works through four problems in the export, making each decision visibly and
naming what the decision costs.

- **2a, one module run twice.** 4,529 enrollment rows but only 4,482 distinct students: 47 people
  sat the module twice, once in each presentation. Student 151917 failed 2013J with 909 clicks and
  passed 2014J with 713. A `groupby` on `id_student` alone reports one imaginary person with 1,622
  clicks who both failed and passed. The decision: the unit of analysis is the **enrollment**, keyed
  on `(id_student, code_presentation)`. The cell also prints where the dependency does and does not
  matter: 589 of the 4,529 rows record a previous attempt at this module in `num_of_prev_attempts`,
  only 47 of those repeats are visible here as a duplicated person, and scoping to one presentation
  in 2e removes the duplication entirely. The optional Your turn 2 pools the years and puts 25 of
  them back.
- **2b, activity before the course starts.** `date` runs from -23 to 268, and 46,884 rows (5.3
  percent) sit before day 0. Those are not corrupt; they are 2,739 people looking at the site before
  it opens. The decision: keep them, because the most voluntary engagement in the file should not be
  deleted. The cost: total clicks is not a rate, so students had unequal windows in which to
  accumulate them. The section is careful about the size of that inequality. Registration runs from
  198 days early to 44 days late, but the 2013J log holds no row before day -23 and the 2014J log
  none before day -9, so the extra pre-start opportunity is capped at about three weeks rather than
  six months. The cell prints both minimums.
- **2c, a blank column and one label typed out of pattern.** `imd_band` has ten deciles and 29
  blanks. Nine deciles carry a percent sign; the band `10-20` does not. There is no duplicate
  category and no error to catch, which is what makes it worth checking for: write the ten labels
  out by hand the sensible way and 586 rows (12.9 percent) fail to match, 557 of them real
  enrollments (550 distinct people) from a single deprivation band, silently. The section also says
  what the column records, which is a decile for a small area rather than anything about a household
  or a person. Week 3 uses this column.
- **2d, enrollments with no activity at all.** 738 of 4,529 enrollments (16.3 percent, about one in
  six) never registered a single click, and 30.8 percent of the cohort ends in `Withdrawn`. The
  students who most concern an early-warning system are the students who leave the least data
  behind.
- **2e, the scoping decision.** Analyze **2013J only**, and say so every time. 2013J ran six
  tutor-marked and five computer-marked assignments; 2014J ran five tutor-marked assignments, no
  computer-marked ones, and the first of the five weighted zero. Pooling two grading regimes and
  calling the result a finding is the error this section avoids.

**3. From 452,638 rows to one row per student.** `groupby` is the tool that moves between grains. It
computes two features at once: `total_clicks` (how much) and `active_days` (how spread out). 1,870
students appear; the median generated 386 clicks and the busiest generated 16,440, roughly 43 times
the median. Two histograms side by side, raw and log10, raise the axis question that Section 7 takes
up. The printed line underneath is the important one: 367 enrollments appear on neither chart,
because a `groupby` can only tell you about people who left rows.

**3b. The enrollments with no recorded activity.** These are not a rounding error and they are not
spread evenly across the cohort. Of 644 withdrawn enrollments in 2013J, 318 (49.4 percent) have no
click recorded at all. Of 896 passes and 176 distinctions, none do. The chart states a fact about
the record rather than about the people in it, and a short table separates what the data show, what
is a plausible interpretation, and what the file cannot establish. The discussion prompt walks the
instrument, the setting, and these adults' circumstances before it reaches a candidate explanation
about a student. Students are also asked to predict which final results are about to vanish from the
analysis before the join happens.

**4. The claim ladder.** This is the section the rest of the semester points back to. A three-row
table lays out feature, indicator, and construct, with `total_clicks = 909` for student 151917 as
the feature and engagement as the construct that no column contains. Real data adds a rung below the
ladder: before a number is even a feature, somebody decided it existed. Then a text cell with three
sentences to finish about your own work.

**5. The other table, then the join.** `studentAssessment` has no presentation column, so the first
move is a lookup join against `assessments`. Three judgment calls are visible in a few lines: 10
blank scores are dropped rather than zeroed, the mean is unweighted (the real module weighted one
tutor-marked assignment at 5 percent, five at 18 percent each, and five computer-marked ones at 1
percent apiece), and **the final exam has no submission rows anywhere**, so every claim today is
about coursework and not final attainment.

**5b. Merge, and an honest count of who left.** The merge takes 2,237 enrollments down to a panel of
1,697, setting aside 540, or 24.1 percent. Then comes a chart that is not about learning at all, which is not
about learning at all. Of the 540 set aside, 441 withdrew and 99 failed, and **not one passed**.
Withdrawn is 28.8 percent of the cohort and 12.0 percent of the panel. An inner join is the correct
operation and the distortion is real anyway.

**6. Does activity buy achievement?** Recorded activity on x, outcome on y, which is the plot behind
a great many dashboards and which quietly invites a reader to call the x axis effort. Two
correlations are reported, not one, because click counts are heavy tailed and a single Pearson
number cannot tell "barely related" from "related, but not in a straight line." Pearson `r = 0.258`
with a 95 percent interval of [0.224, 0.296], so a straight line in raw clicks tracks about 7
percent of the variation in coursework scores. Spearman's rho on the same points is 0.466, interval
[0.425, 0.504]. The two coefficients disagree, and that disagreement is the result to interpret.
Both intervals come from a percentile bootstrap the notebook writes out in four lines, so that
uncertainty appears as something computed rather than something cited. A short table separates what
the pair shows from what it cannot establish.

**7. The same two variables, a different axis, a different answer.** A decile table first shows why
a log is arguable at all: from decile 1 to decile 5, +342 clicks goes with +11.6 score points; from
decile 5 to decile 10, +2,198 clicks goes with +6.5, about 6.4 times the extra clicking for roughly
half the movement. Then the same students on a log x axis: `r` goes from 0.258 to 0.473 [0.429,
0.511], and the variance explained goes from 7 percent to 22 percent. The notebook also puts an
interval on the difference itself, 0.214 [0.173, 0.251], by resampling the same enrollments into
both correlations at once, and then spends a paragraph on why that interval is not permission to
call the relationship stronger. Nobody clicked more. No score moved. Spearman is 0.466 before and
0.466 after. The section's argument: the log version is defensible, the raw version is defensible,
and what is harder to defend is choosing between them after seeing which gives the bigger number.

**8. The students the line gets wrong.** A tercile table: mean scores climb from 70.5 to 82.1 across
the three activity groups, but the standard deviation inside the low group alone is 12.4 points,
wider than the 11.6-point gap between the extremes. Then the scatterplot: 60 enrollments sit in the
low-clicks, high-score corner on a median of 145 clicks against the panel's 439, against the roughly
141 you would expect there if clicks and scores were unrelated. Nine earned distinctions, 21 passed,
17 failed, and 13 withdrew, one of the 13 with a coursework average above 95. That withdrawal share
is 21.7 percent against 12.0 percent for the panel, with a 95 percent interval of [11.7, 33.3] that
reaches down to the panel rate, so the notebook says plainly that 60 enrollments are enough to show
the corner exists and not enough to describe the people in it. Week 3 builds the model that would
flag every one of them.

**Your turn 1: three cleaning decisions, and what they cost.** The first Your turn of the semester
is a data-cleaning decision with consequences rather than a plotting tweak. The switches are: keep
pre-start clicks or not, require 1 or 3 or more scored submissions, keep withdrawn enrollments or
not. Nobody's behavior changes; only who counts changes. Requiring three submissions costs 185 rows
and takes the log Pearson from 0.473 to 0.382 and the Spearman from 0.466 to 0.396, moving the
estimate outside its own interval, which is one way to tell that the sample changed rather than the
fit. Dropping withdrawn enrollments costs 203 rows and moves nothing by more than the interval is
wide. This is a sensitivity analysis.

**9. When does the work happen?** This section brings in time. Clicks per day from day -23 to day
268, with every assignment due day marked, beside a weekly count of distinct students still active.
The left panel has a clearly periodic shape. The right panel starts at 1,372 students in week 0 and
ends at 381 in week 37, but it goes **up** in 14 of its 37 steps, and three of the five biggest
rebounds land on a tutor-marked deadline week with a fourth in the week before one. It stops at week
37 on purpose: the log runs three days into week 38, and plotting a three-day bucket beside
seven-day buckets would draw a final plunge that is entirely an artifact of where the file ends.
Attrition here rises and falls rather than declining steadily, and one question is whether those
students are returning to the course or to the assignment.

**10. Reflection.** Five prompts tied to this week's readings by author name, including one that
asks you to sketch the same next step twice, once as educational data mining and once as learning
analytics. Bring your answers to the closing discussion.

**11. Wrap up.** A short checklist, a reminder about citing CC BY 4.0 data, and a preview of Week 3.

## Going further (optional)

The last part of the notebook is a clearly marked optional section. It is not part of the class hour
and nobody needs to work through it today.

**What is that 0.47 made of?** Two things contribute to the headline number, and neither is about
how hard anybody worked. First, length of stay: the number of scored submissions correlates 0.604
with log clicks and 0.416 with score, and holding it fixed drops the 0.473 to 0.305, so roughly a
third of the association is shared with how many assessments an enrollment lasted long enough to
sit. Second, what counts as achievement: computer-marked assessments average 88.1 and tutor-marked
ones 71.5, so an unweighted mean lets the mix a student happened to sit move their score, and
rebuilding it with the module's own weights takes the log Pearson to 0.399 and the Spearman to
0.414. This keeps Section 7's argument from ending at "the axis changed the number." The definition
of the outcome changes it too.

**Your turn 2: the other year.** Set `WHICH_PRESENTATION = '2014J'` and find out how much the answer
depended on which year you happened to pick. It depends a good deal: `r` on log clicks is 0.473 in
2013J and 0.195 in 2014J, a difference of 0.278 with a 95 percent interval of [0.205, 0.348], and
the Spearman gap is wider still, 0.466 against 0.106, difference 0.360 [0.299, 0.422]. The years do
differ, and the interval is silent about why, because the assessment structure changed at the same
time as the year. Pool them and you get 0.218, a number that describes neither year and rests on
3,485 rows of which 25 are somebody the other year already counted.

**Your turn 3: which clicks count as engagement?** `vle.csv` labels every resource with an
`activity_type`. Narrow the definition and three numbers move: the Pearson correlation, the Spearman
correlation, and how many enrollments vanish because they have no recorded click on the thing you
chose. Restricting to `oucontent`, the actual course material, erases 201 enrollments. The cell
prints the all-types correlation twice, once on the full panel and once recomputed on whoever
survived your definition, because comparing a narrowed feature against the full-panel number
confuses the feature change with the sample change. On the like-for-like comparison no single
activity type beats counting everything. Pearson and Spearman also rank the candidate features
differently, which is worth a minute on its own.

**Appendix.** Expected numbers for all three Your turn cells.

## If you finish early, or arrive with programming experience

1. **Take the weighted score further.** The optional section already rebuilds achievement with the
   module's own weights and reports what happens, 0.473 to 0.399 on the log Pearson. Push it:
   rebuild the decile table and the low-clicks, high-score corner on the weighted score, and see
   whether the same 60 enrollments are in the corner. A finding that survives a change in the
   outcome definition is a different kind of finding from one that does not.
2. **Build a regularity feature.** `active_days` is already computed and then barely used. Add the
   longest gap in days between a student's consecutive active days, correlate both against
   `mean_score`, and compare them to the 0.473 that log clicks gets.
3. **Repair `imd_band` and look.** Fix the `10-20` label, decide out loud what to do with the 29
   blanks, then compare click volume and coursework score across deprivation deciles. Write down
   what you find, along with the group sizes, and then write down what an area-level measure of a
   neighborhood can and cannot tell you about a person. Both sentences are worth bringing to Week 3.
4. **Compute the correlation window by window.** Compute Pearson `r` and Spearman rho between clicks
   in module week *k* and the score on the next assignment due, separately for each assignment. A
   relationship that only appears late is a different finding from one that is stable, and a
   per-window view is the only way to tell them apart.
5. **Model withdrawal instead of score.** Everything in this notebook conditions on students who
   submitted something. Turn the question around: using `studentRegistration.csv`, which has
   `date_unregistration`, predict *whether* someone withdraws from their first two weeks of clicks.
   Then say what the 318 withdrawn students with zero clicks do to your model, since they have no
   first two weeks at all.
6. **Check the second presentation properly.** Your turn 2 gives one number for 2014J. Rebuild the
   whole notebook's analysis for it: the messes, the join losses, the corner. Does 2014J tell the
   same story with a weaker correlation, or a different story? Its Spearman rho is 0.106 against
   0.466 in 2013J, which is a bigger gap than the Pearson numbers alone suggest.

## Troubleshooting

**"The data did not download."**
The setup cell prints a plain-English message naming the repository it was trying to reach. The
usual cause is no internet connection in the runtime. Run the cell again, since brief network
failures are common, then check `github.com/HakeoungLee/edis8100-datasets` in a browser tab. That
repository is public, so this is never about a GitHub account or an invitation. If the repository
itself is unreachable, please send Dr. Lee the URL the message prints.

**"NameError: name 'panel' is not defined" or something similar**
A cell ran out of order, or the runtime restarted. **Runtime > Restart session and run all** in
Colab, or **Kernel > Restart & Run All** in Jupyter, then wait for every cell to finish. This
resolves most notebook problems.

**The download is slow**
`studentVle.csv.gz` is the big one, 891,062 rows, and it is compressed for that reason. On a normal
connection all six files take a couple of seconds. It is not stuck.

**My charts do not appear**
Please check that you ran the first code cell, which contains `%matplotlib inline` along with the
imports. If they still do not appear, restart and run all.

**"I cannot type in the claim ladder cell"**
It is a markdown cell rather than a code cell. Double-click it and it becomes editable. Press Shift
+ Enter when you are done to render it again.

**The panel has 1,697 rows and I expected 2,237**
That is correct, and it is what Section 5b is about. 540 enrollments have no click record, no scored
submission, or neither. The notebook prints who they were: 441 withdrew, 99 failed, none passed.

**My `r` is not 0.258**
If you edited a **Your turn** cell, that is expected and it is what the exercise is for. If you did
not, restart and run all. The dataset is fixed and published, so a clean run reproduces the same
numbers every time, on any machine.

**Section 3's log histogram has fewer people than the raw one**
It has the same 1,870. What both are missing is the 367 enrollments with no recorded clicks. You
cannot take the log of zero, so the log panel has no place to put a count of zero, and neither panel
can say whether those enrollments studied off the platform, never opened it, or opened it in a way
this log does not record.

**Colab says "Cannot find notebook" or shows a 404**
You are most likely signed into a different Google account. Check the profile picture in the top
right corner, switch to the account you want, and open the link again.

**I lost my edits**
Colab discards untitled sessions. **File > Save a copy in Drive** at the start of any session where
you plan to keep something.

**My chart looks different from my neighbour's**
Compare your **Your turn** settings first. That is almost always the difference, and explaining it to
each other is a useful thing to do.

**Red text appeared**
Python errors are wordy, and none of them means something has been damaged. Nothing here can harm
your computer, the course data, or your grade. The **last line** of the error usually names the real
problem. Please ask, and we will read it together.

## Documenting AI use

The course permits AI use in designated activities and asks that you document it. Undisclosed AI use
is an Honor Code violation.

There is **nothing to submit this week**, so there is nothing to document. It is still worth starting
the habit. Beginning with Mini Project 1 in Week 4, every mini project and every course project
milestone asks for an **AI Reflection** submission on Canvas, with two parts in two places:

- **The conversation record goes in a Word file, attached to the submission.** The full exchange,
  across every tool and every session, pasted in rather than summarized.
- **The reflection goes in the Canvas text box**, where you copy in the four questions from the
  syllabus and answer each one: how you used it; whether it helped and how; whether it made your
  work more challenging in any way; and what lesson about AI you would pass on to a friend or the
  class.

If you used an assistant to make sense of `groupby` today, or to check your reading of a
scatterplot, please save the transcript.

## Connections to this week's readings

The required readings are Baker and Inventado (2014), Reich (2022), and Nathan and Sawyer (2014).
Gray and Bergner (2022) on measurement and Sawyer (2006) are the additional readings. The notebook
draws on the required three briefly at a few points, and the reflection returns to them:

- **Baker and Inventado (2014)**, *Educational data mining and learning analytics*: two research
  traditions that handle the gap between a feature and a construct differently. Educational data
  mining tends to work bottom up from features toward automated discovery; learning analytics tends
  to keep a person responsible for the construct and asking whether the indicator deserves the name
  it was given. Section 10 asks you to sketch your own next step both ways and then say which one
  your course project is closer to.
- **Reich (2022)**, *Learning analytics and learning at scale*: what it means to study learning
  through whatever traces a platform happens to keep. It reads well against Sections 7 and 9. The
  weekly rhythm is at least as much a trace of the deadline calendar the institution imposed as it
  is a trace of the students, and Section 7 suggests one clause to add: and through whatever
  transformations the analyst happens to apply.
- **Nathan and Sawyer (2014)**, *Foundations of the learning sciences*: the top rung of the ladder,
  and the reason no column contains it. Their account of learning as deep conceptual understanding
  built through activity in context declines to let learning be defined by whatever is easy to
  capture, which is what `total_clicks` is.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across
the lab weeks, and no notebook in this course generates a row.

This week's files hold records for adults who studied one module at a UK distance-teaching
university in 2013 and 2014, assembled by the university's own systems as a by-product of teaching.
Their records were anonymized and published under CC BY 4.0 so that others could learn from them,
which is what we are about to do, and the only reason the files can be opened at all is that
somebody chose to release them.

None of them agreed to be a teaching example. It is worth asking who could be harmed by a claim
before making it, noticing when a metric reduces a person to one number, and noticing which people
are not in the file at all. That stance runs through every week of the course.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

## Data credit

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset.
*Scientific Data, 4*, 170171. Licensed CC BY 4.0. This folder uses module BBB, presentations 2013J
and 2014J, redistributed unmodified in the course dataset repository
`HakeoungLee/edis8100-datasets`.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
