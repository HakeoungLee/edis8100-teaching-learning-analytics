# 🔁 Week 7: Self-Regulated Learning Traces Lab

Can a stream of timestamped clicks tell you anything real about how a student regulates their own learning?

## At a glance

| | |
|---|---|
| **Session** | Wednesday, October 7, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Learning Analytics for Self-Regulated Learning |
| **Guest speaker** | Conrad Borchers, Carnegie Mellon University. [Bio: confirm with speaker] |
| **In-class time on this notebook** | About 30 minutes, launched in the hands-on studio block (4:40 to 5:00). Finish the last two sections on your own if you run out of room. |
| **Deliverable** | None. Week 7 is an in-class launch, not a graded submission. |
| **Due date** | Not applicable. The next Canvas deliverable is Mini Project 4 in Week 8. |
| **Notebook** | `week07_srl_traces_lab.ipynb` |
| **Data used** | `students.csv`, `srl_traces.csv`, `gradebook.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib |
| **Next session** | **There is no class on October 14.** We meet again on Wednesday, October 21 for Week 8, when Mini Project 4 is due. |

Our guest this week, Conrad Borchers, is a **coauthor of one of the required readings** (Zhang, Borchers, and Barany, 2024). The notebook is built to end somewhere useful: its last reflection section drafts a question you could actually put to him, about how an analyst chooses the window inside which two actions count as connected and how far the conclusions move when that choice changes. Write your own version and bring it on paper. The best questions in this seminar come from something you just did with your own hands.

## Objectives

By the end of this activity you will be able to:

1. **Build** an action frequency profile for each student from raw tutor traces, and explain why two students with the same number of actions can be doing completely different things.
2. **Write and apply** a pattern matcher that decides whether a tutor session contains a complete regulation loop, using a definition you can state out loud and defend.
3. **Use** inter-action timing, not action counts, to distinguish help seeking spread over minutes from runs of hint requests seconds apart, and say what a log cannot tell you about either.
4. **Read** an n-gram transition heatmap of action types, and say what it does and does not show about self-regulated learning.

The through-line of the session: **self-regulated learning is not directly observable, so everything here is an inference from residue.** There is no column in the log for intention, confidence, or effort. There is a column for what got clicked and when. The distance between those two things is the whole lab, and it is the Week 2 claim ladder again: `request_hint` is a feature, help seeking is an indicator somebody has to argue for, and self-regulation is a construct with a literature behind it.

## What is in this folder

| File | What it is |
|---|---|
| `week07_srl_traces_lab.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the three datasets into the runtime.

The data are synthetic on purpose. Learning analytics runs on records about people who rarely got to weigh in on being measured, and a course assignment is a poor reason to touch anyone's real tutor logs. We built a world instead so that we can rehearse the judgment without surveilling a single person. The ask in return is that you treat this data as if it were real.

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

Total time is about 30 minutes if you keep moving. The four ✏️ **Your turn** cells already contain working values, so the notebook runs start to finish without you typing anything. You are not expected to write code from scratch today. You are expected to read numbers and pictures and argue about what they mean, which is the doctoral skill.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the roster, the tutor trace log, and the gradebook inside your runtime. The load cell then prints the shape of what you have: 30,150 logged actions across 844 tutor sessions, and 120 students who used the tutor at least once.

**📊 1. What a trace actually looks like (4 minutes).** Seven action types exist in this tutor: `set_goal`, `view_plan`, `attempt`, `request_hint`, `check_answer`, `review_feedback`, and `reflect`. Look at the raw rows before you compute anything, and notice what is missing: there is no column for whether the student was regulating their learning. The class-wide counts are already an argument. There are 9,866 attempts and 9,273 hint requests, but only 438 goals and 376 reflections. Then one session is printed in order, as a timeline with the seconds that passed between actions, and it is worth slowing down for: S062 opens with `set_goal` and `view_plan`, lets 86 seconds pass between an attempt and checking that answer, and then requests six hints on a single item in twenty seconds, with gaps of 2 to 5 seconds. Every argument the rest of the session makes is visible in that one screen. Section 1.1 turns the log into per-student profiles and shows the spread: the median student spends about 19 percent of their tutor actions on hints, and somebody spends 67 percent. ✏️ **Your turn 1** puts any single student against the class median.

