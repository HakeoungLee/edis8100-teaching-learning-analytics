# 🕸️ Week 8: Mini Project 4, Networks and Temporal Learning Analytics

Who answered whom, who was still in the room in week 20, how early a term becomes legible, and what it feels like when real data refuses to agree with you.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 21, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Cacophony of Networks in Learning Analytics and Temporal Learning Analytics |
| **Guest speaker** | Yukyeong Song, University of Tennessee, Knoxville |
| **In-class time on this notebook** | About 20 minutes, launched in the studio block (4:40 to 5:00). This is a launch, not a completion. Plan on finishing at home. |
| **Deliverable** | **Mini Project 4**: the completed notebook, the network reading memo (600 to 750 words), and the reflection answers. The AI interaction log and reflection are a separate Canvas submission. |
| **Due date** | This week, via Canvas. Check the assignment page for the exact time. |
| **Notebook** | `week08_miniproject4_networks_temporal.ipynb` |
| **Data used, real** | **Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J.** 4,529 enrolments, 18 assessments, 21,783 assignment submissions, 891,062 rows of daily click data, 528 course resources. Licence: **CC BY 4.0**. Cite as Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. Loaded over the internet by the notebook's first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `oulad-bbb`. No account, no password. |
| **Data used, synthetic** | `students.csv`, `forum_posts.csv`, `gradebook.csv` (built by the notebook itself, no download). Only the network half and the "state your expectation" step use these. |
| **Libraries** | pandas, numpy, matplotlib, networkx, scikit-learn |
| **Needs internet?** | **Yes**, for the first code cell only. About four megabytes across six files, a couple of seconds. |

## Objectives

By the end of this activity you will be able to:

1. **Build** a reply network from forum posts with `networkx`, and defend the three modeling decisions that produced it: what counts as a tie, whether direction matters, and who is in the graph at all.
2. **Distinguish** degree centrality from betweenness centrality, and identify the students who bridge one part of a class to another rather than the students who are simply everywhere.
3. **State** the origin, licence, and citation of a real dataset before analyzing it, and name what its collection process makes visible and what it makes impossible.
4. **Carry out** a temporal analysis of a real module from end to end: a Kaplan-Meier survival curve built by hand from 647 withdrawal dates, with delayed entry and right-censoring handled explicitly; a prediction horizon that shows, with a paired resampling check reported two ways, how much each extra week of waiting actually buys and whether you would see it in any single split; and four trajectory clusters recovered from a 1,836 by 35 weekly click matrix, with the diagnostics that say how much to trust them.
5. **Test** a hypothesis you actually hold against 15,347 real assignment submissions, find an effect an order of magnitude smaller than the one you expected, and work out which part of that gap belongs to the students and which part belongs to how the comparison was assembled.
6. **Write** a network reading memo that reports the structure, names the connectors, describes the term as a temporal object, answers what accuracy would justify contacting a student, states the real result you did not get, accounts for the people the analysis cannot see, and confronts what it means that one half of the notebook had to be simulated.

The through-line of the session: a total throws information away, and this week you get two demonstrations of exactly what. A count of posts throws away who answered whom. A count of clicks throws away when: who was still enrolled, how early you could have known, and what shape the term had. Both discarded pieces turn out to matter more than the count did.

The second through-line, and the one that will stay with you longer: **the data you have practised on for six weeks was built to contain its answers, and the world is not.**

## Where the data comes from, and why one half is invented

This is the first notebook in the course that runs on real data, and it runs on real data for exactly half its length. Both facts are deliberate.

**The temporal half is real.** The Open University is a large distance-teaching university in the United Kingdom. It already stored every click its students made. In 2017 a research team there anonymised a slice of that record, obtained clearance to publish it under an open licence, and released it so that people outside the institution could study learning at scale. The students were adults, the release is legal and widely used, and they were not asked. That is the ordinary condition of learning analytics data, and this notebook asks you to feel the weight of it once before you go looking for a dataset for your own project.

Notice what anonymisation cost. No names, no free text, no timestamps finer than a day, no way to ask anyone what they meant. Every limitation the notebook runs into in Part 2 descends from a decision someone made in order to be allowed to share this at all.

**The network half is synthetic, and saying so out loud is part of the lesson.** A reply network needs one specific column: for every post, the identity of the post it answers. Open, downloadable education datasets almost never carry it. OULAD is the demonstration, and the notebook checks it rather than asserting it: the real course site has 22 discussion resources carrying 247,859 rows of activity and 892,495 clicks, and not one arrow you could draw between two people. The text is where the ties live, and the text is what gets removed, because discussion text is identifying in a way that click counts are not.

The corpora that do preserve threading generally sit behind a data use agreement: a signed document, an institutional affiliation, a named principal investigator, sometimes review board approval and a wait of weeks or months. So the practical fact for your course project is this: **a classmate who wants real network data will be filing a data use agreement, not clicking a download link.** Start early.

## What is in this folder

| File | What it is |
|---|---|
| `week08_miniproject4_networks_temporal.ipynb` | The notebook. Downloads the real data in its first cell, then builds its own synthetic forum. Runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook, and it holds only the three synthetic files. Not stored in the repo. |

You do not need to clone anything or download a CSV by hand. The first code cell fetches the real data; the second writes the synthetic files into the runtime.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week08-miniproject4-networks-temporal/week08_miniproject4_networks_temporal.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week08-miniproject4-networks-temporal/week08_miniproject4_networks_temporal.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week08-miniproject4-networks-temporal/week08_miniproject4_networks_temporal.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. This is a graded mini project, so make the copy first and work in it. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and networkx, all of which ship with Anaconda, plus a working internet connection for the first cell. Note that the dataset repository is public, so the first cell works even if you are not signed in to GitHub.

