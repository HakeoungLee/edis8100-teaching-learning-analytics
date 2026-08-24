# Week 7: Self-Regulated Learning Traces Lab

Can a stream of timestamped clicks tell you anything real about how a person regulates their own learning?

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 7, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Learning Analytics for Self-Regulated Learning |
| **Guest speaker** | Conrad Borchers, Carnegie Mellon University |
| **In-class time on this notebook** | About 45 minutes for the core path, launched in the hands-on studio block (4:40 to 5:00). Sections 6 and 7 are the designated finish-at-home if the room runs out of time. |
| **Deliverable** | None. Week 7 is an in-class launch, not a graded submission. |
| **Due date** | Not applicable. The next Canvas deliverable is Mini Project 4 in Week 8. |
| **Notebook** | `week07_srl_traces_lab.ipynb` |
| **Data used** | **Real.** EdNet KT3, a 500-user extract of the released interaction log of the Santa TOEIC tutor in South Korea. One file, `actions.csv.gz`, 1,893,105 rows by 7 columns, downloaded by the notebook from the course dataset repository. **CC BY-NC 4.0: attribution required, non-commercial use only.** |
| **Citation** | Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In *Artificial intelligence in education (AIED 2020)*, Lecture Notes in Computer Science 12164 (pp. 69-73). Springer. |
| **Libraries** | pandas, numpy, matplotlib |
| **Prior coding experience needed** | None |
| **Next session** | **There is no class on October 14.** We meet again on Wednesday, October 21 for Week 8, when Mini Project 4 is due. |

Our guest this week, Conrad Borchers, is a **coauthor of one of the required readings** (Zhang, Borchers, and Barany, 2024). The notebook is built to end somewhere useful: its last reflection section drafts a question you could actually put to him, about how an analyst chooses the window inside which two actions count as connected and how far the conclusions move when that choice changes. It is a question this notebook earns, because every session statistic in it moves by a factor of two or three when the session rule moves. Write your own version and bring it on paper. The best questions in this seminar come from something you just did with your own hands.

## Something changed this week

Weeks 2 through 6 worked with data collected by universities: enrollment registries, virtual learning environments, a research studio. This week the collector is a **company**, and the log was written to run a product rather than to answer a research question.

That changes what is in the file and what is missing from it. There is no answer key, because correctness lived elsewhere in Riiid's systems. There is no demographic column, no score, and no name. What there is, in enormous quantity, is exactly what the interface did and exactly when. The lab is built on that asymmetry, and by the end of it you will have found two patterns that look like learner behaviour and turn out to be the application.

## Objectives

By the end of this activity you will be able to:

1. **Profile** the action vocabulary of a real tutor log, and say which parts of a person's profile are about the person and which are forced by the software.
2. **Cut a continuous stream into sessions** using a stated gap rule, and **report a sensitivity check** showing how far the headline moves when that rule changes.
3. **Read the order** in which answering and explanation viewing occur, and detect when the order is set by the interface rather than chosen by the person.
4. **Use inter-action timing** to separate a screen that was displayed from a screen that was read, and state precisely what the clock still cannot tell you.
5. **Recognise a logging artifact**: a comparison that appears to be about learning and is actually about a logging convention.

The through-line of the session: **self-regulated learning is not directly observable, so everything here is an inference from residue.** There is no column in the log for intention, confidence, or effort. There is a column for what happened on a screen and when. The distance between those two things is the whole lab, and it is the Week 2 claim ladder again: `enter_e` is a feature, help seeking is an indicator somebody has to argue for, and self-regulation is a construct with a literature behind it. Section 5 is the week's hardest lesson, because it shows one of those features failing to reach even the first rung.

## What is in this folder

| File | What it is |
|---|---|
| `week07_srl_traces_lab.ipynb` | The notebook. It downloads its own data from a public URL and runs top to bottom untouched. |
| `README.md` | This file. |

