# 🕸️ Week 8: Mini Project 4, Networks and Temporal Learning Analytics

Who answered whom, when any of it actually happened, and what it feels like when real data refuses to agree with you.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 21, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Cacophony of Networks in Learning Analytics and Temporal Learning Analytics |
| **Guest speaker** | Yukyeong Song, University of Tennessee, Knoxville |
| **In-class time on this notebook** | About 20 minutes, launched in the studio block (4:40 to 5:00). This is a launch, not a completion. Plan on finishing at home. |
| **Deliverable** | **Mini Project 4**: the completed notebook, the network reading memo (500 to 600 words), and the reflection answers. The AI interaction log and reflection are a separate Canvas submission. |
| **Due date** | This week, via Canvas. Check the assignment page for the exact time. |
| **Notebook** | `week08_miniproject4_networks_temporal.ipynb` |
| **Data used, real** | **Open University Learning Analytics Dataset (OULAD), module BBB, presentations 2013J and 2014J.** 4,529 enrolments, 18 assessments, 21,783 assignment submissions, 891,062 rows of daily click data, 528 course resources. Licence: **CC BY 4.0**. Cite as Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. Loaded over the internet by the notebook's first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `oulad-bbb`. No account, no password. |
| **Data used, synthetic** | `students.csv`, `forum_posts.csv`, `gradebook.csv` (built by the notebook itself, no download). Only the network half and the "state your expectation" step use these. |
| **Libraries** | pandas, numpy, matplotlib, networkx |
| **Needs internet?** | **Yes**, for the first code cell only. About four megabytes across six files, a couple of seconds. |

## Objectives

By the end of this activity you will be able to:

1. **Build** a reply network from forum posts with `networkx`, and defend the three modeling decisions that produced it: what counts as a tie, whether direction matters, and who is in the graph at all.
2. **Distinguish** degree centrality from betweenness centrality, and identify the students who bridge one part of a class to another rather than the students who are simply everywhere.
3. **State** the origin, licence, and citation of a real dataset before analyzing it, and name what its collection process makes visible and what it makes impossible.
4. **Test** a hypothesis you actually hold against 15,347 real assignment submissions, report an effect that is not there, and reason in public about why it is not there without pretending to settle the question.
5. **Write** a network reading memo that reports the structure, names the connectors, states the real temporal result and what would be needed to believe an effect exists, accounts for the people the analysis cannot see, and confronts what it means that one half of the notebook had to be simulated.

The through-line of the session: a total throws information away, and this week you get two demonstrations of exactly what. A count of posts throws away who answered whom. A count of clicks throws away when. Both discarded pieces turn out to matter more than the count did.

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

This is the largest of the four mini projects. **In class you will get about 20 minutes**, which is enough to reach the end of section 1.5 (the scatterplot that puts degree and betweenness on one picture). Everything from section 1.6 onward is homework. **Budget about 110 minutes in total**: roughly 70 minutes running and reading the notebook, then about 40 more for the memo and the reflection. The optional stretch section adds about 10.

The four ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. The mini project asks you to edit each of them at least once anyway.

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

**✏️ Your turn 1: move the connector thresholds (3 minutes).** Change the minimum degree and the bridge share cutoff and watch the list change. The instructive failure is setting the minimum degree to 2, where students with a single crossing tie post a bridge share of 1.0.

**✏️ Your turn 2: one week at a time (3 minutes).** Rebuild the network from a single week. Week 3 alone has 177 posts, 74 students, and 147 ties, and the betweenness ranking bears almost no resemblance to the pooled one. That instability is a result about the measure, not a bug in your code.

### Part 2: a hypothesis that does not survive (real)

Everything from here runs on the Open University data. Do it in the stated order. A hypothesis written after the result is not a hypothesis.

**📊 2.1 State the expectation, out loud, before you look (4 minutes).** The synthetic course, measured properly on its 960 quiz submissions: the correlation between how early a quiz arrived and what it scored is r = 0.418, and Cohen's *d* between the 175 submissions handed in during the final six hours (mean 68.15) and the 752 handed in earlier (mean 77.61) is -0.752. Large by any convention, and pointing the way everyone expects. **Then you write down three sentences predicting the real result before you run anything else.** Leave that prediction in your submitted notebook.

**📊 2.2 Building the real lead-time table, mess and all (5 minutes).** Two files have to meet, and four things go wrong, each one stated out loud with its cost. Two exams have no deadline date recorded at all, so the highest stakes assessment in the module leaves the analysis. The 6,416 computer-marked assignments are a different animal and are dropped, leaving 15,367 tutor-marked ones. Twenty submissions have no score and are dropped. And 146 scores are banked from an earlier attempt at the module, so their submission date is not a date on which that student did that work: those are **kept and flagged**, with a sensitivity check in the next section rather than a silent deletion. Analysis set: 15,347 submissions. Real lead times run from 209 days early to 174 days late, the median is one day early, 3,613 submissions arrive on the deadline day itself, and 2,292 arrive after it.

