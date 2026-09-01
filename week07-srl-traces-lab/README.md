# Week 7: Self-Regulated Learning Traces Lab

Can a stream of timestamped clicks tell us anything about how a person regulates their own learning?
This week's notebook works through that question on a real commercial tutor log.

Coding expertise is not assumed. Nothing in the notebook asks you to write code from scratch, this
week or in any other week of the course. You run cells, read what comes out, and change four clearly
marked values to watch a headline move. Questions are welcome at any point, including questions
about a single line of code, and red error text is a normal part of working in a notebook.

## At a glance

| | |
|---|---|
| **Session** | Week 7, Wednesday, October 7, 2026, Ridley Hall 137 |
| **Topic** | Learning Analytics for Self-Regulated Learning |
| **How the session runs** | Opening, then the student-led discussion hour from 3:40 to 4:40, guest speaker preparation from 4:40 to 4:50, a break, and our guest from 5:00 to 6:00 |
| **Guest speaker** | Conrad Borchers, Vanderbilt University, a coauthor of one of this week's required readings |
| **In-class time on this notebook** | None. Our guest holds the last hour, so there is no notebook block in class this week. The notebook is worked through outside class, at your own pace |
| **Notebook** | `week07_srl_traces_lab.ipynb` |
| **Data** | **Real, published.** EdNet KT3, a 500-user extract of the released interaction log of the Santa TOEIC tutor in South Korea. One file, `actions.csv.gz`, 1,893,105 rows by 7 columns, 500 learners. **CC BY-NC 4.0: attribution required, non-commercial use only.** Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `ednet-kt3-500` |
| **Citation** | Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In *Artificial intelligence in education (AIED 2020)*, Lecture Notes in Computer Science 12164 (pp. 69-73). Springer. |
| **Libraries** | pandas, numpy, matplotlib |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | None. Nothing from this notebook is collected. |
| **Due** | Nothing this week. Mini Project 4 launches in class in Week 8; the Canvas assignment page carries its deadline. |
| **Prior coding experience needed** | None |
| **Next session** | Wednesday, October 14, Week 8, where Mini Project 4 launches in class. |

Discussion leadership runs across six weeks between Week 2 and Week 11, and each of the three of you
leads **two** of them. Week 7 is one of them, and it comes first in the session so that the questions
it raises can be carried into the preparation block before our guest.

## What I hope you leave with

1. A way of reading the action vocabulary of a real tutor log out of the file itself, and of saying
   which parts of a learner's profile are about the learner and which are set by the software.
2. Being able to cut a continuous stream into sessions using a stated gap rule, and to report a
   sensitivity check showing how far the headline moves when that rule changes.
3. A feel for reading the order in which answering and explanation viewing occur, and for noticing
   when the order is set by the interface rather than chosen by the person.
4. Using inter-action timing to separate a screen that was displayed from a screen that was read,
   and being able to say what the clock still cannot tell us.
5. Recognizing a logging artifact: a comparison that appears to be about learning and turns out to
   be about a logging convention.

None of these is a coding objective.

The through-line of the session: **self-regulated learning is not directly observable, so everything
here is an inference from residue.** There is no column in the log for intention, confidence, or
effort. There is a column for what happened on a screen and when. The distance between those two
things is what the lab is about, and it is the Week 2 claim ladder again: `enter_e` is a feature,
help seeking is an indicator somebody has to argue for, and self-regulation is a construct with a
literature behind it. Section 5 asks whether one of those features reaches even the first rung.

## Something changed this week

Weeks 2 through 6 worked with data collected by universities: enrollment registries, virtual
learning environments, a research studio. This week the collector is a **company**, and the log was
written to run a product rather than to answer a research question.

That changes what is in the file and what is missing from it. There is no answer key, because
correctness lived elsewhere in Riiid's systems. There is no demographic column, no score, and no
name. What there is, in enormous quantity, is what the interface did and exactly when. The lab is
built on that asymmetry, and it ends with two patterns that look like learner behavior and that the
timing gives good reason to read as the application instead.

## What is in this folder

| File | What it is |
|---|---|
| `week07_srl_traces_lab.ipynb` | The notebook. It downloads its own data from a public URL and runs top to bottom untouched. |
| `README.md` | This file. |

There is nothing to clone, no CSV to download by hand, and no account to create. The first code cell
fetches one 14 MB compressed file over plain HTTPS in a second or two and prints what arrived. If
the download fails, the cell prints a plain-English message naming the repository rather than a long
error trace.

