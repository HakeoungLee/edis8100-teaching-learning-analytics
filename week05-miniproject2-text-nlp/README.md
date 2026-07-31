# 💬 Week 5: Mini Project 2, Whose Writing Gets Called Effective?

A text analytics pipeline built one honest step at a time on 5,531 real student essays, ending in a finding you have to interpret yourself.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 23, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Text-Based Analytics and Natural Language Processing |
| **Guest speaker** | Jiayi (Joyce) Zhang, University of Pennsylvania |
| **In-class time on this notebook** | About 20 minutes, launched in the hands-on studio block (4:40 to 5:00). This is a launch, not the whole project. The notebook's core path is about 75 more minutes; the memo takes the rest, so plan about three focused hours outside class, as the Mini Project 2 Brief sets out. |
| **Deliverable** | Mini Project 2: the executed notebook, a 300-word interpretation memo, and your AI interaction log plus the four reflection answers |
| **Due date** | This week, via Canvas, by the deadline posted on the Canvas assignment page |
| **Notebook** | `week05_miniproject2_text_analytics.ipynb` |
| **Data used** | **PERSUADE 2.0**, a real, published, openly licensed corpus of argumentative essays by United States students. A four-prompt subset: 5,531 essays and 63,211 human-annotated discourse spans. Downloaded by the first code cell from `github.com/HakeoungLee/edis8100-datasets`. **Not synthetic.** |
| **License and citation** | CC BY-NC-SA 4.0 (attribution, non-commercial, share-alike). Crossley, S. A., Baffour, P., Tian, Y., Franklin, A., Benner, M., & Boser, U. (2024). A large-scaled corpus for assessing text readability and writing quality: The PERSUADE corpus. *Assessing Writing, 61*, 100849. |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn. No installs. You do need an internet connection this week. |

## The data, and why it changed

Weeks 1 through 4 ran on a simulated course at a university that does not exist. That was a deliberate ethical choice and it stays defensible: we rehearsed judgment without reading anyone's records. But simulated data arrives clean, balanced, and arranged so that the lesson works, and real data does not arrange itself into lessons.

So this week the data is real.

**PERSUADE 2.0** is a corpus of argumentative essays written by students in United States public schools, collected through state and district writing assessments. Every essay carries a **holistic score from 1 to 6** assigned by a trained human rater. Every essay was then read again by human annotators who marked the **boundaries of each argumentative move** in it (Lead, Position, Claim, Counterclaim, Rebuttal, Evidence, Concluding Statement) and rated each move **Effective, Adequate, or Ineffective**.

The subset in this notebook is four prompts, 5,531 essays by students in grades 8 through 12, and 63,211 marked spans, 55,068 of which carry an effectiveness rating. Nothing was altered except the choice of prompts and the packaging.

That second annotation layer is the reason for the switch. It is human ground truth, and it means you can build a model and check it against what a person actually decided rather than against your own intuition. Synthetic data cannot do that: a generator agrees with you by construction.

The cost is worth naming out loud, because the notebook does. Real students, most of them thirteen to eighteen years old, sat in a testing session and argued about driverless cars, cell phone policy, distance learning, and the Electoral College. Their work was kept, obtained by researchers, rated by paid humans, stripped of names, and released openly. Data does not appear. Somebody's labor is always underneath it, and here some of that labor was done by children. Cite the corpus in your memo, do not redistribute the text, and do not use it commercially.

The mess comes with it. One third of the corpus is missing two demographic fields entirely, and the hole is shaped exactly like one prompt. The spelling is the students' own. Two spans out of 63,211 lost their rating somewhere upstream. The notebook shows you each of these, makes the decision in front of you, and says what the decision cost.

## Objectives

By the end of this activity you will be able to:

