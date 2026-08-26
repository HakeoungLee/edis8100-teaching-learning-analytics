# Week 11: Co-Design Studio

Whose dashboard is this, and who was consulted when we decided?

This is the last hands-on session of the semester. We open the notebook after the student-led
discussion hour and the break, work through it together, and spend the final third of it turning
the semester's own instruments back on the semester.

Nothing in the notebook asks you to write code from scratch. Every edit is changing a word inside
quotes or a number in a list, and coding skill is not what is assessed anywhere in this course.
Questions are welcome at any point, including questions about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 11, Wednesday, November 4, 2026, Ridley Hall 137 |
| **Topic** | Designing and Co-Designing Learning Analytics Systems |
| **Guest speaker** | None this week. The discussion hour is entirely student led. |
| **Notebook portion** | Approximately 4:50 to 5:50 PM, instructor-guided, after the discussion hour and the break |
| **Notebook** | `week11_codesign_studio.ipynb` |
| **Data** | **Real, published, openly licensed.** Canvas Network Person-Course (1/2014 - 9/2015) De-Identified Open Dataset: 325,199 rows by 26 columns, one row per person per course across 238 Canvas Network open courses, January 2014 to September 2015. Collected by Canvas Network, the open-course arm of Instructure, from its own platform logs and its own registration survey. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `canvas-network` |
| **Licence** | **CC BY 4.0.** Free to use, share and adapt, including commercially, with attribution |
| **Citation** | Canvas Network. (2016). *Canvas Network Person-Course (1/2014 - 9/2015) De-Identified Open Dataset* [Data set]. Harvard Dataverse. https://doi.org/10.7910/DVN/1XORAL |
| **Libraries** | pandas, numpy, matplotlib |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | None from this notebook. It is a studio, and nothing here goes to Canvas. |
| **Due** | The **Course Research Project Rough Draft**, by 11:59 PM on Sunday, November 8, 2026, submitted on Canvas separately from anything in this folder, together with your AI interaction log and reflection. |
| **Prior coding experience needed** | None |

Week 11 is the last of the Discussion Leadership weeks. Leadership runs from Week 2 through Week 11,
and each of the four of you leads **two** of those weeks.

## What I hope you leave with

1. A way of holding stakeholders as data: persona cards that carry goals, fears, and decision
   rights, and a sense of why decision rights change what a metric is allowed to mean.
2. A comparison of four "top 500" lists built from four defensible measures of the same enrolments,
   read against what chance and course composition alone would produce.
3. Some practice reading your own sketch as a second persona would, with a file that records what
   learners said they wanted before they started.
4. An audit of our own semester: artifact by artifact from weeks 1 through 11, who might have had a
   voice in the design.

None of these is a coding objective.

The through-line: for ten weeks we have been the people deciding what gets measured, and the people
being measured have not been consulted once.

## Why this dataset, and not another

Canvas Network was a platform for free, open online courses. Anyone could register, nobody had to
finish, and the platform logged everything anyway. Instructure anonymised a slice of that record and
released it under CC BY 4.0 in 2016. Two properties make it a good file for a co-design studio, and
both are unusual.

**One. The choice of measure visibly changes who looks successful.** The file carries four defensible
measures of the same enrolment: the final grade the course recorded, the number of recorded page
views, the number of distinct days with activity, and the percent of the course's modules the person
reached. Give each of the four personas the measure they would reach for, take the top 500 by each,
and the lists barely overlap. The notebook gets there in four steps, because the first answer it
produces is spectacular and wrong, and finding out why is half of the lesson.

**Two. The file records what people said they wanted before they started.** At registration Canvas
Network asked what kind of participant someone expected to be and why they had signed up. 35,110
enrolments answered the participant-type question and 36,495 gave a reason. In almost every other
learning analytics dataset the learner persona is a role-play, and your imagination does the arguing.
Here, when a group builds a completion dashboard and swaps into the learner's chair, something in the
data can answer back.

**And one boundary that travels with property two.** The survey covers 10.8 percent of the rows.
Anyone reasoning from it is reasoning about respondents, and the notebook says so in three separate
places, because it is the same lesson as Week 5's annotated spans nested inside single essays and
Week 9's eight groups.

## What is in this folder

