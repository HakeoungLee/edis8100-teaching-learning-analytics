# Week 4: Mini Project 1, Teacher Dashboards

We build a teacher-facing dashboard with plotly, on real student records, and then take it apart.

If you have never written a line of code, this notebook was written with you in mind. Nothing in it
asks you to write code from scratch. You run cells, read what comes out, and change a few clearly
marked values to see what those choices were doing to the result. Questions are welcome at any
point, including questions about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 4, Wednesday, September 16, 2026, 3:30 to 5:50 PM, Ridley Hall 137 |
| **Topic** | Teacher and Student Facing Learning Analytics and Dashboards |
| **Guest speaker** | Yeonji Jung, Texas A&M University, 4:30 to 5:30 PM |
| **Notebook portion** | 3:30 to 4:20, alongside building a dashboard by vibe coding, and again in the debrief from 5:30 to 5:50. Class launches the project; the rest is finished afterwards. |
| **Notebook** | `week04_miniproject1_teacher_dashboard.ipynb` |
| **Data** | **Real, published, openly licensed.** The Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J: 4,529 enrollments, 891,062 rows of daily clickstream, 21,783 assessment submissions. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `oulad-bbb`. CC BY 4.0. |
| **Citation** | Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Libraries** | pandas, numpy, matplotlib, plotly, scikit-learn |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | **Mini Project 1**: the completed notebook, the 300-word design memo in the marked cell inside it, and the AI interaction log plus reflection |
| **Due** | Canvas, by 11:59 PM on Sunday, September 20, 2026 |
| **Prior coding experience needed** | None |

There is no Discussion Leadership block this week. Discussion Leadership runs in weeks 2 through 11,
and each of the three of you leads two of those weeks.

## What is assessed

The notebook is submitted, so there is something to hand in this week. Coding skill is not what is
assessed. The **design memo in Part F is the primary component used for grading**, with the critique
table in Part E close behind it, and the shorter interpretations in the Your turn cells alongside
them. The notebook runs start to finish with nothing edited, and a run you did not edit still
produces every finding the assignment is about.

## What I hope you leave with

1. A three-panel teacher-facing dashboard built in plotly from a real virtual learning environment
   export, with a static matplotlib snapshot of every panel for readers who cannot run the code.
2. Being able to state the provenance of a dataset: who collected it, under what license, and what it
   may be used for.
3. A reason attached to every automated flag, by decomposing a model's predicted probability into the
   per-feature contributions that produced it, and a look at how the resulting list falls across
   socioeconomic bands.
4. A sense of what a fairness statistic can and cannot support at a given caseload, including when a
   rate has too few events underneath it to compare at all, and the habit of checking a model against
   the simplest rule that would have replaced it rather than against chance.
5. A reading of each panel against the decision a teacher would face, drawing on van Leeuwen,
   Teasley, and Wise (2022) and Wise and Jung (2019).
6. A 300-word design memo arguing for one specific design change and saying who it protects.

The through-line of the session: a dashboard is not a report, it is an intervention in somebody's
Monday morning. The design question is less "is this accurate" than "what would a teacher do because
of this, and who pays if they are wrong."

## Building by vibe coding

Part of the first block is spent building by vibe coding: describing the panel you want to an AI
coding tool such as Claude Code or Codex, then reading what it returns, running it, and correcting
it against the data. The reading and the correcting are the parts that carry the learning, since a
chart that renders is not yet a chart that is true of these records. Whatever you generate that way
belongs in your AI interaction log along with your prompts.

If you do not have access to an AI coding tool, please let me know before class. Access is being
arranged for anyone who needs it, and nobody needs to purchase anything for this session.

## What is different about this week

Two things change, and they change together.