1. **Build** a text analysis pipeline on real student writing: clean, tokenize, count, and state out loud what each cleaning decision deleted from the record.
2. **Score** stance with a lexicon small enough to read in full, then show that it explains less about a human's judgment than the crudest feature in the file does.
3. **Fit and compare** two topic models (NMF and LDA), interpret their topics against four known writing prompts, and explain why a topic model that looks brilliant here should not reassure you.
4. **Train and audit** a bag-of-words classifier against 55,068 spans of human-annotated ground truth: where it succeeds, where it collapses, and what its errors reveal about the construct.
5. **Disaggregate** both the human ratings and the model's errors by writer group, and argue about what the pattern means without pretending the data settles it.

The through-line of the session: the pipeline is the easy part. The deliverable is not the pipeline. It is the defended reading of what the pipeline found.

## What is in this folder

| File | What it is |
|---|---|
| `week05_miniproject2_text_analytics.ipynb` | The notebook. Runs top to bottom untouched. |
| `README.md` | This file. |

There is no `data/` folder this week and nothing to download by hand. The first code cell pulls both files straight from the course dataset repository over the internet, in about a second, and prints what arrived. If the download fails it tells you why in plain English instead of throwing a traceback at you.

## How to open this in Colab

The course repository is **private**, so the ordinary Colab badge will not work until you have authorized Colab to see private repositories. Do this once and it keeps working all semester.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with the Google account you use for class.
2. Choose **File > Open notebook**.
3. Click the **GitHub** tab.
4. Click **Authorize with GitHub**, and on the permissions screen make sure you **include private repositories**. This is the step people miss.
5. In the repository dropdown pick `HakeoungLee/edis8100-teaching-learning-analytics`.
6. Select `week05-miniproject2-text-nlp/week05_miniproject2_text_analytics.ipynb`.

Once you have authorized Colab, this badge works too:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week05-miniproject2-text-nlp/week05_miniproject2_text_analytics.ipynb)

`https://colab.research.google.com/github/HakeoungLee/edis8100-teaching-learning-analytics/blob/main/week05-miniproject2-text-nlp/week05_miniproject2_text_analytics.ipynb`

**Do this before you start editing:** in Colab choose **File > Save a copy in Drive**. Your copy is yours, your edits persist, and nothing you do affects the course repository. You will be submitting your copy.

You can also run the notebook locally with Jupyter. It needs pandas, numpy, matplotlib, and scikit-learn, all of which ship with Anaconda, plus a working internet connection for the first cell.

## Step-by-step walkthrough

Run every cell in order. The whole notebook executes in well under a minute.

**⚙️ Setup: where this data comes from.** Read this markdown cell before you run anything. It names the dataset, its license, its citation, and the one-line story of who collected it and at what cost. You should never analyze data whose origin you cannot state. Then one code cell downloads both files and prints a confirmation: 5,531 essays, 63,211 spans, 2,470,005 words of student writing.

**📊 Section 1: Meet the corpus.** Two files at two grain sizes, and the average essay contributes 11.43 spans. The four prompts are wildly unbalanced (1,818 electoral college essays against 829 cell phone essays) and score very differently (4.41 for distance learning against 3.01 for the electoral college). Then the receipt on missing data, which is the first real-data lesson: **every one of the 1,818 electoral college essays is missing both economic status and disability status**, and the 66 blank ELL values all come from one other prompt. That is a signature of an upstream release decision, not random noise. The notebook makes its decision in front of you (keep all essays for the text work, use only recorded rows for group comparisons, never impute) and states the cost: the economic comparison rests on 3,697 essays and the disability comparison on 3,713, not 5,531.

**📊 Section 2: Cleaning and tokenizing, and a receipt for what you deleted.** Watch one real essay, misspellings intact, pass through lowercasing, punctuation stripping, tokenizing, and stopword removal. Then read the receipt: 56.6 percent of every word in the corpus is gone, along with all 5,697 question marks, and scikit-learn's default stoplist has quietly removed `not` (22,632 uses), `because` (14,417), `but` (11,703), and `however` (1,546). On argumentative writing those are not filler, they are the load-bearing vocabulary of the genre. `alot` appears 422 times across 280 essays and gets its own column, unconnected to the correctly spelled version.

