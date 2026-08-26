# Week 9: Collaboration Analytics Lab

This is the hands-on session for Week 9. Together we will open a real chat export from eight student
groups, find out what the platform's clock could and could not record, measure how evenly each group's
messages were distributed, ask how much of that spread chance alone would produce, carry the same
question to a second dataset in a completely different setting, and finish by deciding what a
collaboration dashboard should refuse to show.

Coding experience is not assumed and is not what this session is about. Nothing here asks you to write
code from scratch. You run cells, read what comes out, and change a few clearly marked values to see
what those choices were doing to the result. Questions are welcome at any point, including questions
about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 9, Wednesday, October 21, 2026, Ridley Hall 137 |
| **Topic** | Learning Analytics for Understanding and Supporting Collaboration |
| **Notebook portion** | Approximately 4:50 to 5:50 PM, instructor guided, after the student-led discussion hour and the break |
| **Guest speaker** | None this week. The discussion hour is entirely student led. |
| **Notebook** | `week09_collaboration_analytics_lab.ipynb` |
| **Data** | **Real, published, openly licensed.** `collab-chat/chat_logs.csv` (1,374 chat messages, 8 groups of 4 or 5 undergraduates, four days in February 2021; CC BY 4.0) and the Week 6 JUSThink files `justhink/per_participant.csv` and `justhink/pehri_team_outcomes.csv` (78 children in 39 teams of two, 34 teams with an outcome row; CC BY 4.0). Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets` |
| **Citations** | Villa-Torrano, C. (2021). *Dataset on an online collaborative learning situation in a computer networks course* [Data set]. Zenodo. Norman, U., Dinkar, T., Nasir, J., Bruno, B., Clavel, C., & Dillenbourg, P. (2021). *JUSThink dialogue and actions corpus* [Data set]. Zenodo. Nasir, J., Norman, U., Bruno, B., Chetouani, M., & Dillenbourg, P. (2021). *PE-HRI: A multimodal dataset for the study of productive engagement in a robot mediated collaborative educational setting* [Data set]. Zenodo. |
| **Libraries** | pandas, numpy, matplotlib, scipy |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | None from this notebook. Nothing in it is collected and nothing in it is graded. |
| **Due** | The **Course Research Project Outline**, on Canvas, by 11:59 PM on Sunday, October 25, 2026, together with your AI interaction log and AI reflection. It is a separate submission from anything in this folder. |
| **Prior coding experience needed** | None |

Discussion Leadership runs in Weeks 2 through 11, and each of the four of you leads two of those
weeks. There is no guest speaker this week, so the full discussion hour belongs to this week's leader.

## What I hope you leave with

1. A way of opening a real, messy export, naming each cleaning decision, and saying what the decision
   costs.
2. A way of noticing when a measure is reporting the instrument's resolution rather than anyone's
   behaviour, and of retiring the measure rather than reporting it with a caveat.
3. The unevenness of a group's recorded participation, read against both its ceiling of (n - 1) / n
   and against what chance alone would produce at that group size and volume.
4. A precise account of why eight groups, two sittings each, will not support a group-level
   significance claim, and of what nesting does to any interval we might print.
5. An argument, with evidence from two settings, about what a collaboration dashboard should refuse to
   display, and to whom.

None of these is a coding objective.

The through-line of the session: Week 6 measured collaboration with one set of instruments and found
something. This week we point a different instrument at a different setting, then ask the question
that matters for anything anyone would build. **Does the finding travel?** The parts that do not
travel are not noise, and they are what the design question at the end is about.

## What is in this folder

| File | What it is |
|---|---|
| `week09_collaboration_analytics_lab.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is nothing to download by hand and nothing to upload. The first code cell fetches three files
over plain HTTPS and prints what arrived: 1,374 chat messages by 4 columns, 78 children by 12, and 34
team outcome rows by 6. If the download fails, the cell prints a plain-English message naming the
repository it was trying to reach rather than a long error trace.

## Opening it in Colab