| File | What it is |
|---|---|
| `week11_codesign_studio.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is no `data/` folder and nothing to clone. The first code cell reads one 3 MB gzipped CSV
straight from the course dataset repository and prints what arrived. If the download fails it says so
in plain English, names the repository it was trying to reach, and gives the three likely causes,
rather than a long error trace.

## Opening it in Colab

The course repository is public, so you need only a Google account and a browser.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week11-codesign-studio/week11_codesign_studio.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week11-codesign-studio/week11_codesign_studio.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`, and select
`week11-codesign-studio/week11_codesign_studio.ipynb`.

The notebook also runs locally under Jupyter with pandas, numpy, and matplotlib, all of which ship
with Anaconda. Every figure is a static matplotlib image, so they render on the GitHub website too.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Your persona choice, your metric
set, and your audit numbers are the record of what you decided today, and three of them belong in
your Rough Draft notes.

## Walkthrough

We will move through this together in class. The timings below are a rough guide rather than a
target, and it is fine if we spend longer somewhere and skip something else.

| Step | Section | Minutes | What happens |
|---|---|---|---|
| 1 | Welcome and how the notebook works | 3 | Orientation, and Shift + Enter. |
| 2 | Setup | 3 | The provenance table, then the first code cell: 325,199 rows, 26 columns, 238 courses, 224,914 distinct people. |
| 3 | 1. The mess, before anything else | 8 | Empty columns, a missingness figure, and the survey column that arrived with two sets of labels. |
| 4 | 2. The personas as data | 5 | Four cards with goals, fears, decision rights, grain, access reality, and one measure each. |
| 5 | 3. The candidate metrics | 5 | The common population, the metric menu, and which measures can even produce a ranking. |
| 6 | 4. Your turn | 6 | Pick a persona and up to four metrics, then read the two-panel sketch. |
| 7 | 5. The leaderboards | 14 | Four steps, two chance baselines, and the overlap figure. |
| 8 | 6. The swap | 9 | The actionability figure, then what the learners said at registration. |
| 9 | 7. Retroactive design audit | 5 | Weeks 1 to 11, scored 0 to 3 for whose voice was owed. |
| 10 | Reflection and closing | 2 | Four prompts, and the checklist. |

**Going further** is a clearly marked optional section near the end, followed by an optional appendix
of worked examples. Neither is part of class time.

## What happens in each section

**Setup.** The provenance table comes before any number: the dataset, who collected it, the licence,
the citation, and one paragraph on what these people were told, which is close to nothing. Instructure
published this file under no obligation to do so, and the people in it did not choose to be a dataset.

**1. The mess, before anything else.** On purpose, first, because two decisions made here change every
number afterwards.

Three columns hold one value on every row: `registered` is 1 because the file only contains
registrations, and `final_cc_cname_DI` (country) and `gender` were withheld to protect the people in
it. That is the price of publishing at all, and it means any fairness question about gender or country
cannot be asked here. Week 3 asked those questions of a dataset that allowed them.

Then the figure that sets up the whole notebook: how much of each column is recorded at all.
`ndays_act` on 31.1 percent of rows, `nevents` on 26.5, `grade` on 25.2, `ncontent` on 12.7, the four
survey fields on 11.8. The prompt that follows walks the instrument, the setting, and the
circumstances in that order, and asks which of the three seems the most plausible account of the 12.7
percent, and what one would want to know about these courses before choosing.

Then the column that speaks two languages. `learner_type` contains both `Active` and `Active
participant`, and both `Passive` and `Passive participant`. Before merging them the notebook checks
whether any single course used both wordings: 112 courses use the short labels, 33 use the long ones,
and **not one uses both**, which is what a one-time change of survey wording looks like. So we merge,
and we write down what the merge costs: there is no overlap anywhere in the file where it could be
verified. The 3,261 rows that literally say `Missing` are dropped, out loud, with the count.

**2. The personas as data.** Dana Okonkwo built and ran an open course. Malik Ferrer enrolled in one.
Tobias Lindqvist runs analytics at the company hosting them. Ana Whitfield is the programme officer at
the foundation that paid for several to be built. Each card carries goals, fears, decision rights,
what they cannot change, the grain they think in, their access reality, and **the one measure they
would reach for first**, which is what makes the rest of the notebook possible.

The access-reality lines are worth reading together. Three of the four can change something. The
fourth can change only which tab he has open, and he is the one every row of the file is about.

The goals repay as much attention as the decision rights, because a persona card is where a deficit
assumption hides most comfortably. Dana's third stated fear is reading a low grade as a fact about a
person rather than about her own assessment design. Malik's first is being counted as somebody's
"dropout" for doing exactly what he said he would do. Neither card treats a learner as a problem to be
detected, and if a fifth persona you write does, that is the thing to notice.

