# Week 11: Co-Design Studio

Whose dashboard is this, and who was in the room when we decided?

## At a glance

| | |
|---|---|
| **Session** | Wednesday, November 11, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Designing and Co-Designing Learning Analytics Systems |
| **Guest speaker** | None this week. The 60-minute discussion block is entirely student led. |
| **In-class time on this notebook** | About 30 minutes, in the hands-on block (4:30 to 5:00). The notebook is deliberately light on machinery: most of today is design dialogue, and the notebook is the sketchpad that gives the dialogue something to push against. |
| **Deliverable** | None from this notebook. It is a studio, not a graded submission. |
| **Due date** | The **Course Research Project Rough Draft** is due this week via Canvas, submitted separately from this notebook, together with your AI interaction log and reflection. |
| **Notebook** | `week11_codesign_studio.ipynb` |
| **Data used** | **Real, not synthetic.** The **Canvas Network Person-Course (1/2014 - 9/2015) De-Identified Open Dataset**: 325,199 rows by 26 columns, one row per person per course across 238 Canvas Network open courses, January 2014 to September 2015. Collected by Canvas Network, the open-course arm of Instructure, from its own platform logs and its own registration survey. Loaded over the network by the notebook's first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `canvas-network`. No account, no password, nothing to download by hand. |
| **Licence** | **CC BY 4.0.** Free to use, share and adapt, including commercially, with attribution. |
| **Citation** | Canvas Network. (2016). *Canvas Network Person-Course (1/2014 - 9/2015) De-Identified Open Dataset* [Data set]. Harvard Dataverse. https://doi.org/10.7910/DVN/1XORAL |
| **Libraries** | pandas, numpy, matplotlib |

## Objectives

By the end of this activity you will be able to:

1. **Represent** stakeholders as data: read a set of persona cards that carry goals, fears, and decision rights, and explain why decision rights change what a metric is allowed to mean.
2. **Show that the measure picks the winner**: build four "top 500" lists from four defensible measures of the same enrolments, compare them against what chance alone would produce, and rule out the two boring explanations before believing the interesting one.
3. **Swap** seats and critique: read your own sketch through a second persona's eyes, and let the file answer back, because this file records what learners said they wanted before they started.
4. **Audit** your own semester: decide, artifact by artifact from weeks 1 through 11, who should have had a voice in each design decision and did not.

The through-line of the session: for ten weeks we have been the people who decide what gets measured, and the people being measured have not been in the room once. This is the last hands-on session of the semester, and it spends its final third turning the semester's own instruments back on the semester.

## Why this dataset, and not another

Canvas Network was a platform for free, open online courses. Anyone could register, nobody had to finish, and the platform logged everything anyway. Instructure anonymised a slice of that record and released it under CC BY 4.0 in 2016. Two properties make it the right file for a co-design studio, and both of them are unusual.

**One. The choice of measure visibly changes who looks successful.** The file carries four defensible measures of the same enrolment: the final grade the course recorded, the number of recorded page views, the number of distinct days with activity, and the percent of the course's modules the person reached. Give each of the four personas the measure they would reach for, take the top 500 by each, and the lists barely overlap. The notebook gets there in four steps, because the first answer it produces is spectacular and wrong, and finding out why is half of the lesson.

**Two. The file records what people said they wanted before they started.** At registration Canvas Network asked what kind of participant someone expected to be and why they had signed up. 35,110 enrolments answered the participant-type question and 36,495 gave a reason. In almost every other learning analytics dataset the learner persona is a role-play, and your imagination does the arguing. Here, when a group builds a completion dashboard and swaps into the learner's chair, the rebuttal is inside the data.

**And one warning that travels with property two.** The survey covers 10.8 percent of the rows. Anyone reasoning from it is reasoning about respondents, and the notebook says so in three separate places, because it is the same lesson as Week 5's annotated spans nested inside single essays and Week 9's eight groups.

## What is in this folder

| File | What it is |
|---|---|
| `week11_codesign_studio.ipynb` | The notebook. It downloads its own data and runs top to bottom untouched in about half a minute. |
| `README.md` | This file. |

