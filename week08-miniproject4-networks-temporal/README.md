# 🕸️ Week 8: Mini Project 4, Networks and Temporal Learning Analytics

Who answered whom, and when any of it actually happened.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 21, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Cacophony of Networks in Learning Analytics and Temporal Learning Analytics |
| **Guest speaker** | Yukyeong Song, University of Tennessee, Knoxville |
| **In-class time on this notebook** | About 20 minutes, launched in the studio block (4:40 to 5:00). This is a launch, not a completion. Plan on finishing at home. |
| **Deliverable** | **Mini Project 4**: the completed notebook, the network reading memo (400 to 500 words), and the reflection answers. The AI interaction log and reflection are a separate Canvas submission. |
| **Due date** | This week, via Canvas. Check the assignment page for the exact time. |
| **Notebook** | `week08_miniproject4_networks_temporal.ipynb` |
| **Data used** | `students.csv`, `forum_posts.csv`, `gradebook.csv`, `lms_clickstream.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib, networkx |

## Objectives

By the end of this activity you will be able to:

1. **Build** a reply network from forum posts with `networkx`, and defend the three modeling decisions that produced it: what counts as a tie, whether direction matters, and who is in the graph at all.
2. **Distinguish** degree centrality from betweenness centrality, and identify the students who bridge one part of a class to another rather than the students who are simply everywhere.
3. **Analyze** submission timing and rolling engagement across eight weeks, and state precisely what a temporal pattern does and does not license you to claim.
4. **Write** a network reading memo that reports the structure, names the connectors, states the temporal finding with its strongest rival explanation, and accounts for the people the analysis cannot see.

The through-line of the session: a total throws information away, and this week you get two demonstrations of exactly what. A count of posts throws away who answered whom. A count of clicks throws away when. Both discarded pieces turn out to matter more than the count did.

## What is in this folder

| File | What it is |
|---|---|
| `week08_miniproject4_networks_temporal.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the four datasets into the runtime.

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

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and networkx, all of which ship with Anaconda.

## Step-by-step walkthrough

This is the largest of the four mini projects, so here is the plan in plain terms. **In class you will get about 20 minutes**, which is enough to reach the end of section 1.5 (the scatterplot that puts degree and betweenness on one picture). Everything from section 1.6 onward is homework. **Budget about 90 minutes in total**: roughly 60 minutes running and reading the notebook, then about 30 more for the memo and the reflection. The optional stretch section adds about 10.

The four ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. The mini project asks you to edit each of them at least once anyway.

### Part 1: the forum as a network

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the roster, the forum, the gradebook, and the clickstream inside your runtime so that nothing has to be downloaded and no real student data is ever involved. Then run the short cell that imports the four libraries and loads the files.

**📊 1.1 What is actually in the forum (2 minutes).** 1,456 posts in 60 threads, of which 1,396 are replies. The column that makes a network possible is `parent_post_id`. Note the number that the section ends on: 102 of the 120 students posted at least once, so **18 students made no ties and will not appear in the network at all**. Everything you say later has to survive that sentence.

**📊 1.2 Turning replies into edges (3 minutes).** Three modeling decisions, all arguable, all stated out loud before the code runs: a reply counts as a tie, self-replies are dropped, and ties are undirected and weighted by how often the pair exchanged replies. Read this section rather than skimming it. Your memo will be graded partly on whether you can defend these choices.

**📊 1.3 Building the graph (3 minutes).** The graph describes itself: 102 nodes, 752 edges, density 0.146, one connected component, average degree 14.75, and an average shortest path of 2.43 hops. Sparse, but nobody is stranded.

**📊 1.4 Two ways of being important (4 minutes).** Two histograms and two top-8 lists. Degree counts your ties. Betweenness counts how often you sit on the shortest path between two other people. S039 tops both lists with 36 ties. S020 is third on betweenness with a degree of 18, which is nowhere near the top of the class. That disagreement is the section.