**3. The candidate metrics.** Seven metrics computed from the file, and a decision made visibly. The
four persona measures are recorded on four different subsets, so comparing lists drawn from them would
confound any disagreement with the file's silence. From here on the notebook works on the **common
population**: the 21,693 enrolments, 6.7 percent of the file, from 19,924 people in 156 of the 238
courses, where all four are recorded. The cost is printed rather than buried: the kept rows are not a
random sample, and the median grade among rows that have one is 0.12 across the file and 0.37 here.

The *mistaken for* column does the framing work. Page views are mistaken for effort, active days for
commitment, modules reached for having understood the modules, and the platform's `explored` flag for
seriousness. Each label describes what was measured and each annotation names the leap it does not
support. Note also what is missing: **not one metric on this menu is "lower is better"**, because on a
platform nobody was required to use there is no measure where less of it is straightforwardly worse.
That is a reason to question any dashboard here that flags a person for having too little of
something.

Then the diagnostic that decides what section 5 is allowed to claim: can each measure even produce a
ranking? Page views can, with essentially no ties. Active days can, with 52 tied at the cut. Grade
cannot cleanly, with 1,370 tied at a perfect 1.0. And modules reached cannot at all, because **10,587
of the 21,693 enrolments, 48.8 percent, reached 100 percent of the modules.** The learner's own
measure is the one here that cannot make a leaderboard, which may be part of why nobody builds one on
it.

**4. Your turn.** Four values to change: `MY_PERSONA`, `MY_METRICS`, `FOCUS_COURSE`, `FOCUS_USER`.
Maximum four metrics, and fewer is a stronger design choice. The cell validates the choices and says
plainly if one is mistyped.

The sketch is two matplotlib panels: the population distribution of your first metric, and the focus
enrolment's percentile on each metric you chose, **shown twice**, once against all 21,693 and once
against only the people in the same course. That second bar is the point. Of the 66 courses here with
at least 30 such enrolments, 17 have a median final grade at or below 0.10 and 7 have a median at or
above 0.95, so a percentile computed across courses is averaging over an enormous difference in how
courses grade.

The default focus enrolment is chosen because it fits none of the easy stories. This person said at
registration that they intended to do the assignments. They then produced the highest page-view count
among all 436 registrations in their course, were the only one of the 64 with a modules-reached number
to reach every module, and the course's own `completed_%` column says they completed 75 percent of the
required modules. Their grade is 0.00, in a course whose median grade is a perfect 1.00. A short table
separates what the data show, what a plausible interpretation would be, and what the file cannot
establish, and the prompt walks the instrument, the setting, and the circumstances before anything
about the person becomes a candidate. The file never says whether a 0.00 means "submitted and scored
zero" or "never submitted anything gradeable".

**5. The leaderboards.** The centre of the session, in four steps, because the first answer is wrong in
an instructive way.

*Step 1.* Sort the whole file and take the top 500 by each measure, which is literally what a
leaderboard query does. The top 500 by grade and the top 500 by page views **share nobody at all**.
Grade against active days, also zero.

*Step 2, rule out the ordinary explanation.* Of the top 500 by grade, only 165 have a page-view number
recorded at all, and only 168 have an active-days number. Most of them were never candidates. The zero
is mostly the file being silent, and reporting it as a finding would have been wrong.

*Step 3, ask again properly.* Same question on the common population, with three things attached. A
**uniform chance baseline**, simulated rather than asserted: two unrelated lists of 500 drawn from
21,693 share about 11, and between 5 and 18 in 95 percent of draws, which matches the arithmetic 500 x
500 / 21,693 = 11.5. A **course-matched chance baseline**, which is the one that matters, because every
list leans heavily on a few courses and two lists leaning on the same big course overlap more than 11
even when they pick independently inside every course; holding each list's course composition fixed,
the expected overlap is the sum over courses of a times b over n. And a **tie-break that can be
defended**: because thousands of enrolments sit tied at the top of grade and modules reached, the
notebook takes each top 500 two hundred times, breaking ties at random, and reports the median and
range. Grade against page views: 19, uniform 11, course-matched 11. Grade against active days: 26
against 13. Grade against modules reached: 14 against 13. Page views against active days: 133 against a
course-matched **43**, which is the pair that agrees, and they are two slices of the same clicking from
largely the same course.

