# Week 3: Ethics and Bias Audit

In this session we audit a non-completion model before anyone acts on it, on real enrollment
records, and then run the identical audit on a second real setting on another continent to see
which of its findings hold there. The week starts by declining the field's usual name for the thing
being predicted.

Coding experience is not assumed, here or in any week of this course. Every cell already holds
working code, and the notebook runs from top to bottom without anything being typed. Attention is
better spent on what the code is doing to the data and on what the output might mean. Questions are
welcome at any point, including questions about a single line of code, and error messages are a
normal part of working in a notebook.

## At a glance

| | |
|---|---|
| **Session** | Week 3, Wednesday, September 9, 2026, Ridley Hall 137 |
| **Topic** | Responsible and Human-Centered Learning Analytics |
| **Notebook portion** | 4:50 to 5:50 PM, instructor-guided, after the student-led discussion hour and the break |
| **Notebook** | `week03_ethics_bias_audit.ipynb` |
| **Deliverable** | None. Nothing from this notebook is collected, and nothing goes to Canvas. |
| **Due** | Nothing. The first Canvas deliverable is Mini Project 1 in week 4. |
| **Data** | **Two real datasets, published and openly licensed, and no synthetic data anywhere.** Part 1: the Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J, CC BY 4.0. Part 2: UCI Student Performance, the mathematics file, 395 Portuguese secondary students, CC BY 4.0, the same file we met in week 1. Both downloaded from `github.com/HakeoungLee/edis8100-datasets` |
| **Needs internet?** | **Yes**, for two cells: the setup cell at the top and the Part 2 setup cell. Both fail with a plain-English message naming the repository rather than a long error trace. |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn, scipy (all present in Colab, and scipy is a dependency of scikit-learn anyway) |
| **Runtime** | Under a minute end to end on a laptop, including both downloads. The two 200-run loops in section 8 are the slow part, and the wait is the argument of that section. |
| **Prior coding experience needed** | None |

Mini projects begin in week 4, and the model audited here returns there as the early-warning panel
of a teacher-facing dashboard.

One student leads the discussion hour in six of the weeks from week 2 through week 11, and each of
the three of you leads **two** of those weeks. Week 3 is one of them.

## What I hope you leave with

1. Being able to load a real, published, openly licensed learning dataset and state where it came
   from and who collected it before analyzing a single row.
2. Being able to name what a model predicts, and to say why "an at-risk model" is a description of
   a person while "a model predicting non-completion" is a description of an outcome.
3. Training that model on activity data, and reading its accuracy against a do-nothing baseline.
4. Disaggregating the model's errors by socioeconomic decile and by disability status, and saying
   which of those differences can be distinguished from noise once thirty comparisons have been made.
5. Redesigning the feature set, re-running the same audit, and being precise about what the redesign
   changed and what it did not.
6. Repeating the identical audit in a second real setting, and saying which findings traveled,
   which did not, and which protocol choice was doing the work.

None of these is a coding objective.

The through-line: a fairness audit measures a model, a group gap measures a world, and the two get
reported in the same table as though they were the same kind of fact. Part 2 adds a second: which
metric you audit determines whether you see unfairness at all, which is a claim we verify twice with
our own arithmetic rather than take on trust.

## What is in this folder

| File | What it is |
|---|---|
| `week03_ethics_bias_audit.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is nothing to download by hand and nothing to upload. Both datasets are read straight from the
internet into memory each time the notebook runs, and there is no local `data/` folder for this week.

## Opening it in Colab

The course repository is public, so you need only a Google account and a browser. There is nothing
to accept or authorize.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, and enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`. Then select
`week03-ethics-bias-audit/week03_ethics_bias_audit.ipynb`.

The notebook can also be run locally with Jupyter. It needs pandas, numpy, matplotlib, and
scikit-learn, all of which ship with Anaconda, plus a working internet connection for two cells.

### Keeping your own copy