**📊 1.5 Putting the two measures on one picture (4 minutes).** Degree on the horizontal axis, betweenness on the vertical, with reference lines at the median degree and the 90th percentile of betweenness. Five students sit in the upper left region: high betweenness, unremarkable degree. **This is the natural place to stop in class.**

**📊 1.6 Finding the communities (3 minutes).** Greedy modularity optimization splits the graph into three communities of 36, 34, and 32 students, with a modularity of 0.612. Of the 752 ties, 700 stay inside a community and only 52 cross between them. Those 52 ties are the rest of Part 1.

**📊 1.7 Bridges, not hubs (4 minutes).** For each student, the share of their ties that leave their own community. Four students clear the cutoff: S020 at 0.78, S101 at 0.53, S031 at 0.47, and S043 at 0.42. None of them is the highest degree student in the class, and all four sit above the 94th percentile of betweenness.

**📊 1.8 The sociogram (5 minutes).** The whole graph drawn with a seeded spring layout, so your picture matches your neighbor's exactly. Color is community, size is degree, gray lines stay inside a community, heavy black lines cross between them, and the four connectors are ringed and labeled. Read the interpretation prompt carefully: it asks you where the other 18 students are in this figure.

**✏️ Your turn 1: move the connector thresholds (3 minutes).** Change the minimum degree and the bridge share cutoff and watch the list change. The instructive failure is setting the minimum degree to 2, where students with a single crossing tie post a bridge share of 1.0.

**✏️ Your turn 2: one week at a time (3 minutes).** Rebuild the network from a single week. Week 3 alone has 177 posts, 74 students, and 147 ties, and the betweenness ranking bears almost no resemblance to the pooled one. That instability is a result about the measure, not a bug in your code.

### Part 2: time, order, and the shape of a semester

**📊 2.1 How long before the deadline did work arrive (5 minutes).** Lead time in hours for all 960 quiz submissions, as a distribution and then as bands. The mean score runs from 83.28 for work submitted more than three days early down to 68.15 for work submitted in the final six hours, which is 18.2 percent of all submissions and a Cohen's *d* of -0.75. Then the interpretation prompt asks you for two non-causal explanations, and points at the 33 late submissions, which average 73.26 and break the trend.

**📊 2.2 From submissions to students (4 minutes).** One dot per person instead of one dot per submission. The correlation between a student's share of last-minute submissions and their mean quiz score is -0.43, weaker than section 2.1 made it look. Sixty-five of the 120 students never submitted in the final six hours, and 19 did so on at least half of their quizzes.

**📊 2.3 Rolling engagement (4 minutes).** 41,117 clickstream events across 56 days, with a seven-day rolling mean over the raw daily bars and the eight quiz deadlines marked. Activity falls 20.3 percent from weeks 1 and 2 to weeks 7 and 8. The third thing to notice is the one people miss: the export stops on November 1 and the last quiz was due on November 3.

**📊 2.4 Does timing behavior show up in the weekly rhythm (3 minutes).** Twenty-eight students submitted in the final six hours on at least three of eight quizzes; the other 92 did not. In week 3 the last-minute group is actually the more active of the two. By week 8 they average 26.1 events per student against 38.0. The prompt asks you to describe that without a causal verb.

**📊 2.5 Two students, one number, two semesters (4 minutes).** S012 logged 485 events across 40 different days and averaged 69.3 on the quizzes. S090 logged 480 events across 7 days, with 132 of them on a single day, and averaged 96.4. A dashboard reporting total activity would have shown them as the same student twice.

**✏️ Your turn 3: move the last-minute boundary (2 minutes).** Six hours is a convention. Try 2, then 12, then 48, and see whether the finding is a fact or an artifact of the window.

**✏️ Your turn 4: find your own pair (3 minutes).** The cell searches for students with near-identical totals and very different rhythms. It finds 48 such pairs, which is the substantive point: in this class the total is nearly uninformative about the shape.

