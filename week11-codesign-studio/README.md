# 🎨 Week 11: Co-Design Studio

Whose dashboard is this, and who was in the room when we decided?

## At a glance

| | |
|---|---|
| **Session** | Wednesday, November 11, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Designing and Co-Designing Learning Analytics Systems |
| **Guest speaker** | None this week. The 60-minute discussion block is entirely student led. |
| **In-class time on this notebook** | About 25 minutes, in the hands-on block (4:30 to 5:00). The notebook is deliberately light: most of today is design dialogue, and the notebook is the sketchpad that gives the dialogue something to push against. |
| **Deliverable** | None from this notebook. It is a studio, not a graded submission. |
| **Due date** | The **Course Research Project Rough Draft** is due this week via Canvas, submitted separately from this notebook, together with your AI interaction log and reflection. |
| **Notebook** | `week11_codesign_studio.ipynb` |
| **Data used** | `students.csv`, `gradebook.csv`, `mmla_studio.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib, plotly |

## Objectives

By the end of this activity you will be able to:

1. **Represent** stakeholders as data: read a set of persona cards that carry goals, fears, and decision rights, and explain why decision rights change what a metric is allowed to mean.
2. **Sketch** a view for one stakeholder: choose a small set of metrics and render a quick plotly mock of what that person would actually see.
3. **Swap** seats and critique: read the same sketch through a second persona's eyes, and use the data to check which of your metrics tell a systematically different story about which students.
4. **Audit** your own semester: decide, artifact by artifact from weeks 3 through 10, who should have had a voice in each design decision and did not.

The through-line of the session: for ten weeks we have been the people who decide what gets measured, and the people being measured have not been in the room once. This is the last hands-on session of the semester, and it spends its final third turning the semester's own instruments back on the semester.

## What is in this folder

| File | What it is |
|---|---|
| `week11_codesign_studio.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
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
6. Select `week11-codesign-studio/week11_codesign_studio.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week11-codesign-studio/week11_codesign_studio.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week11-codesign-studio/week11_codesign_studio.ipynb`

**Colab is the recommended way to run this one.** Three of the figures are plotly, which means they are interactive: you can hover a bar to read its exact value and click a legend entry to hide a series. Colab draws them without any setup. A static preview of the `.ipynb` on the GitHub website often shows a blank space where an interactive figure should be, which is a rendering limitation and not a broken notebook. The two heatmaps also come with the same information printed as a plain table, alongside one and just above the other, precisely so the argument survives when the picture does not.

**Want to keep your edits?** In Colab choose **File > Save a copy in Drive** before you start changing cells. Your persona choice, your metric set, and your audit numbers are the record of what you decided today, and two of them belong in your Rough Draft notes.

You can also run the notebook locally with Jupyter if you prefer. It needs pandas, numpy, matplotlib, and plotly, all of which ship with Anaconda.

## Step-by-step walkthrough

Total time is about 25 minutes of code, which is the whole point: today the code is short so the conversation can be long. Every edit in this notebook is changing a word inside quotes or a number in a list. Nothing asks you to write code from scratch.

**⚙️ Setup (2 minutes).** Run the first code cell. It is long, and it is meant to be collapsed and ignored. It builds the roster, the gradebook, and the studio sensor table inside your runtime in about a second.

**⚙️ Load the tools and the data (1 minute).** Three files at three different grains: 120 students, 1,080 gradebook rows, 960 student-sessions of studio data. The markdown above the cell says what one row of each means and why today needs it. We are not doing statistics today. We are deciding what deserves to be on a screen, with real numbers underneath so the design argument has something to push against.

**🧑‍🤝‍🧑 1. Four people, written down as data (3 minutes).** Dana Okonkwo the teacher, Malik Ferrer the student, Ana Whitfield the advisor, and Bea Njoroge the parent, each with goals, fears, decision rights, the grain they think in, what they cannot change, and their access reality. Read the decision rights carefully: they are the field most dashboards skip, and a metric handed to someone with no authority to act on it is not information, it is pressure. Two of these four can change something about the course. Two can only change how they talk to a person.

**📊 2. The metric menu (3 minutes).** Eleven metrics computed from the real data, one number per student, so that putting one on a screen means putting an actual distribution on a screen. Each carries three annotations that matter more than its formula: its direction (and six of the eleven are marked *contested*), what a tired reader will mistake it for, and who can act on it, scored per persona as 0, 1, or 2. One metric, gaze at peers, scores 0 for everybody. It is on the menu because a camera can produce it, which is the whole of Carvalho and colleagues' argument in a single row.

**✏️ 3. Pick a persona and pick your metrics (2 minutes).** Three values to change: `MY_PERSONA`, `MY_METRICS`, and `FOCUS_STUDENT`. Maximum four metrics, and fewer is braver. Every metric costs the reader attention, and attention is the scarce resource in the room where the dashboard actually gets used. The cell validates your choices and tells you plainly if you mistype one.

