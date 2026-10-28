# Week 10: Game and Emotional Learning Analytics

EDIS 8100, Teaching and Learning Analytics, Fall 2026. Wednesday, October 28, 2026, Ridley Hall 137.
Guest: Chaewon Kim, Southern Illinois University, for the final hour.

There is no in-class notebook block this week, because the guest holds the final hour. The notebook
is worked through outside class. Nothing from it is collected.

## The data

Play logs from two educational games released by Field Day Lab, Wisconsin Center for Educational
Research, University of Wisconsin-Madison, through its Open Game Data infrastructure. The players
are children. Public domain, CC0 1.0.

| File | One row is | Shape |
|---|---|---|
| `fieldday-aqualab/players.csv.gz` | one player in one month, 145 derived features | 19,031 x 145 |
| `fieldday-aqualab/player_jobs.csv.gz` | one player-month on one job attempted | 96,322 x 11 |
| `fieldday-waves/sessions.csv.gz` | one WAVES session, 870 features | 1,581 x 870 |

Field Day. (2019). *Open educational game play logs: AQUALAB and WAVES* [Data set]. Field Day Lab,
University of Wisconsin-Madison. https://opengamedata.fielddaylab.wisc.edu

Gagnon, D., & Swanson, L. (2023). Open Game Data: A technical infrastructure for open science with
educational games. In M. Haahr, A. Rojas-Salazar, & S. Gobel (Eds.), *Serious Games. JCSG 2023*
(LNCS Vol. 14309, pp. 3-19). Springer.

The notebook downloads all three files from `github.com/HakeoungLee/edis8100-datasets` on first
run and writes nothing to your machine. Libraries: pandas, numpy, matplotlib. Runtime under a
minute, most of it the download.

## The notebook

Each section opens with a figure and then reads it. Cells marked `TODO` already hold a working
value, so the notebook runs top to bottom without editing.

| Section | What it establishes |
|---|---|
| 1. The unit of analysis | A row of `players.csv` is one player in one month. 1,922 of 16,384 codenames appear in more than one monthly extract, and no column separates a returning child from a reused codename |
| 2. Problems in the raw files | Eight defects, found by checking distinct values per column: two columns holding one value, five holding zero, a category that is not a job, ten rows with no player, twelve condition strings, 2,631 negative durations, and a bilingual affect column. Three exclusions follow, with what each costs |
| 3. Distribution of argumentation tries | `coral-hunting-lions` has a mean of 31.98 tries against a median of 8. The busiest 5 percent of player-months supply 29.1 percent of the tries, and 42.3 percent logged zero |
| 4. Persistence at the hardest job | A raw gap of +14.81 completed jobs [+12.24, +17.24], of which the two groups' largest difference is whether any further job was completed at all, 67.1 percent against 3.1 percent. Holding that fixed, rho = -0.007 among the 210 player-months that kept playing |
| 5. The in-game affect item | A raw gap of +6.89 jobs between children who selected Frustrated and children who selected Bored. Holding the number of prompts answered fixed moves it to +0.75 [+0.02, +1.44]. The follow-up item has the boredom answers naming the topic and the difficulty setting |
| 6. The second game | WAVES has a sharper spike and a denominator that changes the answer, 17.29 fails against 11.38. The persistence comparison does not come back: 0.749 in AQUALAB, 0.531 in WAVES, on one rank scale. Section 6.1 takes apart the `pre`, `post` and `gain` columns |
| 7. Who is in the file | Of the 6,092 player-months answering the age item, 86.5 percent selected a band at 15 or younger and 79.4 percent selected School. Both items were answered by 32.1 percent of player-months |

Then seven questions and the reflection prompts on the three readings.

## This week's readings

- Reardon, Kumar, & Revelle (2022). Game learning analytics. In Lang et al. (Eds.), *Handbook of
  learning analytics* (2nd ed., pp. 152-162). SoLAR.
- D'Mello & Jensen (2022). Emotional learning analytics. In Lang et al. (Eds.), *Handbook of
  learning analytics* (2nd ed., pp. 120-129). SoLAR.
- Kim, Knowles, Scianna, Lin, & Ruiperez-Valiente (2023). Learning analytics application to examine
  validity and generalizability of game-based assessment for spatial reasoning. *British Journal of
  Educational Technology, 54*(1), 355-372.

## Opening it in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week10-game-emotional-analytics-lab/week10_game_emotional_analytics_lab.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week10-game-emotional-analytics-lab/week10_game_emotional_analytics_lab.ipynb`

**File > Save a copy in Drive** keeps a personal version. Every interval is seeded, so re-running
from the top reproduces the same numbers. If a cell behaves oddly, **Runtime > Restart session and
run all** resolves almost everything.

## What is due this week

Separately from this notebook, and submitted to Canvas:

- Course Research Project Literature Review, by 11:59 PM on Sunday, November 1, 2026.
- The AI interaction log in a Word file, plus the four reflection answers in the Canvas text box.
  Required whether or not AI was used.

## What is in this folder

| File | What it is |
|---|---|
| `week10_game_emotional_analytics_lab.ipynb` | The notebook |
| `README.md` | This file |
| `data/` | Three CSV files left from an earlier version of this activity. Nothing in the notebook reads them |