You do not need to clone anything, download a CSV, or create an account. The first code cell fetches one 14 MB compressed file over plain HTTPS in a second or two and prints what arrived. If the download fails, the cell prints a plain-English message naming the repository rather than a wall of red.

## Where the data comes from

**Dataset.** **EdNet KT3**, restricted to a 500-user extract prepared for this course. EdNet is the released log of **Santa**, a commercial multi-platform tutoring service in South Korea for the **TOEIC** English proficiency test. KT3 is the action-level release: one row per interface event, with the timestamp, what kind of event it was, which item it happened on, which option was chosen if any, and which platform the person was using. The extract runs from 30 August 2018 to 27 November 2019.

**Who collected it.** Riiid, the company that operates Santa, logged every interface event its own product generated as a by-product of running the service. Its research group then anonymised and released four nested versions of that log, KT1 through KT4, so that researchers with no access to a commercial tutor could work on real interaction data at scale.

**License.** **CC BY-NC 4.0.** Use, share, and adapt it **with attribution and for non-commercial purposes only**. That last clause is not decorative and the notebook says so twice. Anything built on this file in this course stays inside this course: not a product, not a consulting deliverable, not a paid workshop. If your course project uses it, cite Choi and colleagues (2020) and say which release and which extract you used. "EdNet" alone is not a citation.

**Who is in it.** People in South Korea preparing for a high-stakes English proficiency test, on a commercial app they chose and in most cases paid for, studying on their own time and, for the majority of these rows, on a phone. Choi and colleagues describe the service, not these 500 individuals. The extract itself carries no age, no gender, no location, and no score.

**What it cost to get here.** Identity is gone: every person is an integer with a `u` in front of it. Item content is gone: a question is `q4142` and nothing more, so you cannot see what was asked or judge whether the item was fair. **And the answer key is gone.** KT3 records the option chosen and never the option that was correct. That single absence removes the most common analysis in this literature, and Section 6 of the notebook argues that its absence is a gift, because the analysis it removes is one you should have distrusted anyway.

**The file the notebook reads** (from `HakeoungLee/edis8100-datasets`, folder `ednet-kt3-500`):

| File | One row is | Size |
|---|---|---|
| `actions.csv.gz` | one interface event by one person at one millisecond | 1,893,105 rows x 7 columns, 500 learners |

