# Week 5: Mini Project 2, Whose Writing Gets Called Effective?

This is the text analytics week. We build a pipeline one step at a time on 5,531 real student essays,
and the week ends in a finding that has to be interpreted rather than reported.

If you have never worked with text data, this notebook was written with you in mind. Nothing in it
asks you to write code from scratch. You run cells, read what comes out, and change a few clearly
marked values to see what those choices were doing to the result. Questions are welcome at any point,
including questions about a single line of code.

## At a glance

| | |
|---|---|
| **Session** | Week 5, Wednesday, September 23, 2026, Ridley Hall 137 |
| **Topic** | Text-Based Analytics and Natural Language Processing |
| **Notebook portion** | 3:30 to 4:20 PM, instructor-guided, opening the class |
| **Guest speaker** | Jiayi (Joyce) Zhang, Worcester Polytechnic Institute, 4:30 to 5:30 PM |
| **Debrief** | 5:30 to 5:50 PM, with time to return to the notebook |
| **Discussion Leadership** | None this week. Student-led discussion runs in Weeks 2 through 11, and each of the three of you leads **two** of those weeks. |
| **Notebook** | `week05_miniproject2_text_analytics.ipynb` |
| **Data** | **PERSUADE 2.0**, real, published, openly licensed: argumentative essays by United States students. A four-prompt subset: 5,531 essays and 63,211 human-annotated stretches of text, 55,070 of them named as a specific argumentative move. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`, folder `persuade-4prompts`. **Not synthetic.** |
| **License and citation** | CC BY-NC-SA 4.0 (attribution, non-commercial, share-alike). Crossley, S. A., Baffour, P., Tian, Y., Franklin, A., Benner, M., & Boser, U. (2024). A large-scale corpus for assessing written argumentation: PERSUADE 2.0. *Assessing Writing, 61*, 100865. https://doi.org/10.1016/j.asw.2024.100865 |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn. No installs. |
| **Needs internet?** | **Yes**, for the first code cell. Every notebook in this course downloads its data. |
| **Deliverable** | Mini Project 2: the executed notebook, an interpretation memo of about 300 words written in the notebook, and your AI interaction log plus the four reflection answers |
| **Due** | Via Canvas by **11:59 PM on Sunday, September 27, 2026** |
| **Prior coding experience needed** | None |

## What is and is not assessed

The notebook is submitted this week, so there is something to hand in. Coding skill is not what is
assessed. Every code cell already contains working code, and running the cells as written and reading
the output carefully is the assignment.

**The interpretation memo is the primary component used for grading.** In the rubric below, the two
criteria that separate the top level from the one beneath it are the last two, and both of them live
in the memo rather than in the code.

## The data, and why it changed

Weeks 1 through 4 were real too, but they were all *tables*: one row per student or per click, with
the interesting quantity already reduced to a number by somebody else. A grade is a number. A click
count is a number. Somebody decided, upstream of you, what counted.

This week the unit of analysis is a sentence a student wrote. Nothing has been reduced yet, and every
reduction from here is one you perform and have to account for.

**PERSUADE 2.0** is a corpus of argumentative essays written by students in United States public
schools, collected through state and district writing assessments. Every essay carries a **holistic
score from 1 to 6** assigned by a trained human rater. Every essay was then read again by human
annotators who marked the **boundaries of each argumentative move** in it (Lead, Position, Claim,
Counterclaim, Rebuttal, Evidence, Concluding Statement) and rated each move **Effective, Adequate, or
Ineffective**.

The subset in this notebook is four prompts, 5,531 essays by students in grades 8 through 12, and
63,211 marked stretches of text. 55,070 of those were named as a specific argumentative move, 55,068
of which also carry an effectiveness rating; the other 8,141 are the text the annotators judged was
not doing argumentative work. Nothing was altered except the choice of prompts and the packaging.

That second annotation layer is the reason for the switch. It is human ground truth, and it means a
model can be checked against what a person actually decided about the writing rather than against
your own intuition. No earlier file in this course carries one: a registry outcome tells you how an
enrollment ended, not what a reader thought of a sentence.

The cost is worth naming out loud, because the notebook does. Real students, most of them thirteen to
eighteen years old, sat in a testing session and argued about driverless cars, cell phone policy,
distance learning, and the Electoral College. Their work was kept, obtained by researchers, rated by
paid humans, stripped of names, and released openly. Data does not appear on its own. Somebody's
labor is always underneath it, and here some of that labor was done by children. Please cite the
corpus in your memo, do not redistribute the text, and do not use it commercially.

The mess comes with it. One third of the corpus is missing two demographic fields entirely, and the
hole is shaped exactly like one prompt. The spelling is the students' own. Two spans out of 63,211
lost their rating somewhere upstream. The notebook shows each of these, makes the decision in view,
and says what the decision cost.

## What I hope you leave with

1. **Building** a text analysis pipeline on real student writing: clean, tokenize, count, and say out
   loud what each cleaning decision deleted from the record.
2. **Scoring** stance with a lexicon small enough to read in full, then comparing what it explains
   about a human's judgment against the crudest feature in the file.
3. **Fitting and comparing** two topic models (NMF and LDA), interpreting their topics against four
   known writing prompts, and considering why a topic model that performs this well here may be less
   reassuring than it looks.
4. **Training and auditing** a bag-of-words classifier against 55,068 spans of human-annotated ground
   truth: where it succeeds, where it collapses, and what its errors suggest about the construct.
5. **Disaggregating** both the human ratings and the model's errors by writer group, and discussing
   what the pattern might mean without pretending the data settles it.

None of these is a coding objective. The pipeline is the more mechanical part of the week; what is
graded is the reading of what the pipeline found.

## What is in this folder

| File | What it is |
|---|---|
| `week05_miniproject2_text_analytics.ipynb` | The notebook. Everything happens here. |
| `README.md` | This file. |

There is nothing to download by hand and nothing to upload before class. The first code cell fetches
both files over plain HTTPS in about a second and prints what arrived. If the download fails, the
cell prints a plain-English message naming the repository it was trying to reach rather than a long
error trace.

## Opening it in Colab

This repository is public, so you need only a Google account and a browser.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week05-miniproject2-text-nlp/week05_miniproject2_text_analytics.ipynb)

Direct link:
`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week05-miniproject2-text-nlp/week05_miniproject2_text_analytics.ipynb`

If you would rather not use the badge, go to
[colab.research.google.com](https://colab.research.google.com), sign in, choose
**File > Open notebook**, click the **GitHub** tab, enter
`HakeoungLee/edis8100-teaching-learning-analytics` with the branch on `main`, and select
`week05-miniproject2-text-nlp/week05_miniproject2_text_analytics.ipynb`.

### Keeping your own copy

**Before you start editing:** in Colab please choose **File > Save a copy in Drive**. Your copy is
yours, your edits persist, and nothing you do affects the course repository. That copy is the one you
submit. **File > Download > Download .ipynb** saves a local one.

You can also run the notebook locally with Jupyter. It needs pandas, numpy, matplotlib, and
scikit-learn, all of which ship with Anaconda, plus a working internet connection for the first cell.

## Walkthrough

We open this together in class and get the pipeline running with colleagues available to ask. The
whole notebook executes in well under a minute. Sections marked **Going further (optional)** sit
outside the core path.

**Setup: where this data comes from.** A markdown cell to read before anything runs. It names the
dataset, its license, its citation, and the one-line story of who collected it and at what cost.
Stating where a dataset came from before opening it is a habit worth keeping. Then one code cell
downloads both files and prints a confirmation: 5,531 essays, 63,211 spans, 2,470,005 words of
student writing.

**Section 1: Meet the corpus.** Two files at two grain sizes, and the average essay contributes 11.43
spans. The four prompts are unbalanced (1,818 electoral college essays against 829 cell phone essays)
and score very differently (4.41 for distance learning against 3.01 for the electoral college). Then
the receipt on missing data, which is the first real-data lesson: **every one of the 1,818 electoral
college essays is missing both economic status and disability status**, and the 66 blank ELL values
all come from one other prompt. That is a signature of an upstream release decision rather than
random noise. The notebook makes its decision in view (keep all essays for the text work, use only
recorded rows for group comparisons, never impute) and states the cost: the economic comparison rests
on 3,697 essays and the disability comparison on 3,713, not 5,531.

**Section 2: Cleaning and tokenizing, and a receipt for what you deleted.** One real essay,
misspellings intact, passes through lowercasing, punctuation stripping, tokenizing, and stopword
removal. Then the receipt: 56.6 percent of every word in the corpus is gone, along with all 5,697
question marks, and scikit-learn's default stoplist has quietly removed `not` (22,632 uses),
`because` (14,417), `but` (11,703), and `however` (1,546). On argumentative writing those are not
filler, they are the load-bearing vocabulary of the genre. `alot` appears 422 times across 280 essays
and gets its own column, unconnected to the standard spelling, so a writer whose spelling differs
from the printed standard is represented as having used a different vocabulary.

**Your turn 1.** Decide which corpus-specific words belong on your stopword list, and see what your
choice does to the top of the frequency table.

**Section 3: Word frequencies with CountVectorizer.** Build the document-term matrix (5,531 by 6,736,
and 98.55 percent empty), plot the top 15 words, and notice that every one of them is a noun from a
prompt. Then the more useful question: which words are unusually common in one prompt relative to the
whole corpus. Try naming each prompt from its distinctive words before you look. Then the detail
worth stopping on: `principal` appears 591 times and `principle` 164, and 570 and 152 of those are in
the essays where students were told to write to their principal.

**Section 4: A stance lexicon you can read in full.** Fifty-two words, hedges and boosters, printed
in the notebook in plain sight. Score every essay, then the uncomfortable result: hedges correlate
with the human holistic score at r = -0.091 and boosters at r = +0.125, while **raw word count**,
which needed no lexicon and no theory, correlates at **r = +0.559**, and at **rho = +0.753** once
ranks are compared instead of raw values. Essay length runs from 146 to 6,188 words, so the notebook
prints both and quotes the rank version. The shortest quarter of essays averages 2.36 and the longest
averages 4.69. And 122 essays contain no word from either list, so the instrument reports them as
neutral when they are simply unmeasured. A three-row table separates what the data show, what is a
plausible interpretation, and what the file cannot establish.

**Your turn 2.** Delete six words from the hedge lexicon and watch the correlation change sign, from
-0.091 to +0.077, and from rho = -0.067 to +0.141. Same corpus, same construct, same defensible
reasoning, six words.

**Section 5: Topic modeling, NMF and LDA side by side.** Fit both at four topics and check them
against the four known prompts. Both recover them: NMF misfiles 1 essay out of 5,531 (adjusted Rand
index 0.9996), LDA misfiles 5 (0.9981). Then the reasons to hold that conclusion loosely. You knew
there were four groups, the four subjects share almost no vocabulary, and the thing recovered was
already a column in the file.

**Your turn 3.** Ask for eight topics instead. Inside the distance learning prompt alone, NMF splits
1,498 essays into three groups of nearly identical length (604, 578, and 572 words) but very
different composition: 12.7, 27.9, and 37.5 percent English language learners, scoring 4.69, 4.18,
and 4.25. Nobody gave the model a demographic column. A model trained on language has access to
language, and language carries traces of the writer.

**Section 6: The step no earlier week could take, human ground truth.** 55,068 rated spans, 19,200
claims against 2,215 rebuttals (8.7 to 1, which is a fact about a timed prompt that never asked for a
rebuttal at least as much as about young writers), and 76.7 percent of everything rated Adequate.
Train a bag-of-words naive Bayes to predict the discourse move and check it against 13,767 human
judgments it has never seen: 54.7 percent accurate against a 34.9 percent baseline. Then read the
rows instead of the average. Position 65.6 percent, Evidence 61.1 percent, Counterclaim 34.3 percent,
**Rebuttal 15.3 percent**. Read the misclassified spans and the diagnosis is precise: Counterclaim
and Rebuttal are defined by their relationship to other moves, and the model was handed a sentence
with no essay attached. The same cell also checks the split itself: 99.9 percent of test spans come
from an essay that also supplied training spans, so it refits the model with `GroupShuffleSplit` on
`essay_id` and prints both accuracies (0.5472 random span split, 0.5644 split by essay). A leak you
can name is not the same as a leak that matters, and this one does not.

**Your turn 4.** Swap in logistic regression. Accuracy climbs from 0.547 to 0.680 and Rebuttal recall
only from 0.153 to 0.265, while Counterclaim gets slightly worse (0.343 to 0.318). When a better
algorithm does not fix a failure, the failure is in the representation. Then have the model label
four sentences and see whether you agree with it.

**Then the harder question:** can a bag of words predict whether a move *worked*? It reports 83.4
percent accuracy. Saying "not Effective" to everything reports 81.5 percent. The model finds 31.1
percent of the genuinely effective spans, and a model whose only feature is span word count reaches
82.7 percent.

**Section 7: Whose writing gets called effective?** The scores raters assigned differ by writer
group: essays by writers classified as English language learners average 3.10 against 3.49 (n = 537
and 4,928, d = -0.33, CI [-0.42, -0.24]), economically disadvantaged 3.41 against 3.86 (n = 1,627 and
2,070, d = -0.40), identified as having a disability 3.41 against 3.68 (n = 350 and 3,363, d = -0.24,
CI [-0.35, -0.13], the widest interval because that group has 350 essays). All three grouping columns
are administrative classifications applied by school systems, not properties of writers, and the
notebook says so on the figure and in the text around it. This is an exercise in reading a recorded
group difference carefully, and the notebook keeps what each variable records, the group size, and
the interval in view alongside every point estimate.

Then the Simpson's paradox detour: the pooled ELL gap of -0.39 is **smaller than the gap inside every
single prompt**, because ELL-classified writers are concentrated in the highest-scoring prompt. Then
the sharper comparison. Among spans a human already identified as a **Counterclaim**, 17.1 percent by
non-ELL-classified writers were rated Effective against 5.5 percent by ELL-classified writers. For
**Evidence** it is 21.9 against 6.6, with Ineffective running the other way at 7.6 against 11.4. The
structural work is already credited. What differs is the judgment of how well it was done.

Because those are percentages of spans and one essay supplies about eleven spans, the notebook puts
an **essay-clustered bootstrap interval** on every one of them: 5,342 ELL spans are 537 people, not
5,342 people. Pooled across moves the gap is -13.7 points, 95 percent [-15.1, -12.2], and all seven
per-move intervals sit on the same side of zero. Clustering nearly doubles the interval, from a
half-width of 0.74 points to 1.43, and the finding survives it. A result that holds only when
clustered data is treated as independent was never a result.

**Then the notebook turns its own lesson on its own finding.** The span-level comparison was pooled
across four prompts, which is the mistake the Simpson's paradox detour just described. So it is
recomputed one prompt at a time. The gap survives: it is negative in all four prompts, running from
-5.0 to -24.9 percentage points against a pooled -13.7. And a second thing falls out. Holding the
classification constant and changing only the prompt, the Effective rate for the same group moves
from 5.4 to 31.1 percent and the Ineffective rate from 0.5 to 11.1. Different students sit in those
rows, so this is not a within-person comparison and it does not show that the raters differed. What
it does establish is that the output of this scale moves a great deal with which pile a span came
from, which is a source of variation larger than the gap anyone is trying to explain.

A second three-row table separates what the data show, the plausible interpretations, and what the
file cannot establish. The notebook then lays out four readings in the order the course insists on,
the instrument, the construct, the setting and circumstances, and only fourth anything about the
writing, and declines to choose between them because this file cannot. It states plainly what may not
be concluded from this evidence: that these students write worse. Finally it audits the Section 6
model by writer group, with intervals on both recalls (31.8 percent [29.8, 33.9] for
non-ELL-classified writers, 14.8 percent [7.3, 23.2] for ELL-classified writers, that second one
resting on 88 effective spans from 60 essays), and traces the chain link by link.

**Section 8, Going further (optional), and Your turn 5.** Try another group and another move.
Evidence spans by writers classified as economically disadvantaged: 15.1 percent Effective against
26.6, a gap of -11.5 points with a 95 percent essay-clustered interval of [-13.8, -9.3]. Then try
`gender`, where the gap is +4.6 points, interval about [+2.7, +6.4], smaller and running the other
way, which is the point of the exercise: the gaps are not all the same size, and the largest fall on
the classifications that track schooling conditions. The cell prints which prompts each comparison
drew on, because economic status is blank for every electoral college essay and gender is not, so the
two comparisons are not on the same corpus until you make them so.

**Reflection and the interpretation memo.** Four reading-linked prompts, five questions to sit with,
and the memo template. This is the graded thinking.

**Submission checklist.** Three items, all required.

**Appendix.** Notes on every "Your turn," written as reasoning rather than answer keys, because in
each case more than one answer is defensible.

## The figures we will make

1. **Essays per prompt, and the distribution of holistic scores.** The corpus holds more than twice
   as much of one prompt as of another, and 59 percent of essays were scored 3 or 4.
2. **The 15 most frequent words.** Every one of them is a noun from a prompt, which is why a raw
   frequency table is a starting point rather than a finding.
3. **Stance rates by human score, beside mean score by essay-length quartile.** The lexicon barely
   moves across the score range; length moves from 2.36 to 4.69.
4. **Two topic-model heatmaps.** Real prompt against assigned topic, for NMF and LDA, with the
   adjusted Rand index on each.
5. **Spans per discourse move, and the effectiveness mix within each.** Many claims, few rebuttals,
   and three quarters of everything Adequate.
6. **The confusion matrix for the discourse-move classifier.** The rows carry the information, not
   the diagonal.
7. **Mean holistic score by administrative classification,** with the group size printed beside every
   bar.
8. **Effective and Ineffective rates for four moves, by ELL classification.**
9. **The rating mix for one move, by whichever group column you choose** in the optional section.

## Rubric: Mini Project 2 (100 points)

Each criterion is scored at one of four levels.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | The full pipeline runs cleanly and every stage is motivated: you can say why each step exists and what it makes possible downstream. | All stages completed and the notebook runs top to bottom. Motivation is present but thin in places. | Most stages completed, with gaps or a step that runs without a stated purpose. | Pipeline incomplete or does not execute. |
| **Data Preparation and Technical Care** | Cleaning decisions are deliberate, documented, and audited: you show what was deleted and where it would have mattered. Missing data is named, not silently dropped. Raw and cleaned text are used appropriately per analysis. | Cleaning is competent and mostly documented. Minor unexamined defaults remain. | Cleaning applied with defaults accepted uncritically. Some analyses run on the wrong version of the text. | Little evidence of preparation care; results depend on choices never named. |
| **Analysis and Visualization Choices** | Method choices are justified against alternatives. Figures are titled, labeled, readable, and chosen to reveal the claim rather than decorate it. | Appropriate methods and clear figures. Justification present but brief. | Methods applied without comparison; figures present but hard to read or unlabeled. | Methods or figures missing, mislabeled, or misleading. |
| **Interpretation and Educational Meaning** | The memo takes a position on the Section 7 finding, cites specific numbers with their sample sizes, states what a reader choosing a different reading would conclude, and connects the result to something a school could act on. | A clear interpretation supported by evidence from the notebook. The competing readings are named but not fully adjudicated. | Interpretation restates the numbers without deciding anything. | Interpretation absent, or contradicted by the output. |
| **Critical Reflection: Limits, Ethics, Equity** | Names who is missing and what that does to the claim, sizes at least one limitation rather than only listing it, and names what would not be appropriate to report and to whom. Treats the writers as children whose work was collected, not as rows. | Limits and ethical considerations addressed substantively. | Limitations mentioned generically ("the sample is not representative"). | Limitations, ethics, or equity not addressed. |

The two criteria that separate a 20 from a 16 in this project are the last two, and both of them live
in the memo rather than in the code.

## Going further (optional)

For anyone who finishes the core path early or wants a stronger analysis section. None of this is
required.

1. **Other groups, other moves** (Section 8, already built). Change `GROUP_COLUMN` and `MOVE`. Try
   `student_disability_status` on `Counterclaim` and notice how a group of 183 spans changes how much
   there is to say.
2. **Split by essay for the effectiveness model too.** Section 6 already checks this for the
   discourse-move classifier and finds the leak costs nothing there. The effectiveness model in the
   next cell still uses a random span split. Redo that one with `GroupShuffleSplit` on `essay_id`,
   and while you are there, put an essay-clustered interval on the 1.9 point accuracy gain over the
   majority-class rule. Report the interval next to the point, whichever way it comes out, and say
   what the width tells a district that was about to buy something on the strength of the point
   alone.
3. **Give the classifier context.** Counterclaim and Rebuttal fail because a span has no essay
   attached. Add features the bag of words cannot see: the span's relative position in the essay, the
   type of the preceding span, whether the essay's Position span is for or against. Feature
   engineering, not modeling, is the fix.
4. **Predict the holistic score instead.** You have `holistic_essay_score` and full text. Fit a
   regression, then disaggregate the residuals by ELL classification, economic classification, and
   disability identification. Which groups does your model systematically under-score relative to the
   rater, and does the residual gap shrink once you control for prompt?
5. **Measure recall on the effectiveness model by prompt.** The model was trained across four prompts
   of very different difficulty. Does it do better on the easy one?
6. **Read fifty spans.** Take fifty Counterclaim spans, twenty-five rated Effective and twenty-five
   Adequate, strip the ratings, and code them yourself against a rubric you write first. Then
   compare. That is a small reliability study, and it is more publishable than the pipeline.

## Troubleshooting

**"The first cell prints a wall of text about the download failing."**
That is the friendly message, not a crash. Work the four steps it lists, in order: check that you are
online, run the cell again, open `https://github.com/HakeoungLee/edis8100-datasets` in a browser tab,
and if you are on a locked-down campus or hospital network, try a different network or run in Colab.
That repository is public, so this is never about a GitHub account or an invitation.

