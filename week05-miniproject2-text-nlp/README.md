# 💬 Week 5: Mini Project 2, What Are Students Actually Saying?

A forum text pipeline built one honest step at a time, ending in a disagreement you have to settle yourself.

## At a glance

| | |
|---|---|
| **Session** | Wednesday, September 23, 2026, 3:30 to 6:00 PM, Ridley 137 |
| **Topic** | Text-Based Analytics and Natural Language Processing |
| **Guest speaker** | Jiayi (Joyce) Zhang, University of Pennsylvania |
| **In-class time on this notebook** | About 20 minutes, launched in the hands-on studio block (4:40 to 5:00). This is a launch, not the whole project. Plan on roughly 60 more minutes for the notebook and additional time for the memo. |
| **Deliverable** | Mini Project 2: the executed notebook, a 300-word interpretation memo, and your AI interaction log |
| **Due date** | This week, via Canvas, by the deadline posted on the Canvas assignment page |
| **Notebook** | `week05_miniproject2_text_analytics.ipynb` |
| **Data used** | `forum_posts.csv`, `students.csv`, `gradebook.csv` (all synthetic, built by the notebook itself) |
| **Libraries** | pandas, numpy, matplotlib, scikit-learn. No installs, no downloads, no network. |

## Objectives

By the end of this activity you will be able to:

1. **Build** a text analysis pipeline on discussion prose: clean, tokenize, count, and state out loud what each cleaning decision deleted from the record.
2. **Score** sentiment with a lexicon small enough to read in full, then diagnose where that lexicon is measuring the topic rather than the writer's stance.
3. **Fit and compare** two topic models (NMF and LDA) on the same corpus, and interpret their topics against what the course actually discussed, without pretending the models handed you labels.
4. **Tag** discourse moves (question, agreement, counterpoint, evidence citing, connecting) with transparent rules, audit the rules against the posts by hand, and report how often they are wrong.
5. **Adjudicate** a genuine disagreement between methods and defend the reading you chose, in writing, to an audience that can check your work.

The through-line of the session: the pipeline is the easy part. Three methods will give you three different answers about the same 1,456 posts, and the deliverable is not the pipeline. It is the defended reading.

## What is in this folder

| File | What it is |
|---|---|
| `week05_miniproject2_text_analytics.ipynb` | The notebook. Self-contained: it builds its own data, needs no downloads, and runs top to bottom untouched. |
| `README.md` | This file. |
| `data/` | Created for you the first time you run the notebook. Not stored in the repo. |

You do not need to clone anything or download a CSV. The first code cell writes the three datasets into the runtime, in under a second, with numpy seed 8100, so your numbers match your classmates' numbers exactly.

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

You can also run the notebook locally with Jupyter. It needs pandas, numpy, matplotlib, and scikit-learn, all of which ship with Anaconda.

## Step-by-step walkthrough

Run every cell in order. The whole notebook executes in well under a minute.

**⚙️ Setup.** One long cell builds `students.csv`, `forum_posts.csv`, and `gradebook.csv` into `./data/`. You do not need to read it. Run it, collapse it, move on. The data are synthetic on purpose: learning analytics is usually practiced on records belonging to people who never got asked, and a course assignment is a poor reason to read a real student's discussion posts.

**📊 Section 1: Meet the corpus.** 1,456 posts, 8 weeks, one discussion topic per week. Note the number that will haunt the rest of the notebook: 18 of the 120 students never posted at all.

**📊 Section 2: Cleaning, and a receipt for what you deleted.** Watch one post pass through lowercasing, punctuation stripping, tokenizing, and stopword removal. Then read the receipt: 56 percent of the corpus is gone, along with all 804 question marks, and scikit-learn's default English stopword list has quietly removed `not`, `no`, `never`, `but`, and `however`. A sentence that was an objection comes out the other side looking like agreement.

**✏️ Your turn 1.** Decide which corpus-specific words belong on your stopword list, and see what your choice does to the top of the frequency table.

**📊 Section 3: Word frequencies with CountVectorizer.** Build the document-term matrix, plot the top 15 words, then move to a real comparison: which words are unusually common in one week relative to the whole forum. Try naming each week's topic from its distinctive words before you look at the answer column.