## Step-by-step walkthrough

This is the largest of the four mini projects. **In class you will get about 20 minutes**, which is enough to reach the end of section 1.5 (the scatterplot that puts degree and betweenness on one picture). Everything from section 1.6 onward is homework. **Budget about 150 minutes in total**: roughly 105 minutes running and reading the notebook, then about 45 more for the memo and the reflection. The optional stretch section adds about 10.

The six ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. The mini project asks you to edit each of them at least once anyway.

### Setup: two data sources, and a dataset card

**⚙️ Read the dataset card, then run the first code cell (2 minutes).** Before any code, a short table gives the name, collector, licence, citation, and one-line origin story of the Open University data. The expectation from this week on is that you can say where your data came from. Never analyze data whose origin you cannot state. Then run the first code cell: it downloads six tables and prints what arrived, including 4,529 enrolments and 891,062 rows of click data. If your internet is down, that cell prints a plain-English explanation naming the dataset repository rather than a traceback.

**📊 Why the network half is synthetic (3 minutes).** A short cell counts the real forum activity in OULAD: 22 discussion resources, 247,859 rows, 892,495 clicks, and six columns that contain no post, no parent, and no thread. The interpretation prompt asks what was removed to make the file publishable, who benefits from that removal, and what you would have to start doing this month if a real forum network were the centrepiece of your course project.

**⚙️ The synthetic setup cell (1 minute).** Long, collapsible, meant to be ignored. It writes `students.csv`, `forum_posts.csv`, and `gradebook.csv` into the runtime in under a second. The gradebook is there because Part 2 holds the synthetic result and the real result up against each other.

### Part 1: the forum as a network (synthetic)

**📊 1.1 What is actually in the forum (2 minutes).** 1,456 posts in 60 threads, of which 1,396 are replies. The column that makes a network possible is `parent_post_id`, and it is exactly the column the real data does not have. Note the number the section ends on: 102 of the 120 students posted at least once, so **18 students made no ties and will not appear in the network at all**. Everything you say later has to survive that sentence.

**📊 1.2 Turning replies into edges (3 minutes).** Three modeling decisions, all arguable, all stated out loud before the code runs: a reply counts as a tie, self-replies are dropped, and ties are undirected and weighted by how often the pair exchanged replies. Read this section rather than skimming it. Your memo will be graded partly on whether you can defend these choices.

**📊 1.3 Building the graph (3 minutes).** The graph describes itself: 102 nodes, 752 edges, density 0.146, one connected component, average degree 14.75, and an average shortest path of 2.43 hops. Sparse, but nobody is stranded.

**📊 1.4 Two ways of being important (4 minutes).** Two histograms and two top-8 lists. Degree counts your ties. Betweenness counts how often you sit on the shortest path between two other people. S039 tops both lists with 36 ties. S020 is third on betweenness with a degree of 18, which is nowhere near the top of the class. That disagreement is the section.

**📊 1.5 Putting the two measures on one picture (4 minutes).** Degree on the horizontal axis, betweenness on the vertical, with reference lines at the median degree and the 90th percentile of betweenness. Five students sit in the upper left region: high betweenness, unremarkable degree. **This is the natural place to stop in class.**

**📊 1.6 Finding the communities (3 minutes).** Greedy modularity optimization splits the graph into three communities of 36, 34, and 32 students, with a modularity of 0.612. Of the 752 ties, 700 stay inside a community and only 52 cross between them. Those 52 ties are the rest of Part 1.

**📊 1.7 Bridges, not hubs (4 minutes).** For each student, the share of their ties that leave their own community. Four students clear the cutoff: S020 at 0.78, S101 at 0.53, S031 at 0.47, and S043 at 0.42. None of them is the highest degree student in the class, and all four sit at or above the 94th percentile of betweenness (98th, 97th, 96th, and 94th).

**📊 1.8 The sociogram (5 minutes).** The whole graph drawn with a seeded spring layout, so your picture matches your neighbor's exactly. Color is community, size is degree, gray lines stay inside a community, heavy black lines cross between them, and the four connectors are ringed and labeled. Read the interpretation prompt carefully: it asks you where the other 18 students are in this figure.

**✏️ Your turn 1: move the connector thresholds (3 minutes).** Change the minimum degree and the bridge share cutoff and watch the list change, which in this forum means watching it not change: the four connectors sit at 0.78, 0.53, 0.47 and 0.42, the next student down sits at 0.20, and any cutoff from 0.25 to 0.42 returns the same names. Section 1.7 now prints that gap so it is checkable rather than asserted. Setting the minimum degree to 2 admits nobody either, because all seven low-degree students have a bridge share of exactly zero here. A guard that does not fire is still worth having, and saying out loud that it did not fire is part of the exercise.

**✏️ Your turn 2: one week at a time (3 minutes).** Rebuild the network from a single week. Week 3 alone has 177 posts, 74 students, and 147 ties, and the betweenness ranking bears almost no resemblance to the pooled one. That instability is a result about the measure, not a bug in your code.

### Part 2: four questions about time (real)

Everything from here runs on the Open University data, and it is a full temporal analytics project in four movements. Movements 2A, 2B and 2C follow **one presentation**, 2013J, 2,237 enrolments, because a survival curve and a weekly trajectory only mean something if everyone in the picture is on the same calendar. Day 0 is the first day of teaching, and negative days are real. Movement 2D pools both presentations and checks that decision.