**📊 2.3 The same test, on people who existed (5 minutes).** r = 0.01. Cohen's *d* between the 1,619 submissions handed in seven or more days early (mean 66.84) and the 5,905 handed in on or after the deadline day (mean 67.44) is -0.028. Nothing. Dropping the banked scores moves it to r = 0.02 and *d* = -0.036, which is also nothing. And the pattern is not even monotonic: binned by lead time the means run 67.44 (n = 5,905), 70.17 (n = 5,563), 69.58 (n = 2,001), 70.56 (n = 1,017), and then fall to 64.21 for the 861 submissions that arrived eleven or more days early. The interpretation prompt sends you back to the prediction you wrote in 2.1.

**📊 2.4 The two worlds side by side (3 minutes).** The same contrast in both datasets on one axis. Synthetic: *d* = 0.87 at three days early, 1.97 at seven. Real: 0.06 and -0.03. The prompt asks which of the two bars is telling you something about how people learn and which is telling you something about how a data generator was written.

**📊 2.5 Maybe the unit is wrong (4 minutes).** One dot per enrolment instead of one per submission, because "procrastination" is usually a claim about people rather than about individual pieces of work. Across 3,496 enrolments, r = 0.025. Restricting to the 2,603 who submitted at least four times: r = 0.031. The fitted line is visibly flat through a very tall cloud.

**📊 2.6 Who is not in the file (4 minutes).** The most important thing in the notebook, and it is not in any of the charts above. To appear in the submission file you have to have submitted something. **1,033 of the 4,529 enrolments never submitted a single tutor-marked assignment**, and 884 of those withdrew. A further 738 enrolments have not one single recorded click. If the strongest version of the effect lives in the students who never hand anything in, this file cannot see it. Two students who never submitted a tutor-marked assignment nevertheless passed, which the prompt asks you to explain institutionally before you call it a data error.

**📊 2.7 The rhythm is real even when the effect is not (4 minutes).** This section exists to stop you concluding that real data is simply inert. Presentation 2013J drawn as a heartbeat: 1,378,656 clicks from 1,870 students across 292 days, from day -23 to day 268, with a seven-day rolling mean and the six deadlines at days 19, 47, 96, 131, 166, and 208. Every deadline has a surge beside it, and the cell prints where each surge actually peaked rather than leaving you to eyeball it: one or two days before the line, never on it. The busiest single day of the whole presentation is day 2, with 19,872 clicks. Mean daily clicks fall from 9,254 in the first 30 days of teaching to 3,660 in days 180 to 209. There is real activity before day 0, in a course that has not started. The data has plenty of temporal structure. It just does not have the structure you went looking for.

**📊 2.8 Two students, one number, two terms (4 minutes).** Student 574973 logged 1,166 clicks across 198 active days and averaged 7.00 days early. Student 614556 logged 1,160 clicks across 58 active days, with 183 of them on a single day, and handed in five of six assignments on the deadline day itself and the sixth two days after it, averaging -0.33 days early. Mean scores: 77.3 and 78.8. Both passed. The student whose rhythm every dashboard would flag scored slightly higher.

**✏️ Your turn 3: move the boundary and watch nothing happen (3 minutes).** Cohen's *d* across eight thresholds, from 0.099 at one day early to -0.205 at fourteen, changing sign along the way and never leaving a narrow band around zero. The non-result is robust, and the sign change is a small lesson in researcher degrees of freedom: you could have reported the threshold that agreed with you.

**✏️ Your turn 4: find your own pair of real students (4 minutes).** The cell finds 294 pairs with near-identical click totals and completely different rhythms, prints the ten most extreme with their final results, and plots whichever pair you name. Choosing a pair that flatters your story is easy. That ease is the exercise.

**📊 2.9 So why is there no effect (5 minutes to read, longer to argue about).** Five explanations that survive contact with the evidence, none of them ranked and none of them settled: the submission date may not measure when work started; these are adult distance learners for whom "early" may mean something different; the very-early group may be doing minimum-viable work; range restriction, since the students who never submit are absent from the file entirely; and the possibility that the effect is simply smaller than the literature and our intuitions suggest. The section closes on the question the course exists to teach: **you had a hypothesis, a plausible mechanism, and a synthetic dataset that confirmed it. What would you need to believe the effect exists in the world?**

**🚀 Stretch: temporal network slices (10 minutes, optional).** Back on the synthetic forum. Weeks 1 to 4 against weeks 5 to 8 as two separate networks: four communities and a modularity of 0.607 in the first half, three and 0.620 in the second, with average path lengths of 2.74 and 2.86. S020 climbs from seventh to second on betweenness. The prompt adds a question you can only ask now: if you ran this on a real forum, which of your conclusions would survive?

