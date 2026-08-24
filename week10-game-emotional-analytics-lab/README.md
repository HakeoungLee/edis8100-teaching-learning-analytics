# Week 10: Game and Emotional Analytics Lab

Two real games, sixteen thousand children's codenames, and the week a finding fails to travel from one game to the next.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, November 4, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Game Learning Analytics and Emotional Learning Analytics |
| **Guest speaker** | Chaewon Kim, Florida State University |
| **In-class time on this notebook** | About 20 minutes, launched in the hands-on studio block (4:40 to 5:00). The full core path runs about 55 minutes, so plan to finish sections 5, 6, and 7 on your own before the discussion. |
| **Deliverable from this notebook** | None. Week 10 is not a mini project. This lab is an in-class launch. |
| **Due this week (separately)** | **Course Research Project Literature Review** plus your **AI interaction log and reflection**, uploaded to Canvas. Submitted on their own, not from this notebook. |
| **Notebook** | `week10_game_emotional_analytics_lab.ipynb` |
| **Data used** | **Open Game Data**, Field Day Lab, University of Wisconsin-Madison. `fieldday-aqualab/players.csv.gz` (19,031 rows by 145 columns), `fieldday-aqualab/player_jobs.csv.gz` (96,322 by 11), `fieldday-waves/sessions.csv.gz` (1,581 by 870). Public domain, **CC0 1.0**. Downloaded by the notebook, nothing to install. |
| **Libraries** | pandas, numpy, matplotlib. Nothing else this week, and every statistic is built from those three in front of the student. |
| **Runtime** | About 15 seconds end to end on a normal connection. |

This is the **only week that uses the Field Day data**, and the only week whose learners are children. Sections 1 and 2 of the notebook establish what one row is and what is wrong with the files before any analysis begins, so do not skip them.

## The data

| | |
|---|---|
| **What** | Play logs from two educational games: **AQUALAB** (*Wake: Tales from the Aqualab*), a marine-science adventure in which players run experiments and then argue for a conclusion from evidence, and **WAVES** (*Wave Combinator*), a 35-level signal-matching puzzle |
| **Who collected it** | **Field Day Lab**, Wisconsin Center for Educational Research, **University of Wisconsin-Madison**, through their Open Game Data infrastructure |
| **Who is in it** | Children. Of the 6,092 player-months that answered the in-game age item, 86.5 percent said they were 15 or younger and the largest single group said 12 to 13; 79.4 percent of those who answered said they were playing at school |
| **When** | Ten monthly AQUALAB extracts, September 2025 through June 2026, plus a set of individual WAVES sessions |
| **Licence** | **CC0 1.0 Universal**, the Creative Commons public domain dedication. No rights reserved, no permission needed, no attribution legally required |
| **Citation** | For the data, the form Field Day's own per-game readme asks for: Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab, University of Wisconsin-Madison. Retrieved from https://opengamedata.fielddaylab.wisc.edu <br> For the infrastructure, the paper the site names: Gagnon, D., & Swanson, L. (2023). Open Game Data: A technical infrastructure for open science with educational games. In M. Haahr, A. Rojas-Salazar, & S. Göbel (Eds.), *Serious Games. JCSG 2023* (Lecture Notes in Computer Science, Vol. 14309, pp. 3-19). Springer. https://doi.org/10.1007/978-3-031-44751-8_1 |
| **Source** | Field Day Lab, University of Wisconsin-Madison. https://opengamedata.fielddaylab.wisc.edu |
| **This extract** | Course-sized subsets, redistributed unchanged, at github.com/HakeoungLee/edis8100-datasets |

CC0 means the class is legally free to do anything with these files. The notebook spends a section on why that makes the ethical question louder rather than quieter, given who is in them.

## Objectives

By the end of this activity you will be able to:

1. **State where a dataset came from** before analysing it: who logged it, from whom, under what licence, and what the file cannot see.
2. **Find and repair the mess in a real telemetry extract**, meaning columns that hold one value, a category that is not an activity, durations that run backwards, rows with no player at all, and answers in two languages, and say out loud what each repair costs.
3. **Summarise a heavily skewed count honestly**, and explain why the mean is the wrong number for the hardest job in AQUALAB and the median is not obviously the right one either.
4. **Separate a selection question from an effect question** when the same event switches both variables on, and carry an interval that respects rows nested inside people.
5. **Read an in-game affect item** without treating a feeling word as a property of a child, and show that a difference between two feelings is really a difference in how much of the game each child saw.
6. **Attempt a replication in a second game**, put both answers on one scale, and report honestly that they disagree.