**"NameError: name 'essays' is not defined"** (or `spans`, `MY_STOPWORDS`, `X_counts`, `rated`, or
similar). A cell above this one has not been run in this session. Cells share memory in order.
**Runtime > Restart session and run all**, then wait for every cell to finish. This resolves most notebook
problems.

**A pink or red block of text that does not say `Error`.**
That is a warning rather than an error. Warnings are normal in scientific Python. Only `Error` and
`Traceback` need your attention.

**`ConvergenceWarning` from NMF, LDA, or logistic regression.**
You may see one if you raise the number of topics in Your turn 3, or if you lower a `max_iter` value.
It is harmless: the model has fit, and the optimizer simply stopped at the iteration cap. Raising
`max_iter` makes it go away.

**My numbers differ from my neighbor's.**
Check that you both ran every cell in a fresh runtime and that neither of you edited a "Your turn"
cell before this point. The data file is fixed and every model is seeded with `RANDOM_STATE = 8100`,
so identical input gives identical output.

**The notebook runs but a figure looks empty.**
Re-run the cell. If a figure is genuinely blank, the cell that produces its data probably did not
run.

**Colab says "Cannot find notebook" or shows a 404.**
You are most likely signed into a different Google account. Check the profile picture in the top right
corner, switch to the account you want, and open the link again.

