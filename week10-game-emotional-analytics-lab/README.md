# 🎮 Week 10: Game and Emotional Analytics Lab

Two hundred middle schoolers, one fractions game, and the week the learners stop being adults.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, November 4, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Game Learning Analytics and Emotional Learning Analytics |
| **Guest speaker** | Chaewon Kim, Florida State University |
| **In-class time on this notebook** | About 20 minutes, launched in the hands-on studio block (4:40 to 5:00). The full core path runs about 30 minutes, so plan to finish sections 4 and 5 on your own before the discussion. |
| **Deliverable from this notebook** | None. Week 10 is not a mini project. This lab is an in-class launch. |
| **Due this week (separately)** | **Course Research Project Literature Review** plus your **AI interaction log and reflection**, uploaded to Canvas. Submitted on their own, not from this notebook. |
| **Notebook** | `week10_game_emotional_analytics_lab.ipynb` |
| **Data used** | `game_players.csv`, `game_telemetry.csv`, `game_emotion.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib. Nothing else this week. |

This is the **only week that uses the FractionQuest data**. Everything else this semester comes from EDUC 1010 at Blue Ridge University. Section 1 of the notebook orients you to the new setting before any analysis starts, so do not skip it.

## Objectives

By the end of this activity you will be able to:

1. **Build a learning curve** from attempt level game telemetry, and explain why the pooled version of that curve points the wrong way while the per-level version does not.
2. **Locate a difficulty cliff** using four independent signals (errors, retries, completion, time) and say what any one signal alone would have missed.
3. **Compare productive strugglers with fast finishers** on pre to post test gains, and separate the claim "this group gained less" from the claim "this group had less to gain."
4. **Read an emotion self report stream as a sequence** rather than as a frequency table, and state what confusion that resolves and confusion that persists each predict.

The through-line of the session: the counterintuitive result. The children who made more mistakes gained more on the fractions test, and the moment you adjust for how much room each child had above their pre-test score, the difference disappears. Both answers come from the same 95 children and the same code. Deciding which one you would put in an abstract is the work.

The second through-line, and the reason this week matters beyond method: **the learners are children.** Every design proposal you have made this semester assumed a consenting adult. The reflection section asks you to rewrite one of them for an eleven year old.

## What is in this folder

| File | What it is |
|---|---|
| `week10_game_emotional_analytics_lab.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the three FractionQuest datasets into the runtime.

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

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda.

## Step-by-step walkthrough

Total time is about 30 minutes if you keep moving. The four ✏️ **Your turn** cells already contain working answers, so the notebook runs start to finish without you typing anything.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the three synthetic FractionQuest files inside your runtime so that nothing has to be downloaded and no real child's play record is ever involved.

**📊 1. A new setting, and a new kind of learner (4 minutes).** Meet FractionQuest: 200 players in grades 6 and 7, eight levels, a 20 item pre-test and post-test, October 2026. Read the short section on why the learners being children changes the ethics of everything you have proposed so far. Then load the three files and count who is still playing at each level. The roster is 200 and only 81 reach level 8, which reframes every average that follows.

**📊 2. Learning curves, and the one that lies (6 minutes).** Three panels of the same 1,428 attempts. The pooled curve says errors go **up** with practice. The per-level curves say level 4 is in its own world. The rescaled curve says errors fall about 16 percent by the third try. All three are arithmetically correct, and the printed table above the figure shows exactly why the first one misleads: level 4 supplies 13 percent of first attempts and 36 percent of third attempts. This is the methodological spine of the session.

**✏️ Your turn 1 (2 minutes).** Swap `errors` for `time_s` or `hints_used` and check whether the same trap appears.

**📊 3. The difficulty cliff (5 minutes).** Four signals per level, in four panels. Errors at level 4 run 1.72 times the average of levels 3 and 5. Players need 1.73 attempts each instead of about 1.3. Half of all level 4 attempts fail. Attempts take nearly twice as long. Four measures that could have disagreed and did not.

**✏️ Your turn 2 (2 minutes).** Point the same neighbour comparison at any other level and see how much weaker the case gets.

**📊 4. Productive strugglers and fast finishers (8 minutes).** The heart of the lab. Two explicit design decisions (who is eligible, what window we measure) then two group definitions, then the outcome. Strugglers gain 4.17 points against 2.47 for the fast finishers, d = 0.69. Section 4.1 then draws the ceiling on a scatterplot and recomputes the gain as a share of available headroom: d = 0.01. Sit with both numbers. This is the teaching moment of the week.

**✏️ Your turn 3 (3 minutes).** Move all four thresholds and watch which of the two findings is stable and which is not.