There is no `data/` folder and nothing to clone. The first code cell reads one 3 MB gzipped CSV straight from the course dataset repository and prints what arrived. If the download fails it says so in plain English, names the repository it was trying to reach, and tells you which of three things it probably was, instead of throwing a traceback at you.

## How to open this in Colab

The course repository is public, so the Colab badge opens the notebook directly. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
5. Select `week11-codesign-studio/week11_codesign_studio.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week11-codesign-studio/week11_codesign_studio.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week11-codesign-studio/week11_codesign_studio.ipynb`

Colab needs internet access for the first cell, which it has. You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda. Every figure is a static matplotlib image, so they all render on the GitHub website too.

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your persona choice, your metric set, and your audit numbers are the record of what you decided today, and three of them belong in your Rough Draft notes.

## Step-by-step walkthrough

Total time is about 30 minutes of code, which is the point: today the code is short so the conversation can be long. Every edit in this notebook is changing a word inside quotes or a number in a list. Nothing asks you to write code from scratch. A few cells pause for five or ten seconds because they repeat a calculation two hundred times to put an honest interval around it.

**Setup: where this data comes from (2 minutes).** Read the provenance table before you run anything: the dataset, who collected it, the licence, the citation, and one paragraph on what these people were told, which is close to nothing. Instructure published this file under no obligation to do so, and the people in it did not choose to be a dataset. Then run the first code cell. It downloads the file and prints 325,199 rows, 26 columns, 238 courses, 224,914 distinct people.

**1. The mess, before anything else (5 minutes).** On purpose, first, because two decisions made here change every number afterwards.

Three columns hold one value on every row: `registered` is 1 because the file only contains registrations, and `final_cc_cname_DI` (country) and `gender` were withheld to protect the people in it. That is the price of publishing at all, and it means any fairness question about gender or country cannot be asked here. Week 3 asked those questions of a dataset that allowed them.

Then the figure that sets up the whole notebook: how much of each column is actually recorded. `ndays_act` on 31.1 percent of rows, `nevents` on 26.5, `grade` on 25.2, `ncontent` on 12.7, the four survey fields on 11.8. The interpretation prompt walks the instrument, the setting, and the circumstances in that order, and you reach anything about a person only at step three, by which point you no longer need it.

Then the column that speaks two languages. `learner_type` contains both `Active` and `Active participant`, and both `Passive` and `Passive participant`. Before merging them the notebook checks whether any single course used both wordings: 112 courses use the short labels, 33 use the long ones, and **not one uses both**, which is what a one-time change of survey wording looks like. So we merge, and we write down what the merge costs: there is no overlap anywhere in the file where we could verify it. The 3,261 rows that literally say `Missing` are dropped, out loud, with the count.

**2. Four people, written down as data (4 minutes).** Dana Okonkwo built and ran an open course. Malik Ferrer enrolled in one. Tobias Lindqvist runs analytics at the company hosting them. Ana Whitfield is the programme officer at the foundation that paid for several to be built. Each card carries goals, fears, decision rights, what they cannot change, the grain they think in, their access reality, and **the one measure they would reach for first**, which is what makes the rest of the notebook possible.

Read the access-reality lines together. Three of the four can change something. The fourth can change only which tab he has open, and he is the one every row of the file is about.

Read the goals as carefully as the decision rights, because a persona card is where a deficit assumption hides most comfortably. Dana's third stated fear is reading a low grade as a fact about a person rather than about her own assessment design. Malik's first is being counted as somebody's "dropout" for doing exactly what he said he would do. Neither card treats a learner as a problem to be detected, and if yours does when you write a fifth persona, that is the thing to notice.

**3. The metric menu (4 minutes).** Seven metrics computed from the file, and a decision made in front of you. The four persona measures are recorded on four different subsets, so comparing lists drawn from them would confound any disagreement with the file's silence. From here on the notebook works on the **common population**: the 21,693 enrolments, 6.7 percent of the file, from 19,924 people in 156 of the 238 courses, where all four are recorded. The cost is printed rather than buried: the kept rows are not a random sample, and the median grade among rows that have one is 0.12 across the file and 0.37 here.