**⚙️ 2.0 One module, one presentation, one clock (2 minutes).** Builds the working tables: the 2013J roster, the registration and withdrawal dates, 1,378,656 clicks running from day -23 to day 268, and the six tutor-marked deadlines at days 19, 47, 96, 131, 166, and 208. Of the 2,237 enrolments, 1,870 clicked something at some point and 1,836 clicked on or after the first day of teaching.

#### 2A. Who is still here? (about 20 minutes)

**📊 2A.1 A withdrawal date, not a withdrawal flag (3 minutes).** `date_unregistration` is not a yes or no marker, it is the day the student left, on the same clock as everything else. 647 of 2,237 enrolments have one, which is 28.9 percent. The dates run from day -178 to day 241 with a median of day 0. **234 of them are negative**, 102 fall on day 0 itself, and 22 land after the last assignment deadline. The roster says 644 Withdrawn and the date column says 647, so three enrolments carry a withdrawal date and a `Fail`, which is the first thing the interpretation prompt asks you to argue about.

**📊 2A.2 The survival curve, built by hand, twice (8 minutes).** No `lifelines` dependency, and two estimators side by side so that the difference between them is the lesson.

**Version 1, the naive proportion**: for each day, the share of all 2,237 enrolments with no withdrawal date yet. It is what a great many published "survival" figures actually are, and it assumes everyone was at risk from the first day of the x axis, which is false here.

**Version 2, Kaplan-Meier**, computed by hand with **delayed entry and right-censoring**. `date_registration` runs from day -198 to day **+32**, so somebody who registered on day 32 must not sit in the denominator on day 10: that is left truncation, and the risk set has to move. Everyone with no withdrawal date is censored on day 268, the last day the click file covers. `S(t)` is the running product of `1 - d(t)/n(t)` over event days.

The two curves separate by **8.4 percentage points** at the end of observation, and the naive one is the optimistic one: 71.1 percent against a Kaplan-Meier estimate of **62.7 percent**. The printed at-risk column shows exactly why. Every row of that table now carries a **Greenwood interval**, so the endpoint reads 62.7 percent [58.9, 66.2] rather than 62.7 percent: an estimator without a width is not finished. **Censoring is taught explicitly**: a student with no withdrawal date has not "not withdrawn", the file simply stopped looking, and the 62.7 percent figure is a statement about people who were still being watched on day 268, not about people who finished.

**📊 2A.3 The 234 who left before teaching started (5 minutes).** The decision the notebook refuses to make for you. Either those 234 belong in the denominator, because a module that loses a tenth of its intake before the first session has a problem worth naming, or they are not part of this population at all. Only 19 of them ever clicked anything, and the median gap between registering and unregistering is 59 days. Both curves are drawn on one axis: the same module is 28.9 percent withdrawal on 2,237 people and 20.6 percent on the 2,003 who reached day 0. **The same module, honestly measured twice, differs by 8.3 points.**

**📊 2A.4 Splitting the curve (5 minutes).** Withdrawal by deprivation decile, with a Wilson interval on every band because the bands hold 142 to 298 enrolments, plus Kaplan-Meier curves for three aggregated groups. The gradient is real and it is not a clean ladder: 34.9 percent [29.7, 40.5] in the most deprived decile and 22.4 percent [17.3, 28.6] in the 60 to 70 percent band, but the highest rate of all is 36.4 percent in the 20 to 30 percent band and the least deprived decile sits at 28.9 percent with an interval running from 22.1 to 36.8. Much of the apparent zigzag is covered by overlapping intervals, so the object here is **a gradient across ten bands**, not ten separate findings. The three aggregated curves then get an interval on the **difference** rather than three overlapping bands, because comparing two curves by eye for overlap is the wrong test and the commonest one: least minus most deprived is +8.1 points [+0.1, +16.1] on the whole register, and +9.5 points [+4.8, +14.2] among those who reached day 0, where the estimate is three times as precise because it is not carrying a handful of pre-teaching leavers on risk sets of twenty. The most deprived third separates from the other two before teaching begins and never closes the gap, which is the part that matters: a difference established before any teaching happened is evidence about the conditions under which people enrol and study, not about the people.

**✏️ Your turn 3: split the curve by something else (3 minutes).** One variable to change. `highest_education` runs from 40.7 percent withdrawal among the 27 students with no formal qualifications down to 22.9 percent among the 245 who already hold a higher education qualification, with a five-person postgraduate group sitting at zero. `disability` gives 34.2 percent against 28.3. And the default `age_band` contains a group of **two people** whose curve drops to 50 percent in a single step. Watching group sizes is the exercise.

#### 2B. How early is early enough? (about 20 minutes)

**📊 2B.1 One model, many windows (9 minutes).** The same plain model fitted nine times, each time seeing one more slice of the term: two features (log cumulative clicks, cumulative active days), one outcome (`Fail` or `Withdrawn`, 52.1 percent of the cohort), AUC from **ten repeats of five-fold cross-validation**, so fifty fold scores per window. The curve rises fast and then flattens: **0.724 with one week, 0.753 at two, 0.769 at four, 0.806 at eight, 0.854 at twenty, 0.897 with the whole term.**

