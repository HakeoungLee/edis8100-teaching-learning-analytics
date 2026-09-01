# Week 13: Reading Research Critically, and Your Own AI Trace

This is the last hands-on session of EDIS 8100. The discussion hour puts two questions to three
published papers: who does this research say the problem is inside, and how much of this paper did
anybody check? The notebook then puts both of them to the person running it.

The file the notebook opens is your own AI interaction log. This is the one lab all semester whose
data nobody else reads. Nothing from the notebook is collected, and the session's written
deliverable is not collected either.

If you have never written a line of code, this notebook was written with you in mind, as every
notebook in this course has been. Nothing in it asks you to write code from scratch. You run cells,
read what comes out, and change a few clearly marked values to see what those choices were doing to
the result. Questions are welcome at any point, including questions about a single line of code, and
red error text is normal.

## At a glance

| | |
|---|---|
| **Session** | Week 13, Wednesday, November 18, 2026, Ridley Hall 137 |
| **Topic** | Reading Research Critically, and Your Own AI Trace |
| **Session type** | Instructor-led throughout. Week 13 has no student Discussion Leadership block. |
| **Notebook** | `week13_reading_critically_own_trace.ipynb` |
| **Data** | **Your own exported AI conversation.** For anyone who would rather not use one, a published alternative: `collab-chat/chat_logs.csv`, 1,374 messages from eight groups of four or five undergraduates in a computer networks course at Universidad de Valladolid, recorded between 15 and 18 February 2021, each group on two of those days, in Spanish. CC BY 4.0. Downloaded by the notebook from `github.com/HakeoungLee/edis8100-datasets`, folder `collab-chat` |
| **Citation** | Villa-Torrano, C. (2021). *Dataset on an online collaborative learning situation in a computer networks course* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5150537 |
| **Libraries** | pandas, numpy, matplotlib |
| **Needs internet?** | **Yes** for the published-transcript path. On your own-log path the file needs to be on the machine you are working from, since it does not arrive over the network. |
| **Deliverable** | The Section 4 write-up, which stays with you. Nothing from this notebook goes to Canvas. |
| **Is it assessed?** | No. The notebook is not collected and it is not graded. Coding is not assessed in this course in any week. |
| **Due** | Nothing is due this week. Final presentation slides are due on Canvas by 11:59 PM on December 2. |
| **Prior coding experience needed** | None |

Discussion Leadership ran in Weeks 2 through 11, with each of the three of you leading two of those
weeks. Week 13 is instructor-led from start to finish.

## What I hope you leave with

1. A conversation seen as a table of turns, and a sense of how little structure that is.
2. Three descriptive measures over a trace, and what each one needs before it means anything.
3. A category built about you by a rule somebody else wrote, held at the evidential status it has.
4. A count of how often you asked an assistant to justify, cite, or check itself, read next to what
   you were asking it for at the time.
5. The habit of naming the evidence that would settle a claim, and then checking whether the trace
   contains any of it.

None of these is a coding objective.

## What is in this folder

