# 🔍 Week 3: Ethics and Bias Audit

Auditing a non-completion model before anyone acts on it, on real enrollment records. The week starts by refusing the field's usual name for the thing being predicted, and the refusal is the first lesson.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 9, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Responsible and Human-Centered Learning Analytics |
| **Guest speaker** | Hansol Lee, Stanford University |
| **In-class time on this notebook** | About 30 minutes, launched in the hands-on studio block (4:40 to 5:00). Finish the last sections on your own if you run out of room. |
| **Deliverable** | None. Week 3 is an in-class launch, not a graded submission. |
| **Due date** | Not applicable. The first Canvas deliverable is Mini Project 1 in week 4. |
| **Notebook** | `week03_ethics_bias_audit.ipynb` |
| **Data used** | **Real:** the Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J, downloaded from `HakeoungLee/edis8100-datasets`. CC BY 4.0. **Synthetic, for contrast:** `students.csv`, `lms_clickstream.csv`, `gradebook.csv`, built by the notebook itself. |
| **Internet required** | Yes, for the first code cell only. Everything after it runs locally. |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn, scipy (already installed in Colab, and a dependency of scikit-learn anyway) |

## The data, and where it came from

This is the first notebook in the course that leaves the invented world of Blue Ridge University.

| | |
|---|---|
| **Dataset** | Open University Learning Analytics Dataset (OULAD), module **BBB**, presentations **2013J** and **2014J** |
| **Who collected it** | The Open University, a large distance-teaching university in the United Kingdom, from its own student records and its own virtual learning environment. Prepared for release by the Knowledge Media Institute. |
| **Size** | 4,529 enrollments (4,482 distinct people), 891,062 daily clickstream rows, 21,783 assignment submissions, 18 assessments, 528 course resources |
| **License** | CC BY 4.0. Free to use and share, including commercially, with attribution. |
| **Citation** | Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Loaded from** | `https://raw.githubusercontent.com/HakeoungLee/edis8100-datasets/main/oulad-bbb/` |

A university that teaches almost entirely online already holds a complete record of what every student clicked, when they submitted, and how it ended. A research group inside that university pulled two years of one module, stripped the names, replaced them with numbers, aggregated the clicks to daily counts, and published the result so that people outside the institution could study early warning systems without needing a data-sharing agreement.

Every row is a person who enrolled in a distance-learning module in 2013 or 2014. None of them enrolled in order to be a teaching example in Charlottesville in 2026. Anonymization and an open license are real protections, and they are not consent. The notebook says this out loud in its second markdown cell, and the ask is the same as it was in weeks 1 and 2, only now it is not a rehearsal: **treat these rows as people.**

**Why the synthetic course is still here.** Part 2 of the notebook rebuilds the EDUC 1010 data from weeks 1 and 2 and runs the identical audit on it. That is not nostalgia. It is the argument of the session: on synthetic data you can read the mechanism off the generator and prove where a disparity came from, and on real data you cannot. Neither dataset is the honest one on its own.

## Objectives

By the end of this activity you will be able to:

1. **Load** a real, published, openly licensed learning dataset, and state where it came from and who collected it before you analyze a single row.
2. **Name** what a model actually predicts, and say why "an at-risk model" describes a person while "a model predicting non-completion" describes an outcome.
3. **Train** that model on activity data, and read its accuracy honestly against a do-nothing baseline.
4. **Disaggregate** the model's errors by socioeconomic decile and by disability status, and say which of those differences you can distinguish from noise once you have made thirty comparisons.
5. **Redesign** the feature set, re-run the same audit, and be precise about what the redesign fixed and what it did not.
6. **Compare** what an audit can prove on real data against what it can prove on data whose mechanism was written down in advance.

The through-line of the session: a fairness audit measures a model, and a gap measures a world, and the two get reported in the same table as though they were the same kind of fact.

## The naming decision, which is the first design decision

The literature calls this an *at-risk model* producing a list of *at-risk students*. This notebook does not, and it spends a markdown cell saying why before any modelling code runs.

The column it builds is `did_not_pass`, and it means one thing: this enrollment's `final_result` was `Fail` or `Withdrawn`. That is a fact about an outcome a registry recorded. "At risk" is not: it relocates the fact into the person, in the present tense, before any evidence has been examined, and it hides the three choices underneath it, namely the threshold, the population, and the outcome definition.

The field's phrase stays in the notebook as an object of study, in quotation marks, with four questions attached every time it appears: **at risk of what, according to whom, measured how, and with what consequence for the person carrying the label?** Students should leave able to answer all four for this specific model.

The reason this is a methods point and not a manners point is visible in the last section: "the model flagged 367 of the 591 enrollments in the most deprived decile" sends a reader to look at the model, and "62 percent of students in the poorest decile are at risk" sends them to look at the students. Only the first is supported by anything in the notebook.

## What is in this folder

