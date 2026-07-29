# 📊 Week 4: Mini Project 1, Teacher Dashboards

Build a teacher-facing dashboard with plotly, then take it apart.

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
| **Data used** | `students.csv`, `lms_clickstream.csv`, `gradebook.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib, plotly, scikit-learn |

## Objectives

By the end of this activity you will be able to:

1. **Build** a three-panel teacher-facing dashboard in plotly from LMS, gradebook, and roster data, with a static snapshot of each panel for readers who cannot run the code.
2. **Attach a reason to every automated flag**, decomposing a model's risk score into the per-feature contributions that produced it.
3. **Evaluate** each panel against the decision a teacher would actually make from it, using van Leeuwen, Teasley, and Wise (2022) and Wise and Jung (2019).
4. **Argue in writing**, in a 300-word design memo, for one specific design change and say who it protects.

The through-line of the session: a dashboard is not a report, it is an intervention in somebody's Monday morning. The design question is not "is this accurate" but "what will a teacher do because of this, and who pays if they are wrong."

## What is different about this week

Weeks 2 and 3 were about finding things. This week is about designing while already knowing them.

You come in holding two findings. From week 2: activity volume relates only weakly to achievement (r near 0.33), and a visible group of students posts low click counts alongside high scores. From week 3: an at-risk model built on activity features over-flagged first generation students who work long hours and study in bursts, and swapping the feature set closed most of that gap.

Neither is a discovery to be re-made this week. Both are constraints your dashboard has to survive.

## What is in this folder

| File | What it is |
|---|---|
| `week04_miniproject1_teacher_dashboard.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the three datasets into the runtime.

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

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, plotly, and scikit-learn, all of which ship with Anaconda.

### A note about the two kinds of chart

Every panel is drawn twice: once with plotly, which is interactive, and once with matplotlib, which is not.

That is deliberate. Plotly charts do not render when a notebook is read on GitHub, because GitHub does not run javascript. If your reader never opens Colab, the plotly panels are blank rectangles to them. The static snapshots are what they actually see. Building both is a habit worth keeping past this course.

## Step-by-step walkthrough

Budget about 20 minutes for the in-class launch (through Part C) and about three hours to finish, which is what the per-section budgets below add up to. The four ✏️ **Your turn** cells already contain working answers, so the notebook runs start to finish without you typing anything. They are numbered in the order you are asked to think about them rather than the order they appear, so Your turn 4 sits in Part D and Your turn 3 in Part E.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long and meant to be collapsed and ignored. It builds the synthetic roster, clickstream, and gradebook inside your runtime so nothing has to be downloaded and no real student is ever involved.

**📊 Part A: orientation (10 minutes).** Load the files, collapse the clickstream to one row per student, and read the calendar boundaries. Two things to notice: `at_risk` is a line somebody drew at 70, and the clickstream export ends two days before quiz 8 and nine days before the final project. Then ✏️ **Your turn 1**: write one question these files can inform and one they cannot touch. Keep the second one in front of you all week.

**📊 Part B: the class overview panel (25 minutes).** Four charts: the score distribution, the daily activity rhythm with quiz deadlines marked, the activity against achievement scatterplot from week 2, and the same data aggregated into thirds. Panels 3 and 4 use identical numbers. One is a cloud, the other is three clean descending bars. Sit with what aggregation did to your confidence.

**📊 Part C: the early warning panel (35 minutes).** The audited week 3 model goes on screen, with a model card printed above it: features, accuracy, and the false positive rate gap next to the retired model's gap. Then the part most real systems skip: each flagged student's risk score is decomposed into what each feature contributed, so the panel can say why a name is on the list. Read the tally of leading reasons carefully. Then ✏️ **Your turn 2**: change the caseload and watch a staffing budget move a fairness metric.

**📊 Part D: the individual drilldown (25 minutes).** One student, four views: quiz trajectory against the class middle half, a profile card that lists what the model saw and what it did not, weekly LMS activity, and submission lead time. The default student is `S008`, first generation, 22 paid hours a week, two weeks with no LMS events at all, and rising quiz scores. She is flagged. Change the student and run it again on somebody you choose.

**💬 Part E: take it apart (30 minutes).** A cell computes five things the dashboard never shows the teacher: how many struggling students the flag list misses, how much the list changes when only the random seed changes, what the reason column really says, what acting on the activity panel would cost, and the calendar problem again. Then ✏️ **Your turn 3**, the critique table, which is the analytic core of the assignment.

**✏️ Part F: the design memo (30 minutes).** 300 words, in the marked markdown cell. Argue for one specific change and defend it against the strongest objection you can think of.

