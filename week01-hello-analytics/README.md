# Week 1: Hello, Learning Analytics

This is the first hands-on session of EDIS 8100. Together we will open Google Colab, run a notebook
on a real published dataset, make a couple of figures, take a closer look at something the summary
numbers were smoothing over, and end with a question the data cannot answer.

If you have never written a line of code, this notebook was written with you in mind. Nothing in it
asks you to write code from scratch, today or in any later week. You run cells, read what comes out,
and change one clearly marked value to see two headline numbers move. Questions are welcome at any
point, including questions about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 1, Wednesday, August 26, 2026, Ridley Hall 137 |
| **Topic** | Course Introduction and Planning |
| **Notebook portion** | Approximately 4:50 to 5:30 PM. Week 1 is an introduction week and ends early. |
| **Notebook** | `week01_hello_learning_analytics.ipynb` |
| **Data** | **Real, published, openly licensed.** UCI Student Performance, the mathematics file: 395 students in two Portuguese secondary schools, one flat file, 33 columns, semicolon delimited. CC BY 4.0. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `uci-student-performance` |
| **Citation** | Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance. *Proceedings of the 5th Future Business Technology Conference*, 5-12. |
| **Libraries** | pandas, matplotlib |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | None. This is in-class work, and nothing goes to Canvas. |
| **Due** | Nothing. Discussion Leadership sign-ups happen in class today: each of the three of you signs up for **two** weeks across the semester. |
| **Prior coding experience needed** | None |

Mini projects begin in Week 4. This week is for getting oriented and getting the tools working.

## What I hope you leave with

1. A sense of what a notebook is and how to run a cell.
2. Being able to say what one row and one column of a dataset represent.
3. Seeing how one analytic decision can change what a summary number says.
4. A feeling for why interpretation needs context that the file may not hold.
5. The idea that data traces are representations of learning activity rather than learning itself.

None of these is a coding objective.

## What is in this folder

| File | What it is |
|---|---|
| `week01_hello_learning_analytics.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is nothing to download by hand and nothing to upload. The first code cell fetches one file
over plain HTTPS in about a second and prints how many rows and columns arrived. If the download
fails, the cell prints a plain-English message naming the repository it was trying to reach rather
than a long error trace.

## Opening it in Colab

This repository is public, so you need only a Google account and a browser. There is nothing to
accept or authorize.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week01-hello-analytics/week01_hello_learning_analytics.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week01-hello-analytics/week01_hello_learning_analytics.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, and enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`.

The notebook opens. Run the first code cell to begin.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Nothing is lost if you forget:
the dataset is a fixed published file, so re-running the notebook from the top reproduces the same
numbers on any machine.

## Walkthrough

We will move through this together in class. The timings below are a rough guide rather than a
target, and it is fine if we spend longer somewhere and skip something else.

| Step | Section | Minutes | What happens |
|---|---|---|---|
| 1 | Welcome and how the notebook works | 3 | Orientation, and Shift + Enter. |
| 2 | Setup | 2 | Run the first code cell. It downloads `student-mat.csv` and prints `Loaded 395 students and 33 columns.` |
| 3 | Where this data came from | 3 | The provenance table, before any number appears. Note `sep=";"`: the comma in CSV is a convention that files do not always follow. |
| 4 | 1. Meet the table | 5 | `students.head()`. Read one row aloud as a sentence about a person, then consider what the file never recorded. |
| 5 | 2. A first look at a group difference | 8 | Mean final grade by mother's education, then the same chart with group sizes on the bars, then a discussion of what a recorded group difference does and does not tell us. |
| 6 | 3. The shape of one variable | 4 | A histogram of all 395 final grades, and the unusual spike at 0. |
| 7 | 4. Looking at the zeros | 6 | The 38 zero records, their absence and earlier-period grades, and several plausible explanations. |
| 8 | Your turn | 3 | Change `TREAT_ZEROS_AS_MISSING` and watch the mean and the pass rate move. |
| 9 | 5. Reflection | 5 | Four short prompts, written in the notebook and brought to the closing discussion. |
| 10 | Before you leave | 1 | The checklist, and Discussion Leadership sign-ups. |

**Going further** is a clearly marked optional section at the end. It is not part of the class time
and nobody needs to work through it today.

## The figures we will make

1. **Mean final grade by mother's education, twice.** The first version rises across bands 1 to 4
   and then has its tallest bar at band 0. The second version puts the group sizes on the bars, and
   band 0 turns out to be three students with grades of 9, 15 and 15. That gives a habit worth
   keeping: put the group size next to the mean.
   The discussion that follows is the part the semester returns to. Bands 1 to 4 do rise, from 8.68
   to 11.76 on 59, 103, 99 and 131 students, and before writing a sentence about that it is worth
   asking what the instrument could not see, what the setting might produce, and what the file does
   not record about these households. A difference between recorded groups is, in the first
   instance, evidence about the conditions under which people studied and about how a school
   recorded outcomes. Whether it is evidence about the people themselves is a separate question that
   this file cannot settle.