**📊 5. Emotion pings (8 minutes).** Three moves. First, what children report level by level: at level 4, confusion jumps to 47 percent of pings and interest collapses from 49 to 27 percent. Second, six individual emotion streams drawn as lanes, so you can see what a frequency table deletes. Third, the sequence question: confusion resolved within two levels goes with a 3.78 point gain and a 34 percent quit rate, unresolved confusion goes with 2.71 points and 63 percent, and the children who quit at the confusing level are kept visible as their own group rather than quietly filed under "resolved."

**✏️ Your turn 4 (2 minutes).** Change the resolution window and watch a construct dissolve.

**💬 Reflection.** Five prompts tied to this week's readings, ending with the one everybody answers: rewrite one of your own design proposals for an eleven year old.

**✅ Before you leave.** A checklist, plus the reminder that the literature review and AI log go to Canvas separately.

**Appendix.** Worked solutions to all four ✏️ Your turn cells, including a 16 cell threshold sweep of the productive struggle finding and a window sweep of the confusion finding.

## Assessment

**Week 10 is not a mini project.** The four mini projects were weeks 4, 5, 6, and 8, and this lab carries no rubric and no Canvas upload of its own. It counts toward **Weekly Participation (15 percent)** through your engagement in the studio block and the quality of the reflection answers you bring to the 5:00 discussion.

What **is** graded this week is the **Course Research Project Literature Review**, submitted separately to Canvas. See `Week 10 Literature Review Guidelines` in the course materials for scope, structure, synthesis versus summary, and the common pitfalls.

## What this connects to in the readings

- **Reardon, Kumar, and Revelle (2022)**, *Game learning analytics*: learning curves, telemetry grain, and what games give learning analytics that a course platform cannot.
- **D'Mello and Jensen (2022)**, *Emotional learning analytics*: affect as a dynamic state rather than a trait, and why confusion that resolves is a different event from confusion that does not.
- **Kim, Knowles, Scianna, Lin, and Ruiperez-Valiente (2023)**, *Learning analytics application to examine validity and generalizability of game-based assessment for spatial reasoning*: whether a game measures what it claims to, and whether that holds beyond the sample it was built on.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Survival analysis of quitting.** Treat each player's last level as a right-censored survival time and estimate a discrete-time hazard of quitting at each level. Which level has the highest hazard once you account for the fact that fewer players are exposed later? Compare that answer to the raw attrition bar chart.
2. **A real learning curve model.** Fit errors as a function of cumulative practice opportunities with a power law or exponential form, one curve per level, and report the fitted learning rate. Then argue about whether "opportunity" should mean attempts at a level or attempts across the whole game.
3. **Condition on the cliff.** Restrict the entire section 4 analysis to what happened *at level 4 only*: errors, retries, and time on that level alone. Does the productive struggle finding get stronger or weaker when the measure is taken at the hardest moment rather than across four levels?
4. **Emotion transitions.** Build a transition matrix over the four emotion labels within player, in timestamp order, and compare the matrix for children who gained a lot against those who gained little. Which transition separates them most, and is that transition one you used to define the groups?
5. **A fairer gain measure.** Headroom gain and raw gain are two of several options. Implement a third (residual gain from a regression of post on pre, sometimes called a regression-adjusted gain) and compare all three on the same two groups. Write the paragraph explaining to a school district why the three disagree.
6. **The ethics of the intervention.** Design, in code, a detector that would flag a child for unresolved confusion in real time using only data available before level 5. Compute its false positive rate. Then write the memo arguing that it should not be deployed, and see whether you believe your own memo.

## Troubleshooting

**"NameError: name 'level_summary' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/game_telemetry.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up, run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the first code cell of section 1, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**"One of the groups has fewer than 5 players."** You tightened the thresholds in ✏️ Your turn 3 past the point where a comparison is meaningful. That message is the cell protecting you from reporting a d computed on three children. Loosen a threshold and rerun.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all: the data generator is seeded, so a clean run reproduces the same numbers every time.

**I got a different answer than my neighbor about who learned more.** Compare which gain measure you are each looking at. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload from **this notebook**. There is something to upload this week: your **literature review**, and alongside it your **AI interaction log plus a short reflection**, in the Canvas "AI Reflection" submission.

The course AI policy is straightforward. AI use is permitted in designated activities and must be documented. If an assistant helped you find sources, summarize a paper, tighten a paragraph, or argue with your framing, log the exchange and write a few sentences on what it did for you and what you verified yourself. Undisclosed use is an Honor Code violation.

If you used an AI assistant on this notebook as well, to explain a line of pandas or to check your reading of a chart, save that exchange now. It costs nothing today and it is much easier than reconstructing it later.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development

All data in this activity are synthetic. No child was measured to make it.