*Step 4, one more ordinary explanation.* Rows nest inside courses. The active-days top 500 turns out to
be **83 percent a single Humanities course**, and the page-views top 500 is 68 percent that same
course. A leaderboard across 156 courses is substantially a list of courses, and a funder who read it
as a fact about people would be making the mistake the whole section exists to prevent.

*Holding the course constant.* Rank within each course, then take the top 500 by within-course
standing. Now the lists span 90 to 155 courses instead of 28 to 56, and the answer is: grade against
page views share **82 of 500**, grade against active days 82, grade against modules reached 70, page
views against active days 145, active days against modules reached 65. Read those against the
course-matched baseline, which runs **42 to 46** for these pairs, and not against the uniform 11: the
measures sit above chance by a factor of roughly one and a half to two for the grade pairs, rather than
by the factor of six or more the uniform number would suggest. They are not unrelated, they are not the
same, and at least four in five of the people on any grade-based list are absent from any clicking-based
one.

The section closes with the objection a good colleague will raise: surely they just correlate? Spearman
rank correlations among the four run from 0.22 to 0.56, and the notebook reports Pearson beside them for
contrast, because page views run from 1 to 530,411 and a Pearson correlation on raw counts is dominated
by a handful of enormous values (grade against page views: Spearman 0.51, Pearson 0.17). So the
objection is half right, and the half it gets wrong is the important half. **Moderate agreement across a
whole population is compatible with almost complete disagreement about who is at the top, and a
dashboard lives at the end of the distribution where the agreement has run out.**

**6. The swap.** First the mechanical part: for each of the other three personas, what they could do
with your chosen metrics and which of their stated fears each one touches. Then the actionability
figure over all seven metrics and all four people, where a `!` marks a metric that touches that
person's fear. Out of a maximum of 14, the platform can act on 11, the course team on 10, the funder on
9, and the learner on 6. The person every row is about can act **directly** on exactly one metric of
the seven; the company that owns the file can act directly on four.

Then something in the file answers back, which is why this dataset is here.

A completion bar at 0.70 is cleared by 17,515 of the 82,002 enrolments that have a grade, which is 21.4
percent, and by 5.4 percent of all 325,199 rows. Which denominator a dashboard uses is a design decision
and it moves the headline by a factor of four.

And of the 35,110 enrolments that answered the participant-type question, from 30,336 distinct people,
**18,941, or 53.9 percent, chose an answer that says in so many words that they were not planning to do
the assignments**: 13,582 passive participants, 2,820 drop-ins, 2,539 observers. Their median grades are
0.083, 0.022 and 0.007 against 0.175 for the people who said they intended to do the work, each with a
95 percent interval from **resampling the 145 courses rather than the rows**, because a course's grading
design is the thing these people have in common. The intervals on adjacent plans overlap, so the file
separates the ends of that list rather than the neighbours. The figure carries the counts beside the
rates and the base rate as a dotted line, and it makes the point that these answers are not a clean
sorting of people either: 257 of the 1,926 self-declared observers with a grade, 13.3 percent, cleared
the bar anyway.

The notebook is explicit that `learner_type` records one answer to one menu, chosen once, before the
course began, rather than a stable property of anyone, and that the four groups differ greatly in size.
The section is framed as an exercise in reading a recorded group difference carefully.

Last, what they said they came for. 36,495 enrolments gave a reason, and the most common one, given by
20,494 of them or 56.2 percent, is *"I enjoy learning about topics that interest me."* There is no
column on the menu that measures that. There is none in OULAD either. The measures we have are not
there because they matter most; they are there because they are what a web server writes down for free.

The prompt then draws the boundary, with a short table separating what the data show, what a plausible
interpretation would be, and what the file cannot establish. The survey is 10.8 percent of the file. The
defensible sentence is "of the people who answered, a majority said they were not planning to do the
assignments", not "most learners were not trying to complete", and the difference between those two
sentences is most of what this course has to say about range restriction.

**7. Retroactive design audit.** Every artifact this course built from week 1 to week 11, **with the
real dataset each one used**, the design decision each one quietly made, and a score from 0 to 3 for how
much voice each persona should have had: none, informed, consulted, veto. Week 1 on UCI student
performance, weeks 2, 3, 4 and 8 on OULAD, week 5 on PERSUADE 2.0, week 6 on JUSThink, week 7 on EdNet
KT3, week 9 on JUSThink and a computer-networks chat corpus, week 10 on Open Game Data from the Field
Day Lab, and week 11 on this file.

The four personas travel across the weeks under different names: somebody who built the learning
experience, somebody it was for, an institution or company whose system did the recording, and somebody
who paid for the work. The names change and the four positions do not.

