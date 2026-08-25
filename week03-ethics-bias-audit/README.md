# Week 3: Ethics and Bias Audit

You audit a non-completion model before anyone acts on it, on real enrollment records, and then run the identical audit on a second real setting on another continent to see which of its findings hold there. The week starts by refusing the field's usual name for the thing being predicted.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 9, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Responsible and Human-Centered Learning Analytics |
| **Guest speaker** | Hansol Lee, Stanford University |
| **In-class time on this notebook** | About 30 minutes for Part 1, launched in the hands-on studio block (4:30 to 5:00), and about 10 more for Part 2. Finish Part 2 on your own if you run out of room. |
| **Deliverable** | None. Week 3 is an in-class launch, not a graded submission. |
| **Due date** | Not applicable. The first Canvas deliverable is Mini Project 1 in week 4. |
| **Notebook** | `week03_ethics_bias_audit.ipynb` |
| **Data used** | **Two real datasets, no synthetic data anywhere.** Part 1: the Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J, CC BY 4.0. Part 2: UCI Student Performance, the mathematics file, 395 Portuguese secondary students, CC BY 4.0, the same file students met in week 1. Both downloaded from `HakeoungLee/edis8100-datasets`. |
| **Internet required** | Yes, for two cells: the setup cell at the top and the Part 2 setup cell. Both fail politely with a plain message naming the repository. |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn, scipy (already installed in Colab, and a dependency of scikit-learn anyway) |
| **Runtime** | Under a minute end to end on a laptop. The two 200-run loops in section 8 are the slow part and they are the point of the section. |

## The data, and where it came from

Two datasets, both real, both openly licensed, both already familiar. Part 1 audits the Open University module you read in week 2. Part 2 runs the same audit on the Portuguese file you read in week 1.

| | |
|---|---|
| **Dataset** | Open University Learning Analytics Dataset (OULAD), module **BBB**, presentations **2013J** and **2014J** |
| **Who collected it** | The Open University, a large distance-teaching university in the United Kingdom, from its own student records and its own virtual learning environment. Prepared for release by the Knowledge Media Institute. |
| **Size** | 4,529 enrollments (4,482 distinct people), 891,062 daily clickstream rows, 21,783 assignment submissions, 18 assessments, 528 course resources |
| **License** | CC BY 4.0. Free to use and share, including commercially, with attribution. |
| **Citation** | Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Loaded from** | `https://raw.githubusercontent.com/HakeoungLee/edis8100-datasets/main/oulad-bbb/` |

A university that teaches almost entirely online already holds a complete record of what every student clicked, when they submitted, and how it ended. A research group inside that university pulled two years of one module, stripped the names, replaced them with numbers, aggregated the clicks to daily counts, and published the result so that people outside the institution could study early warning systems without needing a data-sharing agreement.

Every row is a person who enrolled in a distance-learning module in 2013 or 2014. None of them enrolled in order to be a teaching example in Charlottesville in 2026. Anonymization and an open license are real protections, and they are not consent. The notebook says this out loud in its second markdown cell, and the ask is the same as it was in weeks 1 and 2, and it has been a real ask every time: **treat these rows as people.**

### The second setting

| | |
|---|---|
| **Dataset** | UCI Student Performance, the mathematics file `student-mat.csv`, **semicolon delimited** |
| **Who collected it** | Paulo Cortez and Alice Silva, from school reports and a questionnaire at two Portuguese secondary schools |
| **Size** | 395 students, 349 at school GP and 46 at school MS, 33 columns |
| **When** | The 2005 to 2006 school year |
| **License** | CC BY 4.0. Free to use and share, with attribution. |
| **Citation** | Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance. In *Proceedings of 5th FUture BUsiness TEchnology Conference*, 5-12. |
| **Loaded from** | `https://raw.githubusercontent.com/HakeoungLee/edis8100-datasets/main/uci-student-performance/student-mat.csv` |

**Why the audit runs twice, and why the second dataset is this one.** A fairness result from one course at one university is a hypothesis. The next thing anyone should do with it is take the recipe somewhere else and see whether it survives, and that is what Part 2 does. It picks a setting about as unlike OULAD as a learning dataset gets: 3,136 adults studying at a distance in the United Kingdom, measured by a server log, against 395 teenagers in two buildings in Portugal, measured by a school register and a paper questionnaire. Different country, different decade, different age group, different instrument.