**Where the records end up.** Weeks 2 and 3 already ran on these same Open University records, but
they ran in a notebook only this seminar read. This week the records go onto an interface a teacher
acts on: the same data from a distance-teaching university in the United Kingdom, 2,237 people who
registered for one module in October 2013, and 2,292 more who registered for the same module a year
later. They were anonymized and released by the Open University's Knowledge Media Institute so that
the field could check its own work on data more than one lab can see. They were not asked about a
doctoral seminar in Virginia. What they were given is anonymity and banded categories, and what we
owe them in return is that we do not pretend a row is a person, and that we do not say anything about
them we could not defend to them.

**Real data does not arrange itself into a lesson.** Part A prints a decision log of six places the
export was ragged: a column that spells its own categories two ways, 29 enrollments with no
deprivation band, 738 enrollments with no recorded click at all, 1,062 with no first assignment,
negative day numbers from students who read ahead, and 576 enrollments that unregistered before day 1
and stayed in the enrollment table anyway. Every one of those is a decision somebody has to make in
public, and the notebook makes them in view and then says what each one cost. The last one, the
enrollment table, is the one that decides what the dashboard does on Monday.

You also come in holding a finding from week 3, and this week is careful to inherit what week 3
established rather than a tidier version of it. Week 3 concluded three things: swapping the
schedule-shape features out cut false positives a great deal overall, no error-rate *gradient* across
the deprivation deciles was ever distinguishable from noise, and the gradient in *who gets flagged*
did not flatten. So the model shipped here uses week 3's redesigned feature set, with `active_days`
and its relatives left out.

The dashboard then adds a lesson week 3 could not produce. Its flag rule is a caseload of 150 rather
than a probability threshold, and at that caseload the false positive rate collapses to a handful of
events: three false positives in the whole class. The gap between subgroups on that rate is therefore
not a fairness measurement at all, and the notebook says so with the counts printed beside it.
Meanwhile enrollments from the most deprived third of areas are flagged at 8.5 percent against 5.6
percent for the rest, a ratio of 1.52 with a 95 percent interval of [1.11, 2.07], built from 71 flags
in 833 enrollments against 78 in 1,388. That one has enough events under it to be read, and the
notebook says which numbers on the screen came with an interval and which could not. Part C puts both
in view, and the memo asks what a module team should do about the skew without leaning on the gap.

Part C also asks the question a dashboard is rarely asked. The model's 150 names are right 98.0
percent of the time, which sounds like a working model until the baseline that is not chance is
printed alongside it: the one-line rule "no assignment 1 recorded as submitted" matches 542
enrollments, 98.7 percent of which ended in Fail or Withdraw. Every one of the 150 comes from that
group. Before anyone argues about whether the model is fair, the notebook asks what it is adding.

## A note on the deprivation variable

Chart 4 in Part B and the audit in Part C both split the class by the UK Index of Multiple
Deprivation. That index is an **area-level** measure: it scores small neighborhoods on income,
employment, health, education, housing, crime, and living environment, and the band in this file is
the band of the area a student's address fell in. It is not a measurement of the student, of their
household, or of anything they did, and reading an area score as a property of the people who live
there is a well-known hazard.

The decile groups hold between 126 and 302 enrollments, which is why every point on those charts
carries a 95 percent interval. What the comparison is for is practice in reading a recorded group
difference carefully: what the variable records, how many enrollments sit under each point, how much
of the pattern the intervals can separate from noise, and what the file can and cannot establish.
The notebook keeps a short "what the data show, what is a plausible interpretation, what these files
cannot establish" table beside each of these moments.

## What is in this folder

| File | What it is |
|---|---|
| `week04_miniproject1_teacher_dashboard.ipynb` | The notebook. It downloads its data in the first code cell and writes nothing to disk. |
| `README.md` | This file. |

There is no `data/` folder this week and nothing to clone. The first code cell reads six CSV files
straight from the course dataset repository, `github.com/HakeoungLee/edis8100-datasets`, and prints
what arrived. No account, no authorization, no install. It takes a second or two.

That repository is public and read-only. If it is unreachable, the cell prints a plain-English
message naming the repository and saying what to try, rather than a wall of red traceback.

## Opening it in Colab