Colab discards the session when you close the tab. **File > Save a copy in Drive** keeps a personal
version, and **File > Download > Download .ipynb** saves a local one. Nothing is lost if you forget:
both datasets are fixed published files, every fold sequence is seeded, and every resampling function
carries its own generator, so re-running the notebook from the top reproduces the same numbers on
any machine.

## Walkthrough

We move through this together in class. The timings below are a rough guide rather than a target,
and it is fine if we spend longer somewhere and finish something else afterwards. The four
**Your turn** cells already contain working values, so the notebook runs start to finish without
anything being typed.

| Step | Section | Minutes | What happens |
|---|---|---|---|
| 1 | Setup and orientation | 6 | The first code cell downloads six OULAD files and prints what arrived. Then the provenance section, which names the dataset, its license, its citation, and who collected it, before any number appears. |
| 2 | The concepts the audit needs | 10 | Away from the keyboard: what the field calls an at-risk model and the three human decisions inside it, the confusion matrix stated in terms of what happens to a person, accuracy read against the do-nothing baseline, and why calibration and equal error rates generally cannot both hold when base rates differ. |
| 3 | Sections 1 to 4, the audit itself | 15 | Real data does not arrive clean; the gaps before any model exists; the logistic regression on clicks, active days, and resources; and the disaggregated audit, in pairs. |
| 4 | Sections 7 to 11, the same audit somewhere else | 10 | One recipe, held fixed, run on the Portuguese file and on a rebuilt OULAD table, and the five gaps side by side. |
| 5 | Section 8, the seed | 7 | One fairness quantity measured 200 times under each of two protocols. |
| 6 | Section 5, the redesign round | 6 | Swap the feature set on the OULAD model and run the audit again. |
| 7 | The close | 6 | Which of the two results you believe, and how you would have decided having run only one of them. |

The notebook itself reads top to bottom, and section 5 sits where it belongs in the argument rather
than where it falls in the hour. Anything still open at 5:50 is fine to finish afterwards.

**Going further** sections are clearly marked and optional: the audit of a group nobody asked about
after section 6, and the notes on the Your turn cells at the end. Nothing later depends on either.

## The data, and where it came from

Two datasets, both real, both openly licensed, both already familiar. Part 1 audits the Open
University module we read in week 2. Part 2 runs the same audit on the Portuguese file we read in
week 1.

| | |
|---|---|
| **Dataset** | Open University Learning Analytics Dataset (OULAD), module **BBB**, presentations **2013J** and **2014J** |
| **Who collected it** | The Open University, a large distance-teaching university in the United Kingdom, from its own student records and its own virtual learning environment. Prepared for release by the Knowledge Media Institute. |
| **Size** | 4,529 enrollments (4,482 distinct people), 891,062 daily clickstream rows, 21,783 assignment submissions, 18 assessments, 528 course resources |
| **License** | CC BY 4.0. Free to use and share, including commercially, with attribution. |
| **Citation** | Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. |
| **Loaded from** | `https://raw.githubusercontent.com/HakeoungLee/edis8100-datasets/main/oulad-bbb/` |

A university that teaches almost entirely online already holds a complete record of what every
student clicked, when they submitted, and how it ended. A research group inside that university
pulled two years of one module, stripped the names, replaced them with numbers, aggregated the
clicks to daily counts, and published the result so that people outside the institution could study
early warning systems without needing a data-sharing agreement.

Every row is a person who enrolled in a distance-learning module in 2013 or 2014. None of them
enrolled in order to be a teaching example in Charlottesville in 2026. Anonymization and an open
license are real protections, and they are not consent. The notebook says this in its second
markdown cell, and the ask is the same as it was in weeks 1 and 2: **treat these rows as people.**

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

**Why the audit runs twice, and why the second dataset is this one.** A fairness result from one
course at one university is a hypothesis. The next thing anyone might do with it is take the recipe
somewhere else and see whether it survives, and that is what Part 2 does. It picks a setting about
as unlike OULAD as a learning dataset gets: 3,136 enrollments belonging to 3,127 adults studying at
a distance in the United Kingdom, measured by a server log, against 395 teenagers in two buildings
in Portugal, measured by a school register and a paper questionnaire. Different country, different
decade, different age group, different instrument.

