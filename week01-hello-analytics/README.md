# 👋 Week 1: Hello, Learning Analytics

The first hands-on session of EDIS 8100. You will open Google Colab, run a notebook end to
end, read two real data tables, make three figures, and leave with one question that the
data cannot answer.

If you have never written a line of code, this notebook was designed for you. Nothing in
the core path asks you to write code from scratch. You run cells, you read what comes out,
and you change one or two clearly marked values to watch a chart respond.

## At a glance

| | |
|---|---|
| **Session** | Week 1, Wednesday, August 26, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Course Introduction and Planning |
| **Hands-on block** | 5:00 to 5:40 PM (40 minutes), about 30 minutes of core work |
| **Notebook** | `week01_hello_learning_analytics.ipynb` |
| **Data** | `students.csv`, `gradebook.csv` (built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib |
| **Deliverable** | None. This is in-class work only, nothing goes to Canvas |
| **Due** | Nothing due. Discussion leader sign-ups happen in class today |
| **Prior coding experience needed** | None |

Mini projects start in Week 4. This week is for getting the tools working and getting your
bearings.

## 🎯 Objectives

By the end of the session you will be able to:

1. **Run a notebook.** Execute cells in order in Colab and tell whether a cell is waiting,
   running, or finished.
2. **Read a DataFrame.** Load a CSV into pandas and say in one sentence what a single row
   represents.
3. **Make a plot.** Produce a bar chart and a histogram with a title and labeled axes, then
   change one value and watch the figure change.
4. **Form a question the data cannot answer.** Look at a grade distribution and name
   something important that it hides.

Objective 4 is the one that matters most, and it is not a coding objective.

## 📁 What is in this folder

| File | What it is |
|---|---|
| `week01_hello_learning_analytics.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |
| `data/` | Created when you run the setup cell. Not stored in the repo. |

The notebook contains its own data generator, so it builds `students.csv` and
`gradebook.csv` inside your session. There is nothing to download, nothing to upload, and
no way to end up with the wrong version of a file.

## 🚀 Open it in Colab

This repository is **private**, so the one-click badge only works after you have accepted the
instructor's invitation and authorized Colab to see private repositories. Do the manual route
once, and the badge works forever after.

### First time (do this once)

1. **Accept the repository invitation first.** Hand the instructor your GitHub username in class,
   then click **Accept invitation** in the email GitHub sends you. Until you accept, this
   repository is invisible to you and Colab reports that it does not exist.
2. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the
   Google account you will use for this course.
3. Choose **File > Open notebook**.
4. Click the **GitHub** tab.
5. Click **Authorize with GitHub**. In the GitHub permission screen, make sure the box for
   **"Include private repositories"** is checked, then approve.
6. In the repository dropdown, pick `HakeoungLee/edis8100-teaching-learning-analytics`.
   Leave the branch on `main`.
7. In the file list, click `week01-hello-analytics/week01_hello_learning_analytics.ipynb`.

The notebook opens. Run the first code cell and you are underway.

### Every time after that

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week01-hello-analytics/week01_hello_learning_analytics.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week01-hello-analytics/week01_hello_learning_analytics.ipynb`

If that link shows a "404" or "could not find" message, check three things in this order: the
repository invitation is still unaccepted in your email, the private repositories box in step 5
was not checked, or you are signed into a different Google account. Redo the first-time steps.

### To keep your own edits

Colab discards the session when you close the tab. Use **File > Save a copy in Drive** to
keep a personal version, or **File > Download > Download .ipynb** for a local copy. Nothing
is lost if you forget: the data generator is seeded, so re-running the notebook from the top
rebuilds identical files every time.

## 🧭 Step-by-step walkthrough

Roughly 30 minutes of core work. Timings are a guide, not a race.

| Step | Section | Minutes | What you do |
|---|---|---|---|
| 1 | Banner and "how this notebook works" | 3 | Read the six orientation lines. Learn Shift + Enter. |
| 2 | ⚙️ Setup | 2 | Run the long setup cell. It writes `data/students.csv` and `data/gradebook.csv`. Collapse it and move on. |
| 3 | ⚙️ Libraries | 1 | Run the import cell. Confirm pandas, numpy, and matplotlib all print a version. |
| 4 | 📊 Meet the data | 6 | Load both CSVs. Answer the key question out loud: what is one row of each file? They are different, and that difference is the point. |
| 5 | 📊 First chart | 5 | A bar chart of who is in the course by major area. Discuss the interpretation prompts with a partner. |
| 6 | ✏️ Your turn 1 | 2 | Change `GROUP_COLUMN` to `'gender'`, then `'first_gen'`. Re-run. |
| 7 | 📊 Second chart | 6 | A histogram of all 960 quiz scores with the mean and median marked. Find the ceiling effect at the right edge. |
| 8 | ✏️ Your turn 2 | 2 | Change `MY_ASSESSMENT` to a different quiz, and `BIN_WIDTH` to 2 or 10. Notice that the "true" picture depends on a choice you made. |
| 9 | 📊 What one number hides | 5 | Two students with identical averages and very different eight weeks. |
| 10 | 💬 Reflection | 5 | Write your one question the data cannot answer. Keep it. |
| 11 | ✅ Before you leave | 1 | Run the checklist. Sign up for discussion leadership. |

### The three figures you will make

1. **A bar chart of the roster by major area.** We plot the people before we plot the
   scores. A distribution is always a distribution of somebody.
2. **A histogram of every quiz score in the course.** The class average is 75.7. The
   histogram shows what that number is sitting on top of: a range from 33.8 to 100, a thin
   tail of scores below the 60-point line this course chose, and 46 scores stacked at exactly
   100 because the quiz cannot measure any higher.
3. **A line chart of two students with the same average.** Both average 83.3. One is nearly
   flat, one swings across 30 points. Every gradebook export and every dashboard would put
   them in the same bucket. The notebook also subtracts each quiz's class average, so you can
   see how much of a wobbly line belongs to the quizzes rather than to the student. For the
   flat student most of it does.

### The closing question

Section 6 asks you to write **one question these data cannot answer**. Not a question you
ran out of time for: a question that no additional cleverness with `students.csv` and
`gradebook.csv` would resolve. Bring it to Week 2, when the invented course is replaced by a
real institutional export and we find out whether more data, and messier data, actually
helps.

Some of these questions become course research projects. Keep yours.

## 📈 Stretch goals

For students who finish early or arrive with coding experience. None of these are required
and none are graded.

1. **Averages hide group sizes.** Compute the mean quiz score by `major_area` with
   `groupby`. Then print the group counts next to it. Engineering has 9 students. Write one
   sentence about how much you would trust a bar chart of those means.
2. **The whole gradebook at once.** Build a bar chart of the mean score for each of the nine
   assessments. The class average barely moves across eight quizzes, but the standard
   deviation climbs from 11.1 on quiz 1 to 14.7 on quiz 8. What could make a class spread
   out over a term without its average moving?
3. **Find your own matched pair.** Section 5 hands you two students with identical averages.
   Write code that finds the pair with the closest averages and the most different standard
   deviations, instead of taking the instructor's word for it.
4. **Boxplot, or violin.** Redraw the score distribution as a boxplot by assessment. What
   does the boxplot show better than the histogram, and what does it hide that the histogram
   showed?
5. **Question the ceiling.** 46 quiz scores are exactly 100.0. Count how many distinct
   students produced them. Then argue, in two sentences, whether the ceiling is a property
   of the students or of the instrument.
6. **Move the line.** The notebook counts scores below 60 because that is the line this
   invented course wrote into its syllabus. Recount at 50 and at 65. Write one sentence about
   what a headline count of people is really counting.

Bring anything interesting to Week 2. Stretch work is a good source of discussion material.

## 🔧 Troubleshooting

**"NameError: name 'pd' is not defined"**
You ran a cell out of order, or the runtime restarted. Fix: **Runtime > Restart session and
run all**, then wait for every cell to finish. This is the answer to most notebook problems
and it costs about ten seconds.

**"FileNotFoundError: data/students.csv"**
The setup cell has not run in this session. Scroll to Section 1 and run it. If Colab
disconnected while you were reading, everything in `data/` is gone and needs rebuilding.
Restart and run all.

**"KeyError: 'gendr'"**
A typo in a column name. The valid names are printed in the output of the Your turn cells.
Python is exact about spelling and does not guess.

**The cell shows `[*]` and nothing happens**
It is still running. The setup cell takes a second or two, everything else is instant. If
`[*]` persists for more than a minute, the runtime probably disconnected: **Runtime >
Restart session and run all**.

**Colab says "Cannot find notebook" or shows a 404**
You are signed into a different Google account, or the private repository authorization did
not complete. Redo the first-time steps above, and make sure "Include private repositories"
is checked.

**I lost my edits**
Colab discards untitled sessions. **File > Save a copy in Drive** at the start of any session
where you plan to keep something.

**Red text appeared and I panicked**
Python errors are wordy but they are not damage. Nothing here can harm your computer, the
course data, or your grade. Read the **last line** of the error first, it usually names the
real problem. Then raise your hand.

## 🤖 A note on AI use

The course permits AI use in designated activities and requires that you document it.
Undisclosed AI use is an Honor Code violation.

There is **nothing to submit this week**, so there is nothing to document. But the habit
starts now. Beginning with Mini Project 1 in Week 4, every mini project submission to Canvas
includes three pieces:

1. the completed notebook,
2. your **AI interaction log** (the prompts you sent and the responses you got), and
3. a short **reflection** on where the assistant helped, where it misled you, and what you
   checked yourself.

If you use an assistant to make sense of anything in this notebook today, save the
transcript. Learning to read what an AI tells you about data, with appropriate suspicion, is
itself a course skill.

## 📚 Connections to this week's readings

The reflection section of the notebook ties directly to the required readings:

- **Lang, Wise, Merceron, Gašević, and Siemens (2022)**, "What is learning analytics?" Their
  definition includes learners *and their contexts*. Ask which of today's three figures came
  closest to showing context.
- **Wise (2019)**, on data-informed decision making. Look at the two-student figure and name
  one decision you would make from it, and one you would refuse to make from it.
- **Siemens (2013)**, on learning analytics as an emerging discipline. After thirty minutes
  of it, what do you think the discipline is supposed to be about?

## Data and ethics

Every row you touch this semester is synthetic, generated with numpy seed 8100. EDUC 1010,
Blue Ridge University, and all 120 students are invented. That is deliberate: it lets us
rehearse the judgment calls of learning analytics without surveilling a single real person.

The ask in return is that you treat the data as if it were real. Ask who could be harmed by
a claim before you make it. Notice when a metric flattens a person. That stance is not a
warm-up for the course, it is one of the course's arguments.

Full documentation of the data universe, including the data dictionary, is in
[`../data/README.md`](../data/README.md).

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
