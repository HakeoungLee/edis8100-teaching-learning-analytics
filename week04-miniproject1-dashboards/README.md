# 📊 Week 4: Mini Project 1, Teacher Dashboards

Build a teacher-facing dashboard with plotly, on real student records, then take it apart.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 16, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Teacher and Student Facing Learning Analytics and Dashboards |
| **Guest speaker** | Yeonji Jung, Texas A&M University |
| **In-class time on this notebook** | About 20 minutes, launched in the hands-on studio block (4:40 to 5:00). This is a launch, not the whole assignment. Plan about three more focused hours outside class, as the Mini Project 1 Brief sets out. |
| **Deliverable** | **Mini Project 1**: the completed notebook, a 300-word design memo inside it, and your AI interaction log plus reflection |
| **Due date** | This week, via Canvas. Check Canvas for the exact time. |
| **Notebook** | `week04_miniproject1_teacher_dashboard.ipynb` |
| **Data used** | **Real, not synthetic.** The Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J: 4,529 enrollments, 891,062 rows of daily clickstream, 21,783 assessment submissions. Loaded over the network from `github.com/HakeoungLee/edis8100-datasets`, nothing to download by hand. Licensed **CC BY 4.0**. Cite as Kuzilek, J., Hlosta, M., and Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Libraries** | pandas, numpy, matplotlib, plotly, scikit-learn |

## Objectives

By the end of this activity you will be able to:

1. **Build** a three-panel teacher-facing dashboard in plotly from a real virtual learning environment export, with a static matplotlib snapshot of each panel for readers who cannot run the code.
2. **State the provenance of your data**: who collected it, under what licence, and what it can be used for.
3. **Attach a reason to every automated flag**, decomposing a model's risk score into the per-feature contributions that produced it, and disaggregate the resulting list by socioeconomic band.
4. **Evaluate** each panel against the decision a teacher would actually make from it, using van Leeuwen, Teasley, and Wise (2022) and Wise and Jung (2019).
5. **Argue in writing**, in a 300-word design memo, for one specific design change and say who it protects.

The through-line of the session: a dashboard is not a report, it is an intervention in somebody's Monday morning. The design question is not "is this accurate" but "what will a teacher do because of this, and who pays if they are wrong."

## What is different about this week

Two things change, and they change together.

**The data is real.** Weeks 1 through 3 ran on an invented roster, on purpose, so that you could practise without touching anyone. This week runs on records from a distance-teaching university in the United Kingdom: 2,237 people who registered for one module in October 2013, and 2,292 more who registered for the same module a year later. They were anonymized and released by the Open University's Knowledge Media Institute so that the field could check its own work on data more than one lab can see. They were not asked about a doctoral seminar in Virginia. What they were given is anonymity and banded categories, and what we owe them in return is that we do not pretend a row is a person, and we do not say anything about them we could not defend to them. A dashboard is a claim about people, and this week the people are real.

**Real data does not arrange itself into a lesson.** Part A prints a decision log of six places the export was ragged: a column that spells its own categories two ways, 29 enrollments with no deprivation band, 738 enrollments with no recorded click at all, 1,062 with no first assignment, negative day numbers from students who read ahead, and 576 people who unregistered before day 1 and stayed in the roster anyway. Every one of those is a decision somebody has to make in public, and the notebook makes them in front of you and then says what each one cost. The last one, the roster, is the one that decides what the dashboard does on Monday.

You also come in holding a finding from week 3: an at-risk model built on activity features falls unevenly, and swapping the feature set closes most of the gap. This week that finding survives contact with real data in a form week 3 could not produce. The false positive rate gap does close, and the flag list still draws 48.7 percent of its names from the 37.2 percent of the class living in the most deprived third of areas. Both are true at once. Part C makes you look at both, and the memo makes you say what a module team should do about it.

## What is in this folder

| File | What it is |
|---|---|
| `week04_miniproject1_teacher_dashboard.ipynb` | The notebook. It downloads its data in the first code cell and writes nothing to disk. |
| `README.md` | This file. |