We also arrive at it already knowing something a stranger downloading the file would not. In week 1
we found that 38 of the 395 final grades are exactly 0, that all 38 belong to students with zero
recorded absences, and that most of those students were being graded normally in the second period.
The dataset documentation does not say what those zeros are, so whether they are grades or records
that were never entered remains a hypothesis rather than a finding. Part 2 makes the decision about
them out loud, keeps them, and then reruns the whole audit without them, which changes one of the
two headline findings.

## The naming decision, which is the first design decision

The literature calls this an *at-risk model* producing a list of *at-risk students*. This notebook
does not, and it spends a markdown cell on why before any modeling code runs.

The column it builds is `did_not_pass`, and it means one thing: this enrollment's `final_result` was
`Fail` or `Withdrawn`. That is a fact about an outcome a registry recorded. "At risk" is not: it
relocates the fact into the person, in the present tense, before any evidence has been examined, and
it hides the three choices underneath it, namely the threshold, the population, and the outcome
definition.

The field's phrase stays in the notebook as an object of study, in quotation marks, with four
questions attached every time it appears: at risk of what, according to whom, measured how, and with
what consequence for the person carrying the label? Being able to answer all four for this specific
model is one of the things the session is for.

This is a methods point rather than a manners point, and the last section is where that becomes
visible: "the model flagged 367 of the 591 enrollments in the most deprived decile" sends a reader to
look at the model, and "62 percent of students in the poorest decile are at risk" sends them to look
at the students. Only the first is supported by anything in the notebook.

## What Part 1 does, section by section

**1. Real data does not arrive clean.** The mess is the lesson. One deprivation label is written
`10-20` without a percent sign, 29 enrollments have no deprivation recorded, 47 people took the
module twice, 738 enrollments never appear in the clickstream at all, 46,884 click rows happen
before the module officially starts, and the outcome column has four categories rather than two.
Four decisions are made visibly, each with its cost named. Because 47 people appear twice, every
join in the notebook keys on `(code_presentation, id_student)` rather than on the student id alone,
including the join that attaches submitted coursework. All 47 did not pass in 2013J, which is why
they were back in 2014J, and section 4 later checks whether their double-counting moves the headline
interval. It does not. The section also names an asymmetry the two presentations carry into the
redesign: three assignments fall on or before day 60 in 2013J and two in 2014J, so a feature built
from submitted work is not on the same scale in the two cohorts.

**2. The gaps before any model.** Pass rates by deprivation decile run from 36.9 percent for
enrollments from the most deprived tenth of neighborhoods to 61.9 percent for the least deprived.
Enrollments with a recorded disability pass at 40.3 percent against 50.0 percent. Median clicks in
the first 60 days track the same gradient, 86 against 164.

The notebook is explicit about what these panels are evidence of, before it computes anything else.
A gradient across deprivation deciles measures the conditions under which people studied, and an
institution that produced different outcomes for people in different circumstances. It does not
measure the people, and the Index of Multiple Deprivation is an area-level index in the first place.
A small table separates what the data directly show, what a plausible interpretation would be, and
what these files cannot establish. The third chart is then the crux for the modeling: a
recorded-activity feature is partly a proxy for material circumstance.

**3. Train and read the accuracy.** A logistic regression predicting `did_not_pass` from `clicks`,
`active_days`, and `resources`, tested with five-fold cross validation so no enrollment is scored by
a model that already saw its outcome. Accuracy 0.735. "Never flag anybody" gets 0.491. Every
accuracy figure in this notebook is printed next to that baseline, and the pair is worth sitting with
before moving on.

**4. The audit.** False positive rate, false negative rate, and share flagged, inside every decile
and by recorded disability.