## Where the data comes from

**Dataset.** **EdNet KT3**, restricted to a 500-user extract prepared for this course. EdNet is the
released log of **Santa**, a commercial multi-platform tutoring service in South Korea for the
**TOEIC** English proficiency test. KT3 is the action-level release: one row per interface event,
with the timestamp, what kind of event it was, which item it happened on, which option was chosen if
any, and which platform the person was using. The extract runs from 30 August 2018 to 27 November
2019.

**Who collected it.** Riiid, the company that operates Santa, logged every interface event its own
product generated as a by-product of running the service. Its research group then anonymized and
released four nested versions of that log, KT1 through KT4, so that researchers with no access to a
commercial tutor could work on real interaction data at scale.

**License.** **CC BY-NC 4.0.** The license permits use, sharing, and adaptation **with attribution
and for non-commercial purposes only**. That last clause is not decorative and the notebook says so
twice. Anything built on this file in this course stays inside this course, which rules out a
product, a consulting deliverable, or a paid workshop. If your course project uses it, please cite
Choi and colleagues (2020) and say which release and which extract you used. "EdNet" alone is not a
citation.

**Who is in it.** People in South Korea preparing for a high-stakes English proficiency test, on a
commercial app they chose and in most cases paid for, studying on their own time and, for the
majority of these rows, on a phone. Choi and colleagues describe the service, not these 500
individuals. The extract itself carries no age, no gender, no location, and no score.

**What it cost to get here.** Identity is gone: every person is an integer with a `u` in front of it.
Item content is gone: a question is `q4142` and nothing more, so we cannot see what was asked or
judge whether the item was fair. **And the answer key is gone.** KT3 records the option chosen and
never the option that was correct. That single absence removes the most common analysis in this
literature, and Section 6 of the notebook argues that the absence is useful, because it makes room
to ask what that analysis would have been measuring.

**The file the notebook reads** (from `HakeoungLee/edis8100-datasets`, folder `ednet-kt3-500`):

| File | One row is | Size |
|---|---|---|
| `actions.csv.gz` | one interface event by one person at one millisecond | 1,893,105 rows x 7 columns, 500 learners |

Nothing is sampled or thinned inside the notebook. Loaded with sensible column types the whole file
is about 225 MB in memory and every computation finishes in seconds, so the notebook keeps all
1,893,105 rows and says so. Where a step drops rows, it drops them in view with a count and a
reason, and the largest such drop is 178 rows.

## Opening it in Colab