**📊 Section 4: Sentiment from a lexicon you can read.** The entire lexicon (32 positive words, 34 negative words) is printed in the notebook. Score every post, plot the weekly averages, and then read the five most negative posts in full. Two of them describe strategies that worked. One is a neutral summary of sleep research that scores near the bottom of the corpus because the words for its topic are `debt` and `lapses`.

**✏️ Your turn 2.** Remove the topic vocabulary from the lexicon and rescore. Week 8 moves from the most negative week in the forum to a positive one, on the strength of a single editorial decision about a word list.

**📊 Section 5: Topic modeling, NMF and LDA side by side.** Fit both at 8 topics, print the word lists next to each other, and check both against the weeks the posts were actually written in. NMF recovers the calendar almost exactly (adjusted Rand index 0.999). LDA leaks: 67 posts land in a topic dominated by a different week, and 32 of those come from week 1 alone. Then read two of the leaked posts and decide whether LDA was wrong or whether it noticed something the calendar hides.

**✏️ Your turn 3.** Ask a topic model for 4 topics, then 12. It will always give you exactly the number you asked for and will never tell you the number was wrong.

**📊 Section 6: Discourse moves from rules you can argue with.** Five regular-expression rules, tagged on the raw text (this is why Section 2 kept it). Then the part most pipelines skip: audit the weakest rule by hand, on the posts where the bare word `but` was the only thing that fired.

**✏️ Your turn 4.** Hand-code six posts, compute the precision of the rule, correct the headline number, and add a discourse move of your own.

**📊 Section 7: Where the methods disagree.** All three readings in one table, plus the figure the whole mini project builds toward: mean sentiment against pushback, per topic. The relationship is real (r = -0.74) and two topics refuse to sit on the line. The test anxiety topic is the most negative in the forum and no more argumentative than average. The memory topic is positive and among the most argumentative. Decide which measure you believe, and get ready to defend it.

**📊 Section 8 (stretch): Two weeks compared.** Same forum, different topic, different point in the semester. One gap is large. The rest are noise, and saying so is part of the exercise.

**💬 Reflection and the interpretation memo.** Four reading-linked questions and the memo template. This is the graded thinking.

**✅ Submission checklist.** Three items, all required.

**Appendix.** Notes on every "Your turn," written as reasoning rather than answer keys, because in each case more than one answer is defensible.

## Rubric: Mini Project 2 (100 points)

Each criterion is scored at one of four levels.

| Criterion | Integrated and Insightful (20) | Solid and Complete (16) | Developing (12) | Emerging (8) |
|---|---|---|---|---|
| **End-to-End Analytics Workflow** | The full pipeline runs cleanly and every stage is motivated: you can say why each step exists and what it makes possible downstream. | All stages completed and the notebook runs top to bottom. Motivation is present but thin in places. | Most stages completed, with gaps or a step that runs without a stated purpose. | Pipeline incomplete or does not execute. |
| **Data Preparation and Technical Care** | Cleaning decisions are deliberate, documented, and audited: you show what was deleted and where it would have mattered. Raw and cleaned text are used appropriately per analysis. | Cleaning is competent and mostly documented. Minor unexamined defaults remain. | Cleaning applied with defaults accepted uncritically. Some analyses run on the wrong version of the text. | Little evidence of preparation care; results depend on choices never named. |
| **Analysis and Visualization Choices** | Method choices are justified against alternatives. Figures are titled, labeled, readable, and chosen to reveal the claim rather than decorate it. | Appropriate methods and clear figures. Justification present but brief. | Methods applied without comparison; figures present but hard to read or unlabeled. | Methods or figures missing, mislabeled, or misleading. |
| **Interpretation and Educational Meaning** | The memo takes a position on the specific method disagreement, cites posts by id, states what the rejected reading would have concluded, and connects the result to something a course could act on. | A clear interpretation supported by evidence from the notebook. The disagreement is named but not fully adjudicated. | Interpretation restates the numbers without deciding anything. | Interpretation absent, or contradicted by the output. |
| **Critical Reflection: Limits, Ethics, Equity** | Names who is missing and what that does to the claim, sizes at least one limitation rather than only listing it, and says what you would refuse to report and to whom. | Limits and ethical considerations addressed substantively. | Limitations mentioned generically ("this is only synthetic data"). | Limitations, ethics, or equity not addressed. |