Ten deciles times three rates is thirty numbers, resting on denominators that run from 102 to 591,
and the eye goes straight to the largest and the smallest. The notebook guards against that three
times. First it simulates what the max-minus-min *would* be if all ten deciles shared one identical
rate: about 0.094 for the two error rates and about 0.075 for the share flagged, so the null spread
is larger than either error-rate spread observed. Then it replaces the range with a **gradient**, a
weighted least squares slope of the rate on decile number, which is one question rather than ten,
and puts a bootstrap interval on it. Then it audits the gradient itself: a weighted lack-of-fit check
asks whether one straight line summarizes the ten points at all, and a second bootstrap resamples
*people* rather than enrollments so that the 47 repeat rows stop being a caveat and become a number.

The result is that two panels disagree on purpose, and now defensibly. The error-rate gradients are
about -0.003 and +0.002 per decile step with intervals straddling zero: no detectable trend. The
share-flagged gradient is about -0.014 with an interval nowhere near zero, and its observed spread of
0.151 is double what noise would produce. A bootstrap cell then shows the disability difference in
error rates straddling zero, on a group whose pass rate is nearly ten points lower. The audit came
back clean on a group whose recorded outcomes were measurably worse.

**Your turn 1: the threshold.** Change one number, the cutoff that turns a risk score into a phone
call, and watch a staffing decision move a fairness metric.

**5. Redesign and re-audit.** Drop the two schedule-shape features, add three about what an
enrollment produced by day 60, keep everything else identical. Accuracy rises from 0.735 to 0.788, a
gain of +0.053 with a bootstrap interval of roughly [+0.040, +0.066], and the overall false positive
rate falls from 0.287 to 0.082. The notebook prints both errors as counts as well as rates, because
a rate that small is easy to over-read: 638 false positives become 183, and 562 missed enrollments
become 776. That is 455 letters not sent, bought with 214 more people who did not pass and got
nothing. The share-flagged gradient does not flatten: it goes from about -0.014 to about -0.018 per
decile step, and the change between them has an interval that includes zero, so the defensible
sentence is that the redesign did not flatten it and may have steepened it. Then come the cautions,
because an early mark is not innocent either, and because `n_submitted` carries the two
presentations' different assignment calendars.

**6. What our one big decision bought us.** Rerun on only the enrollments still registered at day 60.
Accuracy falls from 0.735 to 0.692 while the do-nothing baseline rises from 0.491 to 0.631. Most of
the impressive margin was bookkeeping about students the registry had already lost. Which number goes
in the abstract is a reporting decision, and it is yours.

**Going further (optional): auditing a group nobody asked about.** Point the same audit at
`age_band`, `gender`, `region`, or `highest_education`, and find a gap nobody asked you to look for.
Nothing later in the notebook depends on this section.

## What Part 2 does, section by section

One recipe, held fixed, run on both settings. Same outcome definition, same algorithm, same
threshold, same protocol, activity and support features only and **no prior grades on either side**,
because `G1` and `G2` would predict `G3` by being a grade and would mirror nothing in Part 1. OULAD
is rebuilt to match: the 1,393 withdrawn enrollments come out, leaving 3,136 that ran to a graded
end, and activity is counted over the first four weeks rather than sixty days. The Portuguese outcome
is `G3 < 10`, the Portuguese pass mark.

**7. One recipe, two settings.** The two models are almost indistinguishable. AUC **0.688** in both.
Accuracy **0.714** in Portugal against a do-nothing rule of 0.671, and **0.724** in OULAD against
0.709. Base rates 0.329 and 0.291. That is an ordinary published early warning model, twice, on two
continents, and the second panel of figure 4 is the part worth sitting with: the do-nothing rule is
four points behind one of them and one and a half points behind the other.

The grouping column gets a paragraph of its own, because it has to. Portugal is audited by the higher
of the two parents' education, split at 9th grade, 135 students against 260. OULAD is audited by the
student's own prior qualification, split at A level, 1,355 against 1,781. Those are not the same
construct, one being a fact about a household and the other a fact about the adult sitting the
module, and the notebook says so rather than letting "educational background" quietly cover both.
Neither column is a description of a person: both are records of how much formal schooling somebody
in the file completed, in a country and a decade, under conditions the file does not describe.