The *mistaken for* column does the framing work. Page views are mistaken for effort, active days for commitment, modules reached for having understood the modules, and the platform's `explored` flag for seriousness. Each label describes what was measured and each annotation names the leap you are not entitled to make. Note also what is missing: **not one metric on this menu is "lower is better"**, because on a platform nobody was required to use there is no measure where less of it is straightforwardly worse. Be suspicious of any dashboard here that flags a person for having too little of something.

Then the diagnostic that decides what section 5 is allowed to claim: can each measure even produce a ranking? Page views can, with essentially no ties. Active days can, with 52 tied at the cut. Grade cannot cleanly, with 1,370 tied at a perfect 1.0. And modules reached cannot at all, because **10,587 of the 21,693 enrolments, 48.8 percent, reached 100 percent of the modules.** The learner's own measure is the one measure here that cannot make a leaderboard, which may be part of why nobody builds one on it.

**4. Pick a persona and pick your metrics (3 minutes).** Four values to change: `MY_PERSONA`, `MY_METRICS`, `FOCUS_COURSE`, `FOCUS_USER`. Maximum four metrics, fewer is braver. The cell validates your choices and tells you plainly if you mistype one.

The sketch is two matplotlib panels: the population distribution of your first metric, and the focus enrolment's percentile on each metric you chose, **shown twice**, once against all 21,693 and once against only the people in the same course. That second bar is the point. Of the 66 courses here with at least 30 such enrolments, 17 have a median final grade at or below 0.10 and 7 have a median at or above 0.95, so a percentile computed across courses is quietly averaging over an enormous difference in how courses grade.

The default focus enrolment is chosen because it embarrasses every easy story. This person said at registration that they intended to do the assignments. They then produced the highest page-view count among all 436 registrations in their course, were the only one of the 64 with a modules-reached number to reach every module, and the course's own `completed_%` column says they completed 75 percent of the required modules. Their grade is 0.00, in a course whose median grade is a perfect 1.00. The prompt walks the instrument, the setting, and the circumstances before it will let you say anything about the person, and it points out that the file never says whether a 0.00 means "submitted and scored zero" or "never submitted anything gradeable".

**5. Four leaderboards, one file (8 minutes).** The centre of the session, in four steps, because the first answer is wrong in an instructive way.

*Step 1.* Sort the whole file and take the top 500 by each measure, which is literally what a leaderboard query does. The top 500 by grade and the top 500 by page views **share nobody at all**. Grade against active days, also zero.

*Step 2, rule out the boring explanation.* Of the top 500 by grade, only 165 have a page-view number recorded at all, and only 168 have an active-days number. Most of them were never candidates. The zero is mostly the file being silent, and reporting it as a finding would have been wrong.

*Step 3, ask again properly.* Same question on the common population, with three things attached. A **uniform chance baseline**, simulated rather than asserted: two unrelated lists of 500 drawn from 21,693 share about 11, and between 5 and 18 in 95 percent of draws, which matches the arithmetic 500 × 500 / 21,693 = 11.5. A **course-matched chance baseline**, which is the one that matters, because every list leans heavily on a few courses and two lists leaning on the same big course overlap more than 11 even when they pick independently inside every course; holding each list's course composition fixed, the expected overlap is the sum over courses of a·b/n. And an **honest tie-break**: because thousands of enrolments sit tied at the top of grade and modules reached, the notebook takes each top 500 two hundred times, breaking ties at random, and reports the median and range. Grade against page views: 19, uniform 11, course-matched 11. Grade against active days: 26 against 13. Grade against modules reached: 14 against 13. Page views against active days: 133 against a course-matched **43**, which is the pair that agrees, and they are two slices of the same clicking from largely the same course.