The two criteria that separate a 20 from a 16 in this project are the last two, and both of them live in the memo, not in the code.

## Stretch goals

For anyone who finishes the core path early or wants a stronger analysis section.

1. **Compare two weeks' discourse** (Section 8, already built). Change `WEEK_A` and `WEEK_B`. Weeks 1 and 8 are the semester's bookends; weeks 2 and 4 both score low on sentiment for what turn out to be different reasons.
2. **Measure recall, not just precision.** Section 6 audits posts the rule flagged. Hand-code 30 posts the rule did *not* flag and find the counterpoints it missed. Recall is almost always the more damaging number and almost never the reported one.
3. **Model at the thread level.** `forum_posts.csv` has `thread_id` and `parent_post_id`. Concatenate each thread into one document and re-run the topic model. Do threads have topics that individual posts do not?
4. **Test the "silence is data" problem.** Join `students.csv` and find who never posted. Does the group that posts differ from the roster on any observable characteristic? Whatever you find, write down what you would need in order to say anything responsible about it.
5. **Sentiment against outcomes.** `gradebook.csv` is in your `data/` folder. Does a student's mean post sentiment relate to their mean quiz score? Before you compute it, write down what you would conclude from a positive result, a null result, and a negative result. Then compute it and notice whether you changed the story.
6. **Build a better lexicon.** Take 60 posts, hand-code each as positive, negative, or neutral in stance, and check both lexicon versions against your codes. That is a small validation study, and it is more publishable than the pipeline.

## Troubleshooting

**`FileNotFoundError: data/forum_posts.csv`.** You skipped the setup cell, or the runtime restarted and emptied its temporary storage. Scroll up, run the setup cell, and continue. If in doubt: **Runtime > Restart and run all**.

**`NameError: name 'posts' is not defined`** (or `MY_STOPWORDS`, `X_counts`, `only_but`, or similar). A cell above this one has not been run in this session. Cells share memory in order. **Runtime > Restart and run all** fixes it every time.

**A pink or red block of text that does not say `Error`.** That is a warning, not an error. Warnings are normal in scientific Python. Only `Error` and `Traceback` need your attention.

**`ConvergenceWarning` from NMF or LDA.** The defaults in this notebook do not produce one, but you may see it if you raise the number of topics in Your turn 3. It is harmless: the model has fit, the optimizer simply stopped at the iteration cap. Raise `max_iter` if you want it to go away.

**My numbers differ from my neighbor's.** Check that you both ran the setup cell in a fresh runtime, and that neither of you edited a "Your turn" cell before this point. Everything in the notebook is seeded, so identical input gives identical output.

**The notebook runs but a figure looks empty.** Re-run the cell. If a figure is genuinely blank, the cell that produces its data probably did not run.

**Colab cannot see the repository.** You authorized GitHub without checking the box that includes private repositories. Redo the authorization from **File > Open notebook > GitHub**, and grant access to private repositories this time.

**I edited something and now nothing works.** Every "Your turn" cell has a working default. Compare against the appendix, or open a fresh copy of the notebook from Colab and paste your work back in.

Still stuck? Ask a classmate, then post on Canvas, then email the instructor. Do not spend twenty minutes alone with an error message.

## Documenting your AI use

Per the course AI policy, AI use is **permitted** on this mini project and **must be documented**.

- Upload your complete AI interaction log (prompts and responses, or a full export) to the **AI Interactions** submission on Canvas, alongside the notebook.
- Include a short reflection: what you asked, what you accepted, what you rejected and why, and what you verified independently.
- If you used no AI at all, submit a one-line statement saying so. A blank submission is not the same as a declaration.
- Undisclosed AI use is an Honor Code violation. Disclosed use is not penalized.

A note specific to this week. Text analysis is unusually easy to have an AI do for you, and unusually easy to get subtly wrong. If a model writes your sentiment lexicon or names your topics, say so, and then do the thing the model cannot do: read the posts and check whether the labels survive contact with them. That checking is the assignment.

---

*EDIS 8100: Teaching and Learning Analytics, Fall 2026, University of Virginia School of Education and Human Development. Course design and data universe by Dr. Hakeoung Hannah Lee. All data are synthetic.*