**🚀 Stretch: temporal network slices (10 minutes, optional).** Weeks 1 to 4 against weeks 5 to 8, as two separate networks. The first half has four communities and the second has three, and S020 climbs from seventh to second on betweenness. This is the richest place to extend the mini project if you want a stronger memo.

**✍️ Network reading memo (about 20 minutes).** Roughly 400 to 500 words in the memo cell, covering four things: what the network shows, who the connectors are, the temporal finding and its rival explanation, and who is invisible. Required for the mini project.

**💬 Reflection (about 10 minutes).** Five prompts tied to this week's readings and to the guest speaker's work on fairness in behavioral pattern detection. Graded under the Critical Reflection criterion.

**✅ Submission checklist.** Work through it before you upload. It is short and it catches the things people actually lose points on.

## Mini Project 4 rubric

One hundred points, five criteria, twenty points each.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | Thoughtfully completes data, preparation, analysis, and interpretation with coherence. | Completes most stages clearly. | Some stages incomplete or weakly connected. | Workflow is minimal or fragmented. |
| **Data Preparation and Technical Care** | Careful, transparent, and well-documented preparation decisions. | Appropriate preparation with documentation. | Partial or uneven preparation. | Minimal or unclear preparation. |
| **Analysis and Visualization Choices** | Methods and visuals are well-justified and aligned with questions. | Analyses and visuals are appropriate. | Partial misalignment or clarity issues. | Inappropriate or missing analyses. |
| **Interpretation and Educational Meaning** | Interpretation connects findings to learning, teaching, or decision-making. | Interpretation is reasonable and evidence-based. | Interpretation is tentative or weak. | Minimal or absent interpretation. |
| **Critical Reflection: Limits, Ethics, and Equity** | Thoughtfully addresses limitations and ethical and equity implications. | Identifies key considerations. | Mentions considerations superficially. | Does not address considerations. |

Where the points live in this particular notebook: **Data Preparation and Technical Care** is mostly about section 1.2, whether you can say why a reply is a tie and why direction was dropped. **Analysis and Visualization Choices** is about whether you used betweenness where betweenness was the right tool rather than reporting every centrality measure `networkx` offers. **Critical Reflection** is where the 18 non-posters and the November 1 export boundary belong.

## What this connects to in the readings

- **Poquet and Joksimović (2022)**, *Cacophony of networks in learning analytics*: the same students yield a different graph depending on what the analyst counts as a tie. You made one choice in section 1.2, and the reflection asks you to name a second one and say whose importance would rise under it.
- **Molenaar and Wise (2022)**, *Temporal aspects of learning analytics: Grounding analyses in concepts of time*: time as a container to be filled is not the same construct as time as passage, order, or rhythm. Part 2 uses more than one of these without announcing the switch, and the reflection asks you to catch it.
- **Yan, Martinez-Maldonado, Swiecki, Zhao, Li, and Gašević (2025)**, *Dissecting the temporal dynamics of embodied collaborative learning using multimodal learning analytics*: what it looks like to treat sequence rather than frequency as the unit of analysis. Every finding in Part 2 is a frequency finding wearing a temporal coat, and the reflection asks you to redesign one of them as a genuine question about sequence.