Then the check that a rising line does not survive without: **paired differences between consecutive windows on the same folds, reported two ways, because the two answer different questions.** The interval on the *mean* gain, widened by the standard correction for folds that share training data (Nadeau and Bengio, 2003), clears zero at every step: nothing on this curve is a rise out of nothing. The *spread* of the fifty individual fold differences straddles zero at two steps, week 2 to 3 and week 3 to 4, where three splits in fifty come out the wrong way and the gains are worth 0.010 and 0.005 AUC. The honest sentence is not "the climb is noise", it is "the climb is real, smaller than the wobble between folds, and far too small to buy with a fortnight". Conflating the spread of a resampling distribution with a confidence interval on its mean is a common enough error that the section now names it.

And the denominator returns. Restricting to the 2,003 enrolments still enrolled on day 0 drops the week 1 AUC from **0.724 to 0.674**, because the 234 who left before teaching have zero clicks and a certain outcome, so any model gets them for free. Which of those two numbers belongs in a grant application, and which in the design review for the system that will actually email people in week 2, is a question the section asks and does not answer.

**📊 2B.2 An AUC is not a decision (7 minutes).** Turn the ranking into a list. Flag the riskiest 20 percent and the week 1 list is 80.1 percent correct and catches 33.9 percent of the students who eventually fail or withdraw; the week 20 list is 99.3 percent correct and catches 38.2 percent. Waiting nineteen weeks bought precision and almost no reach. Then the week 3 audit runs again, with a Wilson interval on every rate and a stability table across six fold assignments: students from the most deprived third of neighbourhoods are flagged at 28.0 percent [25.0, 31.1] against 18.5 percent [15.3, 22.2] for the least deprived third, with a week 1 false positive rate of 11.5 [8.5, 15.5] against 5.7 [3.5, 9.1]. The flagging gap is clearly wider than the noise; the false positive intervals only just touch, so "about twice as often, on 833 and 497 enrolments" is as far as the table goes. The section ends on the question it exists to pose and does not resolve: **what accuracy would be high enough to justify telling a student that a model has ranked them among the most likely to fail?** The honest answer depends on what happens next, not on the number.

**✏️ Your turn 4: change what you are predicting (3 minutes).** Each option carries two decisions, the outcome and the denominator, and the cell now prints both. Predicting withdrawal across the whole roster works about as well as fail-or-withdraw (0.727 at week 1, 0.849 at week 20). Predicting failure **among the 1,593 enrolments that did not end in withdrawal** is harder but not hopeless: 0.667 at week 1 and 0.792 at week 20, about six points of AUC behind the withdrawal curve at both. Clicks are better at seeing people leave than at seeing who will not pass among those who stay. And that second population is defined by an outcome nobody knows in week 1, which the cell says out loud.

#### 2C. What shapes does a term take? (about 25 minutes)

**📊 2C.1 The class as one line (4 minutes).** The cohort as a heartbeat: daily clicks with a seven-day rolling mean and the six deadlines. Every deadline has a surge beside it, and the cell prints where each surge actually peaked rather than leaving you to eyeball it, together with the margin: one or two days before the line every time, but by half again at the first two deadlines and by two parts in a thousand at the last, which is a tie and is labelled as one. Busiest day of the presentation is day 2, with 19,872 clicks. Mean daily clicks fall from 9,254 across the first 30 days of teaching to 3,660 across days 180 to 209. There is real activity before day 0, in a course that has not started.

**📊 2C.2 One row per student, one column per week (8 minutes).** The temporal analytics workhorse: a 1,836 by 35 matrix of weekly clicks, log transformed, standardised by week, clustered with k-means at `k = 4`. Three preparation decisions are stated and defended rather than performed.

**The diagnostics run before the choice, and they do not endorse it.** Inertia falls smoothly from `k = 2` to `k = 8` with no elbow. The silhouette score is **highest at `k = 2` (0.32) and falls at every step after it**, reaching about **0.17 at `k = 4`**, which is weak separation. The partition is highly stable across random starts (adjusted Rand 0.92 to 1.00), which means it is reproducible and says nothing about whether it is real. The section states plainly that k-means minimising squared distance looks for roughly spherical, roughly equal-sized blobs, that trajectories are under no obligation to come in blobs, and that what these diagnostics support is a **continuum being cut into four useful steps** rather than four kinds of student being discovered.

The clusters are relabelled by total activity so that everyone's Shape A is the same Shape A, and the labels are **deliberately meaningless** at this point.

**✏️📊 2C.3 and 2C.4 Name them, then look (8 minutes).** You write your own name for each of the four shapes in a markdown cell **before** the outcome table exists, then the outcomes arrive: Shape A, n = 170, 94.7 percent pass or distinction and 1.2 percent withdrawn; Shape B, n = 418, 94.0 percent and 0.5 percent; Shape C, n = 606, 65.2 percent and 10.6 percent; Shape D, n = 642, 19.2 percent and 35.8 percent. **Shape A clicks 2.9 times as much as Shape B across the first six weeks, and the difference in passing is +0.7 points with a 95% interval from -3.4 to +4.7**, which is the week 2 finding returning as a shape rather than a correlation. The honest claim is not "the same rate" but "this file cannot locate the payoff the extra volume was supposed to buy", and every group rate in the section now carries a Wilson interval so the difference between those two sentences is visible. The prompt then asks which of your own names now reads like an accusation, and what naming a cluster authorises a human being to do.

**📊 2C.5 Two students inside one shape (4 minutes).** Both landed in Shape B. Student 574973 logged 1,166 clicks across 198 active days; student 614556 logged 1,160 clicks across 58 active days, 183 of them on one day. Both passed. A cluster hides variation exactly the way a total does, one level up.