2. **A histogram of all 395 final grades.** Roughly a bell centered near 11, with a tall spike at
   exactly 0 and nothing at 1, 2 or 3. That is an unusual shape for a grade distribution, and the
   next section takes a closer look.

## The pattern we look at

All 38 students with a final grade of exactly 0 have zero recorded absences, none of the 280
students with any recorded absence scored 0, and every one of the 38 has a first period grade above
zero. For comparison, 115 students in the file have zero recorded absences in total, so a zero
absence record does not by itself go with a zero grade.

Several explanations are plausible: a third period record that was never entered and stored as a
zero, students who left the course partway through the year, an administrative rule the file does
not describe, or something about how absences were recorded in that situation. **The dataset
documentation does not say which is the case**, so each remains a hypothesis rather than a finding.
Distinguishing what the data show, what is a plausible interpretation, and what the file cannot
establish is one of the main ideas of the session.

Treating those 38 as missing moves the mean from 10.42 to 11.52 and the pass rate from 67.1 percent
to 74.2 percent. Both numbers are defensible, as long as the choice is named.

Those 38 records come back in Week 3, where how they are handled affects a fairness comparison.

## The closing question

The reflection asks you to write **one question these data cannot answer**. A good one is a question
that no further work with this particular file would resolve, rather than one you simply ran out of
time for. Please bring it to Week 2, when the setting changes to a UK distance-teaching university
and one flat file of 395 rows becomes six files and 922,449 rows, and we look at whether more data,
and messier data, actually helps.

Some of these questions become course research projects. Please keep yours.

## Troubleshooting

**"The data did not download."**
The setup cell prints a plain-English message naming the repository it was trying to reach. The
usual cause is no internet connection in the runtime. Run the cell again, since brief network
failures are common, then check `github.com/HakeoungLee/edis8100-datasets` in a browser tab. That
repository is public, so this is never about a GitHub account or an invitation.

**"NameError: name 'students' is not defined" or "name 'pd' is not defined"**
A cell ran out of order, or the runtime restarted. **Runtime > Restart session and run all**, then
wait for every cell to finish. This resolves most notebook problems and takes about ten seconds.

**"KeyError: 'gendr'"**
A typo in a column name. The valid names are printed by the cell that lists the columns. Python is
exact about spelling and does not guess.

**The cell shows `[*]` and nothing happens**
It is still running. The setup cell takes a second or two and the rest are close to instant. If
`[*]` persists for more than a minute, the runtime has probably disconnected: **Runtime > Restart
session and run all**.

**Colab says "Cannot find notebook" or shows a 404**
You are most likely signed into a different Google account. Check the profile picture in the top
right corner, switch to the account you want, and open the link again.

**I lost my edits**
Colab discards untitled sessions. **File > Save a copy in Drive** at the start of any session where
you plan to keep something.

**My chart looks different from my neighbor's**
One of you has flipped the Your turn value. Comparing the two settings and explaining the difference
to each other is a useful thing to do.

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

If you use an assistant to make sense of anything in this notebook, please save the transcript.
Reading what an AI tells you about data, with appropriate care, is itself a course skill.

## Connections to this week's readings

The required readings are Siemens (2013), Wise (2019), Lang and colleagues (2022), and the SoLAR
(2025) definition taskforce report. The notebook draws on them briefly at a few points, and the
reflection returns to them:

- **Siemens (2013)** describes digital traces as offering real opportunities while remaining
  ambiguous, since the same trace can support more than one interpretation. The zero grades in this
  file are a small example.
- **Wise (2019)** distinguishes activity, artifact, association, and contextual data, and notes that
  more data do not automatically mean more information. Her account of proxy indicators, which need
  a justified link between what is observed and the construct of interest, is worth holding onto
  when we look at the mother's education column. Her framing of data-informed decision-making is
  what the pass rate question is about: the number contributes to a decision rather than dictating
  it.
- **Lang and colleagues (2022)** present learning analytics as a concern, an opportunity, a field of
  inquiry, and a community, and describe it as dealing with learners *and their contexts*. It may be
  useful to ask which columns in this file are context, and which contexts have no column at all.
- **SoLAR (2025)** describes the work as collection, analysis, interpretation, and communication,
  and emphasizes insights that are theoretically relevant and actionable, a human-centered and
  multidisciplinary field, closing the loop with stakeholders, and attention to responsibility,
  equity, and context.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across
the lab weeks, and no notebook in this course generates a row.

Today's file holds records for real teenagers in two Portuguese secondary schools, assembled from
school reports and a student questionnaire in the 2005 to 2006 school year. They answered questions
about their households and their lives. Their records were anonymized and published under CC BY 4.0
so that others could learn from them, which is what we are about to do, and the only reason the file
can be opened at all is that somebody chose to release it.

None of them agreed to be a teaching example. It is worth asking who could be harmed by a claim
before making it, noticing when a metric reduces a person to one number, and noticing which people
are not in the file at all. That stance runs through every week of the course.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