The through-line of the session: **the same question, asked of two games, gets two answers, and neither of them was planted.** In AQUALAB, children who argued more than ten times at the hardest job in the game completed 14.81 more jobs that month, interval [+12.24, +17.24]. Take that apart and 67.1 percent of the persisting group went on to attempt another job against 3.1 percent of the others, and among the children whose record demonstrably continued, argumentation tries and later completions are uncorrelated (rho = -0.007, n = 210). Carry the same question to WAVES, where the game supplies the next level whether or not you struggled, and the effect is +0.85 levels out of 25 (rho = +0.055). On one common scale the three answers are **0.749**, **0.454**, and **0.531**. The work is deciding which question each of them answers.

The second through-line, and the reason this week matters beyond method: **the learners are children.** Every design proposal you have made this semester assumed a consenting adult. The reflection section asks you to rewrite one of them for an eleven year old.

## What is in this folder

| File | What it is |
|---|---|
| `week10_game_emotional_analytics_lab.ipynb` | The notebook. It downloads its three data files from the course dataset repository on first run and writes nothing to your machine. |
| `README.md` | This file. |

Nothing to clone and no CSV to fetch by hand. The first code cell reads three compressed files over the internet, a few megabytes in total, in a couple of seconds. If the download fails it prints a plain sentence naming `github.com/HakeoungLee/edis8100-datasets` rather than a wall of red text.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week10-game-emotional-analytics-lab/week10_game_emotional_analytics_lab.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week10-game-emotional-analytics-lab/week10_game_emotional_analytics_lab.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week10-game-emotional-analytics-lab/week10_game_emotional_analytics_lab.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda, plus an internet connection for the three files.

## Step-by-step walkthrough

Total time is about 55 minutes if you keep moving, which is what the per-section budgets below add up to. The four **Your turn** cells already contain working answers, so the notebook runs start to finish without you typing anything.

**Setup (2 minutes).** One short code cell. It downloads three files and prints their shapes. Read the provenance table immediately after it: who logged this, from whom, under what licence, with what citation. The rule the course keeps repeating is that you should never analyse data whose origin you cannot state out loud.

**1. What is one row, and who is in it? (4 minutes).** The dataset repository calls `players.csv.gz` "one row per player." It is not. It is 19,031 rows over 16,384 codenames across ten monthly extracts, and 1,922 codenames appear in more than one month with no way to tell whether that is a child returning or a name collision. Two panels draw the shape. The section ends by naming the unit of analysis as the **player-month** and by explaining why every interval later in the notebook resamples codenames rather than rows.

**2. Real data is messy, and the mess is the lesson (7 minutes).** The cheapest check in data analysis, run first: how many distinct values does each column hold? It finds `attempted` (one value, `True`, in all 96,322 rows), `argtime` (one value, `0:00:00`, in all of them), and five `JobTriesInArgumentPerDifficulty` columns that are zero in all 19,031 rows. Then the pseudo-category `no-active-job` (10,340 rows, 10.7 percent), ten rows with no codename at all and hundreds of sessions each, thirteen values of `ExperimentalCondition` of which only four are production, 2,631 player-months with a negative duration (worst: about minus 3.27 million seconds), and an affect column carrying both English and Spanish.

Three exclusions follow, each with its own line in a costs table, and one consistency check that earns the right to use `priorcomplete` for temporal ordering later: the largest "completed before" count in a player-month equals that month's total in 100.0 percent of cases.

**3. The hardest thing in the game (5 minutes).** `coral-hunting-lions` averages **31.98** argumentation tries against a median of **8**, while the median job in AQUALAB has a median of 1. Two panels: mean against median for the ten hardest jobs, and the raw distribution with both lines drawn on it. 42.3 percent of the player-months that took this job logged zero tries and the busiest 5 percent supply 29.1 percent of them all. The prompt does not let students pick a winner between mean and median; it makes them say what is wrong with each.