**I edited something and now nothing works.**
Every "Your turn" cell has a working default. Compare against the appendix, or open a fresh copy of
the notebook from Colab and paste your work back in.

**Red text appeared.**
Python errors are wordy, and none of them means something has been damaged. The **last line** of the
error usually names the real problem. Please ask a classmate, then post on Canvas, then email me, and
we will read it together.

## Documenting AI use

The course permits AI use on this mini project and asks that you document it. Undisclosed AI use is
an Honor Code violation; disclosed, policy-compliant use is not penalized.

Both pieces go to the Canvas **AI Reflection** submission, in two different places on that page.

- **The conversation record goes in a Word file, attached to that submission.** Every relevant
  exchange, across every session and every tool, pasted in full. Not a summary, not a link to a
  shared conversation, and not pasted into the text box.
- **The reflection goes in the Canvas text box on the same page.** Copy in the four questions from
  the syllabus and answer each one: how you used it; whether it helped and how; whether it made your
  work more challenging in any way; and what lesson about AI from this week you would pass on to a
  friend or the class.
- If you used no AI at all, say so in one line in the text box and attach nothing. A blank submission
  is not the same as a declaration.

A note specific to this week. Text analysis is unusually easy to have an AI do for you, and unusually
easy to get subtly wrong. If a model writes your lexicon, names your topics, or drafts your
interpretation of the Section 7 gap, please say so, and then do the thing the model cannot do: open
the spans, read what the students actually wrote, and check whether the interpretation survives
contact with them. That checking is the assignment.