**✏️ Stretch (optional).** A working student-facing rewrite of the drilldown, and an invitation to make it better.

**💬 Reflection and ✅ submission checklist.** Bring the reflection answers to the 5:00 discussion block with Yeonji Jung.

## What this connects to in the readings

- **van Leeuwen, Teasley, and Wise (2022)**, *Teacher and student-facing learning analytics*: the two are different instruments, not one tool with two logins. Part E and the stretch goal are built on this distinction.
- **Wise and Jung (2019)**, *Teaching with analytics: Towards a situated model of instructional decision-making*: what an instructor does with a display depends more on their pedagogical situation than on the numbers. This is the standard the memo is graded against.
- **Jung and Wise (2025)**, *How students engage with learning analytics*: access, action-taking, and the routines that form around received information. Directly relevant to the stretch goal.
- **Li, Jung, and Wise (2025)**, *How instructors use learning analytics: the pivotal role of pedagogy*: listed as additional reading, and the source of reflection question 4.

## Rubric: Mini Project 1 (100 points)

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Every part is completed and connected: the orientation questions shape the panels, and the panels feed the critique and the memo as one argument. | All parts completed and run cleanly, with the connections between them mostly explicit. | Most parts completed; the sections read as separate exercises rather than one workflow. | Parts missing or unrun; the notebook does not execute end to end. |
| **Data Preparation and Technical Care** | Notebook runs top to bottom without error; the per-student table is correct; the calendar and threshold limits are noticed and stated. | Runs cleanly with correct aggregation; limits mentioned but not pursued. | Runs with minor errors or unexamined aggregation choices. | Does not run, or the data preparation is incorrect. |
| **Analysis and Visualization Choices** | Every figure is titled and labeled, colorblind-safe, and each design choice (aggregation, band versus rank, what is omitted) is defended. Static snapshots present and readable. | Figures are clear, titled, and labeled; snapshots present; choices mostly defended. | Figures readable but some are unlabeled, undefended, or missing snapshots. | Figures missing, mislabeled, or uninterpretable. |
| **Interpretation and Educational Meaning** | The critique table names a specific teacher action for each panel and a specific way each could mislead, with evidence from your own outputs. | Actions and risks named for all three panels with some evidence. | Generic actions ("monitor the student") or risks asserted without evidence. | Interpretation absent or unconnected to the outputs. |
| **Critical Reflection: Limits, Ethics, Equity** | The memo names a decision, cites at least two numbers from the notebook, proposes one concrete change, and states who is protected, what it costs, and the strongest objection. Draws on both required readings. | Memo makes a clear argument with evidence and cites at least one reading. | Memo describes the dashboard rather than arguing for a change, or omits the trade-off. | Memo missing, far off length, or unsupported by evidence. |

The AI interaction log and reflection are required for the submission to be considered complete.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **The student-facing redesign (the one in the notebook).** Take the working example and go further: attach one available action to each point on the chart, and argue that a student-facing display without an available action is a report card that arrived early.
2. **Show the uncertainty.** Replace the risk score bar with an interval built from the spread across cross validation splits, and sort the list into "consistently flagged" and "borderline" instead of ranking one to fifteen. Then say what a hurried teacher does with the borderline group, and whether that is better or worse than what they do now.
3. **Build a feature a teacher can act on.** Every leading reason in the panel points at prior GPA, which no teaching move can change. Engineer a feature from this term only, for example the change in quiz score between the first half and the second half, add it to the model, and see whether the reason column starts saying something a teacher could do anything about.
4. **The missing 21.** Twenty-one students below the cutoff never appear on the flag list. Characterise them. What do they have in common, and what panel would have surfaced them?
5. **Design the refusal.** Write down three things this dashboard should refuse to display even though the data supports them, and defend each refusal to a hypothetical dean who wants them added.
6. **Make it real.** Rebuild one panel for a course you have actually taught or taken. What data would you need, who owns it, and who would have to consent?

## Troubleshooting

**"NameError: name 'dash' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/students.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up, run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only there so the notebook works with no downloads and no accounts.

**A plotly chart is blank, or nothing appears where a chart should be.** In Colab this is almost always a stale runtime: `Runtime > Restart and run all`. If you are reading the notebook on GitHub rather than in Colab, plotly charts will never appear, by design. Look at the matplotlib snapshot immediately below each one.

**My matplotlib charts do not appear.** Make sure you ran the first code cell of Part A, which contains `%matplotlib inline`.

**"KeyError: 'S0...'" in Part D.** You typed a student ID that is not on the roster. The cell catches this and falls back to `S008`, but check your spelling: IDs run `S001` to `S120`, always three digits.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all: the data is seeded, so a clean run reproduces the same numbers every time.

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

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