**Your turn 1 (2 minutes).** Point the same three summaries at another job. The appendix solution then scores all 51 common jobs and shows the busiest 5 percent supply a **median of 37.4 percent** of a job's tries, with a floor of 20.5 percent. The skew is not a property of the hard job; it is a property of voluntary-play counts.

**4. Did persisting pay? Two questions that look like one (10 minutes).** The heart of the lab. The trap is named before any code runs: argumentation tries and jobs completed are both counts of activity, so some association is arithmetic rather than finding.

The headline arrives anyway and it is large. Children who argued more than ten times completed **32.76** jobs against **17.96**, gap **+14.81** [+12.24, +17.24], from a cluster bootstrap over the 508 codenames rather than the 617 rows. `priorcomplete` then splits that gap in time: only **+3.52** [+1.12, +5.90] was banked before the job, and **+11.29** [+9.67, +12.91] came after.

Then the boring question that dissolves it, asked precisely. **67.1 percent** of the persisting group completed at least one further job that month; **3.1 percent** of the others did. The rank correlation between tries and jobs-completed-afterwards is +0.654, and between tries and that flag it is +0.649, because they are nearly the same variable: they agree on 607 of the 617 rows. The notebook says so out loud rather than calling the flag "was the child still there", and then measures the limit: **64 percent** of the player-months the flag calls "no further completion" took other jobs at the same completion depth, so they attempted more and finished nothing more, and with no timestamps on job rows nothing can order them. The panel is a decomposition of the outcome, not an independent check on who was in the room. Among the **210** player-months that completed at least one more job, the correlation is **-0.007** and the four try-quartiles average 17.22, 17.75, 16.81, and 18.55 jobs afterwards. Flat.

The section states the honest conclusion in full, including that the two-group comparison inside the still-playing subset has only 10 player-months on one side and therefore cannot rule out a modest effect. The interpretation prompt puts the instrument, the setting, and the circumstances on the table before the child, by name and in that order.

**Your turn 2 (2 minutes).** Move the threshold. The appendix solution sweeps it from 1 to 80 and finds the raw gap correlates with the difference in "share still playing" at **r = 0.961** across thresholds. Stability across a sweep tells you the definition is not fragile. It tells you nothing about whether the thing you defined is what you think it is.

**5. What children said they felt (9 minutes).** AQUALAB interrupts children and asks what they are feeling and **why**. Three quarters of the file never answered; the median respondent answered exactly once.

The counterintuitive comparison the field likes: children who said "frustrated" and never "bored" completed **18.32** jobs, children who said "bored" and never "frustrated" completed **11.42**, gap **+6.89** [+5.26, +8.50]. Then the exposure control. The frustration group answered 3.66 prompts to the boredom group's 2.23 and played 14.6 median hours to their 3.4, and "frustrated" was said by only 9.2 percent of respondents, so a child who answers eight times has eight shots at a rare word. Hold the number of answers fixed and the four bands read 5.17 against 5.52, 12.79 against 13.32, 18.74 against 18.98, 30.16 against 32.48. The size-weighted gap falls from +6.89 to **+0.75** [+0.02, +1.44]. **Eighty-nine percent of the effect was how much of the game each child saw**, and the section is candid that the residue in the widest band is the same confound not yet fully held fixed.

Then the part that needed no statistics. Asked **why** they felt bored, children chose "I don't find this topic interesting" (14.1 percent), "This is too easy" (13.8 percent), and "I'm not sure why I need to know this" (12.3 percent). Asked why they felt frustrated, they chose "I don't know what to do next" (14.9 percent), "This is too hard" (11.8 percent), and "The game isn't working properly" (9.2 percent). Boredom here is a property of the game at least as much as of the player, and for once the course is not inferring that: the children said so.

**Your turn 3 (2 minutes).** Compare any two of the six feeling words. The appendix solution runs all six at once: raw gaps of +10.47, +10.24, +6.61, +4.85, +3.93, and +2.03, all of which collapse into the range -0.39 to +1.03 once the number of answers is held fixed. The ordering of the raw column is the ordering of "mean answers given" and has nothing to do with what the words mean.

**6. The second game, and the disagreement (8 minutes).** WAVES has a sharper spike: level 9 costs a mean of **17.29** fails against 1.31 to 5.65 for every level before it, about 3.1 times the worst of them. It also has a denominator trap, because level 9 is optional. Averaged over the 1,041 sessions that met it the answer is 17.29; averaged over all 1,581 it is 11.38. Both are correct and they answer different questions.