**✍️ Network reading memo (about 25 minutes).** Roughly 500 to 600 words, five parts: what the network shows, who the connectors are, the temporal result you did not get and what would change your mind, who is invisible, and what it means that one half of this notebook had to be simulated. Required for the mini project.

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

Where the points live in this particular notebook: **Data Preparation and Technical Care** is mostly about section 1.2 and section 2.2, whether you can say why a reply is a tie, why direction was dropped, and what each of the four drops in the real data cost you. **Analysis and Visualization Choices** is about whether you used betweenness where betweenness was the right tool rather than reporting every centrality measure `networkx` offers. **Interpretation and Educational Meaning** is where a reported non-effect earns full marks if it is reported honestly and loses them if it is quietly upgraded into a finding. **Critical Reflection** is where the 18 non-posters, the 1,033 enrolments that never reach the submission file, and the reason half this notebook is synthetic all belong.

## What this connects to in the readings

- **Poquet and Joksimović (2022)**, *Cacophony of networks in learning analytics*: the same students yield a different graph depending on what the analyst counts as a tie. You made one choice in section 1.2, and the reflection asks you to name a second one and say whose importance would rise under it.
- **Molenaar and Wise (2022)**, *Temporal aspects of learning analytics: Grounding analyses in concepts of time*: time as a container to be filled is not the same construct as time as passage, order, or rhythm. Part 2 uses more than one of these without announcing the switch, and the reflection asks you to catch it and to consider whether that difference is part of why one analysis found structure and the other did not.
- **Yan, Martinez-Maldonado, Swiecki, Zhao, Li, and Gašević (2025)**, *Dissecting the temporal dynamics of embodied collaborative learning using multimodal learning analytics*: what it looks like to treat sequence rather than frequency as the unit of analysis. The reflection asks you to redesign the submission timing question as a question about sequence, and to say what data OULAD does not have and who would have to agree to collect it.
- **Kuzilek, Hlosta, and Zdrahal (2017)**, *Open University Learning Analytics dataset*: the data paper behind the real half of this notebook. Cite it whenever you report one of these results, and read the reflection question about what open educational data makes possible and what it costs.

Your guest this week, **Yukyeong Song** (University of Tennessee, Knoxville), works on fairness in behavioral pattern detection, which is the seam between this week and week 3. Every threshold in this notebook (the bridge share cutoff, the seven-day window, the decision to analyze tutor-marked assignments only) is a place where a group of students could be systematically misclassified.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Keep the direction.** Rebuild the reply network as a `nx.DiGraph` and separate in-degree (how often you got answered) from out-degree (how often you answered someone). Then check the four connectors: are they bridging because they answer across the boundary, or because people across the boundary answer them? Those are different social roles and they call for different responses.
2. **Change the tie definition.** Build a co-thread network instead: two students share an edge whenever they posted in the same thread, whether or not one replied to the other. Run the same community detection and the same bridge share calculation, then compare the connector list against the one you already have. Whoever appears in one list and not the other is a demonstration of Poquet and Joksimović's argument that you can hold in your hand.
3. **Ask whether the communities are about anything.** Cross-tabulate community membership against `major_area`, `first_gen`, and `multilingual`. If a community turns out to be a demographic category, you have a very different and much more delicate memo to write.
4. **Give the real lead time a slope.** For each student in module BBB, fit a line through their tutor-marked lead times across the presentation. Students whose lead time shrinks assignment by assignment are a different phenomenon from students who were always at the deadline. Relate that slope to the score trajectory, and see whether drift and decline travel together where a single average did not.
5. **Bring in who the students are.** Merge `student_info` back onto the per-enrolment table and re-run the timing correlation inside `age_band`, `disability`, `highest_education`, and `imd_band`. Watch out: `imd_band` has 29 blanks and one category is written `10-20` while every other one carries a percent sign, so you will have to decide what to do about a label that does not match its own scheme. Say what you decided.
6. **Take range restriction seriously.** Model whether a student submits at all, not just what they score when they do. A logistic regression on registration date and early click activity, predicting "submitted at least one tutor-marked assignment", asks a question the timing analysis structurally cannot. Then ask what an institution would be entitled to do with the answer.
7. **Compare the two presentations.** 2013J and 2014J had different assignment schedules and different weights. Run section 2.3 separately for each and see whether the non-effect is stable across them. A non-finding that replicates is worth more than a finding that does not.

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

**Part 2 gives me almost exactly zero and I think I broke something.** You did not. That is the result. The whole point of sections 2.3 through 2.9 is what to do when the effect you expected is not there. If you want to check your code rather than your luck, compare your printout to the numbers in the walkthrough above.

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