Your guest this week, **Yukyeong Song** (University of Tennessee, Knoxville), works on fairness in behavioral pattern detection, which is the seam between this week and week 3. Every threshold in this notebook (the bridge share cutoff, the six-hour window, the three-of-eight grouping) is a place where a group of students could be systematically misclassified.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Keep the direction.** Rebuild the reply network as a `nx.DiGraph` and separate in-degree (how often you got answered) from out-degree (how often you answered someone). Then check the four connectors: are they bridging because they answer across the boundary, or because people across the boundary answer them? Those are different social roles and they call for different responses.
2. **Change the tie definition.** Build a co-thread network instead: two students share an edge whenever they posted in the same thread, whether or not one replied to the other. Run the same community detection and the same bridge share calculation, then compare the connector list against the one you already have. Whoever appears in one list and not the other is a demonstration of Poquet and Joksimović's argument that you can hold in your hand.
3. **Track the connectors week by week.** Extend the stretch section from halves to individual weeks and plot each connector's betweenness as a line across the eight weeks. Print the number of ties behind each point on the same figure, because betweenness on a 147-tie graph is high variance and any ranking you read from it deserves an error bar you cannot compute.
4. **Ask whether the communities are about anything.** Cross-tabulate community membership against `major_area`, `first_gen`, `multilingual`, and studio `group_id` if you merge it in. If a community turns out to be a studio group, your finding is about how the course was structured. If it turns out to be a demographic category, you have a very different and much more delicate memo to write.
5. **Separate structure from volume.** Betweenness and posting volume are entangled: people who post more have more chances to sit on a path. Regress betweenness on post count, take the residuals, and rank students by how much more structurally central they are than their volume predicts. Compare that ranking against the bridge share ranking and say which one you would put in front of an instructor.
6. **Give the lead time a slope.** For each student, fit a line through their eight quiz lead times across the term. Students whose lead time shrinks week by week are a different phenomenon from students who were always last minute. Relate the slope to the quiz trajectory and see whether drift and decline travel together.

## Troubleshooting

**"NameError: name 'G' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart session and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/forum_posts.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**My charts do not appear.** Make sure you ran the short library cell that comes right after the setup cell, which contains `%matplotlib inline`. If they still do not appear, restart and run all.

**The sociogram is a hairball and I cannot read it.** That is a fair description of 102 students and 752 ties, and it is the honest picture. The layout is only a reading aid. Every claim you make about connectors should come from the table in section 1.7, not from where a dot happens to land. If you want a cleaner picture, draw one community at a time.

**My sociogram looks different from my neighbor's.** It should not. The layout is seeded (`seed=8100`) and greedy modularity is deterministic, so a clean run is identical for everyone. Check whether one of you ran a ✏️ **Your turn** cell before the sociogram, which changes what is in memory. Restart and run all to compare fairly.

**"ModuleNotFoundError: No module named 'networkx'".** You are running locally without networkx installed. In a terminal: `conda install networkx` or `pip install networkx`. In Colab this cannot happen, networkx is already there.

**Betweenness is taking a long time.** On the full 102-node graph it takes a couple of seconds. If it is genuinely hanging, you have probably built a graph much larger than intended by editing a filter. Restart and run all.

**My weekly network in Your turn 2 gives a completely different top five.** Yes. That is the finding, not the error. A single week has roughly one eighth of the ties, and betweenness on a sparse graph is unstable. Say so in your memo rather than picking the week that agrees with you.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all: the notebook is seeded, so a clean run reproduces the same numbers every time.

**I only got through section 1.5 in class and I am behind.** You are not behind. That is exactly the plan for the 20-minute launch. Part 2 is designed to be done at your own desk.

## A reminder about documenting AI use

Mini Project 4 has two Canvas submissions, and it is worth being precise about which piece goes where.

1. **The Mini Project 4 assignment**: your completed `.ipynb` file (in Colab, `File > Download > Download .ipynb`), containing your memo and your reflection answers.
2. **The AI Reflection submission**: this one has two parts, and students routinely reverse them.
   - **The conversation record goes in an attached Word file.** Copy your actual exchanges with the AI assistant into a `.docx` and attach it. Transcripts, prompts, and the responses you got. Not a summary, the record itself.
   - **The four reflection questions are answered in the Canvas text box**, directly, not in the attachment. What you asked for, what you accepted, what you rejected, and how you verified anything you kept.

If you used no AI at all, say so in one line in the text box and attach nothing. That is a complete and acceptable submission.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use costs you nothing.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