Then the structural fact that decides the section: **100.0 percent** of the sessions that began level 9 went on to begin level 10. In WAVES the game moves you on. In AQUALAB the child decides, and at `coral-hunting-lions` there was no next job 66.0 percent of the time against 21.9 percent across all job rows.

The replication gives **+0.85** levels [+0.13, +1.60] out of 25, rho = **+0.055**, with failure quartiles averaging 14.09, 14.67, 14.92, and 15.00. Same direction, negligible size. A rank-based common scale then puts all three answers side by side with intervals: **0.749** [0.709, 0.787] in AQUALAB across everyone who attempted the job, **0.454** [0.307, 0.606] among those still playing, **0.531** [0.496, 0.567] in WAVES. The notebook explicitly refuses to resolve the disagreement, offers a mechanism, and then names three rival explanations that the two files cannot separate.

**Section 6.4** is a free extra trap. WAVES ships `pre`, `post`, and `gain`. `pre` is two questions, `post` is two **different** questions, and mean `gain` is **-0.42** with 45.9 percent of sessions below zero. The sentence "playing WAVES made children worse at waves" is available, arithmetically correct, and false.

**Your turn 4 (2 minutes).** Try the other optional levels. The appendix solution runs all four (9, 17, 29, 32) split at each level's own median, and shows both that the two denominators diverge by a factor running 1.5, 2.5, 8.3, 9.8 as the levels get rarer, and that all four persistence intervals contain zero.

**7. These are children (2 minutes).** The demographic items in the file settle what kind of data this is: 86.5 percent of those who answered said 15 or younger, largest group 12 to 13, and 79.4 percent said they were playing at school. The section then says plainly what changes when the user is eleven: who consented and who was logged, that "voluntary use" does not survive a class period, that the affect item is the most intimate data in this course, and that a child who stops playing is not deficient. The final point is the one section 5 proved rather than asserted.

**Reflection.** Five prompts tied to this week's readings, ending with the one everybody answers: rewrite one of your own design proposals for an eleven year old. Plus two suggested questions for the guest, both drawn from something the student has just done.

**Before you leave.** A checklist, plus the reminder that the literature review and AI log go to Canvas separately.

**Appendix.** Worked solutions to all four Your turn cells: the skew of all 51 common jobs, a seven-point threshold sweep with the confound plotted beside the finding, all six feeling words before and after the exposure control, and all four optional WAVES levels.

## Assessment

**Week 10 is not a mini project.** The four mini projects were weeks 4, 5, 6, and 8, and this lab carries no rubric and no Canvas upload of its own. It counts toward **Weekly Participation (15 percent)** through your engagement in the studio block and the quality of the reflection answers you bring to the 5:00 discussion.

What **is** graded this week is the **Course Research Project Literature Review**, submitted separately to Canvas. See `Week 10 Literature Review Guidelines` in the course materials for scope, structure, synthesis versus summary, and the common pitfalls.

## What this connects to in the readings