| File | What it is |
|---|---|
| `week03_ethics_bias_audit.ipynb` | The notebook. Downloads the real data in its first code cell, then builds the synthetic contrast dataset itself. Runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you when you reach Part 2. Holds the three synthetic CSVs only. Not stored in the repo. |

The OULAD files are never written to disk. They are read straight from the internet into memory each time you run the notebook.

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

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and scikit-learn, all of which ship with Anaconda, plus a working internet connection for the first cell.

## Step-by-step walkthrough

The timings below add up to about 30 minutes for Part 1, which is what we do together in class, and about 5 more for Part 2, which is a short finish on your own if we run out of room. The three ✏️ **Your turn** cells already contain working answers, so the notebook runs start to finish without you typing anything.

**⚙️ Setup (2 minutes).** Run the first code cell. It downloads six OULAD files and prints what arrived. If your connection is down it says so in plain language instead of showing a traceback. Then read the short provenance section that follows, which names the dataset, its license, its citation, and who collected it.

**📊 1. Real data does not arrive clean (5 minutes).** The mess is the lesson. One deprivation label is written `10-20` without a percent sign, 29 enrollments have no deprivation recorded, 47 people took the module twice, 738 enrollments never appear in the clickstream at all, 46,884 click rows happen before the module officially starts, and the outcome column has four categories rather than two. Four decisions get made in front of you, each with its cost named. Because 47 people appear twice, every join in the notebook keys on `(code_presentation, id_student)` rather than on the student id alone, including the join that attaches submitted coursework.

**📊 2. The gaps before any model (4 minutes).** Pass rates by deprivation decile run from 36.9 percent for enrollments from the most deprived tenth of neighbourhoods to 61.9 percent for the least deprived. Enrollments with a recorded disability pass at 40.3 percent against 50.0 percent. Median clicks in the first 60 days track the same gradient, 86 against 164.

The notebook is explicit about what these panels are evidence of, before it computes anything else. A gradient across deprivation deciles measures the conditions under which people studied and an institution that produced different outcomes for people in different circumstances. It does not measure the people, and the Index of Multiple Deprivation is an area-level index in the first place. The third chart is then the crux for the modelling: a recorded-activity feature is partly a proxy for material circumstance.

**📊 3. Train and read the accuracy (4 minutes).** A logistic regression predicting `did_not_pass` from `clicks`, `active_days`, and `resources`, tested with five-fold cross validation so no enrollment is scored by a model that already saw its outcome. Accuracy 0.735. "Never flag anybody" gets 0.491. Every accuracy figure in this notebook is printed next to that baseline. Sit with the pair before you move on.

**📊 4. The audit (7 minutes).** False positive rate, false negative rate, and share flagged, inside every decile and by recorded disability.

Ten deciles times three rates is thirty numbers, and the eye goes straight to the largest and the smallest. The notebook guards against that twice. First it simulates what the max-minus-min *would* be if all ten deciles shared one identical rate: about 0.09 to 0.10 at these denominators, which is larger than either error-rate spread actually observed. Then it replaces the range with a **gradient**, a weighted least squares slope of the rate on decile number, which is one question rather than ten, and puts a bootstrap interval on it.

The result is that two panels disagree on purpose, and now defensibly. The error-rate gradients are about -0.003 and +0.002 per decile step with intervals straddling zero: no detectable trend. The share-flagged gradient is about -0.014 with an interval nowhere near zero, and its observed spread of 0.151 is double what noise would produce. A bootstrap cell then shows the disability difference in error rates straddling zero, on a group whose pass rate is nearly ten points lower. The audit came back clean on a group whose recorded outcomes were measurably worse.

**✏️ Your turn 1: the threshold (2 minutes).** Change one number, the cutoff that turns a risk score into a phone call, and watch a staffing decision move a fairness metric.

**📊 5. Redesign and re-audit (5 minutes).** Drop the two schedule-shape features, add three about what an enrollment produced by day 60, keep everything else identical. Accuracy rises from 0.735 to 0.788, a gain of +0.053 with a bootstrap interval of roughly [+0.040, +0.066], and the overall false positive rate falls from 0.287 to 0.082. The share-flagged gradient does not flatten: it goes from about -0.014 to about -0.018 per decile step, and the change between them has an interval that includes zero, so the honest sentence is that the redesign did not flatten it and may have steepened it. The overall false negative rate rises from 0.244 to 0.337, which is what fewer false alarms cost. Then read the three cautions that follow, because an early mark is not innocent either.

**📊 6. What our one big decision bought us (3 minutes).** Rerun on only the students still registered at day 60. Accuracy falls from 0.735 to 0.692 while the do-nothing baseline rises from 0.491 to 0.631. Most of the impressive margin was bookkeeping about students the registry had already lost. Which number goes in the abstract is a reporting decision, and it is yours.

**✏️ Your turn 3 (stretch).** Point the same audit at `age_band`, `gender`, `region`, or `highest_education`, and find a gap nobody asked you to look for.