There is no `data/` folder this week and nothing to clone. The first code cell reads six CSV files straight from the course dataset repository, `github.com/HakeoungLee/edis8100-datasets`, and prints what arrived. No account, no authorization, no install. It takes a second or two.

That repository is public and read-only. If it is unreachable, the cell prints a plain-English message naming the repository and telling you what to try, rather than a wall of red traceback.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week04-miniproject1-dashboards/week04_miniproject1_teacher_dashboard.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week04-miniproject1-dashboards/week04_miniproject1_teacher_dashboard.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week04-miniproject1-dashboards/week04_miniproject1_teacher_dashboard.ipynb`

**This week, saving your copy is not optional.** Mini Project 1 is graded from your notebook, so before you change anything choose **File > Save a copy in Drive**. Work in that copy. When you are finished, **File > Download > Download .ipynb** and upload that file to Canvas.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, plotly, and scikit-learn, all of which ship with Anaconda, plus a working internet connection for the first cell.

### A note about the two kinds of chart

Every panel is drawn twice: once with plotly, which is interactive, and once with matplotlib, which is not.

That is deliberate. Plotly charts do not render when a notebook is read on GitHub, because GitHub does not run javascript. If your reader never opens Colab, the plotly panels are blank rectangles to them. The static snapshots are what they actually see. Building both is a habit worth keeping past this course.

## Step-by-step walkthrough

Budget about 20 minutes for the in-class launch (through Part C) and about three hours to finish, which is what the per-section budgets below add up to. The four ✏️ **Your turn** cells appear in reading order and already contain working answers, so the notebook runs start to finish without you typing anything.

**⚙️ Setup (2 minutes).** Read the provenance cell before you run anything: who collected this data, under what licence, and what we owe the people in it. Then run the first code cell. It fetches six files and prints a line per file saying how many rows arrived and what one row means.

**📊 Part A: orientation (20 minutes).** Build the one table every panel needs, one row per enrollment, and watch the decision log print as it goes. Six ragged places in the export, six decisions made in public, and a stated cost for each. Three of them come back in Part E, and the one to hold on to is the roster: 576 enrollments unregistered on or before day 0 and are still sitting in the enrollment table. Then ✏️ **Your turn 1**: write one question these files can inform and one they cannot touch. Keep the second one in front of you all week.

**📊 Part B: the class overview panel (25 minutes).** Four charts, each drawn once per presentation, because BBB ran twice and the archive can answer a question a teacher in the middle of a term never can: is this a property of my course, or of this particular group of people? How each run ended, when the module was worked, completion by fifth of first-30-day clicks, and completion by deprivation decile. Chart 3 replicates almost exactly across the two years. So does chart 4, and chart 4 is a different kind of finding: in 2013J the most deprived decile completes at 34.2 percent and the least deprived at 61.3.

**📊 Part C: the early warning panel (35 minutes).** The audited week 3 model goes on screen, with a model card printed above it: features, the flag rule, the base rate, and the false positive rate gap next to the retired activity-only model's gap. Every risk score is out of sample. Then the part most real systems skip: each flagged student's risk score is decomposed into what each feature contributed, so the panel can say why a name is on the list. Read the three tallies underneath the chart carefully. They are the ones the memo argues from: 402 students the model cannot tell apart, 132 of the 150 flag slots going to that block, and 100 of the 150 names belonging to people who had already unregistered before the module opened. Then ✏️ **Your turn 2**: change the caseload and the roster rule, and watch a staffing budget move a fairness metric.

**📊 Part D: the individual drilldown (25 minutes).** One student, four views: tutor-marked assignment trajectory against the class middle half, a profile card that lists what the model saw and what it never did, weekly clicks against the class mean, and submission lead time. The default is student `154570`, who clicked more in the first 30 days than anyone else in the presentation, received the second lowest risk score of all 2,237, and unregistered on day 117. The panel never mentioned this student and never could have. Then ✏️ **Your turn 3**: the cell prints six students worth drilling into and why each one breaks the panel in a different direction. Pick one that is not the default.

**💬 Part E: take it apart (30 minutes).** A cell computes five things the dashboard never shows the teacher: how few of the struggling students the list reaches, how many flag slots go to people who had already left, how much the list changes when only the random seed changes, why the deprivation skew survives a closed fairness gap, and what a 30-day window cannot see. Then ✏️ **Your turn 4**, the critique table, which is the analytic core of the assignment.

**✏️ Part F: the design memo (30 minutes).** 300 words, in the marked markdown cell. Argue for one specific change and defend it against the strongest objection you can think of. One requirement is not optional: say what the module team should do about the deprivation skew, and "fix the model" is not available as an answer.

**✏️ Stretch (optional).** A working student-facing rewrite of the drilldown, and an invitation to make it better.

**💬 Reflection and ✅ submission checklist.** Bring the reflection answers to the 5:00 discussion block with Yeonji Jung.

## What this connects to in the readings

- **van Leeuwen, Teasley, and Wise (2022)**, *Teacher and student-facing learning analytics*: the two are different instruments, not one tool with two logins. Part E and the stretch goal are built on this distinction.
- **Wise and Jung (2019)**, *Teaching with analytics: Towards a situated model of instructional decision-making*: what an instructor does with a display depends more on their pedagogical situation than on the numbers. This is the standard the memo is graded against.
- **Jung and Wise (2025)**, *How students engage with learning analytics*: access, action-taking, and the routines that form around received information. Directly relevant to the stretch goal.
- **Li, Jung, and Wise (2025)**, *How instructors use learning analytics: the pivotal role of pedagogy*: listed as additional reading, and the source of reflection question 4.
- **Kuzilek, Hlosta, and Zdrahal (2017)**, *Open University Learning Analytics dataset*: the data paper for the records you are working on. Reflection question 5 is about it. Worth ten minutes even if you read nothing else about the dataset.

## Rubric: Mini Project 1 (100 points)

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Every part is completed and connected: the orientation questions shape the panels, and the panels feed the critique and the memo as one argument. | All parts completed and run cleanly, with the connections between them mostly explicit. | Most parts completed; the sections read as separate exercises rather than one workflow. | Parts missing or unrun; the notebook does not execute end to end. |
| **Data Preparation and Technical Care** | Notebook runs top to bottom without error; the per-enrollment table is correct; the decision log is understood, and the cost of at least one of those decisions is carried into the critique. | Runs cleanly with correct aggregation; the ragged places in the export are mentioned but not pursued. | Runs with minor errors, or the aggregation and missingness choices are accepted without examination. | Does not run, or the data preparation is incorrect. |
| **Analysis and Visualization Choices** | Every figure is titled and labeled, colorblind-safe, and each design choice (aggregation, band versus rank, what is omitted) is defended. Static snapshots present and readable. | Figures are clear, titled, and labeled; snapshots present; choices mostly defended. | Figures readable but some are unlabeled, undefended, or missing snapshots. | Figures missing, mislabeled, or uninterpretable. |
| **Interpretation and Educational Meaning** | The critique table names a specific teacher action for each panel and a specific way each could mislead, with evidence from your own outputs. | Actions and risks named for all three panels with some evidence. | Generic actions ("monitor the student") or risks asserted without evidence. | Interpretation absent or unconnected to the outputs. |
| **Critical Reflection: Limits, Ethics, Equity** | The memo names a decision, cites at least two numbers from the notebook, proposes one concrete change, states who is protected, what it costs, and the strongest objection, and says what should be done about the deprivation skew without proposing a model fix. Draws on both required readings. | Memo makes a clear argument with evidence and cites at least one reading. | Memo describes the dashboard rather than arguing for a change, or omits the trade-off. | Memo missing, far off length, or unsupported by evidence. |

The AI interaction log and reflection are required for the submission to be considered complete.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **The student-facing redesign (the one in the notebook).** Take the working example and go further: attach one available action to each point on the chart, and argue that a student-facing display without an available action is a report card that arrived early.
2. **Show the uncertainty.** Replace the risk score bar with an interval built from the spread across cross validation splits, and sort the list into "consistently flagged" and "borderline" instead of ranking one to fifteen. Part E already shows why this matters: across five random splits, only 6 students appear on all five lists and 410 distinct students compete for 150 slots. Then say what a hurried teacher does with the borderline group, and whether that is better or worse than what they do now.
3. **Move the window.** The model sees days 0 to 29 and assignment 1, and then never looks again. 134 students withdrew after day 100 and the panel had flagged 3 of them. Build a second model that also sees days 30 to 59 and the second tutor-marked assignment, score the same class, and report what it gains, what it costs in lateness, and whether the reason column starts saying something different.
4. **The 1,019 who never appear.** The list reaches 12.5 percent of the students who go on to fail or withdraw. Characterise the rest. What do the missed students have in common, and what panel would have surfaced them?
5. **Rebuild the panel for 2014J.** Change `FOCAL_TERM` and run everything again. Which findings hold and which were properties of one cohort? This is the replication question the two presentations exist to let you ask.
6. **Design the refusal.** Write down three things this dashboard should refuse to display even though the data supports them, and defend each refusal to a hypothetical dean who wants them added.
7. **Make it real.** Rebuild one panel for a course you have actually taught or taken. What data would you need, who owns it, and who would have to consent?

## Troubleshooting

**"NameError: name 'dash' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**The first cell says the download did not work.** It will tell you so in plain English rather than a traceback, and it names the repository it was trying to reach. Check that the runtime has internet (Colab always does; a locked-down campus network sometimes does not), then run the cell again, since short network hiccups are common. If it still fails, download the six CSV files from `github.com/HakeoungLee/edis8100-datasets` by hand, put them beside the notebook, and change `BASE` to `"."` so pandas reads them from disk.

**The first cell is slow.** It is fetching about 4 MB, most of it the compressed clickstream. On a normal connection it takes a couple of seconds. It runs once; later cells reuse what is already in memory.

**A plotly chart is blank, or nothing appears where a chart should be.** In Colab this is almost always a stale runtime: `Runtime > Restart and run all`. If you are reading the notebook on GitHub rather than in Colab, plotly charts will never appear, by design. Look at the matplotlib snapshot immediately below each one.

**My matplotlib charts do not appear.** Make sure you ran the first code cell, which contains `%matplotlib inline`.

**Part D says it cannot find my student.** Student IDs in this dataset are plain numbers, not `S001` style codes, and they are not consecutive: `154570` and `2625315` are both real. The cell catches an id that is not in the presentation, says so, and falls back to `154570`. If you want a valid id to try, take one from the six-student comparison table the cell prints.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all. The dataset is fixed and published, and the model's cross validation is seeded, so a clean run reproduces the same numbers every time.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**I lost my work.** Colab does not save changes back to GitHub. Use `File > Save a copy in Drive` at the start, not at the end.

## A reminder about documenting AI use

Mini Project 1 is the first submission where the course AI policy applies in full.

If you used an AI assistant at any point, to explain a line of code, to check your reading of a chart, to help you name a design flaw, or to draft the memo, everything goes to the Canvas **AI Reflection** submission, in two different places on that page:

- **The conversation record goes in a Word file, attached to that submission.** The full exchanges, across every session and every tool, pasted in. Not a summary and not into the text box.
- **The four reflection questions from the syllabus are answered in the text box** on the same page: how you used it; whether it helped and how; whether it made your work more challenging in any way; and what lesson about AI you would pass on to a friend or the class.

If you used no AI at all, say so in one line in the text box and attach nothing. That is also documentation.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation.

The reflection carries more weight than the log. The question worth answering is not whether you used an assistant, it is what you accepted from it and how you checked. A memo that repeats a plausible sounding critique the assistant produced, without you verifying it against your own printed numbers, is exactly the failure mode this course is about.

## Attribution for the data

If you reuse any figure or number from this notebook outside this course, cite the dataset:

> Kuzilek, J., Hlosta, M., and Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171.

Licensed CC BY 4.0: you may use, share, and adapt it, including commercially, as long as you credit the source. Attribution is not a formality here. It is the condition on which a research team made records about real students available to people like you.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
