# November 18 · The Category and the Log

**Notebook:** `week12b_your_own_trace.ipynb` · about 30 minutes for the core path

At 3:40 the session takes apart three published papers by asking one question of each: where did the category come from, and what is it holding up? This notebook turns the same instrument around and points it at the person running it.

## What this lab does

1. **Gets a conversation into a table.** Turns, speakers, words. That is all the structure the rest of it needs, and noticing how little that is is part of the work.
2. **Computes three descriptive measures.** Turn count, authorship share by words, and the gap before the next message.
3. **Builds a category.** Four keyword rules sort your own turns into asking for a fact, for production, for critique, or for reassurance, and the notebook prints a one-line label of the kind a paper would use. The rules are a dial; change them and the label moves.
4. **Argues against it.** Three things the label gets wrong, the evidence that would settle each, and whether that evidence exists anywhere in the trace. Almost none of it does.

## The data, and why this lab is the exception

Every other lab in this course runs on data somebody else collected and published under a licence. This one does not, and that is deliberate.

**Path 1, your own log.** Students have uploaded their AI interaction logs with every graded submission since Week 4, and they were told in Week 1 that this session was coming. Set `MY_LOG_PATH` to a plain text export. Nobody else opens it, the instructor does not collect it, and the notebook does not record which path was used.

**Path 2, a published transcript.** Leave `MY_LOG_PATH` empty and everything runs on `collab-chat/chat_logs.csv`: 1,374 real messages from eight groups of undergraduates over four days in February 2021, in a computer networks course at Universidad de Valladolid, released **CC BY 4.0** by Cristina Villa-Torrano and colleagues. It reaches every objective except the one in Section 4 that needs the trace to be your own.

Both paths are named at 4:30 as equal options and nobody is asked which they used.

## Two things the published path produces, and both are the lesson

**The gaps come out as 60 seconds, at every quartile.** That file records time to the nearest minute, so every gap it can express is a multiple of 60. The distribution is the clock's rather than the conversation's, and latency is simply not measurable there at the resolution the question needs.

**The category rule classifies nothing.** It reports 100 percent unclassified, because those students were working in Spanish and the four rules are English keywords. The instrument does not announce that it is out of its depth; it returns zeros while looking exactly as authoritative as before. Somebody reading only the output would conclude these students never asked for anything.

Neither is a bug and neither is hidden. They are in the notebook's own text, before the cell that produces them.

## Readings this lab sits under

- Yang, Y., Yuan, K., Li, X., & van Aalst, J. (2022). Fostering low-achieving students' productive disciplinary engagement through knowledge-building inquiry and reflective assessment. *British Journal of Educational Technology, 53*(6).
- Koretsky, M. D., Vauras, M., Jones, C., Iiskala, T., & Volet, S. (2021). Productive disciplinary engagement in high- and low-outcome student groups. *Research in Science Education, 51*(Suppl 1), S159-S182.
- Kaliisa, R., Misiejuk, K., López-Pernas, S., & Saqr, M. (2025). How does artificial intelligence compare to human feedback? *Educational Psychology*.

None of the three is assigned as a bad paper. All three are published, peer reviewed, and doing an ordinary thing clearly enough that the thing is visible.