**🎯 Part 2: the synthetic contrast (5 minutes).** Rebuild EDUC 1010 and run the identical audit on the 30 students who are first generation and work 15 or more hours a week. The point estimates behave as designed and the counts are printed next to them, which is the lesson. The share-flagged difference is 10 of 30 against 4 of 90, Fisher exact p around 0.0001. The false positive rate difference, the one a fairness report would headline, rests on four false positives against two, at p around 0.03.

So the audit does not settle it. Section 8 does, because the generator hands back the latent traits: median active days 7 against 30 at p around 1e-15, while latent ability, total clicks, and quiz scores are all statistically indistinguishable. What makes the synthetic half certain is that somebody typed the mechanism, not that the audit was cleaner.

**💬 Reflection.** Six prompts tied to this week's readings and to the dataset itself. Bring your answers to the 5:00 discussion block.

## What this connects to in the readings

- **Tsai and Martinez-Maldonado (2022)**, *Human-centered approaches to data-informed feedback*: the humans around the system are part of the system, including the ones who choose the features and the ones who choose the dataset.
- **Holstein and Doroudi (2022)**, *Equity and artificial intelligence in education*: what a narrow fairness metric can and cannot see. Section 4 is the concrete version: three fairness numbers, three different answers, about the same predictions.
- **Lee and Gargroetzi (2023)**, *"It's like a double-edged sword": Mentor perspectives on ethics and responsibility in a learning analytics-supported virtual mentoring program*: what it feels like on the receiving end of a flag, for the mentor as well as for the student.
- **Borchers, Liu, Lee, and Zhang (2024)**, *Ethical AIED and AIED ethics*: where in a workflow like this one an ethical framework would actually have to intervene.
- **Kuzilek, Hlosta, and Zdrahal (2017)**, *Open University Learning Analytics dataset*: not on the reading list, but worth skimming. It is the paper that made today's session possible, and reflection prompt 5 asks what you would require of anyone who downloaded a dataset like it from your own institution.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Threshold sweep.** Instead of one cutoff, sweep the threshold from 0.05 to 0.95 and plot the share-flagged gradient across the deciles against the threshold, with bootstrap intervals. Is there any threshold at which the activity-only model closes it? What does your answer imply about "just tune the cutoff" as a remedy?
2. **Move the checkpoint.** The notebook looks at days 0 to 60. Rerun it at day 30 and at day 120. Accuracy climbs steadily with the window, and so does the circularity: students who withdraw stop clicking. Say where you would stop, and why.
3. **Build a better regularity feature.** `active_days` punishes compressed schedules. Design a feature that captures "this student has stopped showing up" without punishing "this student studies in long blocks," compute it from `studentVle.csv.gz`, and audit a model that uses it. Gaps between consecutive active days are a good place to start.
4. **Calibration, not just error rates.** Bin the predicted probabilities and compare predicted against observed non-completion rates separately for each decile. A model can have equal calibration and unequal error rates at the same time, and the fact that the two cannot generally both hold is a well-known impossibility result worth reading about. Section 4 is that result showing up in a real table.
5. **Split the label.** `did_not_pass` merges Fail and Withdrawn. Build two models, one for each, and compare which enrollments each one finds. If they disagree, the single label was hiding two different phenomena and one intervention was never going to serve both.
6. **Use the resource catalogue.** `vle.csv` says what kind of thing each `id_site` is: forum, quiz, resource, subpage, and more. Build features from *what* students clicked rather than how much, and audit that model. Does looking at the kind of activity rather than the amount change who gets flagged?

## Troubleshooting

**"Could not download the OULAD files."** The first cell prints a message naming the repository and three likely causes. In order of likelihood: this machine is offline or the campus network is blocking `raw.githubusercontent.com`; GitHub is briefly unhappy, so wait a minute and run the cell again; or you are on a restricted network, in which case open the notebook in Google Colab instead.

**"NameError: name 'data' is not defined" or something similar.** You ran a cell out of order, or the download cell failed and you carried on anyway. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/students.csv".** That is the Part 2 synthetic data. Scroll up to the collapsed generator cell in Part 2, run it, then continue. It only affects Part 2; Part 1 needs no local files at all.

**The generator cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that Part 2 works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the first code cell, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all. The download is a fixed snapshot and the models are seeded, so a clean run reproduces the same numbers every time.

**I got a different answer than my neighbor.** Compare feature lists first, then thresholds. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload for week 3. Even so, if you used an AI assistant while working through this notebook, to explain a line of code, to check your reading of a chart, or to help you draft a reflection, save that exchange now.

Starting with Mini Project 1 in week 4, the course AI policy requires you to upload your **AI interaction log plus a short reflection** alongside your notebook, in the Canvas "AI Reflection" submission. AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation.

Building the habit this week, when nothing is being graded, is much easier than starting it under a deadline.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development

OULAD is used under CC BY 4.0. Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171.
