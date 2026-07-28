# 🔍 Week 3: Ethics and Bias Audit

Auditing an at-risk model before anyone acts on it.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 9, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Responsible and Human-Centered Learning Analytics |
| **Guest speaker** | Hansol Lee, Stanford University |
| **In-class time on this notebook** | About 30 minutes, launched in the hands-on studio block (4:40 to 5:00). Finish the last two sections on your own if you run out of room. |
| **Deliverable** | None. Week 3 is an in-class launch, not a graded submission. |
| **Due date** | Not applicable. The first Canvas deliverable is Mini Project 1 in week 4. |
| **Notebook** | `week03_ethics_bias_audit.ipynb` |
| **Data used** | `students.csv`, `lms_clickstream.csv`, `gradebook.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn |

## Objectives

By the end of this activity you will be able to:

1. **Train** a simple at-risk prediction model on learning management system activity data, and read its accuracy honestly against a do-nothing baseline.
2. **Disaggregate** the model's errors by student group, computing false positive and false negative rates for first generation students and for students who work long hours.
3. **Explain**, with evidence from the data, how a model can be accurate overall and still be unfair, and point to the exact decision where the unfairness entered.
4. **Redesign** the feature set, re-run the same audit, and say what the redesign fixed and what it did not.

The through-line of the session: the algorithm was never the problem. A design decision about which columns to use was the problem, and design decisions have authors, so they can be revised.

## What is in this folder

| File | What it is |
|---|---|
| `week03_ethics_bias_audit.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the three datasets into the runtime.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and scikit-learn, all of which ship with Anaconda.

## Step-by-step walkthrough

Total time is about 30 minutes if you keep moving. The three ✏️ **Your turn** cells already contain working answers, so the notebook runs start to finish without you typing anything.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the synthetic roster, clickstream, and gradebook inside your runtime so that nothing has to be downloaded and no real student data is ever involved.

**📊 1. Build the table the model will see (4 minutes).** One row per student: who they are, what they clicked, how they scored. Meet the two features that carry the whole session, `total_events` (volume) and `active_days` (regularity). Notice that `at_risk` is defined by a threshold somebody chose.

**📊 2. Train the model and read the accuracy (5 minutes).** A logistic regression on four activity features, tested with five-fold cross validation so that no student is scored by a model that already saw them. The model gets about 74 percent accuracy. The rule "never flag anybody" gets 72 percent. Sit with that before you move on.

**📊 3. The audit (7 minutes).** Split the errors into false positives and false negatives, and compute both inside each group. This is where the notebook stops being a modeling exercise. The gap in the chart is large, and the model was never given the group membership that predicts it.

**📊 4. Where the gap came from (7 minutes).** Three panels comparing the 30 students who are first generation and work 15 or more hours a week against the other 90. Two panels are nearly identical. One is not. The scatterplot that follows shows the flags hugging the left edge of the chart rather than the bottom, which is the visual version of the same finding.

**✏️ Your turn 1: the caseload (2 minutes).** Change one number, the size of the advising office's outreach list, and watch what a staffing budget does to a fairness metric.

**📊 5. Redesign and re-audit (5 minutes).** Swap the feature set for prior GPA plus a couple of behavioral features, keep everything else identical, and run the same audit. The gap collapses and the accuracy goes up. Then read the caution that follows, because prior GPA is not innocent either.

**✏️ Your turn 2 and 3.** Choose your own feature set, then point the audit at a group nobody asked about.

**💬 Reflection.** Four prompts tied to this week's readings. Bring your answers to the 5:00 discussion block.

## What this connects to in the readings

- **Tsai and Martinez-Maldonado (2022)**, *Human-centered approaches to data-informed feedback*: the humans around the system are part of the system, including the ones who choose the features.
- **Holstein and Doroudi (2022)**, *Equity and artificial intelligence in education*: what a narrow fairness metric can and cannot see. Our audit equalizes one error rate across two attributes, which is not the same thing as equity.
- **Lee and Gargroetzi (2023)**, *"It's like a double-edged sword": Mentor perspectives on ethics and responsibility in a learning analytics-supported virtual mentoring program*: what it feels like on the receiving end of a flag, for the mentor as well as for the student.
- **Borchers, Liu, Lee, and Zhang (2024)**, *Ethical AIED and AIED ethics*: where in a workflow like this one an ethical framework would actually have to intervene.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Threshold sweep.** Instead of a fixed caseload, sweep the decision threshold from 0.05 to 0.95 and plot the false positive rate gap against the threshold. Is there any threshold at which the activity-only model is fair? What does your answer imply about "just tune the cutoff" as a remedy?
2. **Add a fairness constraint by hand.** Flag the top 20 percent of risk scores *within* each group instead of the top 25 overall. This is one crude form of group-aware thresholding. Compute what it costs in overall accuracy, then argue about whether an institution could defend doing it.
3. **Build a better regularity feature.** `active_days` punishes compressed schedules. Design a feature that captures "this student has stopped showing up" without punishing "this student studies in long blocks," compute it from the clickstream, and audit a model that uses it. Gaps between consecutive active days are a good place to start.
4. **Calibration, not just error rates.** Bin the risk scores and compare predicted risk against observed at-risk rates separately for each group. A model can have equal calibration and unequal error rates at the same time, and the two disagreeing is a well-known impossibility result worth reading about.
5. **Audit the label.** Re-run the whole notebook with `RISK_CUTOFF` set to 65, then to 75. Does the gap survive? A finding that only exists at one arbitrary threshold is a finding you should report differently.

## Troubleshooting

**"NameError: name 'model_table' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/students.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the first cell of section 1, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all: the notebook is seeded, so a clean run reproduces the same numbers every time.

**I got a different answer than my neighbor.** Compare feature lists first. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload for week 3. Even so, if you used an AI assistant while working through this notebook, to explain a line of code, to check your reading of a chart, or to help you draft a reflection, save that exchange now.

Starting with Mini Project 1 in week 4, the course AI policy requires you to upload your **AI interaction log plus a short reflection** alongside your notebook, in the Canvas "AI Reflection" submission. AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation.

Building the habit this week, when nothing is being graded, is much easier than starting it under a deadline.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