**8. The seed lottery.** Before any fairness claim, a demonstration. The notebook measures one
quantity, the rural minus urban false positive gap in the Portuguese file, two hundred times under
each of two protocols. Under a single stratified 70/30 split, changing nothing but the seed, the
answer ranges from **-0.169 to +0.457**, standard deviation 0.098, with 65.5 percent of seeds saying
rural students who passed were flagged more often and the rest saying the opposite. **Seed 42 gives
+0.327, larger than 99 percent of the other 199 seeds.** Under the protocol the notebook actually
uses, twenty-five fresh five-fold splits averaged, the two hundred answers all land between +0.004
and +0.064.

Then the cell says what the tight histogram does not mean, because this is where people over-read.
All 200 of those runs measure the same 395 students, so they agree by construction. The averaged gap
on the whole file is **+0.027 with a 95 percent bootstrap interval of [-0.065, +0.125]**, which
contains zero. Repeating the split removes the seed. Only the bootstrap shows you the students. Both
are needed, and 55 rural students passed in total. One framing note travels with the comparison:
`address` records whether a student's home was rural or urban, so a gap across it is, in the first
instance, evidence about those places and their schools rather than about the students living in
them, and the subject of the section is the protocol rather than the comparison.

**9 and 10. The audit, and what traveled.** Five metrics, two settings, every rate beside the
denominator it rests on, every gap with a 95 percent bootstrap interval, figure 6 plotting all ten at
once against a line at zero.

- **The accuracy gap replicates.** Lower band minus higher band is **-0.117, 95% [-0.214, -0.020]**
  in Portugal and **-0.150, [-0.182, -0.120]** in OULAD, and it survives a random forest and gradient
  boosting in both settings.
- **The false alarm gap does not.** Portugal: **+0.115, [+0.025, +0.209]**, from 0.185 against 0.071.
  OULAD: **+0.009, [-0.006, +0.024]**, an order of magnitude smaller and straddling zero.
- **The share flagged clears zero in both**, at **+0.113, [+0.030, +0.199]** in Portugal and
  **+0.017, [+0.001, +0.035]** in OULAD. This is the row the person on the receiving end experiences.
- **Being missed is close to even in both**, at -0.041 and +0.017, both intervals containing zero, on
  models whose false negative rates are 0.63 and 0.67 in Portugal and 0.88 and 0.86 in OULAD. The
  OULAD model misses about seven of every eight enrollments that ended in a Fail, evenly. A fairness
  metric can be satisfied by a model that does not work.

Counting only the intervals that clear zero: three of the five gaps do so in Portugal and two in
OULAD. Neither line is a summary of whether the model is fair. Each is a summary of which question
somebody chose to ask.

The OULAD null carries one qualification worth keeping attached to it. It is measured on the 3,136
enrollments that ran to a graded end, and the 1,393 that were dropped did not come evenly from the
two bands: 771 of the 2,126 below-A-level enrollments withdrew, against 622 of the 2,403 at A level
or above, a withdrawal rate of 0.363 against 0.259. It is still by far the better-powered of the two
audits, and it is not the clean comparison a tidy version of this story would want.

**11. What the accuracy gap is made of, and what cannot be settled.** Two stories produce the same
accuracy gap: base-rate arithmetic, or a genuine measurement failure. The notebook separates them.
Put each band's own do-nothing rule beside its accuracy and the gap between the two lifts is
**-0.009, [-0.109, +0.086]** in Portugal and **+0.015, [-0.003, +0.032]** in OULAD. In both settings
the accuracy gap that replicated so convincingly is, once the base rate is accounted for, no longer
distinguishable from zero.

AUC is the base-rate-free version. In OULAD the two bands rank identically, 0.687 [0.656, 0.716]
against 0.689 [0.659, 0.719]. In Portugal the point estimates differ a great deal, 0.624
[0.525, 0.718] against 0.728 [0.659, 0.793], and the gap of -0.104 has an interval of
[-0.226, +0.020] that contains zero, on 135 students of whom 81 passed and 54 did not. The same gap
shrinks from -0.100 to -0.058 and -0.054 when the model class changes. So the contested question,
whether these instruments genuinely read students in the lower band worse or whether this is what 135
students look like when you cut them in half, **does not get an answer**, and the notebook says so
rather than picking one.