| File | What it is |
|---|---|
| `week13_reading_critically_own_trace.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

## Opening it in Colab

This repository is public, so you need only a Google account and a browser.

[![Open In Colab](https://doi.org/10.1111/bjet.13267

Direct link:
`You:`

### Getting your own log into the session

The published transcript arrives over the network like every other week. Your own log does not, so it
needs one extra step in Colab: open the folder icon in the left sidebar, use the upload button, pick
your exported text file, and then set `Me:` in the setup cell to the file name it shows, for
example `User:`. Files uploaded this way live in the temporary session and disappear when the
tab closes, which is the behavior you want here.

If you run the notebook locally instead, `Assistant:` is an ordinary path on your own machine.

## What the notebook does

1. **Gets a conversation into a table.** Turns, speakers, words. That is all the structure the rest
   needs, and how little it is is part of the work.
2. **Computes three descriptive measures.** Turn count, authorship share by words, and the gap
   before the next message.
3. **Runs two counts.** A keyword rule sorts your own turns into asking for a fact, for production,
   for critique, or for reassurance, and prints a one-line label of the kind a paper would use. Then
   a second count: how many of your turns asked the model to justify something, name a source, or
   check itself. The first count is the discussion hour's framing question applied to a sample of
   one. The second is its record question applied to your own practice.
4. **Argues against the label.** Three things it gets wrong, the evidence that would settle each,
   and whether that evidence is anywhere in the trace.

Both rules are dials. Editing them moves both numbers, and that is the second thing worth noticing.

## Walkthrough

We will move through this together in class, and it is fine if we spend longer somewhere and skip
something else.

| Step | Section | What happens |
|---|---|---|
| 1 | How to work through this notebook | Orientation, Shift + Enter, and what is and is not collected. |
| 2 | Setup | Run the first code cell. It imports pandas, numpy and matplotlib and reports which path you are on. |
| 3 | 1. Getting a conversation into a table | The parser, then turns, speakers and word counts. On the published path, a look at what each author in the group wrote before two of the columns are folded into one. |
| 4 | 2. Turns, share, and the gap before the next message | Three descriptive numbers, a two-panel figure, and what the third one needs that the first two do not. |
| 5 | 3. Labeling your turns | The keyword rule, the printed label, the bar chart, and the verification count. |
| 6 | 4. Arguing against the label | The session's written deliverable, which is not collected. |
| 7 | Before December 2 | The category in your own project, and the closing checklist. |

**Going further** is a clearly marked optional section near the end. It is not part of the class
time and nobody needs to work through it today.

## The data, and why this lab is the exception

Every other lab in this course runs on data somebody else collected and published under a license.
This one does not, and that is deliberate.

**Path 1, your own log.** You have uploaded AI interaction logs with every graded submission since
Week 4, and you were told in Week 1 that this session was coming. Set `ChatGPT:` to a plain text
export. Nobody else opens it, the instructor does not collect it, and the notebook does not record
which path was used.

**Path 2, a published transcript.** Leaving `Claude:` empty runs everything on
`You:`. It reaches every objective except the one in Section 4 that needs the
trace to be your own. Both paths are equal options and nobody is asked which they used.

## What the published path produces, and why each of those is the lesson

**The gaps come out as 60 seconds at every quartile.** That file records time to the nearest minute,
so every gap it can express is a multiple of 60. The distribution on screen is the clock's rather
than the conversation's, and a defensible thing to write is that latency is not measurable there at
the resolution the question needs.

**The category rule classifies nothing.** It reports 100 percent unclassified. Those students were
working in Spanish and the four rules are English keywords. The instrument does not announce that it
is out of its depth: it returns zeros while looking as authoritative as it did before. Somebody
reading only the output would come away with a description of students who never asked for anything.

**The verification count comes out at zero.** On a student's own log it often does too. Zero is a
fact about how a tool got used and about how a rule was written, rather than a result about a
person. It is only worth something read next to the first count: a run of production requests with
no backing requests is a different picture from a run of fact requests with no backing requests.

None of the three is a bug and none is hidden. All three are in the notebook's own text, before the
cells that produce them, and each is followed by a short table separating what the data show, what
is a plausible interpretation, and what the run cannot establish.

## Readings this lab sits under

- Yang, Y., Yuan, K., Li, X., & van Aalst, J. (2022). Fostering low-achieving students' productive
  disciplinary engagement through knowledge-building inquiry and reflective assessment. *British
  Journal of Educational Technology, 53*(6). https://doi.org/10.1111/bjet.13267
- Koretsky, M. D., Vauras, M., Jones, C., Iiskala, T., & Volet, S. (2021). Productive disciplinary
  engagement in high- and low-outcome student groups. *Research in Science Education, 51*(Suppl 1),
  S159-S182. https://doi.org/10.1007/s11165-019-9838-8
- Kaliisa, R., Misiejuk, K., López-Pernas, S., & Saqr, M. (2025). How does artificial intelligence
  compare to human feedback? A meta-analysis of performance, feedback perception, and learning
  dispositions. *Educational Psychology*. Advance online publication.
  https://doi.org/10.1080/01443410.2025.2553639

The first two share a framing question: both sort learners before analyzing them, and the thing to
work out is what that sorting does to the people in the study once it leaves the methods section.
The third comes with a task rather than questions. Students audit its reference list against
Crossref and Google Scholar, a quarter of the list each, and bring the record rather than a
conclusion, so that the class picture is built from four independent audits.

All three are published and peer reviewed. None is assigned as a failure, and neither question is
about the authors.

The notebook draws on these at four points, in short italic notes beginning *Connecting to the
readings.*

## Troubleshooting

**"No labeled turns found in that file."**
The parser looks for lines that begin with a speaker label such as `You:`, `Me:`, `User:`,
`Assistant:`, `ChatGPT:`, or `Claude:`. Exports vary, and many arrive as one unbroken block. Pasting
the conversation into a plain text file with `You:` and `Assistant:` at the start of each turn will
parse. The notebook falls back to the published transcript on its own rather than stopping, so
nothing is lost while you sort the file out.

**"FileNotFoundError" on my own log**
`MY_LOG_PATH` is a path, and in Colab it is a path inside the temporary session rather than on your
laptop. Upload the file through the folder icon in the left sidebar first, then use the name exactly
as it appears there.

**"The data did not download."**
On the published-transcript path the notebook fetches one file from
`github.com/HakeoungLee/edis8100-datasets`. Running the cell again resolves most brief network
failures. That repository is public, so this is never about a GitHub account or an invitation.

**"NameError: name 'turns' is not defined" or "name 'pd' is not defined"**
A cell ran out of order, or the runtime restarted. **Runtime > Restart session and run all**, then
wait for every cell to finish.

**The chart is empty where the gaps should be**
Your export dropped the timestamps, so the notebook prints a note in place of the histogram. That is
a finding about the export rather than a problem to work around, and Section 2 has a place to say so.

**Everything came out unclassified on my own log**
The four rules are English keyword patterns, matched case-insensitively, and `classify` returns on
the first rule that matches. A conversation in another language, or one phrased in ways the patterns
do not cover, returns zeros. The optional section at the end of the notebook is where to take that
further.

**Red text appeared**
Python errors are wordy, and none of them means something has been damaged. Your own log file is
opened for reading and never written to. The **last line** of the error usually names the real
problem. Please ask, and we will read it together.

## Documenting AI use

There is nothing to submit from this notebook, so there is nothing to document for it. The habit
still applies to the work that is graded. Every mini project and every course project milestone asks
for an **AI Reflection** submission on Canvas, with two parts in two places:

- **The conversation record goes in a Word file, attached to the submission.** The full exchange,
  across every tool and every session, pasted in rather than summarized.
- **The reflection goes in the Canvas text box**, where you copy in the four questions from the
  syllabus and answer each one.

Undisclosed AI use is an Honor Code violation. Those logs are also the material this session runs
on, which is a reasonable argument for keeping them carefully.

## Data and ethics

This lab inverts the arrangement the other twelve weeks depend on. Every other file we have opened
belongs to somebody who was never asked whether their records should become a teaching example:
secondary students in Portugal, distance learners at the Open University, school writers in the
United States, children with a robot in a Swiss lab, users of a tutoring app in Korea, forum posters
in an open online course, undergraduates in Valladolid, players of two science games. Each was
anonymized and released under a license, and that is the only reason any of it can be opened at all.

Today the trace is yours. You generated it, you kept it, and you decide whether to open it. The
published-transcript path exists so that the exercise works for anyone who would rather not, and it
is offered as an equal option rather than as an accommodation.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
