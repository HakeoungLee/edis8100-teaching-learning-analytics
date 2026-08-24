# Week 1: Hello, Learning Analytics

The first hands-on session of EDIS 8100. You will open Google Colab, run a notebook end to
end on a real published dataset, make two figures, find something the summary numbers were
hiding, and leave with one question the data cannot answer.

If you have never written a line of code, this notebook was designed for you. Nothing in
the core path asks you to write code from scratch. You run cells, you read what comes out,
and you change one clearly marked value to watch two headline numbers move.

## At a glance

| | |
|---|---|
| **Session** | Week 1, Wednesday, August 26, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Course Introduction and Planning |
| **Hands-on block** | 5:00 to 5:40 PM (40 minutes), about 30 minutes of core work |
| **Notebook** | `week01_hello_learning_analytics.ipynb` |
| **Data** | **Real, published, openly licensed.** UCI Student Performance, the mathematics file: 395 students in two Portuguese secondary schools, one flat file, 33 columns, semicolon delimited. CC BY 4.0. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `uci-student-performance` |
| **Citation** | Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance. *Proceedings of the 5th Future Business Technology Conference*, 5-12. |
| **Libraries** | pandas, matplotlib |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data, so this is true in all eleven lab weeks |
| **Deliverable** | None. This is in-class work only, nothing goes to Canvas |
| **Due** | Nothing due. Discussion leader sign-ups happen in class today |
| **Prior coding experience needed** | None |

Mini projects start in Week 4. This week is for getting the tools working and getting your
bearings.

## Objectives

By the end of the session you will be able to:

1. **Run a notebook.** Execute cells in order in Colab and tell whether a cell is waiting,
   running, or finished.
2. **Read a DataFrame.** Load a semicolon-delimited CSV into pandas and say in one sentence
   what a single row represents.
3. **Make a plot.** Produce a bar chart and a histogram with a title and labeled axes.
4. **Find what a summary hid.** Explain why the tallest bar in your first chart was
   misleading, and why a gradient across parental education bands is evidence about
   conditions rather than about people.
5. **Form a question the data cannot answer.**

Objectives 4 and 5 are the ones that matter most, and neither is a coding objective.

## What is in this folder