## Connections to this week's readings

The required readings are Allen, Creer and Öncel (2022), Gibson and Shibani (2022), and Dowell and
Kovanović (2022), all from the *Handbook of Learning Analytics* (2nd ed.). Dowell, Lin, Godfrey and
Brooks (2020) is an additional reading. The notebook draws on them briefly at four points, and the
reflection returns to them:

- **Allen, Creer and Öncel (2022)** argue for a multi-dimensional view of language as evidence about
  learning, on the grounds that no single index of a text captures what a learner is doing. Section 4
  puts two indices side by side and finds that the theoretically motivated one moves least.
- **Gibson and Shibani (2022)** treat writing analytics as a sequence of representational decisions
  and are concerned with the distance between what a tool measures and what a teacher or a student
  should actually be handed. The stoplist in Section 2 and the model audit in Section 7 are both
  versions of that concern.
- **Dowell and Kovanović (2022)** model educational discourse as structured and social, so that what
  a contribution is doing depends on the contributions around it. Section 6 is a concrete case: the
  two relationally defined moves are the two a span-level bag of words cannot recover.
- **Dowell, Lin, Godfrey and Brooks (2020)** connect emergent sociocognitive roles to collaborative
  outcomes, which is the direction this notebook would have to grow in to move from moves to roles.