**📊 2. A sequence detector, and what it detects (9 minutes).** Profiles count actions. Regulation, as Winne describes it, is about order, because setting a goal after you finish is not planning. The notebook states a rule you can hold in your head: the detector fires for a session when a `set_goal` occurs, then an `attempt` at any point after it, then a `review_feedback` or a `reflect` at any point after that. The three actions do not have to be adjacent. Write the definition down. Week 11's retroactive design audit puts this lab back on the table and asks who should have had a say in the labels it produced.

The section is emphatic about one sentence: this detects a pattern in a log, not regulation. **"No loop detected" is a statement about a log file and never a statement about a mind**, because a student who planned on paper, in their head, or with a roommate leaves no trace here, and a tutor with no `set_goal` button would score every student on earth at zero.

A small state machine applies the rule to all 844 sessions: it fires in 410 of them, 48.6 percent, and 406 of the misses are sessions where no goal was ever set. **Then the notebook runs the check almost nobody runs**, and it changes what the measure is. Zero sessions contain a goal and a closer in the wrong order, so "the ordered sequence fired" picks out exactly the same sessions as "a goal appears somewhere and a closer appears somewhere." The ordering requirement, which is the whole conceptual content of the word *loop*, does no work at all on this log, because this tutor can only write `set_goal` at the start of a session and `reflect` at the end. The sophisticated sequence matcher is a two-item checklist wearing a sequence vocabulary, which is precisely what Viberg, Khalil, and Baars warn the field about.

The detected-loop rate then goes up against **quiz growth**, the slope of a line through each student's eight quiz scores: Pearson `r = 0.58` [95% CI 0.44 to 0.68], Spearman 0.59, n = 120. Both are reported because the rate is a proportion over 4 to 8 sessions and lands on a handful of discrete values. Two caveats travel with the slope: the eight quizzes are not equally hard and the file records no difficulty parameter, and **the whole association exists because the generator wrote it in**. ✏️ **Your turn 2** tightens the definition so that only `reflect` closes a loop: prevalence falls to 30.6 percent and `r` falls to 0.52. A measurement decision just changed a finding.

**📊 3. Runs of rapid hint requests, and why counting will not find them (9 minutes).** The field calls this "hint spam" or "gaming the system", and the section opens by holding both phrases at arm's length: each names a motive that no log file can see, and the vocabulary arrived before the evidence did. The course quotes those terms as objects of study and then uses one a timestamp column can actually support, **a run of hint requests a few seconds apart**.

Asking for a lot of hints can mean a student is stuck and seeking help, which is a regulation strategy rather than a failure of one. The counts look identical, only the clock separates them, and even the clock supplies no motive. So the notebook computes the seconds between each action and the one before it: half of all hint requests arrive within 10 seconds of the previous action. A rule follows, three or more consecutive hints each within 10 seconds, occurring at least three times across the term, and it flags 18 of the 120 **logs**. The rule's own defect is left visible: three runs is a count and not a rate, and students attended between 4 and 8 sessions.

The pair to watch is S017 against S072. S017 asks for 14.2 hints a session and waits a median of 21 seconds before each, and is not flagged. S072 asks for 21.0 and waits 4 seconds, firing six hints in nineteen seconds on a single item. The obvious next sentence, "nobody reads a hint in three seconds", is exactly the one the notebook stops to refuse, and it instead asks what would put a person in front of that item pressing hint six times: the item may assume a prerequisite nobody taught, the hints may arrive in a graduated stack whose first two are useless, there is **no other button in this tutor for saying you are stuck**, the quiz is on Tuesday, and only the fifth candidate on the list is about the student. ✏️ **Your turn 3** ships a genuinely different rule so the label moves on first run, from 18 students to 1, and asks which rule you would defend to the eighteen people it names.

**📊 4. Putting the two log patterns next to learning (5 minutes).** Sort every student into three groups whose names describe what was found in a log file rather than what a student is: `loop pattern in half or more sessions`, `loop pattern in under half of sessions`, and `repeated rapid hint runs`. The names are deliberately clumsy, because a name leaves the notebook the moment somebody screenshots the chart.