This repository is public, so you need only a Google account and a browser. There is nothing to accept
or authorize.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week09-collaboration-analytics-lab/week09_collaboration_analytics_lab.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week09-collaboration-analytics-lab/week09_collaboration_analytics_lab.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`, and select
`week09-collaboration-analytics-lab/week09_collaboration_analytics_lab.ipynb`.

The notebook opens. Run the first code cell to begin.

You can also run it locally with Jupyter. It needs pandas, numpy, matplotlib and scipy, all of which
ship with Anaconda, plus an internet connection for the three CSV files.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Nothing is lost if you forget:
the datasets are fixed published files and the simulations are seeded, so re-running the notebook from
the top reproduces the same numbers on any machine. Your Section 6 specification is worth keeping.
Week 11's co-design studio starts from that kind of artifact.

## Walkthrough

We will move through this together in class. The timings below are a rough guide rather than a target,
and it is fine if we spend longer somewhere and skip something else. The five **Your turn** cells
already contain working values, so the notebook runs start to finish without anyone typing anything.

| Step | Section | Minutes | What happens |
|---|---|---|---|
| 1 | Setup | 2 | One cell: the imports, a colourblind safe palette, and a loader that fetches three CSVs and, if the network is down, says so in plain English. |
| 2 | 1. The file as it arrived | 8 | Three ordinary problems, each shown going wrong before it goes right, then the inventory and the four cleaning decisions with their costs. |
| 3 | Your turn 1: read one session | 3 | The opening of any session, with authors relabelled `P1` to `P5` within that session, ordered by message count. |
| 4 | 2. The clock the platform kept | 8 | What resolution the platform's timestamps have, the latency tile computed anyway, and the decision to retire it. |
| 5 | Your turn 2: where one stretch of talk ends | 3 | Change the idle rule from 2 minutes to 1 and to 5, and watch the count of stretches move. |
| 6 | 3. Who the log recorded, and how evenly | 7 | The Gini coefficient, its ceiling of (n - 1) / n, and the stacked bar of each group's shares. |
| 7 | 4. Chance, the group, and the day | 10 | Two null models side by side, each group's two sittings, and what eight units do to an interval. |
| 8 | Your turn 3: what counts as a contribution | 3 | Characters and words instead of messages. |
| 9 | 5. Does any of this travel? | 10 | The Week 6 children again, the dyad ceiling of 0.5, the missingness report, and three wide intervals. |
| 10 | 6. The design question | 6 | Ten tiles, four possible audiences each, a hazard review, and one written refusal. |

**Going further (optional)** is a clearly marked section at the end, followed by an appendix with one
worked answer for each **Your turn** cell. Neither is part of the class time and nobody needs to work
through them today.

## The figures we will make

1. **Every recorded chat session on a clock.** Groups 1 and 2 in the afternoon of 15 and 17 February,
   Groups 3 to 8 after ten at night on 16 and 18 February, sessions running 13 to 35 minutes with a
   median of 17.5. The file does not say why the two blocks of groups sit at different hours.
2. **What the platform's clock could see.** 80.3 percent of consecutive within-session gaps are
   recorded as exactly 0 seconds, every gap is a whole number of minutes, and each occupied minute
   holds 4.9 messages on average and 22 at the busiest.
3. **Who the chat log recorded.** Each group's messages divided among its members, with a tick marking
   where an even split would fall. Group 6's segments sit close to those ticks; Group 8's most
   recorded member holds 44 percent of 106 messages, which is 2.22 times an even share, against 1.18
   times for Group 1.
4. **Unevenness against the ceiling, against chance, and against the same group's other day.** Every
   group sits well below its ceiling. Two sit inside their own chance floor. Group 7's two sittings
   read 0.064 and 0.446.
5. **Message volume against unevenness, with the chance floor drawn in.** The floor falls as volume
   rises, which is why the notebook draws it rather than subtracting it.
6. **Two settings, three channels, one measure.** The busiest member's share as a multiple of an even
   split, for the chat groups and for both JUSThink channels, each with its own chance floor.
7. **What the second setting can and cannot settle.** Action unevenness against learning gain across
   34 teams, and action unevenness against speech unevenness across the 10 teams that have both.

## What the analysis shows, and what it does not

The notebook keeps three things apart at each step, and it may be useful to have the central case in
front of you before class.

| | |
|---|---|
| **What the data directly show** | 1,333 of the 1,374 messages (97.0 percent) share a minute stamp with another message in the same session; every recorded gap is a whole number of minutes; the smallest non-zero gap in the file is 60 seconds; the median seconds until a different person posts is 0.0 in 16 of 16 sessions |
| **A plausible interpretation** | The platform rounded its timestamps to the minute, so intervals shorter than a minute were never written down |
| **What this file cannot establish** | How quickly anybody actually replied, and whether any two of these groups differed in responsiveness at all |

That is why the notebook retires the latency tile rather than reporting it with a caveat. What the
decision costs is stated too: no responsiveness measure, no uptake speed, and no burst structure finer
than a minute. What survives is co-presence at minute grain, with 222 of 283 occupied minutes (78.4
percent) holding two or more writers, printed with counts beside every rate.

The same discipline applies to the group comparison. Gini runs from 0.092 (Group 6) to 0.306 (Group
8), a ratio of 3.32, and the eight groups have four or five members each, so group size on its own
does not account for the spread. What the measure records is the unevenness of *recorded messages*,
which is not the same as participation: this extract holds the chat and not the shared document, and
with no roster a student who never typed is missing from the denominator, so every number is a lower
bound.

Three questions come before that spread counts as a finding.

**Chance.** Twenty thousand simulated draws per group give each group its own floor, and the floor is
neither zero nor constant. The obvious null treats each of the 1,374 messages as an independent draw,
and that null is too generous, because people type in runs: the file's 1,374 messages arrive in 982
runs, averaging 1.40 messages and reaching 7. Independent draws are smoother than bursty ones, so that
null puts the floor too low. The burst-preserving floor, which resamples **turns** with run lengths
drawn from that group's own runs, sits about 35 percent higher than the naive one on average and
nearly half again as high for Group 8: 0.077 for Group 5 with 260 messages, and 0.143 for Group 8 with
106 messages and five members, against 0.053 and 0.098 naive. Six of the eight groups are more uneven
than 95 percent of their own simulations, and Groups 1 and 6 are not distinguishable from chance at
all. The verdict is the same under either null. The distances are not, which is the transferable
lesson: a distance from a floor is only as good as the floor. The two rankings also disagree at the
top, since the most uneven group by raw Gini is Group 8 while the most uneven above its own floor is
Group 5.

**The day.** Every group was recorded twice, and the figure plots both sittings beside the pooled
value. Group 7 reads 0.064 on one day and 0.446 on the other, a swing of 0.382, which is larger than
the entire spread of 0.214 across all eight groups. A dashboard labelling a group after one session is
labelling a single sitting. The notebook leaves both readings of that swing open: the measure may be
noisy at this sample size, or groups may genuinely reorganise between sittings.

**The units.** The nesting is written out: 1,374 messages inside 34 people inside 8 groups, each seen
twice. Group-level claims have eight units. The section then asks whether groups that send more
messages spread them more evenly, and answers with the interval rather than the estimate: Spearman
+0.26 with a bootstrap interval of [-0.59, +1.00] over 4,000 resamples of the eight groups. "This file
cannot tell" is presented as a complete answer.

**Your turn 3** offers a check on the measure itself. Ranking the eight groups by characters typed
agrees with ranking them by messages sent at Spearman +0.929, and words agrees at the same level. The
notebook declines to read that as reassurance: both measures count typing, 28.5 percent of messages
are two words or fewer, and neither measure sees the student who solved the problem on a voice call.

## Does it travel?

Everything above describes eight groups of undergraduates typing Spanish in February 2021. Section 5
changes almost every variable at once and looks again at the Week 6 children: 78 of them, in 39 teams
of two, with a robot, in a different country, language, medium and age band. The dyad ceiling is 0.5,
which is why the cross-setting comparison uses the busiest member's share as a multiple of an even
split, defined identically at any group size, with the chance floor drawn beside each strip.

Two honesty notes travel with that figure. The chat floor keeps the burst structure; the two JUSThink
floors cannot, because those files record totals and not sequences, so they are lower bounds and the
gap above them is an upper bound. And the speech floor is computed on speaking **turns** while the
plotted statistic is a share of **seconds**, which pushes the same way, since seconds arrive in
unequal lumps.

The notebook is explicit that this is an exercise in reading a recorded difference between two
settings cautiously. The two settings differ in country, language, age band, medium, group size, task
and instrument all at once, so a gap between them is in the first instance evidence about the
recording conditions rather than about either set of people. "University students collaborate less
evenly than children" is named in the notebook as a claim these data do not support.

Missingness is reported rather than absorbed: 34 of the 39 teams have an outcome row, teams 11, 33,
34, 35 and 36 do not, 10 teams have speech, and 9 have both. A cross-file check confirms that
`T_LG_absolute` equals the pair's mean test change divided by 10 to within 0.000000, which is one way
to learn what a derived column actually means. Base rates come before any comparison: pre-test mean
5.85 of 10, post-test 5.95, with 17 teams rising, 8 unchanged and 14 falling.

Then the question the chat data cannot ask, because it records no outcome at all. Across 34 teams,
unevenness of interface actions against absolute learning gain gives Spearman -0.008 with an interval
of [-0.37, +0.36]; against final task error, -0.183 with [-0.50, +0.18]. Across the 10 teams with both
channels, action unevenness against speech unevenness gives -0.200 with [-0.80, +0.63]. The notebook
holds apart "the channels disagree" and "ten teams cannot tell us whether they agree." Three
comparisons are reported as three, not as the best of three.

## The design question

**Your turn 4** offers ten tiles and four possible audiences each: `teacher`, `group`, `student`,
`nobody`. You assign every tile and the cell checks your specification against hazards drawn only from
what this notebook found, then prints a review. Changing at least three of the defaults, and being
ready to say why, is the useful version of the exercise. The principle underneath: a measure may be
shown to an audience only if that audience can act on it in a way that helps, and only if being wrong
about a person costs less than staying silent.

**Your turn 5** then asks for one sentence, written out: what should this dashboard refuse to show, to
whom, and who decided. The appendix shows one worked refusal and names the test it has to pass, which
is that every clause of the "because" describes the instrument rather than a student.

The closing question is the one worth bringing to the discussion leader: **what should a collaboration
dashboard refuse to show, and to whom?**

## Going further (optional)

The notebook ends with a clearly marked optional section for anyone who wants to keep going after
class. None of it is required and none of it is graded. It includes recomputing every Gini under one
and then two assumed silent members, building a minute-grain co-presence graph and comparing it
against a shuffle, repeating the character-count comparison at the level of the individual, treating
all 16 sessions as the unit, fitting a random intercept model and reporting the instability of the
intraclass correlation, rebuilding the sessions with an idle rule instead of a group-day rule, and
downloading the full Villa-Torrano release, which also holds document edit logs, Moodle logs and
questionnaires for these same students.

An appendix after that gives one worked answer for each of the five **Your turn** cells.

## Troubleshooting

**"Could not download: collab-chat/chat_logs.csv"**
The runtime could not reach the internet. The files live at `github.com/HakeoungLee/edis8100-datasets`,
which is public, so this is never about a GitHub account or an invitation. Run the cell again, since
brief network failures are common, then check that address in a browser tab. Nothing else in the
notebook works until that cell prints "All three files loaded."

**"NameError: name 'groups' is not defined"**
A cell ran out of order, or the runtime restarted. `groups` is built in Section 3, and Sections 4 and
5 both need it. **Runtime > Restart session and run all** in Colab, or **Kernel > Restart & Run All**
in Jupyter, then wait for every cell to finish. This resolves most notebook problems.

**"KeyError: 'timestamp'"**
The file is being read without `encoding="utf-8-sig"` on a pandas version that does not strip the byte
order mark, or with `latin-1`. Section 1 shows exactly this happening on purpose.

**"ValueError: time data ... does not match format"**
The date format string has changed. The file is day first: `%d/%m/%Y %H:%M`.

**My charts do not appear**
The first line of the first code cell is `%matplotlib inline`. If that cell did not run, no figure
renders. Restart session and run all.

**Your turn 1 prints nothing**
The group and day do not go together. Groups 1 and 2 met on `2021-02-15` and `2021-02-17`. Groups 3 to
8 met on `2021-02-16` and `2021-02-18`. The dates are strings in quotes.

**The messages are in Spanish and I do not read Spanish**
That is expected, and it is the honest cost of using this dataset. Every measure in the notebook is
built from metadata: who wrote, when, and how much. Nothing asks you to interpret content. The
notebook says plainly that giving up content is a large thing to give up in a week about
collaboration.

**My numbers do not match the ones in the text**
If you changed a **Your turn** cell, that is expected and useful. If you did not, restart and run all.
The simulations and bootstraps are seeded, so a clean run reproduces the same numbers every time.

**The design review flagged fewer tiles than I expected**
The line underneath is the important one: the hazard list holds only the problems this notebook
happened to surface, from eight groups over four days. A clean review is not the same as a safe
dashboard, and treating it as one is the failure mode Section 6 is about.

**My refusal list is completely different from my neighbour's**
There is no answer key in Section 6, only better and worse arguments. Comparing the principles you
each used, rather than the slots you each chose, is a useful thing to do.

**Red text appeared**
Python errors are wordy, and none of them means something has been damaged. The **last line** of the
error usually names the real problem. Please ask, and we will read it together.

## Documenting AI use

This notebook is not a graded submission, but something is due this week: the **Course Research
Project Outline**, uploaded to Canvas by 11:59 PM on Sunday, October 25, 2026, separately from
anything in this folder.

If you used an AI assistant while drafting that outline, or while working through this notebook, the
course AI policy asks for two things, and they go in two different places in the **AI Reflection**
submission on Canvas:

- **The conversation record goes in a Word file, attached to the submission.** The full exchange,
  across every tool and every session, pasted in rather than summarized.
- **The reflection goes in the Canvas text box**, where you copy in the four questions from the
  syllabus and answer each one: how you used it; whether it helped and how; whether it made your work
  more challenging in any way; and what lesson about AI you would pass on to a friend or the class.

If you used no AI at all, one line in the text box saying so is a complete and acceptable submission.
AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code
violation.

## Connections to this week's readings

The required readings are Chen and Teasley (2022), Praharaj, Scheffel, Drachsler and Specht (2021),
and Martinez-Maldonado, Kay, Buckingham Shum and Yacef (2019). Cohn and colleagues (2025) and
Schneider and colleagues (2018) are additional. The notebook draws on the three required readings
briefly at a few points, and the reflection returns to them:

- **Chen and Teasley (2022)**, *Learning analytics for understanding and supporting collaboration*,
  argue that indicators of collaboration should be anchored in a construct of collaboration quality
  rather than in whatever a platform happens to log. This notebook runs that argument backwards on
  purpose, taking the sensor it was handed and asking which construct survives it. They also treat
  understanding collaboration and supporting it as two connected but distinct tasks, which is the
  question Section 6 puts to every tile.
- **Praharaj, Scheffel, Drachsler, and Specht (2021)**, *Literature review on co-located collaboration
  modeling using multimodal learning analytics: Can we go the whole nine yards?*, review the chain
  from sensing through analysis to feedback and report how rarely published work carries it all the
  way through. Here the chain breaks at the first link for one measure and holds for another. Note
  also which channel turned out to be affordable: in the JUSThink data the interface log is complete
  for all 39 teams and unrelated to the outcome, while the speech transcript exists for 10 teams and
  cannot be evaluated at that size.
- **Martinez-Maldonado, Kay, Buckingham Shum, and Yacef (2019)**, *Collocated collaboration analytics:
  Principles and dilemmas for mining multimodal interaction data*, set out the dilemmas that Section 6
  makes concrete. You resolve one per tile, ten times, and write down who sees the result. The
  sharpest one this year is the roster: the notebook's participation shares have a denominator that
  cannot be observed, and a tile displaying them to a group presents a lower bound as if it were a
  fact about people.

## Data and ethics

Everything we touch this semester is real. Nothing here was collected by this course, and no notebook
in this course generates a row. Both datasets are redistributed under the licence their authors chose,
and both citations belong in your reference manager the moment you use anything from them.

**Villa-Torrano (2021), `collab-chat/chat_logs.csv`, CC BY 4.0.** 1,374 messages, four columns, from
undergraduates in a computer networks course working through Moodle and a platform called CoTrackV2.
Eight groups of four or five, each recorded on two days between 15 and 18 February 2021, online, in
Spanish. Semicolon delimited, UTF-8 with a byte order mark, day-first dates.

> Villa-Torrano, C. (2021). *Dataset on an online collaborative learning situation in a computer
> networks course* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5150537

**JUSThink and PE-HRI (2021), `justhink/`, CC BY 4.0.** The Week 6 children: 78 nine to twelve year
olds in 39 teams of two, building a minimum spanning tree with a robot in the room. Interface actions
for all 78, speech for 20 of them, team level learning outcomes for 34 of the 39 teams.

> Norman, U., Dinkar, T., Nasir, J., Bruno, B., Clavel, C., & Dillenbourg, P. (2021). *JUSThink
> dialogue and actions corpus* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4627104
>
> Nasir, J., Norman, U., Bruno, B., Chetouani, M., & Dillenbourg, P. (2021). *PE-HRI: A multimodal
> dataset for the study of productive engagement in a robot mediated collaborative educational
> setting* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4633092

Neither dataset carries a name, an age band for the chat students, a gender, a language background, a
prior grade, or, in the chat data, any measure at all of what a group produced. Those absences shape
the whole week, and the notebook names each one where it bites rather than working around it quietly.

None of these students or children agreed to be a teaching example. It is worth asking who could be
harmed by a claim before making it, noticing when a metric reduces a person to one number, and
noticing which people are not in the file at all. That stance runs through every week of the course.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*