**📊 The sketch (3 minutes).** Two plotly panels, because nearly every learning analytics view is secretly one of these two shapes: the class distribution of your first metric with your focus student marked, and your focus student's class percentile on each metric you chose. Read the warning attached to the second panel. Converting everything to percentiles makes mixed units comparable and also guarantees that somebody is at the bottom, even in a class where everyone is fine. The default focus student, S022, sits near the bottom of the class on speaking share, near the top on ideas contributed in chat, and well above the class average on quizzes. The prompt asks which of your four metrics would have found this student, and which would have misfiled them.

**📊 4. Whose story does each metric change (4 minutes).** For every metric on the menu, the standardized difference (Cohen's *d*) between a comparison group and everyone else. With the default group, the 24 multilingual students, the pattern is not "these students participate less." It is that **the channel decides the answer**: speaking time -0.59, share of the floor -0.58, speaking turns -0.58, and interruptions -0.47, against ideas contributed in chat +0.52, gaze at peers +0.42, and document edits +0.41. The grade metrics sit near zero. A view built on speaking time and a view built on chat ideas would generate two opposite lists of students to worry about from the same 120 people.

**🔁 5. The swap (2 minutes), then the whole menu crossed with the whole room (2 minutes).** First the mechanical part: for each of the other three personas, what they could actually do with your chosen metrics and which of their stated fears each one touches. Then the heatmap over all eleven metrics and all four people, where a `!` marks a metric that touches that person's fear. The interesting cells are the dark ones with a `!`: things somebody can act on and has reason to dread. The printed totals are worth staring at. Out of a maximum of 22, the teacher can act on 17, the student on 13, the advisor on 7, and the parent on 2.

**🕰️ 6. Retroactive design audit (4 minutes).** Every artifact this course built from week 3 to week 10, the design decision each one quietly made, and a score from 0 to 3 for how much voice each persona should have had: none, informed, consulted, veto. The dictionary comes pre-filled with the instructor's first guess and you are expected to argue with it. In the default scoring the student column totals 23 out of 24 and no student was in the room for any of it. One nuance to catch: week 10 is FractionQuest, played by 12-year-olds, and the same four persona labels carry very different weight when the learner is a child.

**✏️ 7. Stretch (optional, only if you finish early).** Add a fifth persona this course has ignored, write the refusal list, or run the worked scatter of speaking share against chat ideas. That last one prints a number worth carrying into the discussion: 27 students sit in the quiet, idea-rich quadrant, 12 of them multilingual, and their mean quiz score is 75.8 against a class mean of 75.7. That quadrant is not an anomaly to explain away. It is a list of specific people whom one dashboard would put on a worry list and another would put on a leaderboard.

**💬 Reflection.** Four prompts, one per reading plus one that turns the lens on your own project. These are the questions the discussion block opens with, and they are directly usable in your Rough Draft.

**✅ Submission checklist.** Nothing here is submitted. Save your copy, and paste two things into your project notes: your metric set with a one-sentence defense of why those and not others, and the one audit cell you moved with your reason for moving it.

## What this connects to in the readings

- **Carvalho, Martinez-Maldonado, Tsai, Markauskaite, and De Laat (2022)**, *How can we design for learning in an AI world?*: design starts from the activity, its purposes, and its setting, not from the traces a system happens to emit. The `gaze_at_peers` row on the metric menu exists only because a camera could produce it, and nobody in the room can act on it. The reflection asks what activity you would have had to design first for that metric to earn its place.
- **Bang and Vossoughi (2016)**, *Participatory design research and educational justice: Studying learning and relations within social change making*: participatory design is about studying and changing relations, not about collecting stakeholder preferences and then proceeding as planned. The decision-rights heatmap is a picture of a relation. The studio metrics are actionable for the teacher and inert for the advisor, the student, and the parent, which tells you who is the object of the measurement and who holds it.
- **Prieto-Alvarez, Martinez-Maldonado, and Anderson (2018)**, *Co-designing learning analytics tools with learners*: learners as designers rather than as data sources. Section 6 is the uncomfortable receipt for ten weeks of not doing this, and the prompt that follows it asks the only question that matters: not what would have felt better, but what would have been **different on the screen**.

## Stretch goals

For students who finish early or who arrive with programming experience:

1. **Add the fifth persona this course forgot.** Copy an entry in `PERSONAS`, write a teaching assistant, a disability services coordinator, a department chair, or an admissions office, then add the matching `act_` column to `CATALOG` and redraw the heatmap. The teaching assistant is the instructive case: close to a teacher's access and close to a student's lack of authority, so almost every cell in their column is a 1, and a column of 1s is a fair description of burnout.
2. **Write the refusal list and the interface copy.** Name the three metrics you would refuse to show to any of the four personas, and then write the exact sentence you would put in the interface where each one would have gone. "We do not show this" is a design decision that has to be readable by the person who wanted it, and drafting that sentence is harder and more useful than choosing the metric.
3. **Change the comparison group and compare the shapes.** Re-run section 4 with `COMPARE_GROUP` set to `'works_15plus'`, then to first generation status. The multilingual pattern is a clean modality story. The others are weaker and messier. Write down what it means that the same metric menu is fairer to one group than to another, and which group your Rough Draft's proposed system would treat worst.
4. **Design the percentile out of the sketch.** Replace the percentile panel with an absolute-scale panel that marks a band of no meaningful difference, so that a view can say "all good here" when all is in fact good. Then check whether your persona can still take the action they came for. If they cannot, you have found a real tension between honesty and actionability, and it is worth a paragraph in your draft.
5. **Cost out one co-design session.** Take the single artifact where you moved an audit score to 2 or 3 and write the agenda for the 45-minute session that score implies: who is in the room, what artifact you put in front of them, what decision they actually get to make, and what you do if they say no. Then specify what would have changed on the screen. A veto nobody can exercise is a 1 in disguise.
6. **Cross the menu against the semester.** Build a small table linking each of the eleven metrics to the week whose notebook produced it, and mark which ones you audited for group differences at the time. The metrics that arrived unaudited are the ones your own project is most likely to repeat.

## Troubleshooting

**"AssertionError: MY_PERSONA must be one of ['teacher', 'student', 'advisor', 'parent']"**, or an assertion about metrics or the focus student. Those checks are deliberate: they tell you about a typo immediately rather than letting it fail strangely three cells later. Read the message, fix the quoted string, and rerun that one cell. Metric keys are printed just above, and student ids run `S001` to `S120`.

**"Pick between 1 and 4 metrics."** That is the design constraint, not a bug. Four is the ceiling on purpose.

**"NameError: name 'M' is not defined" or something similar.** `M` is the metric table built in section 2, and everything downstream needs it. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart & Run All` in Jupyter. This fixes the large majority of problems.

**"FileNotFoundError: data/students.csv".** The setup cell did not run, or you restarted the runtime and skipped it. Scroll up and run the setup cell, then continue.

**The setup cell looks terrifying.** It is supposed to be ignored. Click the arrow at its left edge to collapse it. It is only in the notebook so that the notebook works with no downloads and no accounts.

**The interactive figures are blank when I look at the notebook on GitHub.** Expected. GitHub renders a static preview and plotly figures need a live page. Open the notebook in Colab and they appear. For the two heatmaps, the same numbers are also printed as a plain table (alongside the actionability heatmap, and in the cell just above the audit heatmap), so you can read the whole argument either way.

**A plotly figure is blank in my local Jupyter.** The notebook already switches to a lightweight renderer when it detects that it is not in Colab, but local setups vary. Try JupyterLab rather than classic Notebook, and if it is still blank, run this one in Colab. Colab is the supported path for week 11.

**I cannot tell the shades of the heatmap apart.** Do not try. Every cell prints its value as text on top of the color, and the same table is printed underneath in plain numbers. Read the numbers and the column totals, which is where the finding lives anyway.

**My audit numbers are different from the ones in the printout.** They should be. The dictionary in section 6 is the instructor's first guess and you were asked to argue with it. Bring one moved cell and your reason to the discussion.

**I have no idea which metrics to choose.** Start from your persona's question, not from the menu. If you are stuck, the appendix at the end of the notebook has a defensible set for each of the four personas with the reasoning attached. Read it after you have made an attempt, not before.

**Colab says it cannot find the repository.** You are signed into a different Google account, or you authorized GitHub without ticking the option that includes private repositories. Repeat the authorization step and watch for that checkbox.

**My numbers do not match the ones in the text.** If you changed a ✏️ **Your turn** cell, that is expected and good. If you did not, restart and run all: the notebook is seeded, so a clean run reproduces the same numbers every time.

## A reminder about documenting AI use

This notebook is not a graded submission, but something substantial is due this week: the **Course Research Project Rough Draft**, uploaded to Canvas separately from anything here.

If you used an AI assistant while drafting, or while working through this notebook, the course AI policy requires two things, and they go in two different places in the **AI Reflection** submission on Canvas:

- **The conversation record goes in an attached Word file.** Copy the actual exchanges into a `.docx` and attach it. The tool, the prompts, and the responses you got, as a record rather than a summary.
- **The four reflection questions are answered in the Canvas text box**, directly, not inside the attachment: what you asked for, what you accepted, what you rejected, and how you verified anything you kept.

If you used no AI at all, one line in the text box saying so is a complete and acceptable submission.

AI use is permitted in designated activities and must be documented. Undisclosed use is an Honor Code violation. Disclosed use costs you nothing. In a week spent arguing about who deserves a say in a system that measures them, disclosure is the same courtesy, pointed at yourself.

---

EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee · University of Virginia School of Education and Human Development