The high-loop group sits clearly above zero at +0.66 and both other groups sit below it. Then look again, because **the rapid-run group and the low-loop group have almost the same mean growth**, -0.55 against -0.56, and the effect size between them is `d = +0.01` with an interval from -0.54 to +0.56. On this evidence they are indistinguishable. The headline a vendor would print, that rapid hint requesting is associated with worse learning, is an artifact of the comparison group: it holds only when the flagged group is compared against a pool that includes the high-loop students, and then the difference belongs to the loops.

The effect sizes here use a **degrees-of-freedom weighted** pooled standard deviation, which is the correct form when one comparison is 18 students against 102, and every one carries an interval. The interpretation prompt has teeth: what would you be entitled to do on Monday morning if somebody handed you this chart and a list of 18 names, and what would you refuse to do?

**📊 5. What follows what: the transition heatmap (6 minutes).** The detected-loop rate compresses a whole session to one bit. Bigrams keep more of the sequence: count every neighbouring pair of actions, put the earlier action in the rows and the later one in the columns, and divide each row by its total. Class-wide, an attempt is followed by a check 72 percent of the time and a hint request is followed by another hint request 42 percent of the time. The empty `reflect` row gets named for what it is, a consequence of how this tutor writes its log rather than a discovery about students, which is a failure mode worth carrying: an action that structurally cannot be followed shows up as a striking empty row and gets read as a striking behavioural finding.

Section 5.1 computes the identical grid twice, once for each of two log profiles, with a difference panel. The `request_hint` to `request_hint` cell reads 0 percent on the left and 77 percent in the middle, which is about as stark as behavioural data gets and is also **circular**, because the groups were built out of hint timing in the first place. The table marks which rows are contaminated that way, and the prompt asks what the uncontaminated contrasts suggest and how much smaller they are. ✏️ **Your turn 4** splits by outcome instead of by profile, which is the non-circular version of the same question.

**💬 Reflection.** Four prompts, three tied to this week's readings by author and one that reaches back to Week 3. Then the guest question section: come with a real question for Conrad Borchers, and the notebook drafts one you are welcome to improve on.

**✅ Before you leave.** A short checklist. The one item worth taking seriously is being able to state the definition of a complete regulation loop from memory.

## What this connects to in the readings

- **Winne (2022)**, *Learning analytics for self-regulated learning*: the argument the entire lab is built on, that self-regulated learning is not directly observable and traces are the footprints it leaves. Our detected-loop rate is a coarse stand-in for the recursive phase structure Winne describes, with `set_goal` standing in for planning, `attempt` for enacting, and `review_feedback` or `reflect` for evaluating. Section 2 then shows that on this log the stand-in collapses to a two-item checklist. The reflection asks the honest questions: what does the measure get most wrong about a real student, would more trace data fix it or is the problem of a different kind, and about a student whose detector never fired, what have you actually learned?
- **Zhang, Borchers, and Barany (2024)**, *Studying the interplay of self-regulated learning cycles and scaffolding through ordered network analysis across three tutoring systems*: the paper our transition heatmap is a blunt first cousin of. Ordered network analysis connects actions across a window of surrounding actions and weights them; our bigram matrix only sees the action immediately next door. Their framing also supplies the sharpest reflection prompt of the week, which is whether the tutor's hints, feedback, and plan view are revealing the regulation we measured or shaping it. Conrad Borchers is a coauthor, so this is the reading to arrive having actually read.
- **Viberg, Khalil, and Baars (2020)**, *Self-regulated learning and learning analytics in online learning environments: A review of empirical research*: the review that asks how much work on SRL measures SRL and how much of it measures activity wearing an SRL vocabulary. Turn it on this notebook. Of the four measures you built today, which would you defend as self-regulated learning, and which is activity with a nicer name?

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Audit the flag the way Week 3 audited the model.** The notebook says explicitly that it never opened `students.csv`. Open it, merge it onto the 18 flagged students, and compute what share of them are first generation, multilingual, or working long hours, against the base rates in the class. Week 3 taught you that bias enters through a feature choice. The feature here is a ten-second threshold. Say whether it enters, and if it does not, say how you would know if it had.
2. **Make the loop a real cycle rather than a single pass, and make the order matter.** The current rule asks whether a session contains at least one instance of the sequence, and Section 2 shows the ordering requirement selects nothing the presence of two buttons would not have selected. Count how many closures each session contains, using a matcher that resets to stage 0 after each one, and use closures per hour of tutor time instead of a binary. Then design a rule whose result would actually differ from the two-item checklist, and say what kind of tutor log would be needed for it to have anything to bite on. Re-run the correlation with quiz growth.
3. **Put time back into the transitions.** The heatmap treats a two-second transition and a four-minute transition as the same event. Build two heatmaps instead, one from transitions faster than the median gap and one from transitions slower, and difference them. What separates fast practice from slow deliberation, and which of the two looks more like the regulation you set out to measure?
4. **Sequence mining without a hand-written rule.** Instead of the state machine, extract every session's action sequence as a string and count the most frequent trigrams across the class, then compare the top ten for the highest and lowest quiz-growth thirds. This finds patterns you did not decide to look for in advance, which is the educational data mining move that Baker and Inventado described back in Week 2. Then argue about whether a pattern you did not name in advance can be called self-regulation.
5. **Sensitivity as a deliverable, not a footnote.** The appendix sweeps the rapid-hint-run thresholds and finds a broad plateau at 18 students with a cliff at the strictest corner, where a 3 second gap and 4 hints in a row leaves 1 student flagged and 5 in a row leaves none. Do the same sweep for the loop definition: vary which actions open and close a loop, and plot both prevalence and the correlation with growth across every combination. The notebook already reports that prevalence swings by tens of percentage points while the correlation barely moves. Explain why, in two sentences, and you will have understood something most published papers do not report.