**✏️ Your turn 5: choose a different k (3 minutes).** At `k = 2` you get busy and quiet. At `k = 5` a group appears that a ranking on totals could not have produced: about 196 students with a moderate click total of whom only 7.1 percent pass and 45.9 percent withdraw, sitting beside about 507 students with **fewer** clicks of whom 80.3 percent pass. Volume cannot tell those two apart. Shape can. The silhouette at `k = 5` is 0.15, lower than at every smaller k, so the right sentence is "a group the totals could not separate", not "a new kind of student".

#### 2D. The one it cannot see (about 30 minutes)

Now, and only now, the hypothesis. The literature calls it **procrastination**, a disposition inside a person; this file records a **lead time**, the days between a submission arriving and its deadline. The notebook says so before it starts, and keeps the two words apart throughout. It lands differently here than it would have alone: this file has already told you who left and when, how early risk becomes legible, and what four shapes a term takes.

**📊 2D.1 State the expectation, out loud, before you look (4 minutes).** The synthetic course, measured properly on its 960 quiz submissions: Pearson r = 0.418, Spearman 0.42, and Cohen's *d* between the 175 submissions handed in during the final six hours (mean 68.15) and the 752 handed in earlier (mean 77.61) is -0.752. Large by any convention, and pointing the way everyone expects. **Then you write down three sentences predicting the real result before you run anything else.** Leave that prediction in your submitted notebook.

**📊 2D.2 Building the real lead-time table, mess and all (5 minutes).** Two files have to meet, and four things go wrong, each stated out loud with its cost. Two exams have no deadline date recorded at all, so the highest stakes assessment in the module leaves the analysis. The 6,416 computer-marked assignments are a different animal and are dropped, leaving 15,367 tutor-marked ones. Twenty submissions have no score and are dropped. And 146 scores are banked from an earlier attempt at the module, so their submission date is not a date on which that student did that work: those are **kept and flagged**, with a sensitivity check rather than a silent deletion. Analysis set: 15,347 submissions. Lead times run from 209 days early to 174 days late, the median is one day early, 3,613 submissions arrive on the deadline day itself, and 2,292 after it.

**📊 2D.3 The same test, on people who existed (7 minutes).** Pearson r = 0.010, Spearman rho = 0.121, more than ten times larger. The cell tests the obvious explanation for that gap, the long tails, and refutes it: trimming to -14 to 30 days leaves Pearson at -0.004. The real reason is that the relationship is not a line. Cohen's *d* between the 1,619 submissions handed in seven or more days early and the 5,905 handed in on or after the deadline day is **-0.028, 95% CI [-0.083, +0.027]**, while **Cliff's delta on the same two groups is +0.133**: an early submission beats an on-or-after one about 57 times in 100. The two effect sizes disagree in sign because the early group has the higher median (74 against 70), three times the variance, and a long left tail (14.9 percent under 40, against 4.6 percent), so a pooled standard deviation is the wrong yardstick and *d* ends up reporting the tail.

Read the intervals rather than the point estimates, and read which summary produced them. Dropping the banked scores gives r = 0.02, Spearman 0.126, *d* = -0.036, and all 54 submissions arriving more than 60 days early turn out to be banked. The pattern is not monotonic: binned by lead time the means run 67.44 (n = 5,905), 70.17 (n = 5,563), 69.58 (n = 2,001), 70.56 (n = 1,017), and then fall to 64.21 for the 861 submissions that arrived eleven or more days early, while the medians for the same bins run 70, 73, 74, 75, 72. The prompt sends you back to the prediction you wrote in 2D.1.

**📊 2D.4 The two worlds side by side (3 minutes).** The same contrast in both datasets on one axis, now with a 95% interval on every bar. Synthetic: *d* = 0.87 [0.50, 1.25] at three days early, 1.97 [1.44, 2.50] at seven, on fifty submissions against thirty-three. Real: 0.06 [0.02, 0.10] and -0.03 [-0.08, +0.03]. The synthetic intervals are about ten times wider, on data built to contain the answer, which is the point: size and certainty are different axes.

**📊 2D.5 Maybe the unit is wrong (4 minutes).** One dot per enrolment instead of one per submission, because the procrastination literature is usually making a claim about people rather than about Tuesdays. Across 3,496 enrolments, Pearson r = 0.025 [-0.008, +0.058], which contains zero, and Spearman 0.088 [0.053, 0.123], which does not. Then the same people again with **each assignment standardised against itself first**, because averaging raw lead times and raw scores across the six assignments of 2013J and the five of 2014J gives every student a number that partly records which assignments they happened to submit: r rises to 0.101 [0.068, 0.134] and is positive in both presentations. That is a real association and it is still about one percent of the variation in scores. The two students from 2C.5 are marked on the figure: one averages 7.00 days early with a mean score of 77.3, the other -0.33 days early with a mean score of 78.8.

**📊 2D.6 Who is not in the file (4 minutes).** To appear in the submission file you have to have submitted something. **1,033 of the 4,529 enrolments never submitted a single tutor-marked assignment**, and 884 of those withdrew. A further 738 enrolments have not one recorded click. You have already met these people: they are the fall in the survival curve in 2A and most of Shape D in 2C. If the strongest version of the effect lives in the students who never hand anything in, this file cannot see it.