Then the last turn. Week 1's 38 zero grades are not spread evenly: **21 of the 135 students in the
lower band against 17 of the 260 in the higher band**, 15.6 percent against 6.5 percent, Fisher exact
p = 0.006. Rerun the whole of setting two without them and the one clean finding, the false alarm
gap, falls from **+0.115 [+0.025, +0.209] to +0.046 [-0.028, +0.124]** and stops clearing zero. Those
38 records are not in the false alarm comparison at all, since a false positive rate is computed among
students who passed and a recorded grade of zero is a `did_not_pass` row: the denominators are 81 and
184 either way. The gap moved because those rows were in the model's **training** data. The audit
measured a model, and part of what it measured was a filing cabinet.

**Your turn 4.** Point the same two-group audit at any column of the Portuguese file. `sex` is the
working default and it produces a gap nobody went looking for: a false negative gap of **+0.219,
[+0.053, +0.378]**. The notebook frames that as an exercise in reading a recorded group difference
cautiously rather than as a finding about either group: `sex` here records a category on a school
form, and the file holds nothing about who taught which class or how grading was done. `higher`
splits 375 against 20 and the 20 contribute 7 students who passed, which is what a fragile rate looks
like. Three of the offered columns are model inputs, and the cell says so in its heading when one of
them is picked.

**Why the course runs the audit twice.** One replication, one failure to replicate, and one metric
that was clean in both settings on models that miss most of the students they are looking for. A
single-setting fairness result is a hypothesis, and the next thing anyone might do with it is take
the recipe somewhere else. The section closes with a short coda pointing at week 5, where the same
audit runs on **human raters** rather than a model, using PERSUADE 2.0. You cannot rerun a rater with
a different seed.

**Reflection.** Seven prompts tied to this week's readings and to both datasets. They are for
talking rather than for uploading, and nothing from them is collected. The discussion hour runs
before the notebook, so these belong to the closing minutes of the session and to week 4.

## Going further (optional)

For anyone who finishes early, or who arrives with programming experience, or who wants a thread for
a course project. None of this is part of the session.

1. **Threshold sweep.** Instead of one cutoff, sweep the threshold from 0.05 to 0.95 and plot the
   share-flagged gradient across the deciles against the threshold, with bootstrap intervals. Is
   there any threshold at which the activity-only model closes it? What does that imply about "just
   tune the cutoff" as a remedy?
2. **Move the checkpoint.** The notebook looks at days 0 to 60. Rerun it at day 30 and at day 120.
   Accuracy climbs steadily with the window, and so does the circularity, since students who withdraw
   stop clicking. Where would you stop, and why?
3. **Build a better regularity feature.** `active_days` penalises compressed schedules. Design a
   feature that captures "this student has stopped showing up" without penalising "this student
   studies in long blocks," compute it from `studentVle.csv.gz`, and audit a model that uses it. Gaps
   between consecutive active days are a good place to start.
4. **A different model for the gradient.** The notebook fits weighted least squares to ten proportions
   and bootstraps it. Fit a logistic regression of the flag on decile number at the enrollment level
   instead, cluster the standard errors by person, and compare. Does the more conventional model say
   anything the ten-point line did not, and is it easier or harder to explain to an advising office?
5. **Calibration, not just error rates.** Bin the predicted probabilities and compare predicted
   against observed non-completion rates separately for each decile. A model can have equal
   calibration and unequal error rates at the same time, and the fact that the two cannot generally
   both hold is a well-known impossibility result worth reading about. Section 4 is that result
   showing up in a real table.
6. **Split the label.** `did_not_pass` merges Fail and Withdrawn. Build two models, one for each, and
   compare which enrollments each one finds. If they disagree, the single label was hiding two
   different phenomena and one intervention was never going to serve both.