*Step 4, one more boring explanation.* Rows nest inside courses. The active-days top 500 turns out to be **83 percent a single Humanities course**, and the page-views top 500 is 68 percent the same one. A leaderboard across 156 courses is substantially a list of courses, and a funder who read it as a fact about people would be making the mistake the whole section exists to prevent.

*The honest version.* Rank within each course, then take the top 500 by within-course standing. Now the lists span 90 to 155 courses instead of 28 to 56, and the answer is: grade against page views share **82 of 500**, grade against active days 82, grade against modules reached 70, page views against active days 145, active days against modules reached 65. Read those against the course-matched baseline, which runs **42 to 46** for these pairs, and not against the uniform 11: the measures sit above chance by a factor of about one and a half, not by a factor of six. They are not unrelated, they are not the same, and at least four in five of the people on any grade-based list are absent from any clicking-based one. The uniform baseline would have made 65 of 500 look like six times chance; the right baseline makes it barely above what course composition produces on its own.

The section closes with the objection a good colleague will raise: surely they just correlate? Spearman rank correlations among the four run from 0.22 to 0.56, and the notebook reports Pearson beside them for contrast, because page views run from 1 to 530,411 and a Pearson correlation on raw counts is dominated by a handful of enormous values (grade against page views: Spearman 0.51, Pearson 0.17). So the objection is half right, and the half it gets wrong is the important half. **Moderate agreement across a whole population is perfectly compatible with almost complete disagreement about who is at the top, and a dashboard lives at the end of the distribution where the agreement has run out.**

**6. The swap (6 minutes).** First the mechanical part: for each of the other three personas, what they could actually do with your chosen metrics and which of their stated fears each one touches. Then the actionability figure over all seven metrics and all four people, where a `!` marks a metric that touches that person's fear. Out of a maximum of 14, the platform can act on 11, the course team on 10, the funder on 9, and the learner on 6. The person every row is about can act **directly** on exactly one metric of the seven; the company that owns the file can act directly on four.

Then the file answers back, which is why this dataset is here.

A completion bar at 0.70 is cleared by 17,515 of the 82,002 enrolments that have a grade, which is 21.4 percent, and by 5.4 percent of all 325,199 rows. Which denominator a dashboard uses is a design decision and it moves the headline by a factor of four.

And of the 35,110 enrolments that answered the participant-type question, from 30,336 distinct people, **18,941, or 53.9 percent, chose an answer that says in so many words that they were not planning to do the assignments**: 13,582 passive participants, 2,820 drop-ins, 2,539 observers. Their median grades are 0.083, 0.022 and 0.007 against 0.175 for the people who said they intended to do the work, each with a 95 percent interval from **resampling the 145 courses rather than the rows**, because a course's grading design is the thing these people have in common. The figure also carries the counts beside the rates, and the base rate as a dotted line, and it makes the point that these answers are not a clean sorting of people either: 257 of the 1,926 self-declared observers with a grade, 13.3 percent, cleared the bar anyway.

Last, what they said they came for. 36,495 enrolments gave a reason, and the most common one, given by 20,494 of them or 56.2 percent, is *"I enjoy learning about topics that interest me."* There is no column on the menu that measures that. There is none in OULAD either. The measures we have are not there because they matter most; they are there because they are what a web server writes down for free.

The interpretation prompt then draws the boundary hard. The survey is 10.8 percent of the file. The defensible sentence is "of the people who answered, a majority said they were not planning to do the assignments", not "most learners were not trying to complete", and the difference between those two sentences is the whole of what this course teaches about range restriction.

**7. Retroactive design audit (5 minutes).** Every artifact this course built from week 1 to week 11, **with the real dataset each one used**, the design decision each one quietly made, and a score from 0 to 3 for how much voice each persona should have had: none, informed, consulted, veto. Week 1 on UCI student performance, weeks 2, 3, 4 and 8 on OULAD, week 5 on PERSUADE 2.0, week 6 on JUSThink, week 7 on EdNet KT3, week 9 on JUSThink and a computer-networks chat corpus, week 10 on Open Game Data from the Field Day Lab, and week 11 on this file.