**📊 2D.7 One more place the non-finding could be hiding (4 minutes).** The sharpest section in the movement, and it works in four steps. **Step 1** prints the tutor-marked assessments of both presentations: 2013J sets six, weighted 5/18/18/18/18/18; 2014J sets five, weighted 0/10/20/35/35, on different days. They are not "the same assessment design". **Step 2** runs the naive split and produces the tempting result: **2013J *d* = +0.321 [+0.237, +0.405] on 7,949 submissions, 2014J *d* = -0.105 [-0.180, -0.031] on 7,398**, two cohorts of one module disagreeing in sign with intervals that both exclude zero. **Step 3** asks what is inside those groups and finds that 53.6 percent of 2014J's "seven or more days early" submissions belong to assessment 15020, the zero-weight opener, which has the lowest mean score in the module (58.9 against 70.0 elsewhere); drop that one assessment and 2014J's *d* goes from -0.105 to +0.224. **Step 4** compares every assessment with itself and pools the eleven comparisons inverse-variance: **pooled *d* = +0.220 [+0.159, +0.280], with 2013J at +0.334 and 2014J at +0.107.** Ten of the eleven within-assessment comparisons are positive. The sign disagreement was the pooling, not the cohorts: it is Simpson's paradox, produced by comparing groups drawn from different mixes of assignments, and the repair is one `groupby`. The lesson generalises past this dataset, and it is the reason the section exists.

**✏️ Your turn 6: move the boundary (4 minutes).** Eight thresholds, three answers on every row. Cohen's *d* runs from +0.099 at one day early to -0.205 at fourteen and changes sign along the way. A **cluster bootstrap that resamples the 3,496 students instead of the 15,347 rows** widens every interval, because a student who submits six times is one person six times. **Cliff's delta** is positive at all eight thresholds and never changes sign. The practical non-result is robust to all three: no threshold, no unit and no effect size produces something worth an intervention.

The statistical picture is sharper than "nothing happens", though, and the cell says so. **Five of the eight thresholds produce a naive interval that excludes zero; four do once the bootstrap resamples students rather than rows; and on ranks, six do and all of them point the same way.** So the sign flip belongs to Cohen's *d*, not to the association: "the sign depends on where the analyst puts the line" would have been a claim about students that was really a claim about arithmetic. The researcher-degrees-of-freedom lesson survives and sharpens. You could have reported the threshold that agreed with you, and it would have cleared a significance test.

**📊 2D.8 So what can and cannot be said (6 minutes to read, longer to argue about).** The section opens by writing the closing sentence three ways and keeping only the defensible one. Not "there is no relationship", which claims something about the world. Not "the effect is zero", which the within-assignment comparison contradicts. Not "early submitters score lower", which is available only from the pooled *d* at a ten or fourteen day threshold and which 2D.7 took apart. But: *across two presentations and 15,347 tutor-marked submissions from 3,496 enrolments, work handed in seven or more days before its own deadline scored higher than work handed in on or after it; compared within each assignment and pooled across the eleven, the standardised difference is about +0.22 (95% CI +0.16 to +0.28), or about 57 wins in 100; at the level of a person rather than a submission it is smaller again, r = 0.10 (95% CI 0.07 to 0.13);* **the direction is stable, the size is roughly a tenth of what the synthetic course led us to expect, and nothing here is large enough to act on.** That last clause is what an interval buys and a significance test does not, and how much of the sentence is about the analysis rather than about the students is the point. Five explanations that survive contact with the evidence, none ranked and none settled: the submission date may not measure when work started; these are adult distance learners for whom "early" may mean something different; the very-early group holds two things at once, with the higher median and three times the variance and 14.9 percent of its work under 40; range restriction, since the 1,033 enrolments who never submit are absent entirely; and the possibility that the effect is simply smaller than the field believes, given that the synthetic course produced it at nine times the size. The framing sentence to carry out of the week: **this file showed us a great deal, and about this question it shows something an order of magnitude smaller than the thing the field sells.** Then the closing question: **you had a hypothesis, a plausible mechanism, and a synthetic dataset that confirmed it. What would you need in order to believe that the construct the literature calls procrastination affects achievement in the world?**

**🚀 Stretch: temporal network slices (10 minutes, optional).** Back on the synthetic forum. Weeks 1 to 4 against weeks 5 to 8 as two separate networks: four communities and a modularity of 0.607 in the first half, three and 0.620 in the second, with average path lengths of 2.74 and 2.86. S020 climbs from seventh to second on betweenness. The prompt adds a question you can only ask now: if you ran this on a real forum, which of your conclusions would survive?

**✍️ Network reading memo (about 30 minutes).** Roughly 600 to 750 words, six parts: what the network shows, who the connectors are, the term as a temporal object (2A and 2C), the prediction horizon and what accuracy would justify contacting a student (2B), the result you did not get and what would change your mind (2D), and limits, ethics, and equity, including what it means that one half of this notebook had to be simulated. Required for the mini project.

**💬 Reflection (about 15 minutes).** Six prompts tied to this week's readings, to the ethics of the open dataset, and to the guest speaker's work on fairness in behavioral pattern detection. Graded under the Critical Reflection criterion.

**✅ Submission checklist.** Work through it before you upload. It is short and it catches the things people actually lose points on, including citing the real dataset anywhere you report a result from it.

## Mini Project 4 rubric

