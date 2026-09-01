# Week 10: Game and Emotional Analytics Lab

Two real games, sixteen thousand children's codenames, and a persistence finding that does not
travel from one game to the next.

This notebook is worked through on your own schedule rather than in class. If you have never
written a line of code, it was written with you in mind: nothing in it asks you to write code from
scratch, and the core path is run-and-interpret. Questions are welcome at any point, including
questions about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 10, Wednesday, October 28, 2026, Ridley Hall 137 |
| **Topic** | Game Learning Analytics and Emotional Learning Analytics |
| **Guest speaker** | Chaewon Kim, Southern Illinois University, for the last hour |
| **Notebook portion of the session** | **None.** The guest holds the final hour this week, so there is no in-class notebook block. You work through the notebook outside class, at your own pace, before or after we meet |
| **Notebook** | `week10_game_emotional_analytics_lab.ipynb` |
| **Data** | **Real, published, openly licensed.** Open Game Data, Field Day Lab, University of Wisconsin-Madison. `fieldday-aqualab/players.csv.gz` (19,031 rows by 145 columns), `fieldday-aqualab/player_jobs.csv.gz` (96,322 by 11), `fieldday-waves/sessions.csv.gz` (1,581 by 870). Public domain, **CC0 1.0**. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets` |
| **Citation** | Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab, University of Wisconsin-Madison. https://opengamedata.fielddaylab.wisc.edu |
| **Libraries** | pandas, numpy, matplotlib. Nothing else this week, and every statistic is built from those three and stays visible in the notebook |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data |
| **Runtime** | Well under a minute end to end on a normal connection, most of it the download |
| **Deliverable from this notebook** | **None.** Nothing here is collected, and Week 10 is not a mini project |
| **Due this week (separately)** | **Course Research Project Literature Review**, plus the **AI Reflection** submission, uploaded to Canvas by **11:59 PM on Sunday, November 1, 2026** |
| **Prior coding experience needed** | None |

The mini projects were weeks 4, 5, 6, and 8. This week the notebook carries no rubric and no
upload; the literature review is the graded submission.

## How the session runs

| Time | Segment |
|---|---|
| 3:30 to 3:40 | Opening and introduction |
| 3:40 to 4:40 | Reading discussion, led by the instructor |
| 4:40 to 4:50 | Guest speaker preparation, including questions for the Q&A |
| 4:50 to 5:00 | Break |
| 5:00 to 6:00 | Guest lecture and Q&A: Chaewon Kim, Southern Illinois University |

Discussion Leadership runs weeks 2 through 11 across six weeks, and each of the three of you leads
**two** of them. This is not one of those weeks. Six turns divide exactly among three of us, and
Weeks 7 and 10 are the two with a guest, so the instructor runs the reading hour in both.

The notebook is not opened together in class. Please bring one plot or one question from it to
Week 11, the co-design studio.

## The data

| | |
|---|---|
| **What** | Play logs from two educational games: **AQUALAB** (*Wake: Tales from the Aqualab*), a marine-science adventure in which players run experiments and then argue for a conclusion from evidence, and **WAVES** (*Wave Combinator*), a 35-level signal-matching puzzle |
| **Who collected it** | **Field Day Lab**, Wisconsin Center for Educational Research, **University of Wisconsin-Madison**, through their Open Game Data infrastructure |
| **Who is in it** | Children. The age item was answered in 6,092 of 18,959 player-months, which is 32.1 percent, and among those who answered, 86.5 percent selected a band at 15 or younger, the largest single group selected 12 to 13, and 79.4 percent said they were playing at school. Those are the demographics of the third who answered rather than of the file as a whole |
| **When** | Ten monthly AQUALAB extracts, September 2025 through June 2026, plus a set of individual WAVES sessions |
| **License** | **CC0 1.0 Universal**, the Creative Commons public domain dedication. No rights reserved, no permission needed, no attribution legally required |
| **Citation** | For the data, the form Field Day's own per-game readme asks for: Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab, University of Wisconsin-Madison. Retrieved from https://opengamedata.fielddaylab.wisc.edu <br> For the infrastructure, the paper the site names: Gagnon, D., & Swanson, L. (2023). Open Game Data: A technical infrastructure for open science with educational games. In M. Haahr, A. Rojas-Salazar, & S. Göbel (Eds.), *Serious Games. JCSG 2023* (Lecture Notes in Computer Science, Vol. 14309, pp. 3-19). Springer. https://doi.org/10.1007/978-3-031-44751-8_1 |
| **Source** | Field Day Lab, University of Wisconsin-Madison. https://opengamedata.fielddaylab.wisc.edu |
| **This extract** | Course-sized subsets, redistributed unchanged, at github.com/HakeoungLee/edis8100-datasets |

CC0 means the class is legally free to do anything with these files. The notebook spends a section
on why that makes the ethical question louder rather than quieter, given who is in them.

This is the only week that uses the Field Day data. It is not the only week whose learners are
young: week 1 and week 3 work with Portuguese secondary school students, week 5 with school
students writing to a test prompt, and week 6 with nine to twelve year olds working with a robot.
What is different here is that the record is play rather than assessed work.

## What I hope you leave with

1. Being able to state where a dataset came from before analyzing it: who logged it, from whom,
   under what license, and what the file cannot see.
2. A way of finding the mess in a real telemetry extract, meaning columns that hold one value, a
   category that is not an activity, durations that run backwards, rows with no player at all, and
   answers in two languages, and a habit of saying what each repair costs.
3. A sense of how to summarize a heavily skewed count, and of why the mean is a poor number for the
   hardest job in AQUALAB and the median is not obviously the right one either.
4. Being able to separate a selection question from an effect question when the same event switches
   both variables on, and to carry an interval that respects rows nested inside people.
5. A way of reading an in-game affect item without treating a feeling word as a property of a child.
6. A feeling for what happens when a replication in a second game disagrees with the first, and for
   how to report that.

None of these is a coding objective.

The through-line: **the same question, asked of two games, gets two answers, and neither of them
was planted.** In AQUALAB, children who argued more than ten times at the hardest job in the game
completed 14.81 more jobs that month, interval [+12.24, +17.24]. Take that apart and 67.1 percent
of the persisting group went on to complete another job against 3.1 percent of the others, and
among the player-months whose record demonstrably continued, argumentation tries and later
completions are uncorrelated (rho = -0.007, n = 210). Carry the same question to WAVES, where the
game supplies the next level whether or not you struggled, and the gap is +0.85 levels out of 25
(rho = +0.055). On one common scale the three answers are **0.749**, **0.454**, and **0.531**. The
work is deciding which question each of them answers.

The second through-line, and the reason this week matters beyond method: **the learners are
children.** Most of the design proposals made this semester assumed a consenting adult. The
reflection section invites you to rewrite one of them for an eleven year old.

## What is in this folder

| File | What it is |
|---|---|
| `week10_game_emotional_analytics_lab.ipynb` | The notebook. It downloads its three data files from the course dataset repository on first run and writes nothing to your machine. |
| `README.md` | This file. |
| `data/` | Three small CSV files left from an earlier version of this activity. Nothing in the notebook reads them. |

There is nothing to clone and no CSV to fetch by hand. The first code cell reads three compressed
files over the internet, a few megabytes in total, in a couple of seconds. If the download fails it
prints a plain sentence naming `github.com/HakeoungLee/edis8100-datasets` rather than a wall of red
text.

## Opening it in Colab

The course repository is public, so you need only a Google account and a browser.

[![Open In Colab](https://opengamedata.fielddaylab.wisc.edu

Direct link:
`argtime`

If you would rather not use the badge, go to
[colab.research.google.com](https://opengamedata.fielddaylab.wisc.edu sign in, choose
**File > Open notebook**, click the **GitHub** tab, enter
`0:00:00` with the branch on `JobTriesInArgumentPerDifficulty`, and select
`no-active-job`.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Nothing is lost if you forget:
the three files are fixed published extracts, and every interval in the notebook is seeded, so
re-running from the top reproduces the same numbers.

You can also run the notebook locally with Jupyter. It needs pandas, numpy, and matplotlib, all of
which ship with Anaconda, plus an internet connection for the three files.

## Walkthrough

The four **Your turn** cells already contain working answers, so the notebook runs start to finish
without you typing anything. Take the sections at whatever pace suits you; there is no clock on this.

**Setup.** One short code cell. It downloads three files and prints their shapes. The provenance
table follows immediately: who logged this, from whom, under what license, with what citation.
Being able to state where a dataset came from before analyzing it is a habit the course keeps
returning to.

**1. What is one row, and who is in it?** The dataset repository calls `ExperimentalCondition` "one row
per player." It is not. It is 19,031 rows over 16,384 codenames across ten monthly extracts, and
1,922 codenames appear in more than one month with no way to tell whether that is a child returning
or a name collision. Two panels draw the shape. The section names the unit of analysis as the
**player-month** and explains why every interval later in the notebook resamples codenames rather
than rows.

**2. Real data is messy, and the mess is the lesson.** The cheapest check in data analysis, run
first: how many distinct values does each column hold? It finds `production` (one value, `priorcomplete`, in
all 96,322 rows), `argtime` (one value, `0:00:00`, in all of them), and five
`JobTriesInArgumentPerDifficulty` columns that are zero in all 19,031 rows. Then the pseudo-category
`no-active-job` (10,340 rows, 10.7 percent), ten rows with no codename at all and hundreds of
sessions each, thirteen values of `ExperimentalCondition` of which only four begin with
`production`, 2,631 player-months with a negative duration (the most negative about minus 3.27
million seconds), and an affect column carrying both English and Spanish.

Three exclusions follow, each with its own line in a costs table, and one consistency check that
earns the right to use `priorcomplete` for temporal ordering later: the largest "completed before"
count in a player-month equals that month's total in 100.0 percent of cases.

**3. The hardest thing in the game.** `coral-hunting-lions` averages **31.98** argumentation tries
against a median of **8**, while the typical job in AQUALAB has a median of 1. Two panels: mean
against median for the ten hardest jobs, and the raw distribution with both lines drawn on it. 42.3
percent of the player-months that took this job logged zero tries, and the busiest 5 percent supply
29.1 percent of them all. The prompt asks what each of the two summaries misses rather than which
one wins, and a short table separates what the data show from what would be an interpretation.

**Your turn 1.** Point the same three summaries at another job. The optional solution then scores
all 51 common jobs and shows the busiest 5 percent supplying a **median of 37.4 percent** of a job's
tries, with a floor of 20.5 percent. The concentration is not a property of the hard job; it is a
property of voluntary-play counts.

**4. Did persisting pay? Two questions that look like one.** The heart of the lab. The trap is named
before any code runs: argumentation tries and jobs completed are both counts of activity, so some
association follows from arithmetic alone.

The headline arrives anyway and it is large. Children who argued more than ten times completed
**32.76** jobs against **17.96**, gap **+14.81** [+12.24, +17.24], from a cluster bootstrap over the
508 codenames rather than the 617 rows. `priorcomplete` then splits that gap in time: only **+3.52**
[+1.12, +5.90] was banked before the job, and **+11.29** [+9.67, +12.91] came after.

Then the boring question that dissolves it, asked precisely. **67.1 percent** of the persisting
group completed at least one further job that month; **3.1 percent** of the others did. The rank
correlation between tries and jobs-completed-afterwards is +0.654, and between tries and that flag
it is +0.649, because they are nearly the same variable: they agree on 607 of the 617 rows. The
notebook says so rather than calling the flag "was the child still playing", and then measures the
limit: **64 percent** of the player-months the flag calls "no further completion" took other jobs at
the same completion depth, so they attempted more and finished nothing more, and with no timestamps
on job rows nothing can order them. The panel is a decomposition of the outcome, not an independent
check on who was still playing. Among the **210** player-months that completed at least one more
job, the correlation is **-0.007** and the four try-quartiles average 17.22, 17.75, 16.81, and 18.55
jobs afterwards. Flat.

The section states what the file supports in full, including that the two-group comparison inside
the still-playing subset has only 10 player-months on one side and therefore cannot rule out a
modest effect. A three-row table separates the numbers from the reading of them, and the discussion
prompts put the instrument, the setting, and the circumstances on the table before the child, in
that order.

**Your turn 2.** Move the threshold. The optional solution sweeps it from 1 to 80 and finds the raw
gap correlating with the difference in "share still completing" at **r = 0.961** across thresholds.
Stability across a sweep tells you the definition is not fragile. It tells you nothing about whether
the thing you defined is what you think it is.

**5. What children said they felt.** AQUALAB interrupts children and asks what they are feeling and
**why**. Three quarters of the file never answered; the median respondent answered exactly once.

The counterintuitive comparison the field likes: children who said "frustrated" and never "bored"
completed **18.32** jobs, children who said "bored" and never "frustrated" completed **11.42**, gap
**+6.89** [+5.26, +8.50]. Then the exposure control. The frustration group answered 3.66 prompts to
the boredom group's 2.23 and played 14.6 median hours to their 3.4, and "frustrated" was said by
only 9.2 percent of respondents, so a child who answers eight times has eight chances at a rare
word. Hold the number of answers fixed and the four bands read 5.17 against 5.52, 12.79 against
13.32, 18.74 against 18.98, 30.16 against 32.48. The size-weighted gap falls from +6.89 to **+0.75**
[+0.02, +1.44], which removes **89 percent** of it. The section is candid that the residue in the
widest band may be the same difference in exposure, not yet fully held fixed.

Then the part that needed no statistics. Asked **why** they felt bored, children chose "I don't find
this topic interesting" (14.1 percent), "This is too easy" (13.8 percent), and "I'm not sure why I
need to know this" (12.3 percent). Asked why they felt frustrated, they chose "I don't know what to
do next" (14.9 percent), "This is too hard" (11.8 percent), and "The game isn't working properly"
(9.2 percent). Those answers point at the content and the pitch rather than at the child, and here
the course is not inferring that from behavior: the children selected it. A three-row table records
what the menu can and cannot establish.

**Your turn 3.** Compare any two of the six feeling words. The optional solution runs all six at
once: raw gaps of +10.47, +10.24, +6.61, +4.85, +3.93, and +2.03, all of which collapse into the
range -0.39 to +1.03 once the number of answers is held fixed. The ordering of the raw column is the
ordering of "mean answers given" and has nothing to do with what the words mean.

**6. The second game, and the disagreement.** WAVES has a sharper spike: level 9 costs a mean of
**17.29** fails against 1.31 to 5.65 for every level before it, about 3.1 times the worst of them.
It also has a denominator trap, because level 9 is optional. Averaged over the 1,041 sessions that
met it the answer is 17.29; averaged over all 1,581 it is 11.38. Both are correct and they answer
different questions.

Then the structural fact that decides the section: **100.0 percent** of the sessions that began
level 9 went on to begin level 10. In WAVES the game moves you on. In AQUALAB the child decides, and
at `coral-hunting-lions` there was no next completed job 66.0 percent of the time against 21.9
percent across all job rows.

The replication gives **+0.85** levels [+0.13, +1.60] out of 25, rho = **+0.055**, with failure
quartiles averaging 14.09, 14.67, 14.92, and 15.00. Same direction, negligible size. A rank-based
common scale then puts all three answers side by side with intervals: **0.749** [0.709, 0.787] in
AQUALAB across everyone who attempted the job, **0.454** [0.307, 0.606] among those who completed at
least one more job, **0.531** [0.496, 0.567] in WAVES. The notebook leaves the disagreement
unresolved on purpose, offers one mechanism, and then names three rival explanations that the two
files cannot separate.

**Section 6.1** is a further trap, and it is free. WAVES ships `pre`, `post`, and `gain`. `pre` is
two questions, `post` is two **different** questions, and mean `gain` is **-0.42** with 45.9 percent
of sessions below zero. The sentence "playing WAVES made children worse at waves" is available and
arithmetically correct, and it is more than these four items can support.

**Your turn 4.** Try the other optional levels. The optional solution runs all four (9, 17, 29, 32)
split at each level's own median, and shows both that the two denominators diverge by a factor
running 1.5, 2.5, 8.3, 9.8 as the levels get rarer, and that all four persistence intervals contain
zero.

**7. These are children.** The demographic items settle what kind of data this is, read with their
denominator attached: of the 6,092 player-months that answered, 86.5 percent selected a band at 15
or younger, the largest group selected 12 to 13, and 79.4 percent said they were playing at school.
The section then says plainly what changes when the user is eleven: who consented and who was
logged, that "voluntary use" does not survive a class period, that the affect item is the most
intimate data in this course, and that a child who stops playing is not deficient. The last point is
the one section 5 shows rather than asserts.

**Reflection.** Five prompts tied to this week's readings, ending with the one worth answering:
rewrite one of your own design proposals for an eleven year old. Plus two suggested questions for
the guest, both drawn from something you have just done.

**Wrapping up.** A checklist for your own use, plus the reminder that the literature review and AI
log go to Canvas separately.

**Going further (optional).** Worked solutions to all four Your turn cells: the concentration of all
51 common jobs, a seven-point threshold sweep with the confound plotted beside the finding, all six
feeling words before and after the exposure control, and all four optional WAVES levels. Nothing in
this section is needed for the main path.

## Assessment

**Nothing from this notebook is collected.** Week 10 is not a mini project; those were weeks 4, 5,
6, and 8. This lab carries no rubric and no Canvas upload of its own, and coding skill is not what
the course assesses.

What **is** graded this week is the **Course Research Project Literature Review**, submitted
separately to Canvas by **11:59 PM on Sunday, November 1, 2026**, together with the **AI
Reflection** submission that accompanies every project milestone. See `Week 10 Literature Review
Guidelines` in the course materials for scope, structure, the difference between synthesis and
summary, and the common pitfalls.

## Connections to this week's readings

The required readings are Reardon, Kumar, and Revelle (2022), D'Mello and Jensen (2022), and Kim,
Knowles, Scianna, Lin, and Ruipérez-Valiente (2023). The notebook draws on them briefly at four
points:

- **Reardon, Kumar, and Revelle (2022)**, *Game learning analytics*: telemetry grain, and what games
  give learning analytics that a course platform cannot. Section 1 borrows their prior question
  about what a row is and whether the identifier attached to it is a person; section 4 borrows their
  question about what has to be true of a game's design before behavior in it can serve as evidence
  of learning rather than of activity.
- **D'Mello and Jensen (2022)**, *Emotional learning analytics*: affect as a dynamic state rather
  than a trait, and the trade-offs among asking, watching, and inferring. Section 5 works an item
  most respondents answered exactly once, which is its own lesson about what a dynamic analysis
  would require.
- **Kim, Knowles, Scianna, Lin, and Ruipérez-Valiente (2023)**, *Learning analytics application to
  examine validity and generalizability of game-based assessment for spatial reasoning*: whether a
  game measures what it claims to, and whether it holds beyond the sample it was built on. Section 6
  is a small version of the second question, and the answer does not hold.

## Going further, beyond the notebook

Optional extensions, for anyone whose project touches games, telemetry, or affect:

1. **Survival analysis of the record ending.** Section 4 uses a crude binary, "did the record
   continue." Treat each player-month's position in the job graph as a discrete-time survival
   process and estimate the hazard of the record ending at each job, handling right-censoring at the
   month boundary properly. Which job has the highest hazard once exposure is accounted for, and
   does `coral-hunting-lions` stay on top?
2. **The month boundary, directly.** Every AQUALAB extract is a calendar month, which truncates play
   arbitrarily. Restrict section 4 to player-months whose codename also appears in the following
   month's file, so that the record demonstrably continues past the boundary. How many player-months
   survive that restriction, what does it do to the +14.81, and what new selection problem have you
   just created?
3. **Non-response in the affect item.** 75.1 percent of player-months never answered. Model who
   answered as a function of the play measures, then reweight the section 5 comparison by the
   inverse of the estimated response probability. Report the reweighted gap beside the unweighted
   one, and say what assumption the reweighting requires and whether you believe it.
4. **The `argfails` column, unused here.** Section 3 built everything on `tries`. Repeat it on
   `argfails`, which counts failed arguments rather than attempts, and see whether the same job comes
   out hardest. Where the two disagree, work out which one a game designer would want.
5. **WAVES slider behavior.** The WAVES extract carries `PercentAmplitudeMoves`,
   `PercentOffsetMoves`, `PercentWavelengthMoves`, and slider ranges per level. Build a measure of
   strategy rather than effort (are the moves systematic or scattered?) and ask whether *that*
   predicts progress where sheer failure count did not. This is among the most promising unexplored
   material in either file.
6. **Two games, one model.** Fit the same specification to both games with the outcome standardized
   within game, and report the interaction between game and persistence with an interval. Then work
   through whether pooling two games with different logging, different children, and different
   session lengths into one model is defensible at all.
7. **The ethics of the intervention.** Design, in code, a detector that would flag a child in real
   time for the pattern section 4 found. Compute its false positive rate against the base rate. Then
   write the memo arguing that it should not be deployed, and see whether the memo persuades you.

## Troubleshooting

**"Could not download this week's data."**
You are offline, or a firewall is blocking `raw.githubusercontent.com`. Check your connection and
run the first code cell again. Nothing else in the notebook can run until it succeeds. That
repository is public, so this is never about a GitHub account or an invitation.

**"NameError: name 'jobs' is not defined" or something similar.**
A cell ran out of order, or the runtime restarted. Use **Runtime > Restart session and run all** in Colab,
or **Kernel > Restart & Run All** in Jupyter. This resolves most notebook problems.

**The download is slow.**
The three files are a few megabytes compressed. On a poor connection this can take a minute. It
happens once per session.

**My charts do not appear.**
Check that you ran the first code cell, which begins with `%matplotlib inline`. Without it the
notebook can compute everything and show you nothing. If they still do not appear, restart and run
all.

**Colab says it cannot find the notebook, or shows a 404.**
You are most likely signed into a different Google account. Check the profile picture in the top
right corner, switch to the account you want, and open the link again.

**"One of those groups has fewer than 30 player-months," or "one persistence group is under 20
sessions."**
You moved a **Your turn** setting past the point where a comparison is meaningful. Those messages
are the cells declining to report a result computed on a handful of people. Loosen the setting and
run the cell again.

**My numbers do not match the ones in the text.**
If you changed a **Your turn** cell, that is expected and good. If you did not, restart and run all.
Every interval in this notebook is seeded (`SEED = 8100`), so a clean run reproduces the same
numbers every time. If the underlying files in the dataset repository were ever updated, the
notebook's numbers would move and the text would not; that is a real consequence of working from
live URLs and it is worth knowing about.

**A `SettingWithCopyWarning` or similar yellow text.**
Warnings are not errors. If the cell printed its output and drew its chart, it worked.

**Red text appeared.**
Python errors are wordy, and none of them means something has been damaged. The **last line** of the
error usually names the real problem. Please ask, and we will read it together.

## Documenting AI use

There is nothing to upload from **this notebook**. There is something to upload this week: your
**literature review**, and alongside it your **AI interaction log plus a short reflection**, in the
Canvas AI Reflection submission.

The course AI policy is straightforward. AI use is permitted in designated activities and is to be
documented. If an assistant helped you find sources, summarize a paper, tighten a paragraph, or
question your framing, log the exchange and write a few sentences on what it did for you and what
you verified yourself. The AI Reflection is required whether or not you used AI; if you used none,
saying so in the text box is a complete answer. Undisclosed use is an Honor Code violation.

If you used an AI assistant on this notebook as well, to explain a line of pandas or to check your
reading of a chart, it is worth saving that exchange now. It costs nothing today and is easier than
reconstructing it later.

## Data and ethics

Everything we touch this semester is real, and no notebook in this course generates a row.

This week's files hold play by real children, logged automatically as they played, and released
into the public domain by the lab that collected them so that others could learn from them without a
new cohort being recorded for every study. None of those children agreed to be a teaching example.
It is worth asking who could be harmed by a claim before making it, noticing when a metric reduces a
person to one number, and noticing which people are not in the file at all.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*

The data in this activity are real play logs from AQUALAB (*Wake: Tales from the Aqualab*) and
WAVES (*Wave Combinator*), collected and released into the public domain under CC0 1.0 by Field Day
Lab at the Wisconsin Center for Educational Research, University of Wisconsin-Madison.
https://opengamedata.fielddaylab.wisc.edu

Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab,
University of Wisconsin-Madison. Retrieved from https://opengamedata.fielddaylab.wisc.edu

Gagnon, D., & Swanson, L. (2023). Open Game Data: A technical infrastructure for open science with
educational games. In M. Haahr, A. Rojas-Salazar, & S. Göbel (Eds.), *Serious Games. JCSG 2023*
(Lecture Notes in Computer Science, Vol. 14309, pp. 3-19). Springer.
https://doi.org/10.1007/978-3-031-44751-8_1