The four personas travel across the weeks under different names: somebody who built the learning experience, somebody it was for, an institution or company whose system did the recording, and somebody who paid for the work. The names change and the four positions do not.

In the default scoring the learner column totals 32 out of 33 and no learner was in the room for any of it. The dictionary is the instructor's first guess and you are expected to argue with it.

The last row is today. This notebook ranked 21,693 enrolments four ways and put 500 names on each list without asking one of them which measure they would have chosen, and the second prompt asks the only useful version of the question: not what would have felt better, but what would have been **different on the screen**.

**8. Stretch (optional, only if you finish early).** Add a persona this platform has no column for, write the refusal list, or read the worked scatter of page views against grade for the 4,213 survey respondents in the common population, coloured by what they said they intended to do. It prints two numbers worth carrying into the discussion: 1,217 enrolments sit in the many-page-views, low-grade corner and 649 of them, 53 percent, had said they intended to do the assignments; 275 sit in the mirror corner. Neither corner is an anomaly to explain away. Each is a list of specific people, and the two dashboards would do opposite things to them.

**Reflection.** Four prompts, one per reading plus one that turns the lens on your own project. These are the questions the discussion block opens with, and they are directly usable in your Rough Draft.

**Submission checklist.** Nothing here is submitted. Save your copy, and paste three things into your project notes: your metric set with a one-sentence defense, the one audit cell you moved with your reason, and the sentence you would say to Malik with your dashboard on the screen.

## What this connects to in the readings

- **Carvalho, Martinez-Maldonado, Tsai, Markauskaite, and De Laat (2022)**, *How can we design for learning in an AI world?*: design starts from the activity, its purposes, and its setting, not from the traces a system happens to emit. Every measure on this menu is something a web server writes down for free, and the single most common answer people gave for why they registered has no column at all. The reflection asks what activity you would have had to design first for a measure of that answer to be worth reading.
- **Bang and Vossoughi (2016)**, *Participatory design research and educational justice: Studying learning and relations within social change making*: participatory design is about studying and changing relations, not about collecting stakeholder preferences and then proceeding as planned. The actionability figure is a picture of a relation. The person the file is about can act directly on one metric of seven and the company that owns the file can act directly on four. That asymmetry is the relation, and it is worth naming before you propose another one.
- **Prieto-Alvarez, Martinez-Maldonado, and Anderson (2018)**, *Co-designing learning analytics tools with learners*: learners as designers rather than as data sources. Section 7 is the uncomfortable receipt for eleven weeks of not doing this, and section 6 is the closest a dataset gets to letting the learners answer back on their own behalf.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Add the fifth persona this platform has no column for.** Copy an entry in `PERSONAS`, write a guardian of a child in the week 6 or week 10 data, a disability services coordinator, a translator, or a research ethics board, then add the matching `act_` column to `CATALOG` and redraw the actionability figure. The guardian is the instructive case: their column is almost all `3`s where the learner is a minor and almost all `0`s everywhere else, which makes them the one persona whose relevance is a property of the dataset rather than of the role.
2. **Write the refusal list and the interface copy.** Name the metrics you would refuse to show any of the four personas, then write the exact sentence you would put in the interface where each one would have gone. "We do not show this" is a design decision that has to be readable by the person who wanted it, and drafting that sentence is harder and more useful than choosing the metric.
3. **Put forum posts back on the menu, honestly.** `nforum_posts` is deliberately excluded, because it is recorded for only 9,516 of the 21,693 enrolments in the common population and adding it would silently change the population again. Build the five-measure version on its own smaller common population, report how many rows and courses survive, and then say whether the extra measure was worth the extra restriction. That trade is the whole job.
4. **Change the tie-break and watch what moves.** Re-run the overlap matrix with `B=1` and a fixed seed, then with `B=1000`. The pairs involving page views and active days barely move; the pairs involving grade and modules reached move a lot. Write the two sentences you would put under the figure explaining why, and then say what that implies about any leaderboard built on a measure with a ceiling.
5. **Cost out one co-design session.** Take the single artifact where you moved an audit score to 2 or 3 and write the agenda for the 45-minute session that score implies: who is in the room, what artifact you put in front of them, what decision they actually get to make, and what you do if they say no. Then specify what would have changed on the screen. A veto nobody can exercise is a 1 in disguise.
6. **Ask the question the survey did not.** The intake survey asked what kind of participant someone expected to be and why they registered. Write the one extra question that would have made a learner-facing dashboard possible, then work out what the platform would have had to log to answer it, and what that logging would have cost the person. Most proposals in this field skip both halves of that sentence.