One hundred points, five criteria, twenty points each.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Thoughtfully completes data, preparation, analysis, and interpretation with coherence. | Completes most stages clearly. | Some stages incomplete or weakly connected. | Workflow is minimal or fragmented. |
| **Data Preparation and Technical Care** | Careful, transparent, and well-documented preparation decisions. | Appropriate preparation with documentation. | Partial or uneven preparation. | Minimal or unclear preparation. |
| **Analysis and Visualization Choices** | Methods and visuals are well-justified and aligned with questions. | Analyses and visuals are appropriate. | Partial misalignment or clarity issues. | Inappropriate or missing analyses. |
| **Interpretation and Educational Meaning** | Interpretation connects findings to learning, teaching, or decision-making. | Interpretation is reasonable and evidence-based. | Interpretation is tentative or weak. | Minimal or absent interpretation. |
| **Critical Reflection: Limits, Ethics, and Equity** | Thoughtfully addresses limitations and ethical and equity implications. | Identifies key considerations. | Mentions considerations superficially. | Does not address considerations. |

Where the points live in this particular notebook: **End-to-End Analytics Workflow** is Part 2 taken as a whole, whether the four movements read as one project (who is here, when can we know, what shapes exist, what this file cannot answer) rather than four disconnected exercises. **Data Preparation and Technical Care** is mostly section 1.2, section 2A.3, and section 2D.2: whether you can say why a reply is a tie, why direction was dropped, which denominator you chose for the 234 and why, and what each of the four drops in the real data cost you. **Analysis and Visualization Choices** is about whether you used betweenness where betweenness was the right tool, and whether you can defend `k = 4`, the 20 percent flag rate, and the seven-day window as choices rather than facts. **Interpretation and Educational Meaning** is where a reported non-effect earns full marks if it is reported honestly and loses them if it is quietly upgraded into a finding. **Critical Reflection** is where the 18 non-posters, the 234 who left before teaching started, the disaggregated week 1 flag list, the 1,033 enrolments that never reach the submission file, and the reason half this notebook is synthetic all belong.

## What this connects to in the readings

- **Poquet and Joksimović (2022)**, *Cacophony of networks in learning analytics*: the same students yield a different graph depending on what the analyst counts as a tie. You made one choice in section 1.2, and the reflection asks you to name a second one and say whose importance would rise under it.
- **Molenaar and Wise (2022)**, *Temporal aspects of learning analytics: Grounding analyses in concepts of time*: time as a container to be filled is not the same construct as time as passage, order, or rhythm. Part 2 uses at least three of these without announcing the switch, and the reflection asks you to say which one the survival curve in 2A rests on, which the rolling engagement chart in 2C.1 uses, and which the timing analysis in 2D.3 uses, then to consider whether that difference is part of why two of them found structure and one did not.
- **Yan, Martinez-Maldonado, Swiecki, Zhao, Li, and Gašević (2025)**, *Dissecting the temporal dynamics of embodied collaborative learning using multimodal learning analytics*: what it looks like to treat sequence rather than frequency as the unit of analysis. The reflection asks you to redesign the submission timing question as a question about sequence, and to say what data OULAD does not have and who would have to agree to collect it.
- **Kuzilek, Hlosta, and Zdrahal (2017)**, *Open University Learning Analytics dataset*: the data paper behind the real half of this notebook. Cite it whenever you report one of these results, and read the reflection question about what open educational data makes possible and what it costs.

Your guest this week, **Yukyeong Song** (University of Tennessee, Knoxville), works on fairness in behavioral pattern detection, which is the seam between this week and week 3. Every threshold in this notebook (the bridge share cutoff, the decision to keep or drop the 234 who left before day 0, the 20 percent flag rate, `k = 4`, the seven-day window) is a place where a group of students could be systematically misclassified. Section 2B.2 makes that concrete: the week 1 flag list has a false positive rate twice as high in the most deprived third of neighbourhoods as in the least.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Keep the direction.** Rebuild the reply network as a `nx.DiGraph` and separate in-degree (how often you got answered) from out-degree (how often you answered someone). Then check the four connectors: are they bridging because they answer across the boundary, or because people across the boundary answer them? Those are different social roles and they call for different responses.
2. **Change the tie definition.** Build a co-thread network instead: two students share an edge whenever they posted in the same thread, whether or not one replied to the other. Run the same community detection and the same bridge share calculation, then compare the connector list against the one you already have. Whoever appears in one list and not the other is a demonstration of Poquet and Joksimović's argument that you can hold in your hand.
3. **Ask whether the communities are about anything.** Cross-tabulate community membership against `major_area`, `first_gen`, and `multilingual`. If a community turns out to be a demographic category, you have a very different and much more delicate memo to write.
4. **Give the real lead time a slope.** For each student in module BBB, fit a line through their tutor-marked lead times across the presentation. Students whose lead time shrinks assignment by assignment are a different phenomenon from students who were always at the deadline. Relate that slope to the score trajectory, and see whether drift and decline travel together where a single average did not.
5. **Bring in who the students are.** Section 2A.4 split withdrawal by deprivation. Do the same to the timing analysis: merge `student_info` onto the per-enrolment table from 2D.5 and re-run the correlation inside `age_band`, `disability`, `highest_education`, and `imd_band`. Watch out: `imd_band` has 29 blanks across the two presentations and one category is written `10-20` while every other one carries a percent sign, so you will have to decide what to do about a label that does not match its own scheme. Say what you decided.
6. **Take range restriction seriously.** Movement 2B predicted fail-or-withdraw. Predict something else: whether a student submits at all. A logistic regression on registration date and first-week click activity, predicting "submitted at least one tutor-marked assignment", asks a question the timing analysis structurally cannot. Then ask what an institution would be entitled to do with the answer.
7. **Compare against a package.** Section 2A.2 computes Kaplan-Meier by hand with delayed entry and right-censoring, and shows it running 8.4 points below the naive proportion. Install `lifelines`, fit `KaplanMeierFitter` with `entry=` set to the registration day, and check that it reproduces the by-hand curve. Check its confidence band against the Greenwood interval the notebook computes by hand, and then extend section 2A.4: it gives the least-minus-most deprived gap at day 268 two ways, about eight points with a wide interval on the whole register and about nine and a half with a tight one among those who reached day 0. Fit a log-rank test or a Cox model with `imd_group` and see whether it tells you the same thing.
8. **Join 2A to 2C.** Draw a survival curve for each of the four trajectory shapes. Then notice the trap before you write it up: the shapes were built from weekly clicks, and clicks stop when a student withdraws, so some of what the curves show is definitional rather than empirical. Say precisely how much, and design a version of the analysis that would not have that problem.