Students also arrive at it already knowing something a stranger downloading the file would not. In week 1 they found that 38 of the 395 final grades are exactly 0, that all 38 belong to students with zero recorded absences, and that most of those students were being graded normally in the second period. Those 38 look like records that were never entered. Part 2 makes the decision about them out loud, keeps them, and then reruns the whole audit without them, which changes one of the two headline findings.

## Objectives

By the end of this activity you will be able to:

1. **Load** a real, published, openly licensed learning dataset, and state where it came from and who collected it before you analyze a single row.
2. **Name** what a model actually predicts, and say why "an at-risk model" describes a person while "a model predicting non-completion" describes an outcome.
3. **Train** that model on activity data, and read its accuracy honestly against a do-nothing baseline.
4. **Disaggregate** the model's errors by socioeconomic decile and by disability status, and say which of those differences you can distinguish from noise once you have made thirty comparisons.
5. **Redesign** the feature set, re-run the same audit, and be precise about what the redesign fixed and what it did not.
6. **Repeat** the identical audit in a second real setting, and say which findings travelled, which did not, and which of your own protocol choices was doing the work.

The through-line of the session: a fairness audit measures a model, and a gap measures a world, and the two get reported in the same table as though they were the same kind of fact.

And the one Part 2 adds: **which metric you audit determines whether you see unfairness at all**, which is a claim students verify twice with their own arithmetic rather than take on trust.

## The naming decision, which is the first design decision

The literature calls this an *at-risk model* producing a list of *at-risk students*. This notebook does not, and it spends a markdown cell saying why before any modelling code runs.

The column it builds is `did_not_pass`, and it means one thing: this enrollment's `final_result` was `Fail` or `Withdrawn`. That is a fact about an outcome a registry recorded. "At risk" is not: it relocates the fact into the person, in the present tense, before any evidence has been examined, and it hides the three choices underneath it, namely the threshold, the population, and the outcome definition.

The field's phrase stays in the notebook as an object of study, in quotation marks, with four questions attached every time it appears: **at risk of what, according to whom, measured how, and with what consequence for the person carrying the label?** Students should leave able to answer all four for this specific model.

The reason this is a methods point and not a manners point is visible in the last section: "the model flagged 367 of the 591 enrollments in the most deprived decile" sends a reader to look at the model, and "62 percent of students in the poorest decile are at risk" sends them to look at the students. Only the first is supported by anything in the notebook.

## What is in this folder

| File | What it is |
|---|---|
| `week03_ethics_bias_audit.ipynb` | The notebook. Downloads both real datasets over the internet, one in its first code cell and one at the start of Part 2. Runs top to bottom untouched. |
| `README.md` | This file. |

Nothing is written to disk. Both datasets are read straight from the internet into memory each time you run the notebook, and there is no local `data/` folder for this week.

## How to open this in Colab