7. **Use the resource catalog.** `vle.csv` says what kind of thing each `id_site` is: forum, quiz,
   resource, subpage, and more. Build features from *what* students clicked rather than how much, and
   audit that model. Does looking at the kind of activity rather than the amount change who gets
   flagged?
8. **A third setting.** The same repository holds `student-por.csv`, the Portuguese-language course
   from the same project, 649 students, many of whom also appear in the mathematics file. Run the
   Part 2 recipe on it unchanged. Then consider what the overlap between the two files does to the
   phrase "replicated in a third setting," and how you would report it.
9. **Sweep the threshold in both settings at once.** Section 8 fixed the threshold at 0.50. Sweep it
   and plot the false alarm gap against the threshold for both settings on one pair of axes, with
   bootstrap intervals. Does the Portuguese gap survive every threshold, and does the OULAD gap appear
   at any of them?
10. **Match the sample sizes.** Much of the difference between the two audits is that one rests on 395
    rows and the other on 3,136. Subsample OULAD down to 395, repeatedly, and see how often its false
    alarm gap would have looked like Portugal's by chance. That is the cleanest available test of
    whether the two settings really differ or whether one of them is simply better measured.
11. **Calibration by band, in both settings.** Bin the predicted probabilities and compare predicted
    against observed rates inside each education band, in Portugal and in OULAD. Equal calibration and
    equal error rates cannot generally both hold when base rates differ, and here they differ by 11
    and 17 points.

## Troubleshooting

**"Could not download the OULAD files." or "Could not download the second dataset."**
Both download cells print a message naming `github.com/HakeoungLee/edis8100-datasets` and three
likely causes, rather than a traceback. In order of likelihood: this machine is offline or the campus
network is blocking `raw.githubusercontent.com`; GitHub is briefly unhappy, so wait a minute and run
the cell again; or you are on a restricted network, in which case the notebook is worth opening in
Google Colab instead. The Part 2 cell is a separate download, so it can fail on its own even if Part 1
worked half an hour earlier. That repository is public, so this is never about a GitHub account or an
invitation.

**"NameError: name 'data' is not defined" or something similar.**
A cell ran out of order, or the download cell failed and the run carried on anyway.
**Runtime > Restart session and run all** in Colab, or **Kernel > Restart & Run All** in Jupyter. This
resolves the large majority of notebook problems.

**The Portuguese file loaded as one enormous column.**
`sep=";"` was changed or dropped. That file is semicolon delimited, and pandas does not warn you: it
hands back a single column of 33 things glued together and no error at all. It is worth doing once on
purpose so the shape of the mistake is recognizable later.

**Section 8 is the slowest cell in the notebook.**
That is correct. It fits the model 200 times under one protocol and 5,000 times under the other, and
the wait is the argument of the section. The whole notebook runs end to end in under a minute.

**My charts do not appear.**
The first code cell contains `%matplotlib inline`, so it needs to have run. If they still do not
appear, restart and run all.

**The cell shows `[*]` and nothing happens.**
It is still running. If `[*]` persists for several minutes on a cell other than section 8, the runtime
has probably disconnected: **Runtime > Restart session and run all**.

**Colab says "Cannot find notebook" or shows a 404.**
You are most likely signed into a different Google account. Check the profile picture in the top right
corner, switch to the account you want, and open the link again.

**My numbers do not match the ones in the text.**
If you changed a **Your turn** cell, that is expected and good. If you did not, restart and run all.
Both downloads are fixed snapshots, every fold sequence is seeded, and every bootstrap function
carries its own generator, so running a cell twice or out of order cannot change the interval it
prints. A clean run reproduces the same numbers every time.

**My numbers differ from my neighbor's.**
Compare feature lists first, then thresholds. That is almost always the difference, and noticing it is
one of the points of the session.

**Red text appeared.**
Python errors are wordy, and none of them means something has been damaged. This runs on a temporary
machine in the cloud, on a copy of two published files, and nothing on your computer is touched. The
**last line** of the error usually names the real problem. Please ask, and we will read it together.