## Troubleshooting

**"NameError: name 'traces' is not defined" or something similar.** You ran a cell out of order. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/srl_traces.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**I changed the student in the Section 1 timeline and got an empty table.** Not every student attended every session, so a student and session pair that does not exist returns nothing at all. The class averages seven of the eight tutor sessions per student. Before you call `show_session` with your own pair, run `traces[traces["student_id"] == "S003"]["session_id"].unique()` to see which sessions that student actually has, then pass one of those.

**My charts do not appear.** Make sure you ran the first code cell after the setup, which contains the imports and `%matplotlib inline`. If they still do not appear, restart and run all.

**"KeyError: 'S121'" in a Your turn cell.** The roster runs from `S001` to `S120`, zero-padded, so `S7` will not match anything either. Session IDs run `tutor_1` through `tutor_8`.

**My detected-loop rate is not 48.6 percent.** If you changed the closers in Your turn 2, that is expected and it is exactly what the exercise is for: `reflect` alone gives 30.6 percent. If you did not, restart and run all. The data generator is seeded, so a clean run reproduces the same numbers every time.

**Nothing changed when I moved the rapid-hint-run thresholds.** Then you moved along the plateau. Most of the threshold grid flags the same 18 logs, because the planted behaviour is extreme, but the strictest corner does not: a 3 second gap requiring 4 hints in a row flags 1 student and requiring 5 flags none. The lesson is not that thresholds do not matter, and it is not that this one is stable. It is that you cannot know which region you are standing in until you sweep the whole grid, which is what the appendix does.

**The transition heatmap has a grey row.** That is the `reflect` row, and it is grey because `reflect` always ends a session in this data, so there is no next action to record. An empty cell in a transition matrix is information, not a bug.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**I got a different answer than my neighbor.** Compare your loop definition and your two hint thresholds first. That is almost always the difference, and noticing it is the point of the session.

## A reminder about documenting AI use

There is nothing to upload for Week 7. This lab is a launch: we start it together in class and you finish reading and arguing with it on your own time. The next Canvas deliverable is Mini Project 4 in Week 8, and remember that there is no class on October 14, so Week 8 arrives on October 21 with the project already due.

Even though nothing is submitted this week, if you used an AI assistant while working through this notebook, to explain what a state machine does, to check your reading of the transition heatmap, or to help you sharpen the question you are bringing for our guest, save that exchange now.

The course AI policy has two parts that go in two different places, and it applies in full the moment any of this work reaches a mini project or your course research project. The conversation record itself goes into a **Word file attached to the Canvas AI Reflection submission**. The reflection goes in the **Canvas text box**, not in the Word file, and answers four questions: how you used it, whether it helped and how, whether it made your work more challenging and how, and what you learned about AI that you could pass on to the class.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. The habit that makes this painless is keeping the log as you go rather than reconstructing it afterward, and a week with nothing due is the cheapest possible time to practice.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