| File | What it is |
|---|---|
| `week01_hello_learning_analytics.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is nothing to download by hand and nothing to upload. The first code cell fetches one
file over plain HTTPS in about a second and prints how many rows and columns arrived. If the
download fails, the cell prints a plain-English message naming the repository it was trying
to reach rather than a wall of red.

## Open it in Colab

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

**If your invitation has not arrived yet, you are not stuck.** The same notebook file is posted
in the Week 1 Canvas module. Download it from Canvas, then in Colab choose **File > Upload
notebook**. That route uses no GitHub at all and everything below works identically, because the
*dataset* repository is public and needs no authorization of any kind.

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
is lost if you forget: the dataset is a fixed published file, so re-running the notebook from
the top reproduces exactly the same numbers, on any machine, for everyone in the room.

## Step-by-step walkthrough

Roughly 30 minutes of core work. Timings are a guide, not a race.

| Step | Section | Minutes | What you do |
|---|---|---|---|
| 1 | Banner and "how this notebook works" | 3 | Read the orientation lines. Learn Shift + Enter. |
| 2 | Setup | 2 | Run the first code cell. It downloads `student-mat.csv` and prints `Loaded 395 students and 33 columns.` |
| 3 | Where this data came from | 3 | Read the provenance table before any number appears. Note `sep=";"`: a CSV is a convention, not a law. |
| 4 | 1. Meet the table | 5 | `students.head()`. Read one row aloud as a sentence about a person, then name three things the file never recorded. |
| 5 | 2. Your first chart | 7 | Mean final grade by mother's education, then the same chart with group sizes on the bars. Work the interpretation prompt: instrument, setting, circumstances, in that order. |
| 6 | 3. A histogram | 4 | All 395 final grades. Find the spike at exactly 0 and the empty space at 1, 2, and 3. |
| 7 | 4. What the summary was hiding | 4 | Look at the 38 zeros and at their absence records. |
| 8 | Your turn | 2 | Flip `TREAT_ZEROS_AS_MISSING` and watch the mean and the pass rate move. |
| 9 | 5. The gap that shrinks | 3 | The same recording decision, applied to a group comparison. |
| 10 | 6. Reflection | 5 | Four prompts. Write in the cell. Bring them to the 5:00 block. |
| 11 | 7. Before you leave | 1 | Run the checklist. Sign up for three discussion leadership weeks. |

### The two figures you will make

1. **Mean final grade by mother's education, twice.** The first version climbs neatly across
   bands 1 to 4 and then has its tallest bar at band 0. The second version puts the group
   sizes on the bars, and band 0 turns out to be three students with grades of 9, 15 and 15.
   The first rule of the course arrives in the first ten minutes: put the n next to the mean.
   The second half of that section is the harder one, and it is the one the whole semester
   repeats: bands 1 to 4 really do climb, from 8.68 to 11.76 on 59, 103, 99 and 131 students,
   and before you write a sentence about that you name what the instrument could not see,
   what the setting produces, and what the file does not record about these households.
   A gradient across parental education bands is evidence about the conditions under which
   people study and about a school that produces different outcomes for different
   circumstances. It is not evidence about the people.
2. **A histogram of all 395 final grades.** Roughly a bell centred near 11, a tall spike at
   exactly 0, and nothing at all at 1, 2 or 3. Grades do not usually fall off a cliff, and
   the next section finds out why.

### The finding you are meant to reach on your own

All 38 students with a final grade of exactly 0 have zero recorded absences, and not one of
the 280 students with any recorded absence scored 0. That looks like third-period records
that were never entered and stored as zeros rather than like 38 people failing. Treating
those 38 as missing moves the mean from 10.42 to 11.52 and the pass rate from 67.1 percent
to 74.2 percent. Both numbers are defensible. What is not defensible is reporting either one
without saying which choice you made.

Then the same decision is pointed at a group comparison, with the intervals attached
because a difference between two means cannot be read without one. The recorded gap between
the two sex groups' mean grades is 0.95 of a point, 95 percent interval 0.05 to 1.85, on all
395 students. Take the 38 non-records out, which fall 23 to 15 across the two groups rather
than evenly, and what is left is 0.66 of a point with an interval of **-0.01 to 1.33**. That
interval contains zero, so the recording artifact did not merely shrink the gap by a third,
it removed the only reason this file had to report one. Nobody did anything wrong. A number
moved because a recording decision moved.

Those 38 zeros come back in Week 3, where removing them decides whether the one clean
fairness finding in the Portuguese half of the audit exists at all.

### The closing question

Section 6 asks you to write **one question these data cannot answer**. Not a question you
ran out of time for: a question that no additional cleverness with this file would resolve.
Bring it to Week 2, when the setting changes to a UK distance-teaching university and one
flat file of 395 rows becomes six files and 922,449 rows, and we find out whether more data,
and messier data, actually helps.

Some of these questions become course research projects. Keep yours.

## Stretch goals

For students who finish early or arrive with coding experience. None of these are required
and none are graded.

1. **The other zeros.** `absences` has a mean of 5.71, a median of 4, a maximum of 75, and
   29 percent of students sitting at exactly zero. Ask whether every one of those zeros
   means the same thing, and say how you would tell.
2. **G1 and G2, before the gap.** Redo the mother's-education chart on the first-period
   grade instead of the final one. Is the gradient already there in period 1, or does it
   open up over the year? Those are different findings about different things.
3. **Put an interval on it.** Bootstrap the difference between band 1 and band 4 mean
   grades. With 59 and 131 students, how much of the gradient survives resampling?
4. **The other 24 columns.** The file records travel time, study time, internet at home,
   family support, and paid tutoring, among others. Pick two, cross them, and then write
   the sentence you would have to defend before that cross went into a report.
5. **Whose absence is recorded.** Compare the recorded absence distribution across the two
   schools in the file. Then write two sentences: one about students, one about how two
   schools record.

Bring anything interesting to Week 2. Stretch work is a good source of discussion material.

## Troubleshooting

**"The data did not download."**
The setup cell prints a plain-English message naming the repository it was trying to reach.
The usual cause is no internet connection in the runtime. Run the cell again, since brief
network failures are common, then check `github.com/HakeoungLee/edis8100-datasets` in a
browser tab. That repository is **public**, so this failure is never about your GitHub
account or your invitation.

**"NameError: name 'students' is not defined" or "name 'pd' is not defined"**
You ran a cell out of order, or the runtime restarted. Fix: **Runtime > Restart session and
run all**, then wait for every cell to finish. This is the answer to most notebook problems
and it costs about ten seconds.

**"KeyError: 'gendr'"**
A typo in a column name. The valid names are printed by the cell that lists the columns.
Python is exact about spelling and does not guess.

**The cell shows `[*]` and nothing happens**
It is still running. The setup cell takes a second or two, everything else is instant. If
`[*]` persists for more than a minute, the runtime probably disconnected: **Runtime >
Restart session and run all**.

**Colab says "Cannot find notebook" or shows a 404**
You are signed into a different Google account, or the private repository authorization did
not complete. Redo the first-time steps above, and make sure "Include private repositories"
is checked. If the invitation has not arrived, use the Canvas copy and **File > Upload
notebook** instead.

**I lost my edits**
Colab discards untitled sessions. **File > Save a copy in Drive** at the start of any session
where you plan to keep something.

**My chart looks different from my neighbor's**
One of you flipped the Your turn value. Compare the two settings and explain the
difference to each other. That is the exercise.

**Red text appeared and I panicked**
Python errors are wordy but they are not damage. Nothing here can harm your computer, the
course data, or your grade. Read the **last line** of the error first, it usually names the
real problem. Then raise your hand.

## A note on AI use

The course permits AI use in designated activities and requires that you document it.
Undisclosed AI use is an Honor Code violation.

There is **nothing to submit this week**, so there is nothing to document. The habit starts
now anyway. Beginning with Mini Project 1 in Week 4, every mini project and every course
project milestone carries an **AI Reflection** submission on Canvas, and it has two parts
that go in two different places on that page:

- **The conversation record goes in a Word file, attached to the submission.** The full
  exchange, across every tool and every session, pasted in. Not a summary, and not into the
  text box.
- **The reflection goes in the Canvas text box**, where you copy in the four questions from
  the syllabus and answer each one: how you used it; whether it helped and how; whether it
  made your work more challenging in any way; and what lesson about AI you would pass on to
  a friend or the class.

If you use an assistant to make sense of anything in this notebook today, save the
transcript. Learning to read what an AI tells you about data, with appropriate suspicion, is
itself a course skill.

## Connections to this week's readings

The reflection section of the notebook ties directly to the required readings:

- **Lang, Wise, Merceron, Gašević, and Siemens (2022)**, "What is learning analytics?" Their
  definition includes learners *and their contexts*. Ask which columns in this file are
  about context, and which contexts it has no column for at all.
- **Wise (2019)**, on data-informed decision making. An administrator asks you for "the pass
  rate." You have two defensible answers, 67.1 percent and 74.2 percent. Name one decision
  you would make from this file and one you would refuse to make from it.
- **Siemens (2013)**, on learning analytics as an emerging discipline. After thirty minutes
  of it, what would you add to the field's definitions about the gap between what happened
  and what got recorded?

## Data and ethics

Everything you touch this semester is real. Nine published, openly licensed datasets carry
the eleven lab weeks, and no notebook in this course generates a row.

Today's file holds records for real teenagers in two Portuguese secondary schools, assembled
from school reports and a student questionnaire in the 2005 to 2006 school year. They
answered questions about their households and their lives. Their records were anonymised and
published under CC BY 4.0 so that people could learn from them, which is what we are about
to do, and the only reason you can open the file at all is that somebody chose to release it.

None of them agreed to be a teaching example. Ask who could be harmed by a claim before you
make it. Notice when a metric flattens a person. Notice which people are not in this file at
all. That stance is not a warm-up for the course, it is one of the course's arguments, and
the full statement of it is in the **Affordances and Limits Guide** in your Canvas module.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the
course guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