The course repository is public, so you need only a Google account and a browser.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week04-miniproject1-dashboards/week04_miniproject1_teacher_dashboard.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week04-miniproject1-dashboards/week04_miniproject1_teacher_dashboard.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, and enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`. Then select
`week04-miniproject1-dashboards/week04_miniproject1_teacher_dashboard.ipynb`.

### Keeping your own copy

Mini Project 1 is graded from your notebook, so before you change anything please choose **File >
Save a copy in Drive** and work in that copy. When you are finished, **File > Download > Download
.ipynb** and upload that file to Canvas.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy,
matplotlib, plotly, and scikit-learn, all of which ship with Anaconda, plus a working internet
connection for the first cell.

### A note about the two kinds of chart

Every panel is drawn twice: once with plotly, which is interactive, and once with matplotlib, which
is not.

That is deliberate. Plotly charts do not render when a notebook is read on GitHub, because GitHub
does not run javascript. If your reader never opens Colab, the plotly panels are blank rectangles to
them. The static snapshots are what they see. Building both is a habit worth keeping past this
course.

## Walkthrough

We move through Parts A to C together in class. The timings below are a rough guide rather than a
target, and it is fine if we spend longer somewhere and skip something else. Parts D to F are
finished afterwards. The four **Your turn** cells appear in reading order and already contain working
answers, so the notebook runs start to finish without you typing anything.

**Setup.** The provenance cell comes before any number: who collected this data, under what license,
and what we owe the people in it. Then the first code cell. It fetches six files and prints a line
per file saying how many rows arrived and what one row means.

**Part A: orientation (about 20 minutes).** Build the one table every panel needs, one row per
enrollment, and watch the decision log print as it goes. Six ragged places in the export, six
decisions made in public, and a stated cost for each. Three of them come back in Part E, and the one
to hold on to is the enrollment table: 576 enrollments unregistered on or before day 0 and are still
sitting in it. Then **Your turn 1**: one question these files can inform and one they cannot touch.
The second one is worth keeping in view all week.

**Part B: the class overview panel (about 25 minutes).** Four charts, each drawn once per
presentation, because BBB ran twice and the archive can address a question a teacher in the middle of
a term never can: is this a property of my course, or of this particular group of people? How each
run ended, when the module was worked, completion by fifth of first-30-day clicks, and completion by
deprivation decile. Every point on charts 3 and 4 carries a 95 percent interval, because the reading
of both turns on whether two lines coincide and whether a decile is genuinely below its neighbor.
Chart 3 replicates: every 2013J interval overlaps its 2014J twin. Chart 4 is a different kind of
finding: completion rises about 2.7 points per decile step in 2013J, 95 percent interval [2.0, 3.5],
and 2.2 points [1.4, 2.9] in 2014J. Neighboring deciles overlap, so the dip at decile 5 is not a
finding and the gradient is.

**Part C: the early warning panel (about 35 minutes).** Week 3's redesigned model goes on screen
(`clicks_first30`, `tma1_score_filled`, `tma1_submitted`), with a model card printed above it:
features, the flag rule, the base rate, and the false positive rate gaps with the event counts they
are built from. Every predicted probability is out of sample. Then the part most systems in the field
skip: each flagged enrollment's score is decomposed into what each feature contributed, so the panel
can say why a name is on the list.

The tallies underneath the chart repay a slow read, because they are what the memo argues from: 402
enrollments the model cannot tell apart, because all three of their feature values are identical; 128
of the 150 flag slots going to that block; 101 of the 150 names belonging to people who had
unregistered before the module opened, and 116 by day 30, which is the earliest the list could have
been drawn; and false positive rate gaps built from one, two, four, and six events. Then **Your turn
2**: change the caseload and the roster rule, and watch a staffing budget move a fairness statistic.

**Part D: the individual drilldown (about 25 minutes).** One person, four charts: tutor-marked
assignment trajectory against the middle half of the enrollments that submitted each assignment, a
profile card that lists what the model saw and the longer list of what it never did, weekly clicks
against the class mean, and submission lead time.

This is the only panel in the notebook that puts one real person alone on a screen, and the section
opens by saying so and setting three rules: every label here is a sentence somebody may say out loud
about this person, so labels describe what was recorded rather than what it means; the file holds no
job, no commute, no diagnosis, no broken laptop, and no reason; and a rank is a position inside one
cross-validation split rather than a property of a person. The band's denominator is printed under
every point, because it is not the class: submissions fall from 1,695 on day 19 to 1,033 on day 208,
46 percent of the 2,237 enrolled, so a line staying inside the band late in the term is staying
inside a smaller and more selected group. The default is student `154570`, whose recorded clicks in
the first 30 days are the highest in the presentation, to whom the model gave the lowest predicted
probability of all 2,237, and who unregistered on day 117. The panel never mentioned this person and
never could have. Then **Your turn 3**: the cell prints six students worth drilling into and why each
one breaks the panel in a different direction. Please pick one that is not the default.

**Part E: critique (about 30 minutes).** A cell computes six things the dashboard never shows the
teacher: how few of the enrollments that ended badly the list names (12.6 percent), how many flag
slots go to people who had already left (101 of 150 by day 0, 116 by day 30), how much the list
changes when only the random seed changes (5 of 150 names appear on all five draws, and 429 distinct
enrollments compete for the 150 slots), why the deprivation skew is not something a fairness metric
computed on completers will catch, what a 30-day window cannot see, and what the model added over one
column.

Three of those six are places where an obvious comparison is misleading and the notebook says why.
The roster rule appears to lift "reach" from 12.6 to 17.2 percent, but that comparison moves its own
denominator; a comparison that holds its denominator still counts correct names belonging to somebody
still registered on day 1, and goes from 46 to 143, and the version that uses day 30, the earliest
the list can exist, goes from 31 to 96. The false positive rate gap looks closed, but it is built
from three events across the whole class, so it cannot distinguish one design from another at this
caseload. And the 98.0 percent precision looks like a model earning its place until it is set beside
the 98.7 percent of a rule with no model in it. Then **Your turn 4**, the critique table, which is the
analytic core of the assignment.

**Part F: the design memo.** 300 words, in the marked markdown cell. Argue for one specific change
and respond to the strongest objection you can think of. One element is required: say what the module
team should do about the deprivation skew, and "fix the model" is not available as an answer.

**Going further (optional).** A working student-facing rewrite of the drilldown, an invitation to
improve it, and an appendix of worked examples for the Your turn cells. This is outside the class
session and nobody needs to work through it.

**Reflection and submission checklist.** Please bring the reflection answers to the debrief from 5:30
to 5:50.

## What this connects to in the readings

- **van Leeuwen, Teasley, and Wise (2022)**, *Teacher and student-facing learning analytics*: the two
  are different instruments, not one tool with two logins. The chapter also treats the reference
  frame, what a display compares the viewer to, as a design choice that decides what the display
  means. Parts B, D, E, and the optional section all draw on this.
- **Wise and Jung (2019)**, *Teaching with analytics: Towards a situated model of instructional
  decision-making*: pedagogical intentions shape what an instructor looks for, interpretation runs
  data against expectations and contextual knowledge the system does not hold, and responses come
  from a repertoire the instructor already has. This is the standard the memo is graded against.
- **Jung and Wise (2025)**, *How students engage with learning analytics*: access, action-taking, and
  the routines that form around received information, in a setting where the information arrives as
  messages rather than as a dashboard somebody has to go and visit. Directly relevant to the optional
  student-facing section.
- **Li, Jung, and Wise (2026)**, *How instructors use learning analytics: the pivotal role of
  pedagogy*: listed as additional reading, and the source of reflection question 4.
- **Kuzilek, Hlosta, and Zdrahal (2017)**, *Open University Learning Analytics dataset*: the data
  paper for the records you are working on. Reflection question 5 is about it, and it is worth ten
  minutes even if you read nothing else about the dataset.

## Rubric: Mini Project 1 (100 points)

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Every part is completed and connected: the orientation questions shape the panels, and the panels feed the critique and the memo as one argument. | All parts completed and run cleanly, with the connections between them mostly explicit. | Most parts completed; the sections read as separate exercises rather than one workflow. | Parts missing or unrun; the notebook does not execute end to end. |
| **Data Preparation and Technical Care** | Notebook runs top to bottom without error; the per-enrollment table is correct; the decision log is understood, and the cost of at least one of those decisions is carried into the critique. | Runs cleanly with correct aggregation; the ragged places in the export are mentioned but not pursued. | Runs with minor errors, or the aggregation and missingness choices are accepted without examination. | Does not run, or the data preparation is incorrect. |
| **Analysis and Visualization Choices** | Every figure is titled and labeled, colorblind-safe, and each design choice (aggregation, band versus rank, what is omitted) is defended. Static snapshots present and readable. | Figures are clear, titled, and labeled; snapshots present; choices mostly defended. | Figures readable but some are unlabeled, undefended, or missing snapshots. | Figures missing, mislabeled, or uninterpretable. |
| **Interpretation and Educational Meaning** | The critique table names a specific teacher action for each panel and a specific way each could mislead, with evidence from your own outputs. | Actions and risks named for all three panels with some evidence. | Generic actions ("monitor the student") or risks asserted without evidence. | Interpretation absent or unconnected to the outputs. |
| **Critical Reflection: Limits, Ethics, Equity** | The memo names a decision, cites at least two numbers from the notebook, proposes one concrete change, states who is protected, what it costs, and the strongest objection, and says what should be done about the deprivation skew without proposing a model fix. Draws on both required readings. | Memo makes a clear argument with evidence and cites at least one reading. | Memo describes the dashboard rather than arguing for a change, or omits the trade-off. | Memo missing, far off length, or unsupported by evidence. |

The AI interaction log and reflection are required for the submission to be considered complete.

## Going further (optional)

None of these is required. They are here for anyone who finishes early or who arrives with
programming experience.

1. **The student-facing redesign (the one in the notebook).** Take the working example and go
   further: attach one available action to each point on the chart, and argue that a student-facing
   display without an available action is a report card that arrived early.
2. **Show the uncertainty.** Replace the risk score bar with an interval built from the spread across
   cross validation splits, and sort the list into "consistently flagged" and "borderline" instead of
   ranking one to fifteen. Part E already shows why this matters: across five random splits, only 5
   enrollments appear on all five lists and 429 distinct enrollments compete for 150 slots. Then say
   what a hurried teacher does with the borderline group, and whether that is better or worse than
   what they do now.
3. **Move the window.** The model sees days 0 to 29 and assignment 1, and then never looks again. 134
   enrollments were withdrawn after day 100 and the panel had flagged 4 of them. Build a second model
   that also sees days 30 to 59 and the second tutor-marked assignment, score the same class, and
   report what it gains, what it costs in lateness, and whether the reason column starts saying
   something different.
4. **The 1,018 who never appear.** The list names 12.6 percent of the enrollments that go on to fail
   or withdraw. Characterize the rest. What do they have in common, what would a panel have to look at
   to surface them, and what would that panel cost in attention and in privacy?
5. **Rebuild the panel for 2014J.** Change `FOCAL_TERM` and run everything again. Which findings hold
   and which were properties of one cohort? This is the replication question the two presentations
   exist to let you ask.
6. **Design the refusal.** Write down three things this dashboard should not display even though the
   data supports them, and provide a reason for each refusal that would hold up with a dean who
   wants them added.
7. **Make it real.** Rebuild one panel for a course you have taught or taken. What data would you
   need, who owns it, and who would have to consent?

## Troubleshooting

**"NameError: name 'dash' is not defined" or something similar.**
A cell ran out of order, or the runtime restarted. **Runtime > Restart session and run all** in Colab, or
**Kernel > Restart & Run All** in Jupyter, then wait for every cell to finish. This resolves most
notebook problems.

**"The download did not work."**
The first cell prints a plain-English message naming the repository it was trying to reach. The usual
cause is no internet connection in the runtime. Colab always has one; a locked-down campus network
sometimes does not. Run the cell again, since brief network failures are common. If it still fails,
download the six CSV files from `github.com/HakeoungLee/edis8100-datasets` by hand, put them beside
the notebook, and change `BASE` to `"."` so pandas reads them from disk. That repository is public, so
this is never about a GitHub account or an invitation.

**The first cell is slow.**
It is fetching about 4 MB, most of it the compressed clickstream. On a normal connection it takes a
couple of seconds. It runs once, and later cells reuse what is already in memory.

**A plotly chart is blank, or nothing appears where a chart should be.**
In Colab this is almost always a stale runtime: **Runtime > Restart session and run all**. If you are reading
the notebook on GitHub rather than in Colab, plotly charts will never appear, by design. The
matplotlib snapshot immediately below each one is the version to look at.

**My matplotlib charts do not appear.**
The first code cell contains `%matplotlib inline`, so it needs to have been run.

**Part D says it cannot find my student.**
Student IDs in this dataset are plain numbers rather than `S001` style codes, and they are not
consecutive: `154570` and `2625315` are both real. The cell catches an id that is not in the
presentation, says so, and falls back to whichever enrollment has the most recorded clicks in the
first 30 days of whatever presentation is loaded, which in 2013J is `154570`. For a valid id to try,
take one from the six-student comparison table the cell prints.

**My numbers do not match the ones in the text.**
If you changed a **Your turn** cell, that is expected and good. If you did not, restart and run all.
The dataset is fixed and published, and the model's cross validation is seeded, so a clean run
reproduces the same numbers every time.

**Colab says "Cannot find notebook" or shows a 404.**
You are most likely signed into a different Google account. Check the profile picture in the top
right corner, switch to the account you want, and open the link again.

**I lost my edits.**
Colab does not save changes back to GitHub. **File > Save a copy in Drive** at the start of any
session where you plan to keep something.

**Red text appeared.**
Python errors are wordy, and none of them means something has been damaged. The **last line** of the
error usually names the real problem. Please ask, and we will read it together.

## Documenting AI use

Mini Project 1 is the first submission where the course AI policy applies in full.

If you used an AI assistant at any point, to explain a line of code, to check your reading of a
chart, to help you name a design flaw, to build a panel by vibe coding, or to draft the memo,
everything goes to the Canvas **AI Reflection** submission, in two different places on that page:

- **The conversation record goes in a Word file, attached to that submission.** The full exchanges,
  across every session and every tool, pasted in. Not a summary, and not into the text box.
- **The four reflection questions from the syllabus are answered in the text box** on the same page:
  how you used it; whether it helped and how; whether it made your work more challenging in any way;
  and what lesson about AI you would pass on to a friend or the class.

If you used no AI at all, one line in the text box saying so, with nothing attached, is also
documentation.

AI use is permitted in designated activities and is to be documented. Undisclosed use is an Honor
Code violation.

The reflection carries more weight than the log. The question worth answering is not whether you used
an assistant, it is what you accepted from it and how you checked. A memo that repeats a
plausible-sounding critique the assistant produced, without verification against your own printed
numbers, is the failure mode this course is about.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across
the lab weeks, and no notebook in this course generates a row.

These records describe real adults, many of them studying part time around jobs and families, which
is what the Open University is for. Their records were anonymized and released under CC BY 4.0 so
that the field could check its own work on data more than one lab can see. None of them agreed to be
a teaching example. It is worth asking who could be harmed by a claim before making it, noticing when
a metric reduces a person to one number, and noticing which people are not in the file at all.

If you reuse any figure or number from this notebook outside this course, please cite the dataset:

> Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset.
> *Scientific Data, 4*, 170171.

Licensed CC BY 4.0: you may use, share, and adapt it, including commercially, as long as you credit
the source. Attribution is not a formality here. It is the condition on which a research team made
records about real students available to people like you.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