The course repository is public, so the Colab badge opens the notebook directly. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
5. Select `week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and scikit-learn, all of which ship with Anaconda, plus a working internet connection for the first cell.

## Step-by-step walkthrough

The timings below add up to about 30 minutes for Part 1, which is what we do together in class, and about 10 more for Part 2, which is a finish on your own if we run out of room. The four **Your turn** cells already contain working answers, so the notebook runs start to finish without you typing anything.

**Setup (2 minutes).** Run the first code cell. It downloads six OULAD files and prints what arrived. If your connection is down it says so in plain language instead of showing a traceback. Then read the short provenance section that follows, which names the dataset, its license, its citation, and who collected it.

**1. Real data does not arrive clean (5 minutes).** The mess is the lesson. One deprivation label is written `10-20` without a percent sign, 29 enrollments have no deprivation recorded, 47 people took the module twice, 738 enrollments never appear in the clickstream at all, 46,884 click rows happen before the module officially starts, and the outcome column has four categories rather than two. Four decisions get made in front of you, each with its cost named. Because 47 people appear twice, every join in the notebook keys on `(code_presentation, id_student)` rather than on the student id alone, including the join that attaches submitted coursework. All 47 did not pass in 2013J, which is why they were back in 2014J, and section 4 later checks whether their double-counting moves the headline interval. It does not. The section also names an asymmetry the two presentations carry into the redesign: three assignments fall on or before day 60 in 2013J and two in 2014J, so a feature built from submitted work is not on the same scale in the two cohorts.

**2. The gaps before any model (4 minutes).** Pass rates by deprivation decile run from 36.9 percent for enrollments from the most deprived tenth of neighbourhoods to 61.9 percent for the least deprived. Enrollments with a recorded disability pass at 40.3 percent against 50.0 percent. Median clicks in the first 60 days track the same gradient, 86 against 164.

The notebook is explicit about what these panels are evidence of, before it computes anything else. A gradient across deprivation deciles measures the conditions under which people studied and an institution that produced different outcomes for people in different circumstances. It does not measure the people, and the Index of Multiple Deprivation is an area-level index in the first place. The third chart is then the crux for the modelling: a recorded-activity feature is partly a proxy for material circumstance.

**3. Train and read the accuracy (4 minutes).** A logistic regression predicting `did_not_pass` from `clicks`, `active_days`, and `resources`, tested with five-fold cross validation so no enrollment is scored by a model that already saw its outcome. Accuracy 0.735. "Never flag anybody" gets 0.491. Every accuracy figure in this notebook is printed next to that baseline. Sit with the pair before you move on.

**4. The audit (7 minutes).** False positive rate, false negative rate, and share flagged, inside every decile and by recorded disability.

Ten deciles times three rates is thirty numbers, resting on denominators that run from 102 to 591, and the eye goes straight to the largest and the smallest. The notebook guards against that three times. First it simulates what the max-minus-min *would* be if all ten deciles shared one identical rate: about 0.09 for the two error rates and about 0.075 for the share flagged, so the null spread is larger than either error-rate spread actually observed. Then it replaces the range with a **gradient**, a weighted least squares slope of the rate on decile number, which is one question rather than ten, and puts a bootstrap interval on it. Then it audits the gradient itself: a weighted lack-of-fit check asks whether one straight line summarises the ten points at all, and a second bootstrap resamples *people* rather than enrollments so that the 47 repeat rows stop being a caveat and become a number.

The result is that two panels disagree on purpose, and now defensibly. The error-rate gradients are about -0.003 and +0.002 per decile step with intervals straddling zero: no detectable trend. The share-flagged gradient is about -0.014 with an interval nowhere near zero, and its observed spread of 0.151 is double what noise would produce. A bootstrap cell then shows the disability difference in error rates straddling zero, on a group whose pass rate is nearly ten points lower. The audit came back clean on a group whose recorded outcomes were measurably worse.

**Your turn 1: the threshold (2 minutes).** Change one number, the cutoff that turns a risk score into a phone call, and watch a staffing decision move a fairness metric.

**5. Redesign and re-audit (5 minutes).** Drop the two schedule-shape features, add three about what an enrollment produced by day 60, keep everything else identical. Accuracy rises from 0.735 to 0.788, a gain of +0.053 with a bootstrap interval of roughly [+0.040, +0.066], and the overall false positive rate falls from 0.287 to 0.082. The notebook prints both errors as counts as well as rates, because a rate that small is easy to over-read: 638 false positives become 183, and 562 missed enrollments become 776. That is 455 letters not sent, bought with 214 more people who did not pass and got nothing. The share-flagged gradient does not flatten: it goes from about -0.014 to about -0.018 per decile step, and the change between them has an interval that includes zero, so the honest sentence is that the redesign did not flatten it and may have steepened it. Then read the cautions that follow, because an early mark is not innocent either, and because `n_submitted` carries the two presentations' different assignment calendars.

**6. What our one big decision bought us (3 minutes).** Rerun on only the students still registered at day 60. Accuracy falls from 0.735 to 0.692 while the do-nothing baseline rises from 0.491 to 0.631. Most of the impressive margin was bookkeeping about students the registry had already lost. Which number goes in the abstract is a reporting decision, and it is yours.

**Your turn 3 (stretch).** Point the same audit at `age_band`, `gender`, `region`, or `highest_education`, and find a gap nobody asked you to look for.

**Part 2: does the unfairness travel? (10 minutes).** One recipe, held fixed, run on both settings. Same outcome definition, same algorithm, same threshold, same protocol, activity and support features only and **no prior grades on either side**, because `G1` and `G2` would predict `G3` by being a grade and would mirror nothing in Part 1. OULAD is rebuilt to match: the 1,393 withdrawn enrollments come out, leaving 3,136 that ran to a graded end, and activity is counted over the first four weeks rather than sixty days. The Portuguese outcome is `G3 < 10`, the Portuguese pass mark.

**7. One recipe, two settings.** The two models are almost indistinguishable. AUC **0.688** in both. Accuracy **0.714** in Portugal against a do-nothing rule of 0.671, and **0.724** in OULAD against 0.709. Base rates 0.329 and 0.291. That is an ordinary published early warning model, twice, on two continents, and the second panel of figure 4 is the part worth sitting with: the do-nothing rule is four points behind one of them and one and a half points behind the other.

The grouping column gets a paragraph of its own, because it has to. Portugal is audited by the higher of the two parents' education, split at 9th grade, 135 students against 260. OULAD is audited by the student's own prior qualification, split at A level, 1,355 against 1,781. Those are not the same construct, one being a fact about a household and the other a fact about the adult sitting the module, and the notebook says so rather than letting "educational background" quietly cover both.

**8. The seed lottery, which is the most valuable cell in Part 2.** Before any fairness claim, a demonstration. The notebook measures one quantity, the rural minus urban false positive gap in the Portuguese file, two hundred times under each of two protocols. Under a single stratified 70/30 split, changing nothing but the seed, the answer ranges from **-0.169 to +0.457**, standard deviation 0.098, with 65.5 percent of seeds saying rural students who passed were flagged more often and the rest saying the opposite. **Seed 42 gives +0.327, larger than 99 percent of the other 199 seeds.** Under the protocol the notebook actually uses, twenty-five fresh five-fold splits averaged, the two hundred answers all land between +0.004 and +0.064.

Then the cell says what the tight histogram does not mean, because this is where people over-read. All 200 of those runs measure the same 395 students, so they agree by construction. The averaged gap on the whole file is **+0.027 with a 95 percent bootstrap interval of [-0.065, +0.125]**, which contains zero. Repeating the split removes the seed. Only the bootstrap shows you the students. Both are needed, and 55 rural students passed in total.

**9 and 10. The audit, and what travelled.** Five metrics, two settings, every rate beside the denominator it rests on, every gap with a 95 percent bootstrap interval, figure 6 plotting all ten at once against a line at zero.

- **The accuracy gap replicates.** Lower band minus higher band is **-0.117, 95% [-0.214, -0.020]** in Portugal and **-0.150, [-0.182, -0.120]** in OULAD, and it survives a random forest and gradient boosting in both settings.
- **The false alarm gap does not.** Portugal: **+0.115, [+0.025, +0.209]**, from 0.185 against 0.071. OULAD: **+0.009, [-0.006, +0.024]**, an order of magnitude smaller and straddling zero.
- **Being missed is close to even in both**, at -0.041 and +0.017, both intervals containing zero, on models whose false negative rates are 0.63 and 0.67 in Portugal and 0.88 and 0.86 in OULAD. The OULAD model misses about seven of every eight enrollments that ended in a Fail, evenly. A fairness metric can be satisfied by a model that does not work.

**11. What the accuracy gap is actually made of, and what cannot be settled.** Two stories produce the same accuracy gap: base-rate arithmetic, or a genuine measurement failure. The notebook separates them. Put each band's own do-nothing rule beside its accuracy and the gap between the two lifts is **-0.009, [-0.109, +0.086]** in Portugal and **+0.015, [-0.003, +0.032]** in OULAD. In both settings the accuracy gap that replicated so convincingly is, once the base rate is accounted for, no longer distinguishable from zero.

AUC is the base-rate-free version. In OULAD the two bands rank identically, 0.687 [0.656, 0.716] against 0.689 [0.659, 0.719]. In Portugal the point estimates differ a great deal, 0.624 [0.525, 0.718] against 0.728 [0.659, 0.793], and the gap of -0.104 has an interval of [-0.226, +0.020] that contains zero, on 135 students of whom 81 passed and 54 did not. The same gap shrinks from -0.100 to -0.058 and -0.054 when the model class changes. So the contested question, whether these instruments genuinely read students in the lower band worse or whether this is what 135 students look like when you cut them in half, **does not get an answer**, and the notebook says so rather than picking one.

Then the last honest turn. Week 1's 38 zero grades are not spread evenly: **21 of the 135 students in the lower band against 17 of the 260 in the higher band**, 15.6 percent against 6.5 percent, Fisher exact p = 0.006. Rerun the whole of setting two without them and the one clean finding, the false alarm gap, falls from **+0.115 [+0.025, +0.209] to +0.046 [-0.028, +0.124]** and stops clearing zero. The audit measured a model, and part of what it measured was a filing cabinet.

**Your turn 4.** Point the same two-group audit at any column of the Portuguese file. `sex` is the working default and it produces a gap nobody went looking for: a false negative gap of **+0.219, [+0.053, +0.378]**. `higher` splits 375 against 20 and the 20 contribute 7 students who passed, which is what a fragile rate looks like. Three of the offered columns are model inputs, and the cell says so in its heading when you pick one.

**Why the course runs the audit twice.** The synthesis: one replication, one failure to replicate, and one metric that was clean in both settings on models that miss most of the students they are looking for. A single-setting fairness result is a hypothesis, and the next thing anyone should do with it is take the recipe somewhere else. The section closes with a one-paragraph coda pointing at week 5, where the same audit is run on **human raters** rather than a model, using PERSUADE 2.0. You cannot rerun a rater with a different seed.

**Reflection.** Seven prompts tied to this week's readings and to both datasets. Bring your answers to the 5:00 discussion block.

## What this connects to in the readings

- **Tsai and Martinez-Maldonado (2022)**, *Human-centered approaches to data-informed feedback*: the humans around the system are part of the system, including the ones who choose the features and the ones who choose the dataset.
- **Holstein and Doroudi (2022)**, *Equity and artificial intelligence in education*: what a narrow fairness metric can and cannot see. Section 4 is the concrete version: three fairness numbers, three different answers, about the same predictions.
- **Lee and Gargroetzi (2023)**, *"It's like a double-edged sword": Mentor perspectives on ethics and responsibility in a learning analytics-supported virtual mentoring program*: what it feels like on the receiving end of a flag, for the mentor as well as for the student.
- **Borchers, Liu, Lee, and Zhang (2024)**, *Ethical AIED and AIED ethics*: where in a workflow like this one an ethical framework would actually have to intervene.
- **Kuzilek, Hlosta, and Zdrahal (2017)**, *Open University Learning Analytics dataset*, and **Cortez and Silva (2008)**, *Using data mining to predict secondary school student performance*: neither is on the reading list, and both are worth skimming. They are the papers that made today's session possible, and reflection prompt 5 asks what you would require of anyone who downloaded a dataset like either of them from your own institution.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Threshold sweep.** Instead of one cutoff, sweep the threshold from 0.05 to 0.95 and plot the share-flagged gradient across the deciles against the threshold, with bootstrap intervals. Is there any threshold at which the activity-only model closes it? What does your answer imply about "just tune the cutoff" as a remedy?
2. **Move the checkpoint.** The notebook looks at days 0 to 60. Rerun it at day 30 and at day 120. Accuracy climbs steadily with the window, and so does the circularity: students who withdraw stop clicking. Say where you would stop, and why.
3. **Build a better regularity feature.** `active_days` punishes compressed schedules. Design a feature that captures "this student has stopped showing up" without punishing "this student studies in long blocks," compute it from `studentVle.csv.gz`, and audit a model that uses it. Gaps between consecutive active days are a good place to start.
4. **A different model for the gradient.** The notebook fits weighted least squares to ten proportions and bootstraps it. Fit a logistic regression of the flag on decile number at the enrollment level instead, cluster the standard errors by person, and compare. Does the more conventional model tell you anything the ten-point line did not, and is it easier or harder to explain to the advising office?
5. **Calibration, not just error rates.** Bin the predicted probabilities and compare predicted against observed non-completion rates separately for each decile. A model can have equal calibration and unequal error rates at the same time, and the fact that the two cannot generally both hold is a well-known impossibility result worth reading about. Section 4 is that result showing up in a real table.
6. **Split the label.** `did_not_pass` merges Fail and Withdrawn. Build two models, one for each, and compare which enrollments each one finds. If they disagree, the single label was hiding two different phenomena and one intervention was never going to serve both.
7. **Use the resource catalogue.** `vle.csv` says what kind of thing each `id_site` is: forum, quiz, resource, subpage, and more. Build features from *what* students clicked rather than how much, and audit that model. Does looking at the kind of activity rather than the amount change who gets flagged?
8. **A third setting.** The same repository holds `student-por.csv`, the Portuguese-language course from the same project, 649 students, many of whom also appear in the mathematics file. Run the Part 2 recipe on it unchanged. Then say what the overlap between the two files does to the phrase "replicated in a third setting," and how you would report it honestly.
9. **Sweep the threshold in both settings at once.** Section 8 fixed the threshold at 0.50. Sweep it and plot the false alarm gap against the threshold for both settings on one pair of axes, with bootstrap intervals. Does the Portuguese gap survive every threshold, and does the OULAD gap appear at any of them?
10. **Match the sample sizes.** Much of the difference between the two audits is that one rests on 395 rows and the other on 3,136. Subsample OULAD down to 395, repeatedly, and see how often its false alarm gap would have looked like Portugal's by chance. That is the cleanest available test of whether the two settings really differ or whether one of them is simply better measured.
11. **Calibration by band, in both settings.** Bin the predicted probabilities and compare predicted against observed rates inside each education band, in Portugal and in OULAD. Equal calibration and equal error rates cannot generally both hold when base rates differ, and here they differ by 11 and 17 points.

## Troubleshooting

**"Could not download the OULAD files."** or **"Could not download the second dataset."** Both download cells print a message naming `github.com/HakeoungLee/edis8100-datasets` and three likely causes, instead of a traceback. In order of likelihood: this machine is offline or the campus network is blocking `raw.githubusercontent.com`; GitHub is briefly unhappy, so wait a minute and run the cell again; or you are on a restricted network, in which case open the notebook in Google Colab instead. The Part 2 cell is a separate download, so it can fail on its own even if Part 1 worked half an hour earlier.

**"NameError: name 'data' is not defined" or something similar.** You ran a cell out of order, or the download cell failed and you carried on anyway. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**The Portuguese file loaded as one enormous column.** You changed `sep=";"` or copied the read into a new cell without it. That file is semicolon delimited, and pandas does not warn you: it hands back a single column of 33 things glued together and no error at all. It is worth doing once on purpose so you recognise the shape of the mistake.

**Section 8 takes about twenty seconds.** That is correct. It fits the model 200 times under one protocol and 5,000 times under the other. The wait is the argument of the section.

**My charts do not appear.** Make sure you ran the first code cell, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**Colab says it cannot find the notebook.** You are signed into a different Google account. Check the profile picture in the top right corner.

**My numbers do not match the ones in the text.** If you changed a **Your turn** cell, that is expected and good. If you did not, restart and run all. Both downloads are fixed snapshots, every fold sequence is seeded, and every bootstrap function carries its own generator so that running a cell twice or out of order cannot change the interval it prints. A clean run reproduces the same numbers every time.

**I got a different answer than my neighbor.** Compare feature lists first, then thresholds. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload for week 3. Even so, if you used an AI assistant while working through this notebook, to explain a line of code, to check your reading of a chart, or to help you draft a reflection, save that exchange now.

Starting with Mini Project 1 in week 4, the course AI policy requires an **AI Reflection** submission on Canvas alongside your notebook, and it has two parts that go in two different places on that page:

- **The conversation record goes in a Word file, attached to the submission.** The full exchange, across every tool and every session, pasted in. Not a summary, and not into the text box.
- **The reflection goes in the Canvas text box.** Copy in the four questions from the syllabus and answer each one: how you used it; whether it helped and how; whether it made your work more challenging in any way; and what lesson about AI you would pass on to a friend or the class.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation.

Building the habit this week, when nothing is being graded, is much easier than starting it under a deadline.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development

Both datasets are used under CC BY 4.0, with attribution and no modification to the published files.

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171.

Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance. In *Proceedings of 5th FUture BUsiness TEchnology Conference*, 5-12.