Nothing is sampled or thinned inside the notebook. Loaded with sensible column types the whole file is about 225 MB in memory and every computation finishes in seconds, so the notebook keeps all 1,893,105 rows and says so. Where a step drops rows, it drops them in front of you with a count and a reason, and the largest such drop is 178 rows.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week07-srl-traces-lab/week07_srl_traces_lab.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week07-srl-traces-lab/week07_srl_traces_lab.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week07-srl-traces-lab/week07_srl_traces_lab.ipynb`

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your copy is yours, and nothing you do to it affects the course repository.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, and matplotlib, all of which ship with Anaconda.

## Step-by-step walkthrough

Total time is about 45 minutes if you keep moving. The four **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. You are not expected to write code from scratch. You are expected to read numbers and pictures and argue about what they mean, which is the doctoral skill.

**Setup (1 minute).** Run the first code cell. It imports three libraries, sets the plotting defaults, and downloads `actions.csv.gz`. It prints 1,893,105 rows, 7 columns, 500 learners, about 225 MB, and a reminder that the licence is non-commercial.

**1. One row, and the alphabet of this log (10 minutes).** The vocabulary is not documented anywhere in the file, so the notebook reads it out of the file, which is the ordinary situation. Crossing `action_type` against the first letter of `item_id` shows that four action types and four item kinds combine into exactly **seven** legal events rather than sixteen: `enter_b`, `respond_q`, `submit_b`, `enter_e`, `quit_e`, `enter_l`, `quit_l`. Two of the seven are already suspicious as measures of a person, because `enter_b` and `submit_b` occur exactly 314,791 times each: a bundle you open is a bundle you submit, so a profile reporting both reports one number twice. The section closes by having you check, in the column list, that **there is no correctness column**.

Section 1.1 prints 25 consecutive actions by one learner. It is the screen to slow down for. Three timescales live in the `seconds_since_previous` column: gaps of **0.05 seconds**, which are the interface moving by itself; gaps of twenty to thirty seconds between opening a bundle and answering it, which is the only stretch that plausibly contains thinking; and one place where the learner submits `b1073`, re-enters it 3.23 seconds later, answers the same question twice with different options, and submits again. The prompt asks for two stories that produce those rows, one about the person and one about the interface, and refuses to adjudicate.

Section 1.2 is the mess, named out loud, with a decision and a stated cost for each of six items: **2,637** rows tied to the millisecond, **19** learners whose logs begin mid-flow (costing 178 rows and zero answers), **14,417** bundles submitted with nothing answered, **18** explanation items with no matching bundle, **42** learners with no explanation event and 91 with no lecture event, and the shape of the people. That last one is the one that bites: rows per learner run from **5 to 52,917**, the busiest ten learners hold 16.0 percent of all rows, and the quietest 250 hold 4.6 percent. The rule the whole notebook then obeys is stated once and applied everywhere: **compute per person, then summarise across people; put a count next to every rate; when you need an interval, resample the people, not the rows.**

**2. What a learner's action profile does and does not say (5 minutes).** Per-learner shares of the five substantive events. Most boxes are narrow: the middle half of learners spend between 21.0 and 25.2 percent of their events opening bundles, and the notebook insists you exhaust the instrument and the setting before you call that a finding about consistent people. The explanation box is the one to watch, and not because it is wide. Its middle half is narrow too, 19.4 to 24.1 percent, but its tenth percentile is 4.0 percent, so the spread is all in a lower tail. You are asked to write down a hypothesis about that tail. Section 5 checks it. **Your turn 1** puts any single learner against the class median, with counts printed beside the percentages.

**3. Cutting a stream into sessions, and admitting it is a choice (10 minutes).** The file has no session column, so the analyst invents one. The gap histogram is worth the whole section: there **is** a valley in this distribution, at about **0.2 seconds**, and what it separates is the machine from the person rather than one sitting from the next. Everywhere a session rule could plausibly go, from a few minutes to a couple of hours, the curve just slides downward. The only feature that behaves like a natural unit is the rise after six hours peaking near a day, which is people coming back tomorrow.

The notebook states a 30 minute rule, applies it, and reports a headline: **a typical sitting is about 8.75 bundles and 16.0 minutes**, computed per learner and then medianed across the 500. It also prints, for contrast, what you get if you pool over the 23,810 sessions and forget the nesting.

Then it moves the rule, which is the part most papers skip. Across gap rules from 5 to 120 minutes the headline runs from **5.0 to 10.0** bundles, a factor of 2.0, and the minutes figure from **6.5 to 22.8**, a factor of 3.5. The number of sessions found runs from 48,578 to 17,535. Nothing about the learners changes between those rows. **Your turn 2** ships a 10 minute rule so a number moves on the first run.

**4. Order: what follows what (5 minutes).** A bigram matrix over 1,892,605 within-learner pairs. Only **19 of 49** cells ever occur, and the notebook labels never-occurred cells with a dot and rounds-to-zero cells with `<1`, so that the five cells that happened but round away are visible. Two cells set up everything that follows: `submit bundle` is followed by `open explanation` **94.4 percent** of the time, and `close explanation` is followed by `open explanation` 12.9 percent of the time.

**5. The first logging artifact: the explanation nobody asked for (8 minutes).** The section opens with an abstract you could write this afternoon, operationalising help seeking as the number of explanation screens opened. Then it measures the seconds between submitting a bundle and the explanation appearing. The overall median is **0.077 seconds**. Human simple reaction time to a visual signal is about 0.2 to 0.25 seconds, and that is before deciding anything.

The second half of that chart is sharper still. **On mobile 98.6 percent of these screens appear within a fifth of a second (median 0.057 s); on web the median is 1.317 s and the share under 0.2 seconds is 18 screens out of 114,214.** Same product, same behaviour, different client. A latency you might have read as how quickly a learner turns to help is a measure of what device they were holding.

The consequence is then made quantitative: across the 500 learners, explanation screens opened correlates with bundles submitted at **Spearman 0.995**, with a median of 1.008 explanations per bundle. Ranking people on "explanation use" reproduces ranking them on volume. And the hypothesis from Section 2 gets checked: all **42** learners with no explanation event have between 7 and 40 total logged events against a class median of 1,051, and **not one** learner with 100 or more events is among them. Among the 409 regular users the explanation share sits between 18.3 and 26.0 percent from the 5th to the 90th percentile. The lower tail was not a kind of learner. It was people with almost no log, which is a general failure mode worth naming: a measure that behaves differently for people with little data manufactures a group that is really a sample-size artifact.

**6. The second logging artifact: the answer you have already been shown (8 minutes).** This is the section to be able to reproduce from memory. The study everybody wants to run on a tutor log is whether learners who use the help do better, comparing accuracy with and without help. This extract has no answer key, so you cannot run it, and the section shows what you would have been measuring if you could.

Three steps. First, **222,958 of 544,487 answers (40.9 percent)** are repeats of a question that learner had already answered. Second, **83,779 answers (15.4 percent of all of them, and 35.7 percent of repeats)** were given by somebody who had already opened the explanation for that bundle. Third, and this is the move that needs no answer key: if a post-explanation answer is reproduction rather than knowledge, the chosen options should pile up on one option. They do. Across **1,241** questions with at least ten independent answers in each condition, the share of answers falling on the single most chosen option rises from a median of **0.551** at first exposure to **0.700** after the explanation has been shown, with the difference rising on 81.6 percent of questions and a bootstrap interval over questions of [+0.125, +0.145]. Then the notebook corrects its own statistic, because "share on the most chosen option" is inflated when a question has fewer answers and the two conditions here do not have the same number: 67 per question at first exposure against 14 afterwards. Thinning the first-exposure side to match, question by question, the median difference falls from **+0.136 to about +0.110**, so roughly a fifth of the raw effect was sample size and four fifths was not. The bootstrap interval quoted above is an interval on the uncorrected statistic and does not contain the corrected one, which is worth a sentence of its own in class. Restricted to answers arriving within 24 hours of the explanation, the post-explanation median is **0.812** against 0.496, and the same thinning lifts the 0.496 to about 0.527.

The notebook then does two things most treatments do not. It states the caveat that questions are not independent either, because the same 500 learners recur across them, so the interval is optimistic. And it generalises the artifact: wherever a tutor logs help before the outcome it scores, the outcome after help is partly determined by the logging. The transfer exercise asks for three things to check about **when a row gets written**, before computing anything at all. **Your turn 3** ships a stricter minimum of 25 answers per question.

**7. Timing: separating a screen that appeared from a screen that was read (10 minutes).** What the clock gives back. All 342,634 explanation opens pair perfectly with a close, and the dwell between them is the closest thing in this file to evidence that a person did something with the help. Median 15.4 seconds; 8.7 percent close within two seconds and 40.2 percent within ten. Per learner, among the 404 with at least 20 screens, the share held for ten seconds or more has a median of **0.629, 95 percent interval [0.604, 0.660] from resampling learners**, and runs from 0.316 at the tenth percentile to 0.866 at the ninetieth. The 96 excluded learners are named and the notebook says plainly that they are not missing at random.

Section 7.1 is the best part of the lab, because a hypothesis dies in it. An explanation the learner opened themselves ought to hold their attention longer than one the app put in front of them. Within learner, among the 258 with at least 20 screens of each kind, the difference goes the **other** way: **-7.77 seconds, 95 percent interval [-9.76, -5.50]**, entirely below zero. Then the reason: of the screens not opened by the flow, **54.9 percent** are the learner reopening the explanation they had just closed, at a median of 6.5 seconds each. Flicking back is not deliberation. The label "opened it themselves" was ours, not the log's, and the repair required is to the operationalisation rather than to the theory.

Section 7.2 measures the seconds from a bundle opening to the first answer inside it. Per learner, the middle half of the 415 learners with enough bundles sit between **17.6 and 23.2 seconds**, which is a startlingly narrow band, and again the instrument and the setting get asked first. This is also where the field's vocabulary appears: 1.3 percent of bundles are answered within three seconds, the field calls patterns like this **"gaming the system"** and **"hint spam"**, and the notebook quotes those phrases, points out that each names a motive no timestamp can see, and then says what was actually recorded. **Your turn 4** moves the ten second line and prints how many learners change decile because of it.

**Reflection.** Four prompts, three tied to this week's readings by author and one that reaches back to Week 3 and lists the six choices this notebook made. Then the guest question section, with a drafted question for Conrad Borchers about window choice in ordered network analysis that comes straight out of Section 3.

**Before you leave.** A checklist. The two items worth taking seriously are being able to explain both logging artifacts to somebody who was not in the room, and remembering that the licence is non-commercial.

**Appendix.** Worked solutions to all four Your turn cells, including a twelve-point sweep of the session rule, a full sweep of the concentration threshold, and a Jaccard overlap grid showing that of the 85 learners who could ever land in the bottom decile of explanation dwell, only **5** land there under every threshold.

## What this connects to in the readings

- **Winne (2022)**, *Learning analytics for self-regulated learning*: the argument the entire lab is built on, that self-regulated learning is not directly observable and traces are the footprints it leaves. This week you get 1,893,105 footprints and no answer key. The reflection asks which of the measures you built comes closest to evidence about regulation, what would have to be true of the Santa interface for it to mean what you want it to mean, and, about one of the 42 learners who never opened an explanation, what you have actually learned.
- **Zhang, Borchers, and Barany (2024)**, *Studying the interplay of self-regulated learning cycles and scaffolding through ordered network analysis across three tutoring systems*: the paper our transition matrix is a blunt first cousin of. Ordered network analysis connects actions across a window of surrounding actions and weights them; our bigram matrix only sees the action immediately next door. Their framing supplies the sharpest prompt of the week, because Section 5 found that Santa's central piece of scaffolding is not requested at all, it is delivered, at a speed that depends on the device. Is the scaffolding shaping the regulation we measured or revealing it, and what would a fair comparison across three systems have to hold constant? Conrad Borchers is a coauthor, so this is the reading to arrive having actually read.
- **Viberg, Khalil, and Baars (2020)**, *Self-regulated learning and learning analytics in online learning environments: A review of empirical research*: the review that asks how much work on SRL measures SRL and how much of it measures activity wearing an SRL vocabulary. Turn it on this notebook. Rank the four candidate measures you built, the action profile, bundles per sitting, explanation dwell, and time to first answer, from "activity with a nicer name" to "defensible evidence about regulation", and defend the ordering.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Use the `source` column, which the notebook deliberately leaves alone.** Santa logs eight study modes, from `sprint` and `diagnosis` to `review_quiz` and `my_note`. Recompute the explanation dwell measure separately by mode. Then ask the question that matters: is the between-learner spread in Section 7 partly a between-mode spread, meaning that what looks like a difference between people is a difference in which part of the product they used?
2. **Split the mobile and web populations everywhere.** Section 5 shows the client changes a latency by a factor of twenty. Find out how far that goes. Recompute the session statistics, the dwell distribution, and the time to first answer separately for the 292 mobile-only learners and the 33 web-only ones, and say which of the notebook's headlines survive.
3. **Build a real sequence measure and make the order do work.** Our bigram sees one step. Extract each session's event sequence as a string, count the most frequent 4-grams, and compare the top ten between the top and bottom thirds on explanation dwell. Then argue about whether a pattern nobody named in advance can be called self-regulation.
4. **Attack the concentration analysis.** Section 6 infers reproduction from the fact that post-explanation answers concentrate on one option. Design the check that would falsify it. One candidate: within questions, compare the concentration of answers given after the explanation with the concentration of answers given on a second exposure with **no** explanation in between, which isolates repetition from being shown the answer. Report how many questions have enough of both.
5. **Sensitivity as a deliverable, not a footnote.** The appendix sweeps the session rule and the concentration threshold separately. Sweep them jointly and report the surface. Then write the two-sentence methods note you would actually put in a paper, and notice how rarely you have read one.

## Troubleshooting

**"NameError: name 'actions' is not defined" or something similar.** You ran a cell out of order, or the runtime restarted. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**The download failed.** The setup cell prints a plain-English message naming the repository and the exact URL instead of a traceback. The usual cause is no internet connection in the runtime. Check the connection and restart and run all. If the repository itself is unreachable, send Dr. Lee the URL the cell printed.

**It is taking a long time.** The file is 14 MB compressed and about 225 MB in memory. End to end the notebook executes in about 25 seconds on a laptop and comfortably under two minutes on a free Colab runtime. If a cell seems stuck, it is almost always the download, not the arithmetic.

**"KeyError: 'u501'" in Your turn 1.** Learner ids are not a contiguous range. The cell prints six valid ids for you and tells you when the one you typed is not in the file. Try `u1`, `u170`, or any id from the printed list.

**My session numbers are different from my neighbour's.** Compare `MY_GAP_MINUTES` first. That is almost always the difference, and noticing it is the point of Section 3.

**My concentration numbers are different.** Compare `MY_MIN_ANSWERS`. At 5 the comparison keeps 3,295 questions and the median difference is +0.121; at 30 it keeps 104 and the difference is +0.184. Both are real, and the appendix explains why the gap widens as the bar rises.

**The dwell histogram has a gap on the left.** That is the log scale, not a bug. Dwell times below about a tenth of a second are rare because closing a screen is a physical action.

**Some cells in the transition heatmap show a dot and some show `<1`.** That is deliberate. A dot means the transition never happened once, which is a fact about what the software permits. `<1` means it happened, in two cases 1,434 times, and rounds to zero at whole-percentage precision.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

## A reminder about the licence

EdNet is released under **CC BY-NC 4.0**. Two obligations follow and they are not optional. **Attribution**: cite Choi and colleagues (2020) wherever this data appears in your work. **Non-commercial**: nothing built on this file may be used commercially, which includes consulting deliverables, paid workshops, and product prototypes shown to a buyer. If your course research project wants to go further with tutor logs, that is a conversation worth having with Dr. Lee early, because the licence, and not the analysis, is usually what decides it.

## A reminder about documenting AI use

There is nothing to upload for Week 7. This lab is a launch: we start it together in class and you finish reading and arguing with it on your own time. The next Canvas deliverable is Mini Project 4 in Week 8, and remember that there is no class on October 14, so Week 8 arrives on October 21 with the project already due.

Even though nothing is submitted this week, if you used an AI assistant while working through this notebook, to explain what a bigram matrix is, to check your reading of the concentration chart, or to help you sharpen the question you are bringing for our guest, save that exchange now.

The course AI policy has two parts that go in two different places, and it applies in full the moment any of this work reaches a mini project or your course research project. The conversation record itself goes into a **Word file attached to the Canvas AI Reflection submission**. The reflection goes in the **Canvas text box**, not in the Word file, and answers four questions: how you used it, whether it helped and how, whether it made your work more challenging and how, and what you learned about AI that you could pass on to the class.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. The habit that makes this painless is keeping the log as you go rather than reconstructing it afterward, and a week with nothing due is the cheapest possible time to practice.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development

Data: EdNet KT3, a 500-user extract. Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In *Artificial intelligence in education (AIED 2020)*, Lecture Notes in Computer Science 12164 (pp. 69-73). Springer. Licensed CC BY-NC 4.0.