**✏️ Your turn 1.** Decide which corpus-specific words belong on your stopword list, and see what your choice does to the top of the frequency table.

**📊 Section 3: Word frequencies with CountVectorizer.** Build the document-term matrix (5,531 by 6,736, and 98.55 percent empty), plot the top 15 words, and notice that every one of them is a noun from a prompt. Then the real move: which words are unusually common in one prompt relative to the whole corpus. Try naming each prompt from its distinctive words before you look. Then the detail worth stopping on: `principal` appears 591 times and `principle` 164, and 570 and 152 of those are in the essays where students were told to write to their principal.

**📊 Section 4: A stance lexicon you can read in full.** Fifty-two words, hedges and boosters, printed in the notebook in plain sight. Score every essay, then discover the uncomfortable result: hedges correlate with the human holistic score at r = -0.091 and boosters at r = +0.125, while **raw word count**, which needed no lexicon and no theory, correlates at **r = +0.559**. The shortest quarter of essays averages 2.36 and the longest averages 4.69. And 122 essays contain no word from either list, so the instrument reports them as neutral when they are simply unmeasured.

**✏️ Your turn 2.** Delete six words from the hedge lexicon and watch the correlation change sign, from -0.091 to +0.077. Same corpus, same construct, same defensible reasoning, six words.

**📊 Section 5: Topic modeling, NMF and LDA side by side.** Fit both at four topics and check them against the four known prompts. Both nail it: NMF misfiles 1 essay out of 5,531 (adjusted Rand index 0.9996), LDA misfiles 5 (0.9981). Then the argument for why that is not a happy ending. You knew there were four groups, the four subjects share almost no vocabulary, and the thing recovered was already a column in the file.

**✏️ Your turn 3.** Ask for eight topics instead. Inside the distance learning prompt alone, NMF splits 1,498 essays into three groups of nearly identical length (604, 578, and 572 words) but very different composition: 12.7, 27.9, and 37.5 percent English language learners, scoring 4.69, 4.18, and 4.25. Nobody gave the model a demographic column. A model trained on language has access to language, and language carries the writer.

**📊 Section 6: The step synthetic data could never support, human ground truth.** 55,068 rated spans, 19,200 claims against 2,215 rebuttals (8.7 to 1), and 76.7 percent of everything rated Adequate. Train a bag-of-words naive Bayes to predict the discourse move and check it against 13,767 human judgments it has never seen: 54.7 percent accurate against a 34.9 percent baseline. Then read the rows instead of the average. Position 65.6 percent, Evidence 61.1 percent, Counterclaim 34.3 percent, **Rebuttal 15.3 percent**. Read the misclassified spans and the diagnosis is precise: Counterclaim and Rebuttal are defined by their relationship to other moves, and you handed the model a sentence with no essay attached.

**✏️ Your turn 4.** Swap in logistic regression. Accuracy climbs from 0.547 to 0.680 and Rebuttal recall only from 0.153 to 0.264, while Counterclaim gets slightly worse. When a better algorithm does not fix a failure, the failure is in the representation. Then have the model label four sentences and see whether you agree with it.

**Then the harder question:** can a bag of words predict whether a move *worked*? It reports 83.4 percent accuracy. Saying "not Effective" to everything reports 81.5 percent. The model finds 31.1 percent of the genuinely effective spans, and a model whose only feature is span word count reaches 82.7 percent.

**📊 Section 7: Whose writing gets called effective?** Human holistic scores differ by writer group: ELL writers average 3.10 against 3.49 (n = 537 and 4,928), economically disadvantaged writers 3.41 against 3.86, writers identified as having a disability 3.41 against 3.68. Then the Simpson's paradox detour: the pooled ELL gap of -0.39 is **smaller than the gap inside every single prompt**, because ELL writers are concentrated in the highest-scoring prompt. Then the sharper finding. Among spans a human already identified as a **Counterclaim**, 17.1 percent by non-ELL writers were rated Effective against 5.5 percent by ELL writers. For **Evidence** it is 21.9 against 6.6, with Ineffective running the other way at 7.6 against 11.4. The structural work is already credited. What differs is the judgment of how well it was done. The notebook gives you three defensible readings and refuses to choose between them, because this file cannot. Finally it audits your own Section 6 model by writer group and traces the chain link by link.