## Troubleshooting

**"Could not download the data file."** The first cell prints this instead of a traceback, along with the URL it tried and the three likely causes: no internet in the runtime, a firewall between you and github.com, or the course dataset repository `github.com/HakeoungLee/edis8100-datasets` having moved. Try `Runtime > Restart and run all` first. If it still fails, send the instructor the error line the cell prints.

**"NameError: name 'core' is not defined", or `pc`, or `CATALOG`.** Those are built in the setup and section 3 cells and everything downstream needs them. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"AssertionError: MY_PERSONA must be one of ['teacher', 'learner', 'platform', 'funder']"**, or an assertion about metrics or the focus enrolment. Those checks are deliberate: they tell you about a typo immediately rather than letting it fail strangely three cells later. Read the message and fix the quoted string. Metric keys are printed just above.

**"That course/user pair is not in the common population."** Only 21,693 of the 325,199 rows have all four measures recorded, so most `course_id_DI` and `userid_DI` pairs in the file are not selectable here. Keep the default, or pick a pair by running `core[['course_id_DI', 'userid_DI']].head(20)`.

**"Pick between 1 and 4 metrics."** That is the design constraint, not a bug. Four is the ceiling on purpose.

**A cell is taking ten seconds.** Expected, three times. The chance baseline simulates 2,000 random pairs of lists, each overlap matrix rebuilds the four top-500 lists 200 times with different random tie-breaks, and the grade-by-plan figure resamples 145 courses 400 times. Each of those is buying you an interval instead of a single number, which is the difference between a finding and an anecdote. The whole notebook runs in well under a minute.

**My numbers are slightly different from the ones in this README.** If you changed a **Your turn** cell, expected and good. If you did not, check the third digit: every resampling step is seeded, so a clean run reproduces the same numbers every time. If a whole column has changed, restart and run all.

**My audit numbers are different from the ones in the printout.** They should be. The dictionary in section 7 is the instructor's first guess and you were asked to argue with it. Bring one moved cell and your reason to the discussion.

**I cannot tell the shades of the heatmaps apart.** Do not try. Every cell prints its value as text on top of the colour, and both heatmaps have the same numbers printed as a plain table in the cell above or below. Read the numbers and the column totals, which is where the finding lives anyway.

**I have no idea which metrics to choose.** Start from your persona's question, not from the menu. If you are stuck, the appendix at the end of the notebook has a defensible set for each of the four personas with the reasoning attached. Read it after you have made an attempt, not before.

**Colab says it cannot find the notebook.** You are signed into a different Google account. Check the profile picture in the top right corner.

## A reminder about documenting AI use

This notebook is not a graded submission, but something substantial is due this week: the **Course Research Project Rough Draft**, uploaded to Canvas separately from anything here.

If you used an AI assistant while drafting, or while working through this notebook, the course AI policy requires two things, and they go in two different places in the **AI Reflection** submission on Canvas:

- **The conversation record goes in an attached Word file.** Copy the actual exchanges into a `.docx` and attach it. The tool, the prompts, and the responses you got, as a record rather than a summary.
- **The four reflection questions from the syllabus are answered in the Canvas text box**, directly, not inside the attachment. Copy them in and answer each one: how you used it; whether it helped and how; whether it made your work more challenging in any way; and what lesson about AI from this week you would pass on to a friend or the class.

If you used no AI at all, one line in the text box saying so is a complete and acceptable submission.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use costs you nothing. In a week spent arguing about who deserves a say in a system that measures them, disclosure is the same courtesy, pointed at yourself.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