## Troubleshooting

**"The download did not work."** The first cell prints this in plain English, with steps, when it cannot reach the dataset repository. The usual cause is no internet connection, a network that blocks GitHub, or GitHub being briefly down. Nothing there needs a password. Check that you are online, re-run the cell, and if that fails open `github.com/HakeoungLee/edis8100-datasets` in a browser tab. If it does not load there either, the problem is outside this notebook.

**"NameError: name 'student_vle' is not defined" or similar.** You skipped or restarted past the first code cell. Use `Runtime > Restart session and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter.

**"FileNotFoundError: data/forum_posts.csv".** The synthetic setup cell did not run. Scroll up and run it, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only there so that the network half works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the short library cell that comes after the synthetic setup cell, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**The sociogram is a hairball and I cannot read it.** That is a fair description of 102 students and 752 ties, and it is the honest picture. The layout is only a reading aid. Every claim you make about connectors should come from the table in section 1.7, not from where a dot happens to land. If you want a cleaner picture, draw one community at a time.

**My sociogram looks different from my neighbor's.** It should not. The layout is seeded (`seed=8100`) and greedy modularity is deterministic, so a clean run is identical for everyone. Check whether one of you ran a ✏️ **Your turn** cell before the sociogram, which changes what is in memory. Restart and run all to compare fairly.

**"ModuleNotFoundError: No module named 'networkx'".** You are running locally without networkx installed. In a terminal: `conda install networkx` or `pip install networkx`. In Colab this cannot happen, networkx is already there.

**The real data cell is slow.** It reads about four megabytes, including a compressed file of 891,062 rows that unpacks to a great deal more. A couple of seconds is normal; ten is fine on a slow connection. It only has to happen once per session.

**Movement 2D gives me almost exactly zero and I think I broke something.** You did not. The pooled Cohen's *d* at seven days really is -0.028, and section 2D.7 then shows that the pooled comparison was drawing its two groups from different mixes of assignments; compared inside each assignment the answer is +0.22, small and positive. Both numbers are the result. The movement lands where it does precisely because 2A, 2B and 2C already found real structure in the same file. If you want to check your code rather than your luck, compare your printout to the numbers in the walkthrough above.

**"ModuleNotFoundError: No module named 'sklearn'".** Movements 2B and 2C use scikit-learn, the same library you used in week 3. In Colab it is already installed. Locally: `conda install scikit-learn` or `pip install scikit-learn`.

**My cluster sizes are off by a student or two from the ones in this README.** k-means is seeded (`random_state=8100`) and the clusters are relabelled by total activity, so Shape A is always the busiest group and a clean run reproduces these numbers. A different version of scikit-learn can move a borderline student between two shapes. The pattern is what matters: Shape A and Shape B differ threefold in early clicking and by +0.7 points [-3.4, +4.7] in passing.

**My weekly network in Your turn 2 gives a completely different top five.** Yes. That is the finding, not the error. A single week holds roughly one eighth of the posts, its density falls to about 0.054 against 0.146 for the pooled graph, and betweenness on a sparse graph is unstable. Say so in your memo rather than picking the week that agrees with you.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox. Note that this applies to the course repository holding the notebook, not to the dataset repository, which is public.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all. The synthetic half is seeded and the real half is a fixed published file, so a clean run reproduces the same numbers every time, for everyone.

**I only got through section 1.5 in class and I am behind.** You are not. That is exactly the plan for the 20-minute launch. Part 2 is designed to be done at your own desk, slowly.

## A reminder about documenting AI use

Mini Project 4 has two Canvas submissions, and it is worth being precise about which piece goes where.

1. **The Mini Project 4 assignment**: your completed `.ipynb` file (in Colab, `File > Download > Download .ipynb`), containing your memo and your reflection answers.
2. **The AI Reflection submission**: this one has two parts, and students routinely reverse them.
   - **The conversation record goes in an attached Word file.** Copy your actual exchanges with the AI assistant into a `.docx` and attach it. Transcripts, prompts, and the responses you got. Not a summary, the record itself.
   - **The four reflection questions are answered in the Canvas text box**, directly, not in the attachment. What you asked for, what you accepted, what you rejected, and how you verified anything you kept.

If you used no AI at all, say so in one line in the text box and attach nothing. That is a complete and acceptable submission.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use costs you nothing.

## Data credits

Real data: **Open University Learning Analytics Dataset (OULAD)**, module BBB, presentations 2013J and 2014J. Licensed **CC BY 4.0**.

> Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171.

Synthetic data: the EDIS 8100 data universe, generated by `data/generate_all_data.py` with numpy seed 8100. Nobody in it exists.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