**📊 Section 8 (stretch) and ✏️ Your turn 5.** Try another group and another move. Evidence spans by economically disadvantaged writers: 15.1 percent Effective against 26.6. Then try `gender`, where the spread is 4.6 points and runs the other way, which is the point of the exercise.

**💬 Reflection and the interpretation memo.** Five reading-linked questions and the memo template. This is the graded thinking.

**✅ Submission checklist.** Three items, all required.

**Appendix.** Notes on every "Your turn," written as reasoning rather than answer keys, because in each case more than one answer is defensible.

## Rubric: Mini Project 2 (100 points)

Each criterion is scored at one of four levels.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | The full pipeline runs cleanly and every stage is motivated: you can say why each step exists and what it makes possible downstream. | All stages completed and the notebook runs top to bottom. Motivation is present but thin in places. | Most stages completed, with gaps or a step that runs without a stated purpose. | Pipeline incomplete or does not execute. |
| **Data Preparation and Technical Care** | Cleaning decisions are deliberate, documented, and audited: you show what was deleted and where it would have mattered. Missing data is named, not silently dropped. Raw and cleaned text are used appropriately per analysis. | Cleaning is competent and mostly documented. Minor unexamined defaults remain. | Cleaning applied with defaults accepted uncritically. Some analyses run on the wrong version of the text. | Little evidence of preparation care; results depend on choices never named. |
| **Analysis and Visualization Choices** | Method choices are justified against alternatives. Figures are titled, labeled, readable, and chosen to reveal the claim rather than decorate it. | Appropriate methods and clear figures. Justification present but brief. | Methods applied without comparison; figures present but hard to read or unlabeled. | Methods or figures missing, mislabeled, or misleading. |
| **Interpretation and Educational Meaning** | The memo takes a position on the Section 7 finding, cites specific numbers with their sample sizes, states what a reader choosing a different reading would conclude, and connects the result to something a school could act on. | A clear interpretation supported by evidence from the notebook. The competing readings are named but not fully adjudicated. | Interpretation restates the numbers without deciding anything. | Interpretation absent, or contradicted by the output. |
| **Critical Reflection: Limits, Ethics, Equity** | Names who is missing and what that does to the claim, sizes at least one limitation rather than only listing it, and says what you would refuse to report and to whom. Treats the writers as children whose work was collected, not as rows. | Limits and ethical considerations addressed substantively. | Limitations mentioned generically ("the sample is not representative"). | Limitations, ethics, or equity not addressed. |

The two criteria that separate a 20 from a 16 in this project are the last two, and both of them live in the memo, not in the code.

## Stretch goals

For anyone who finishes the core path early or wants a stronger analysis section.

1. **Other groups, other moves** (Section 8, already built). Change `GROUP_COLUMN` and `MOVE`. Try `student_disability_status` on `Counterclaim` and notice how a group of 183 spans changes how much you are willing to say.
2. **Split by essay, not by span.** The notebook splits spans at random and says so: spans from the same essay land on both sides of the split, which slightly overstates performance. Redo the split with `GroupShuffleSplit` on `essay_id` and report how much the numbers move. That is a real methods contribution.
3. **Give the classifier context.** Counterclaim and Rebuttal fail because a span has no essay attached. Add features the bag of words cannot see: the span's relative position in the essay, the type of the preceding span, whether the essay's Position span is for or against. Feature engineering, not modeling, is the fix.
4. **Predict the holistic score instead.** You have `holistic_essay_score` and full text. Fit a regression, then disaggregate the residuals by ELL status, economic status, and disability status. Whose essays does your model systematically under-score?
5. **Measure recall on the effectiveness model by prompt.** The model was trained across four prompts of very different difficulty. Does it do better on the easy one?
6. **Read fifty spans.** Take fifty Counterclaim spans, twenty-five rated Effective and twenty-five Adequate, strip the ratings, and code them yourself against a rubric you write first. Then compare. That is a small reliability study, and it is more publishable than the pipeline.