In the default scoring the learner column totals 32 out of 33 and no learner was consulted for any of
it. The dictionary is my first guess, and revising it is the exercise.

The last row is today. This notebook ranked 21,693 enrolments four ways and put 500 names on each list
without asking one of them which measure they would have chosen, and the second prompt asks the useful
version of the question: not what would have felt better, but what would have been **different on the
screen**.

**Reflection.** Four prompts, one per reading plus one that turns the lens on your own project, with a
cell to write in. These are the questions the discussion block opens with, and they are directly usable
in your Rough Draft.

**Before you leave.** Nothing here is submitted. Save your copy, and paste three things into your
project notes: your metric set with a one-sentence account of why those and not others, the one audit
cell you moved with your reason, and the sentence you would say to Malik with your dashboard on the
screen.

## Going further (optional)

Optional, and not part of class time. Nothing later depends on any of it.

1. **Add the fifth persona this platform has no column for.** Copy an entry in `PERSONAS`, write a
   guardian of a child in the week 6 or week 10 data, a disability services coordinator, a translator,
   or a research ethics board, then add the matching `act_` column to `CATALOG` and redraw the
   actionability figure. The guardian is the instructive case: their column is almost all `3`s where the
   learner is a minor and almost all `0`s everywhere else, which makes them the one persona whose
   relevance is a property of the dataset rather than of the role.
2. **Write the refusal list and the interface copy.** Name the metrics you would decline to show any of
   the four personas, then write the exact sentence you would put in the interface where each one would
   have gone. "We do not show this" is a design decision that has to be readable by the person who
   wanted it, and drafting that sentence is harder and more useful than choosing the metric.
3. **Put forum posts back on the menu, carefully.** `nforum_posts` is deliberately excluded, because it
   is recorded for only 9,516 of the 21,693 enrolments in the common population and adding it would
   silently change the population again. Build the five-measure version on its own smaller common
   population, report how many rows and courses survive, and then say whether the extra measure was
   worth the extra restriction. That trade is most of the work.
4. **Change the tie-break and watch what moves.** Re-run the overlap matrix with `B=1` and a fixed seed,
   then with `B=1000`. The pairs involving page views and active days barely move; the pairs involving
   grade and modules reached move a lot. Write the two sentences you would put under the figure
   explaining why, and then say what that implies about any leaderboard built on a measure with a
   ceiling.
5. **Cost out one co-design session.** Take the single artifact where you moved an audit score to 2 or
   3 and write the agenda for the 45-minute session that score implies: who attends, what artifact you
   put in front of them, what decision they actually get to make, and what happens if they say no. Then
   specify what would have changed on the screen. A veto nobody can exercise is a 1 in disguise.
6. **Ask the question the survey did not.** The intake survey asked what kind of participant someone
   expected to be and why they registered. Write the one extra question that would have made a
   learner-facing dashboard possible, then work out what the platform would have had to log to answer
   it, and what that logging would have cost the person. Most proposals in this field skip both halves
   of that sentence.

The notebook also ends with an optional appendix of worked examples: a defensible metric set for each
persona, what the four steps in section 5 were for, and the audit cells people most often move. It is
worth reading after your own attempt rather than before.

## Troubleshooting

**"Could not download the data file."**
The first cell prints this instead of a traceback, along with the URL it tried and the three likely
causes: no internet in the runtime, a firewall between you and github.com, or the course dataset
repository `github.com/HakeoungLee/edis8100-datasets` having moved. Try `Runtime > Restart session and run all`
first. If it still fails, please send the instructor the error line the cell prints.