## Documenting AI use

The course permits AI use in designated activities and asks that you document it. Undisclosed AI use
is an Honor Code violation.

There is **nothing to submit this week**, so there is nothing to document. It is still worth starting
the habit. Beginning with Mini Project 1 in week 4, every mini project and every course project
milestone asks for an **AI Reflection** submission on Canvas, with two parts in two places:

- **The conversation record goes in a Word file, attached to the submission.** The full exchange,
  across every tool and every session, pasted in rather than summarized.
- **The reflection goes in the Canvas text box**, where you copy in the four questions from the
  syllabus and answer each one: how you used it; whether it helped and how; whether it made your work
  more challenging in any way; and what lesson about AI you would pass on to a friend or the class.

If you use an assistant to make sense of anything in this notebook, please save the transcript.
Reading what an AI tells you about data, with appropriate care, is itself a course skill.

## Connections to this week's readings

The required readings are Tsai and Martinez-Maldonado (2022), Holstein and Doroudi (2022), Borchers,
Liu, Lee and Zhang (2024), and Lee and Gargroetzi (2023). The notebook draws on them briefly at four
points, and the reflection returns to them:

- **Tsai and Martinez-Maldonado (2022)**, *Human-centered approaches to data-informed feedback*:
  information is not feedback until somebody is in a position to act on it, and the conditions for
  acting are part of the system rather than a separate matter. The humans around the system include
  the ones who choose the features and the ones who choose the dataset. An accuracy figure says
  nothing about any of that.
- **Holstein and Doroudi (2022)**, *Equity and artificial intelligence in education*: what a narrow
  fairness metric can and cannot see, and why equity does not collapse into algorithmic fairness.
  Section 4 is the concrete version: three fairness numbers, three different answers, about the same
  predictions.
- **Borchers, Liu, Lee, and Zhang (2024)**, *Ethical AIED and AIED ethics*: the distinction between
  conducting AIED research ethically and studying the ethics of AIED, and where in a workflow like
  this one an ethical framework would have to intervene. The naming decision sits in both strands at
  once.
- **Lee and Gargroetzi (2023)**, *"It's like a double-edged sword": Mentor perspectives on ethics and
  responsibility in a learning analytics-supported virtual mentoring program*: what it is like on the
  receiving end of a flag, for the mentor as well as for the student. The metaphor in the title comes
  from a participant rather than from the authors.
- Among the additional readings, **Uttamchandani and Quick (2022)** is the short account of why
  fairness, absence of bias, and equity name three different commitments, and it is the vocabulary
  section 2 uses. **Alfredo and colleagues (2024)** map how the field has operationalized the label
  "human-centered." **Kizilcec and Lee (2022)** survey the formal fairness criteria for educational
  prediction, including why they conflict with one another, and it is the closest companion to this
  notebook.
- **Kuzilek, Hlosta, and Zdrahal (2017)** and **Cortez and Silva (2008)** are not on the reading list,
  and both are worth skimming. They are the papers that made this session possible, and reflection
  prompt 5 asks what you would require of anyone who downloaded a dataset like either of them from
  your own institution.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across
the lab weeks, and no notebook in this course generates a row.

Today's files hold records for several thousand adults who enrolled in a distance-learning module in
2013 and 2014, and for 395 teenagers in two Portuguese secondary schools in 2005 and 2006. Their
records were anonymized and published under CC BY 4.0 so that others could learn from them, which is
what we are about to do, and the only reason either file can be opened at all is that somebody chose
to release it.

None of them agreed to be a teaching example. It is worth asking who could be harmed by a claim
before making it, noticing when a metric reduces a person to one number, and noticing which people
are not in the file at all. That stance runs through every week of the course.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*

Both datasets are used under CC BY 4.0, with attribution and no modification to the published files.

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset.
*Scientific Data, 4*, 170171.

Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance.
In *Proceedings of 5th FUture BUsiness TEchnology Conference*, 5-12.