## Troubleshooting

**The first cell prints a wall of text about the download failing.** That is the friendly error, not a crash. Work the four steps it lists, in order: check that you are online, run the cell again, open `https://github.com/HakeoungLee/edis8100-datasets` in a browser tab, and if you are on a locked-down campus or hospital network, try a different network or run in Colab. Unlike previous weeks, this notebook needs the internet.

**`NameError: name 'essays' is not defined`** (or `spans`, `MY_STOPWORDS`, `X_counts`, `rated`, or similar). A cell above this one has not been run in this session. Cells share memory in order. **Runtime > Restart and run all** fixes it every time.

**A pink or red block of text that does not say `Error`.** That is a warning, not an error. Warnings are normal in scientific Python. Only `Error` and `Traceback` need your attention.

**`ConvergenceWarning` from NMF, LDA, or logistic regression.** The defaults in this notebook do not produce one, but you may see it if you raise the number of topics in Your turn 3. It is harmless: the model has fit, the optimizer simply stopped at the iteration cap. Raise `max_iter` if you want it to go away.

**My numbers differ from my neighbor's.** Check that you both ran every cell in a fresh runtime and that neither of you edited a "Your turn" cell before this point. The data file is fixed and every model is seeded with `RANDOM_STATE = 8100`, so identical input gives identical output.

**The notebook runs but a figure looks empty.** Re-run the cell. If a figure is genuinely blank, the cell that produces its data probably did not run.

**Colab cannot see the repository.** You authorized GitHub without checking the box that includes private repositories. Redo the authorization from **File > Open notebook > GitHub**, and grant access to private repositories this time.

**I edited something and now nothing works.** Every "Your turn" cell has a working default. Compare against the appendix, or open a fresh copy of the notebook from Colab and paste your work back in.

Still stuck? Ask a classmate, then post on Canvas, then email the instructor. Do not spend twenty minutes alone with an error message.

## Documenting your AI use

Per the course AI policy, AI use is **permitted** on this mini project and **must be documented**.

Both pieces go to the Canvas **AI Reflection** submission, in two different places on that page, and students routinely reverse them.

- **The conversation record goes in a Word file, attached to that submission.** Every relevant exchange, across every session and every tool, pasted in full. Not a summary, not a link to a shared conversation, and not pasted into the text box.
- **The reflection goes in the Canvas text box on the same page.** Copy in the four questions from the syllabus and answer each one: how you used it; whether it helped and how; whether it made your work more challenging in any way; and what lesson about AI from this week you would pass on to a friend or the class.
- If you used no AI at all, say so in one line in the text box and attach nothing. A blank submission is not the same as a declaration.
- Undisclosed AI use is an Honor Code violation. Disclosed use is not penalized.

A note specific to this week. Text analysis is unusually easy to have an AI do for you, and unusually easy to get subtly wrong. If a model writes your lexicon, names your topics, or drafts your interpretation of the Section 7 gap, say so, and then do the thing the model cannot do: open the spans, read what the students actually wrote, and check whether the interpretation survives contact with them. That checking is the assignment.

---

*EDIS 8100: Teaching and Learning Analytics, Fall 2026, University of Virginia School of Education and Human Development. Course design by Dr. Hakeoung Hannah Lee.*

*Data: PERSUADE 2.0, a four-prompt subset, licensed CC BY-NC-SA 4.0. Crossley, S. A., Baffour, P., Tian, Y., Franklin, A., Benner, M., & Boser, U. (2024). A large-scaled corpus for assessing text readability and writing quality: The PERSUADE corpus. Assessing Writing, 61, 100849. These are real essays by real students. Attribute the corpus, do not redistribute the text, and do not use it commercially.*