**"NameError: name 'core' is not defined", or `pc`, or `CATALOG`**
Those are built in the setup and section 3 cells, and everything downstream needs them. Use `Runtime >
Restart session and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This resolves most notebook
problems.

**"AssertionError: MY_PERSONA must be one of ['teacher', 'learner', 'platform', 'funder']"**
The same goes for an assertion about metrics or the focus enrolment. Those checks are deliberate: they
report a typo immediately rather than letting it fail strangely three cells later. The message names
the problem, and the valid metric keys are printed just above.

**"That course/user pair is not in the common population."**
Only 21,693 of the 325,199 rows have all four measures recorded, so most `course_id_DI` and `userid_DI`
pairs in the file are not selectable here. Keep the default, or pick a pair by running
`core[['course_id_DI', 'userid_DI']].head(20)`.

**"Pick between 1 and 4 metrics."**
That is the design constraint rather than a bug. Four is the ceiling on purpose.

**A cell is taking ten seconds**
Expected, three times. The chance baseline simulates 2,000 random pairs of lists, each overlap matrix
rebuilds the four top-500 lists 200 times with different random tie-breaks, and the grade-by-plan figure
resamples 145 courses 400 times. Each of those buys an interval instead of a single number. The whole
notebook runs in well under a minute.

**My numbers are slightly different from the ones in this README**
If you changed a **Your turn** cell, that is expected. If you did not, check the third digit: every
resampling step is seeded, so a clean run reproduces the same numbers every time. If a whole column has
changed, restart and run all.

**My audit numbers are different from the ones in the printout**
They should be. The dictionary in section 7 is my first guess and you were invited to revise it. One
moved cell and your reason for moving it is plenty to bring to the discussion.

**I cannot tell the shades of the heatmaps apart**
No need to. Every cell prints its value as text on top of the colour, and both heatmaps have the same
numbers printed as a plain table in the cell above or below. The numbers and the column totals are
where the finding lives.

**I have no idea which metrics to choose**
Starting from your persona's question rather than from the menu tends to help. The optional appendix at
the end of the notebook has a defensible set for each of the four personas with the reasoning attached,
and it is worth reading after an attempt rather than before.

**Colab says "Cannot find notebook" or shows a 404**
You are most likely signed into a different Google account. Check the profile picture in the top right
corner, switch to the account you want, and open the link again.

**Red text appeared**
Python errors are wordy, and none of them means something has been damaged. The **last line** of the
error usually names the real problem. Please ask, and we will read it together.

## Documenting AI use

This notebook is not a graded submission, but something substantial is due this week: the **Course
Research Project Rough Draft**, uploaded to Canvas by 11:59 PM on Sunday, November 8, 2026, separately
from anything here.

If you used an AI assistant while drafting, or while working through this notebook, the course AI policy
asks for two things, and they go in two different places in the **AI Reflection** submission on Canvas:

- **The conversation record goes in an attached Word file.** The full exchange, across every tool and
  every session, pasted in rather than summarized.
- **The four reflection questions from the syllabus are answered in the Canvas text box**, directly,
  rather than inside the attachment. Copy them in and answer each one: how you used it; whether it
  helped and how; whether it made your work more challenging in any way; and what lesson about AI you
  would pass on to a friend or the class.

If you used no AI at all, one line in the text box saying so is a complete and acceptable submission.

AI use is permitted in designated activities and is documented. Undisclosed use is an Honor Code
violation. Disclosed use costs you nothing. In a week spent asking who deserves a say in a system that
measures them, disclosure is the same courtesy, pointed at yourself.

## Connections to this week's readings

- **Carvalho, Martinez-Maldonado, Tsai, Markauskaite, and De Laat (2022)**, on designing for learning in
  an AI world: design starts from the activity, its purposes, and its setting, rather than from the
  traces a system happens to emit. Every measure on this menu is something a web server writes down for
  free, and the single most common answer people gave for why they registered has no column at all. The
  reflection asks what activity you would have had to design first for a measure of that answer to be
  worth reading.
- **Bang and Vossoughi (2016)**, on participatory design research and educational justice: participatory
  design is about studying and changing relations, not about collecting stakeholder preferences and then
  proceeding as planned. The actionability figure is a picture of a relation. The person the file is
  about can act directly on one metric of seven and the company that owns the file can act directly on
  four. That asymmetry is the relation, and it is worth naming before proposing another one.
- **Prieto-Alvarez, Martinez-Maldonado, and Anderson (2018)**, on co-designing learning analytics tools
  with learners: learners as designers rather than as data sources. Section 7 is the uncomfortable
  receipt for eleven weeks of not doing this, and section 6 is the closest a dataset comes to letting
  the learners answer back on their own behalf.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across the
lab weeks, and no notebook in this course generates a row.

Today's file holds records for real people who signed up for free online courses on the open internet
between 2014 and 2015. Their clicks were logged because logging is what a learning platform does, and
some of them also answered a short survey at registration. They were not recruited into a study.
Instructure anonymised the file and published it under CC BY 4.0 so that people outside the company
could learn from it, which is what we are about to do, and the only reason the file can be opened at all
is that somebody chose to release it.

None of them agreed to be a teaching example. It is worth asking who could be harmed by a claim before
making it, noticing when a metric reduces a person to one number, and noticing which people are not in
the file at all. That stance runs through every week of the course.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