## Data and ethics

Everything we touch this semester is real. Nine published, openly licensed datasets are used across
the lab weeks, and no notebook in this course generates a row.

This week's corpus holds writing by real children in United States public schools, produced in a
testing session, rated by paid human raters, anonymized, and released under CC BY-NC-SA 4.0 so that
others could learn from it. None of them agreed to be a teaching example. It is worth asking who
could be harmed by a claim before making it, noticing when a metric reduces a person to one number,
and noticing which people are not in the file at all.

Where every dataset in the course comes from, who is in it, and how it is licensed is in the course
guide *Finding and Evaluating Learning Analytics Data*.

---

*EDIS 8100: Teaching and Learning Analytics · Fall 2026 · Dr. Hakeoung Hannah Lee ·
University of Virginia, School of Education and Human Development.*

*Data: PERSUADE 2.0, a four-prompt subset, licensed CC BY-NC-SA 4.0. Crossley, S. A., Baffour, P.,
Tian, Y., Franklin, A., Benner, M., & Boser, U. (2024). A large-scale corpus for assessing written
argumentation: PERSUADE 2.0. Assessing Writing, 61, 100865.
https://doi.org/10.1016/j.asw.2024.100865 These are real essays by real students. Please attribute
the corpus, do not redistribute the text, and do not use it commercially.*