The course repository is public, so you need only a Google account and a browser. There is nothing
to accept or authorize.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week07-srl-traces-lab/week07_srl_traces_lab.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week07-srl-traces-lab/week07_srl_traces_lab.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, and enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`. Then select
`week07-srl-traces-lab/week07_srl_traces_lab.ipynb`.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Nothing is lost if you forget:
the dataset is a fixed published file, so re-running the notebook from the top reproduces the same
numbers on any machine. You can also run the notebook locally with Jupyter if you prefer; it needs
pandas, numpy, and matplotlib, all of which ship with Anaconda.

## Walkthrough

The four **Your turn** cells already contain working values, so the notebook runs start to finish
without you typing anything. The interpretation prompts after each figure are where the attention
belongs.

**Setup.** The first code cell imports three libraries, sets the plotting defaults, and downloads
`actions.csv.gz`. It prints 1,893,105 rows, 7 columns, 500 learners, about 225 MB, and a reminder
that the license is non-commercial.

**1. One row, and the alphabet of this log.** The vocabulary is not documented anywhere in the file,
so the notebook reads it out of the file, which is the ordinary situation. Crossing `action_type`
against the first letter of `item_id` shows that four action types and four item kinds combine into
exactly **seven** legal events rather than sixteen: `enter_b`, `respond_q`, `submit_b`, `enter_e`,
`quit_e`, `enter_l`, `quit_l`. Two of the seven are worth treating carefully as measures of a
person, because `enter_b` and `submit_b` occur exactly 314,791 times each: in this app a bundle that
is opened is a bundle that is submitted, so a profile reporting both reports one number twice. The
section closes by checking, in the column list, that **there is no correctness column**.

Section 1.1 prints 25 consecutive actions by one learner. It is the screen to slow down for. Three
timescales live in the `seconds_since_previous` column: gaps of **0.05 seconds**, faster than a
person can act; gaps of twenty to thirty seconds between opening a bundle and answering it, which is
the only stretch that plausibly contains thinking; and one place where the learner submits `b1073`,
re-enters it 3.23 seconds later, answers the same question twice with different options, and submits
again. The prompt invites two stories that produce those rows, one about the person and one about
the interface, and leaves them both open.

Section 1.2 sets out the mess with a decision and a stated cost for each of six items: **2,637** rows
tied to the millisecond, **19** learners whose logs begin mid-flow (costing 178 rows and zero
answers), **14,417** bundles submitted with nothing answered, **18** explanation items with no
matching bundle, **42** learners with no explanation event and 91 with no lecture event, and the
shape of the people. That last one carries the most weight: rows per learner run from **5 to
52,917**, the busiest ten learners hold 16.0 percent of all rows, and the quietest 250 hold 4.6
percent. The rule the whole notebook then obeys is stated once and applied everywhere: **compute per
person, then summarize across people; put a count next to every rate; when an interval is needed,
resample the people, not the rows.**

**2. What a learner's action profile does and does not say.** Per-learner shares of the five
substantive events. Most boxes are narrow: the middle half of learners spend between 21.0 and 25.2
percent of their events opening bundles, and the notebook works through the instrument and the
setting before treating that as a finding about consistent people. The explanation box is the one to
watch, and not because it is wide. Its middle half is narrow too, 19.4 to 24.1 percent, but its
tenth percentile is 4.0 percent, so the spread is all in a lower tail. The prompt invites a
hypothesis about that tail, and Section 5 supplies the evidence. **Your turn 1** puts any single
learner against the class median, with counts printed beside the percentages.

**3. Cutting a stream into sessions, and admitting it is a choice.** The file has no session column,
so the analyst invents one. The gap histogram is worth the whole section: there **is** a valley in
this distribution, at about **0.2 seconds**, and what it separates is the machine from the person
rather than one sitting from the next. Everywhere a session rule could plausibly go, from a few
minutes to a couple of hours, the curve just slides downward. The only feature that behaves like a
natural unit is the rise after six hours peaking near a day, which is consistent with people coming
back the next day.

The notebook states a 30 minute rule, applies it, and reports a headline: **a typical sitting is
about 8.75 bundles and 16.0 minutes**, computed per learner and then medianed across the 500. It
also prints, for contrast, what comes out of pooling over the 23,810 sessions and forgetting the
nesting.

Then it moves the rule, which is the part most papers skip. Across gap rules from 5 to 120 minutes
the headline runs from **5.0 to 10.0** bundles, a factor of 2.0, and the minutes figure from **6.5
to 22.8**, a factor of 3.5. The number of sessions found runs from 48,578 to 17,535. Nothing about
the learners changes between those rows. **Your turn 2** ships a 10 minute rule so a number moves on
the first run.

**4. Order: what follows what.** A bigram matrix over 1,892,605 within-learner pairs. Only **19 of
49** cells ever occur, and the notebook labels never-occurred cells with a dot and rounds-to-zero
cells with `<1`, so that the five cells that happened but round away stay visible. Two cells set up
everything that follows: `submit bundle` is followed by `open explanation` **94.4 percent** of the
time, and `close explanation` is followed by `open explanation` 12.9 percent of the time.

**5. The first logging artifact: the explanation nobody asked for.** The section opens with an
abstract anybody could write this afternoon, operationalising help seeking as the number of
explanation screens opened. Then it measures the seconds between submitting a bundle and the
explanation appearing. The overall median is **0.077 seconds**. Human simple reaction time to a
visual signal is about 0.2 to 0.25 seconds, and that is before deciding anything.

The second half of that chart is sharper still. **On mobile 98.6 percent of these screens appear
within a fifth of a second (median 0.057 s); on web the median is 1.317 s and the share under 0.2
seconds is 18 screens out of 114,214.** Same product, same behavior, different client. A latency
that might have been read as how quickly a learner turns to help tracks what device they were
holding.

The consequence is then made quantitative: across the 500 learners, explanation screens opened
correlates with bundles submitted at **Spearman 0.995**, with a median of 1.008 explanations per
bundle, so ranking people on "explanation use" reproduces ranking them on volume. And the hypothesis
from Section 2 gets its evidence: all **42** learners with no explanation event have between 7 and 40
total logged events against a class median of 1,051, and **no** learner with 100 or more events is
among them. Among the 409 regular users the explanation share sits between 18.3 and 26.0 percent
from the 5th to the 90th percentile. The lower tail is people with almost no log, which is a general
failure mode worth naming: a measure that behaves differently for people with little data
manufactures a group that is really a sample-size artifact.

**6. The second logging artifact: the answer you have already been shown.** The study everybody
wants to run on a tutor log is whether learners who use the help do better, comparing accuracy with
and without help. This extract has no answer key, so that study cannot be run, and the section works
out what it would have been measuring.

Three steps. First, **222,958 of 544,487 answers (40.9 percent)** are repeats of a question that
learner had already answered. Second, **83,779 answers (15.4 percent of all of them, and 35.7
percent of repeats)** were given by somebody who had already opened the explanation for that bundle.
Third, and this is the move that needs no answer key: if a post-explanation answer is reproduction
rather than knowledge, the chosen options should pile up on one option. They do. Across **1,241**
questions with at least ten independent answers in each condition, the share of answers falling on
the single most chosen option rises from a median of **0.551** at first exposure to **0.700** after
the explanation has been shown, with the difference rising on 81.6 percent of questions and a
bootstrap interval over questions of [+0.125, +0.145].

Then the notebook corrects its own statistic, because "share on the most chosen option" is inflated
when a question has fewer answers and the two conditions here do not have the same number: 67 per
question at first exposure against 14 afterwards. Thinning the first-exposure side to match,
question by question, the median difference falls from **+0.136 to about +0.110**, so roughly a
fifth of the raw effect was sample size and four fifths was not. The bootstrap interval quoted above
is an interval on the uncorrected statistic and does not contain the corrected one, which is worth a
sentence of its own. Restricted to answers arriving within 24 hours of the explanation, the
post-explanation median is **0.812** against 0.496, and the same thinning lifts the 0.496 to about
0.527.

The notebook then does two things most treatments do not. It states the caveat that questions are
not independent either, because the same 500 learners recur across them, so the interval is
optimistic. And it is explicit that the reproduction reading rests on an assumption the extract
cannot confirm, namely that a Santa explanation screen presents the solution: the log records that a
screen opened, not what was on it. What the notebook can generalize is the direction. Wherever a
tutor logs help before the outcome it scores, the outcome after help is partly determined by the
logging. The transfer exercise asks for three things to check about **when a row gets written**,
before computing anything at all. **Your turn 3** ships a stricter minimum of 25 answers per
question.

**7. Timing: separating a screen that appeared from a screen that was read.** What the clock gives
back. All 342,634 explanation opens pair perfectly with a close, and the dwell between them is the
closest thing in this file to evidence that a person did something with the help. Median 15.4
seconds; 8.7 percent close within two seconds and 40.2 percent within ten. Per learner, among the
404 with at least 20 screens, the share held for ten seconds or more has a median of **0.629, 95
percent interval [0.604, 0.660] from resampling learners**, and runs from 0.316 at the tenth
percentile to 0.866 at the ninetieth. The 96 excluded learners are named and the notebook says
plainly that they are not missing at random.

Section 7.1 is where a hypothesis dies. An explanation the learner opened themselves ought to hold
their attention longer than one the app put in front of them. Within learner, among the 258 with at
least 20 screens of each kind, the difference goes the **other** way: **-7.77 seconds, 95 percent
interval [-9.76, -5.50]**, entirely below zero. Then the breakdown: of the screens not opened by the
flow, **54.9 percent** are the learner reopening the explanation they had just closed, at a median
of 6.5 seconds each. Flicking back is quick. The label "opened it themselves" was ours rather than
the log's, and the repair required is to the operationalisation rather than to the theory.

Section 7.2 measures the seconds from a bundle opening to the first answer inside it. Per learner,
the middle half of the 415 learners with enough bundles sit between **17.6 and 23.2 seconds**, a
startlingly narrow band, and again the instrument and the setting get asked first. This is also
where the field's vocabulary appears: 1.3 percent of bundles are answered within three seconds, the
field calls patterns like this **"gaming the system"** and **"hint spam"**, and the notebook quotes
those phrases, points out that each names a motive no timestamp can see, and then says what was
actually recorded. **Your turn 4** moves the ten second line and prints how many learners change
decile because of it.

**Reflection.** Four prompts, three tied to this week's readings by author and one that reaches back
to Week 3 and lists the six choices this notebook made. Then the guest question section, with a
drafted question for Conrad Borchers about window choice in ordered network analysis that comes
straight out of Section 3.

**Before we meet again.** A checklist. The two items worth taking seriously are being able to
explain both logging artifacts to somebody who was not in the room, and remembering that the license
is non-commercial.

**Going further (optional).** Worked versions of all four Your turn cells, including a twelve-point
sweep of the session rule, a full sweep of the concentration threshold, and a Jaccard overlap grid
showing that of the 85 learners who could ever land in the bottom decile of explanation dwell, only
**5** land there under every threshold.

## What this connects to in the readings

- **Winne (2022)**, *Learning analytics for self-regulated learning*: the argument the whole lab is
  built on, that self-regulated learning is not directly observable and that traces are observable
  behavior tightly coupled to unobservable cognitive operations, with inferences that are
  probabilistic rather than certain. He also sets out four features of ideal trace data: near
  complete sampling of operations, identification of the information operated on, timestamps, and a
  record of the products produced. This file has the second and the third, and neither of the
  others. Among his open questions is whose model of a learning session overlays the data, the
  analyst's or the learner's, which is the question Section 3 sits with.
- **Zhang, Borchers, and Barany (2024)**, *Studying the interplay of self-regulated learning cycles
  and scaffolding through ordered network analysis across three tutoring systems*: the paper our
  transition matrix is a blunt first cousin of. They code think-aloud data from fifteen students
  across three intelligent tutoring systems and use ordered network analysis, which connects actions
  inside a moving stanza window (theirs is four, with checks at five and six); our bigram matrix
  only sees the action immediately next door. They report more SRL transitions in the less
  scaffolded, open-ended platforms, and that heavily scaffolded environments made it easier to enact
  problem-solving operations without prior planning. Santa sits at the heavily scaffolded end.
  Conrad Borchers is a coauthor, so this is the reading to arrive having read closely.
- **Viberg, Khalil, and Baars (2020)**, *Self-regulated learning and learning analytics in online
  learning environments: A review of empirical research*: a review of 54 empirical studies published
  between 2011 and 2019, which finds most of them concentrated on the forethought and performance
  phases with much less attention to reflection, and concludes that the work has been used mainly to
  measure self-regulated learning rather than to support it. The reflection turns that on this
  notebook: rank the four candidate measures built here, the action profile, bundles per sitting,
  explanation dwell, and time to first answer, from "activity with a nicer name" to "defensible
  evidence about regulation", and make the case for the ordering.

## Going further (optional)

None of this is needed, and it is here for anyone who finishes early or arrives with programming
experience.

1. **The `source` column, which the notebook deliberately leaves alone.** Santa logs eight study
   modes, from `sprint` and `diagnosis` to `review_quiz` and `my_note`. Recomputing the explanation
   dwell measure separately by mode opens a question worth asking: is the between-learner spread in
   Section 7 partly a between-mode spread, meaning that what looks like a difference between people
   is a difference in which part of the product they used?
2. **The mobile and web populations, split everywhere.** Section 5 shows the client changing a
   latency by a factor of twenty. Recomputing the session statistics, the dwell distribution, and
   the time to first answer separately for the 292 mobile-only learners and the 33 web-only ones
   would show how far that goes, and which of the notebook's headlines survive.
3. **A real sequence measure, so that the order does more work.** Our bigram sees one step.
   Extracting each session's event sequence as a string, counting the most frequent 4-grams, and
   comparing the top ten between the top and bottom thirds on explanation dwell is a start. Then the
   harder question: can a pattern nobody named in advance be called self-regulation?
4. **An attack on the concentration analysis.** Section 6 infers reproduction from the fact that
   post-explanation answers concentrate on one option. What check would falsify it? One candidate:
   within questions, compare the concentration of answers given after the explanation with the
   concentration of answers given on a second exposure with **no** explanation in between, which
   isolates repetition from being shown the answer. How many questions have enough of both?
5. **Sensitivity as a deliverable rather than a footnote.** The optional section sweeps the session
   rule and the concentration threshold separately. Sweeping them jointly gives a surface. Then the
   two-sentence methods note you would put in a paper is worth drafting, alongside a note of how
   rarely such a sentence turns up in the papers you have read.

## Troubleshooting

**"NameError: name 'actions' is not defined" or something similar.**
A cell ran out of order, or the runtime restarted. **Runtime > Restart session and run all** in Colab, or
**Kernel > Restart & Run All** in Jupyter, then wait for every cell to finish. This resolves the
large majority of notebook problems.

**"The data did not download."**
The setup cell prints a plain-English message naming the repository and the exact URL instead of a
traceback. The usual cause is no internet connection in the runtime. Run the cell again, since brief
network failures are common, then check the repository in a browser tab. That repository is public,
so this is never about a GitHub account or an invitation. If the repository itself is unreachable,
please send Dr. Lee the URL the cell printed.

**It is taking a long time.**
The file is 14 MB compressed and about 225 MB in memory. End to end the notebook executes in about
half a minute on a laptop and comfortably under two minutes on a free Colab runtime. If a cell seems
stuck, it is almost always the download rather than the arithmetic.

**"KeyError: 'u501'" in Your turn 1.**
Learner ids are not a contiguous range. The cell prints six valid ids and says when the one you
typed is not in the file. `u1`, `u170`, or any id from the printed list will work.

**My session numbers are different from my neighbor's.**
Compare `MY_GAP_MINUTES` first. That is almost always the difference, and noticing it is the point
of Section 3.

**My concentration numbers are different.**
Compare `MY_MIN_ANSWERS`. At 5 the comparison keeps 3,295 questions and the median difference is
+0.121; at 30 it keeps 104 and the difference is +0.184. Both are real, and the optional section
explains why the gap widens as the bar rises.

**The dwell histogram has a gap on the left.**
That is the log scale rather than a bug. Dwell times below about a tenth of a second are rare
because closing a screen is a physical action.

**Some cells in the transition heatmap show a dot and some show `<1`.**
That is deliberate. A dot means the transition never happened once, which is a fact about what the
software permits. `<1` means it happened, in two cases 1,434 times, and rounds to zero at
whole-percentage precision.

**Colab says it cannot find the notebook, or shows a 404.**
You are most likely signed into a different Google account. Check the profile picture in the top
right corner, switch to the account you want, and open the link again.

**Red text appeared.**
Python errors are wordy, and none of them means something has been damaged. Nothing here can harm
your computer, the course data, or your grade. The **last line** of the error usually names the real
problem. Please ask, and we can read it together.

## A reminder about the license

EdNet is released under **CC BY-NC 4.0**, and two obligations follow. **Attribution**: please cite
Choi and colleagues (2020) wherever this data appears in your work. **Non-commercial**: nothing
built on this file may be used commercially, which includes consulting deliverables, paid workshops,
and product prototypes shown to a buyer. If your course research project wants to go further with
tutor logs, that is a conversation worth having with Dr. Lee early, because the license, rather than
the analysis, is usually what decides it.

## Documenting AI use

The course permits AI use in designated activities and asks that you document it. Undisclosed AI use
is an Honor Code violation.

There is **nothing to submit this week**, so there is nothing to document. It is still worth keeping
the habit. If you used an AI assistant while working through this notebook, to explain what a bigram
matrix is, to check your reading of the concentration chart, or to help sharpen the question you are
bringing for our guest, please save that exchange now.

The policy has two parts that go in two different places, and it applies in full the moment any of
this work reaches a mini project or your course research project:

- **The conversation record goes in a Word file, attached to the submission.** The full exchange,
  across every tool and every session, pasted in rather than summarized.
- **The reflection goes in the Canvas text box**, where you copy in the four questions from the
  syllabus and answer each one: how you used it; whether it helped and how; whether it made your
  work more challenging in any way; and what lesson about AI you would pass on to a friend or the
  class.

Keeping the log as you go is easier than reconstructing it afterward, and a week with nothing due is
the cheapest possible time to practice.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across
the lab weeks, and no notebook in this course generates a row.

This week's file holds records of adults in South Korea studying for a test that gates jobs,
generated by a product that was measuring them in order to sell them something. Nobody in it agreed
to be a teaching example. It is worth asking who could be harmed by a claim before making it,
noticing when a metric reduces a person to one number, and remembering that "the log shows" is a
sentence about a file. That stance runs through every week of the course.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*

*Data: EdNet KT3, a 500-user extract. Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek,
J., Bae, C., Kim, B., & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In*
Artificial intelligence in education (AIED 2020), *Lecture Notes in Computer Science 12164 (pp.
69-73). Springer. Licensed CC BY-NC 4.0: attribution required, non-commercial use only.*
