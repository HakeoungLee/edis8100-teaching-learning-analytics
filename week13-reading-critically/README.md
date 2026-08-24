# Week 13 · Reading Research Critically, and Your Own AI Trace

**Notebook:** `week13_reading_critically_own_trace.ipynb` · about 30 minutes for the core path

The reading hour asks two questions of three published papers: who does this research say the problem is inside, and how much of this paper did anybody check? This notebook asks both of them about the person running it.

## What this lab does

1. **Gets a conversation into a table.** Turns, speakers, words. That is all the structure the rest needs, and noticing how little that is is part of the work.
2. **Computes three descriptive measures.** Turn count, authorship share by words, and the gap before the next message.
3. **Two counts.** A keyword rule sorts your own turns into asking for a fact, for production, for critique, or for reassurance, and prints a one-line label of the kind a paper would use. Then a second count: how many of your turns asked the model to justify something, name a source, or check itself. The first count is the reading hour's framing problem applied to a sample of one. The second is its record problem applied to your own practice.
4. **Argues against the label.** Three things it gets wrong, the evidence that would settle each, and whether that evidence exists anywhere in the trace. Almost none of it does.

Both rules are dials. Change them and both numbers move, which is the second thing worth noticing.

## The data, and why this lab is the exception

Every other lab in this course runs on data somebody else collected and published under a licence. This one does not, and that is deliberate.

**Path 1, your own log.** Students have uploaded their AI interaction logs with every graded submission since Week 4, and they were told in Week 1 that this session was coming. Set `MY_LOG_PATH` to a plain text export. Nobody else opens it, the instructor does not collect it, and the notebook does not record which path was used.

**Path 2, a published transcript.** Leave `MY_LOG_PATH` empty and everything runs on `collab-chat/chat_logs.csv`: 1,374 real messages from eight groups of undergraduates over four days in February 2021, in a computer networks course at Universidad de Valladolid, released **CC BY 4.0** by Cristina Villa-Torrano and colleagues. It reaches every objective except the one in Section 4 that needs the trace to be your own.

Both paths are named at 4:30 as equal options and nobody is asked which they used.

## Three things the published path produces, and all three are the lesson

**The gaps come out as 60 seconds at every quartile.** That file records time to the nearest minute, so every gap it can express is a multiple of 60. The distribution is the clock's rather than the conversation's, and latency is not measurable there at the resolution the question needs.

**The category rule classifies nothing.** It reports 100 percent unclassified, because those students were working in Spanish and the four rules are English keywords. The instrument does not announce that it is out of its depth; it returns zeros while looking exactly as authoritative as before. Somebody reading only the output would conclude these students never asked for anything.

**The verification count comes out at zero.** On a student's own log it often does too. Zero is a fact about how a tool got used, not a character result, and the lesson plan says explicitly not to moralize about it. It is only worth something read next to the first count: a run of production requests with no backing requests is a different picture from a run of fact requests with no backing requests.

None of the three is a bug and none is hidden. All three are in the notebook's own text, before the cells that produce them.

## Readings this lab sits under

- Yang, Y., Yuan, K., Li, X., & van Aalst, J. (2022). Fostering low-achieving students' productive disciplinary engagement through knowledge-building inquiry and reflective assessment. *British Journal of Educational Technology, 53*(6).
- Koretsky, M. D., Vauras, M., Jones, C., Iiskala, T., & Volet, S. (2021). Productive disciplinary engagement in high- and low-outcome student groups. *Research in Science Education, 51*(Suppl 1), S159-S182.
- Kaliisa, R., Misiejuk, K., López-Pernas, S., & Saqr, M. (2025). How does artificial intelligence compare to human feedback? *Educational Psychology*.

The first two share a framing problem: both sort learners before analyzing them, and the question is what that does to the people in the study once it leaves the methods section. The third comes with a task rather than questions. Students audit its reference list against Crossref and Google Scholar, a quarter of the list each, and bring the record rather than a conclusion; the class picture gets built from four independent audits in the room.

All three are published and peer reviewed. None is assigned as a failure.