- **Reardon, Kumar, and Revelle (2022)**, *Game learning analytics*: telemetry grain, and what games give learning analytics that a course platform cannot. This week the answer is complicated by the fact that the analysis nearly went wrong four separate times on data of exactly that grain.
- **D'Mello and Jensen (2022)**, *Emotional learning analytics*: affect as a dynamic state rather than a trait. Section 5 tests that with an item most respondents answered exactly once, which is its own lesson about what dynamic analysis requires.
- **Kim, Knowles, Scianna, Lin, and Ruiperez-Valiente (2023)**, *Learning analytics application to examine validity and generalizability of game-based assessment for spatial reasoning*: whether a game measures what it claims to, and whether it holds beyond the sample it was built on. Section 6 is a small version of exactly that study, and it does not hold.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Survival analysis of the record ending.** Section 4 uses a crude binary, "did the record continue." Treat each player-month's position in the job graph as a discrete-time survival process and estimate the hazard of the record ending at each job, handling right-censoring at the month boundary properly. Which job has the highest hazard once exposure is accounted for, and does `coral-hunting-lions` stay on top?
2. **The month boundary, directly.** Every AQUALAB extract is a calendar month, which truncates play arbitrarily. Restrict section 4 to player-months whose codename also appears in the following month's file, so that the record demonstrably continues past the boundary. How many player-months survive that restriction, what does it do to the +14.81, and what new selection problem have you just created?
3. **Non-response in the affect item.** 75.1 percent of player-months never answered. Model who answered as a function of the play measures, then reweight the section 5 comparison by the inverse of the estimated response probability. Report the reweighted gap beside the unweighted one, and say plainly what assumption the reweighting requires and whether you believe it.
4. **The `argfails` column, unused here.** Section 3 built everything on `tries`. Repeat it on `argfails`, which counts failed arguments rather than attempts, and see whether the same job comes out hardest. Where the two disagree, work out which one the game designer would want.
5. **WAVES slider behaviour.** The WAVES extract carries `PercentAmplitudeMoves`, `PercentOffsetMoves`, `PercentWavelengthMoves`, and slider ranges per level. Build a measure of strategy rather than effort (are the moves systematic or scattered?) and ask whether *that* predicts progress where sheer failure count did not. This is the most promising unexplored thing in either file.
6. **Two games, one model.** Fit the same specification to both games with the outcome standardized within game, and report the interaction between game and persistence with an interval. Then argue with yourself about whether pooling two games with different logging, different children, and different session lengths into one model is a defensible thing to do at all.
7. **The ethics of the intervention.** Design, in code, a detector that would flag a child in real time for the pattern section 4 found. Compute its false positive rate against the base rate. Then write the memo arguing that it should not be deployed, and see whether you believe your own memo.

## Troubleshooting

**"Could not download this week's data."** You are offline, or a firewall is blocking `raw.githubusercontent.com`. Check your connection and rerun the first code cell. Nothing else in the notebook can run until it succeeds.

**"NameError: name 'jobs' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**The download is slow.** The three files are a few megabytes compressed. On a poor connection this can take a minute. It only happens once per session.

**My charts do not appear.** Make sure you ran the first code cell, which begins with `%matplotlib inline`. Without it the notebook can compute everything and show you nothing. If they still do not appear, restart and run all.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**"One of those groups has fewer than 30 player-months."** or **"one persistence group is under 20 sessions."** You moved a Your turn setting past the point where a comparison is meaningful. Those messages are the cells protecting you from reporting a result computed on four people. Loosen the setting and rerun.

**My numbers do not match the ones in the text.** If you changed a **Your turn** cell, that is expected and good. If you did not, restart and run all. Every interval in this notebook is seeded (`SEED = 8100`), so a clean run reproduces the same numbers every time. If the underlying files in the dataset repository were ever updated, the notebook's numbers would move and the text would not; that is a real risk of working from live URLs and it is worth knowing about.

**A `SettingWithCopyWarning` or similar yellow text.** Warnings are not errors. If the cell printed its output and drew its chart, it worked.

## A reminder about documenting AI use

There is nothing to upload from **this notebook**. There is something to upload this week: your **literature review**, and alongside it your **AI interaction log plus a short reflection**, in the Canvas "AI Reflection" submission.

The course AI policy is straightforward. AI use is permitted in designated activities and must be documented. If an assistant helped you find sources, summarize a paper, tighten a paragraph, or argue with your framing, log the exchange and write a few sentences on what it did for you and what you verified yourself. Undisclosed use is an Honor Code violation.

If you used an AI assistant on this notebook as well, to explain a line of pandas or to check your reading of a chart, save that exchange now. It costs nothing today and it is much easier than reconstructing it later.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development

The data in this activity are real play logs from AQUALAB (*Wake: Tales from the Aqualab*) and WAVES (*Wave Combinator*), collected and released into the public domain under CC0 1.0 by Field Day Lab at the Wisconsin Center for Educational Research, University of Wisconsin-Madison. https://opengamedata.fielddaylab.wisc.edu

Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab, University of Wisconsin-Madison. Retrieved from https://opengamedata.fielddaylab.wisc.edu

Gagnon, D., & Swanson, L. (2023). Open Game Data: A technical infrastructure for open science with educational games. In M. Haahr, A. Rojas-Salazar, & S. Göbel (Eds.), *Serious Games. JCSG 2023* (Lecture Notes in Computer Science, Vol. 14309, pp. 3-19). Springer. https://doi.org/10.1007/978-3-031-44751-8_1
