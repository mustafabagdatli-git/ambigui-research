# Accepted moves — spec (Oct 21, 2026)

Accepted by you on Oct 21: suggestions 1–9 from "Gaps, open items and suggestions", except the stranger round. This spec covers the moves that are rules rather than tests (1, 2, 4, 6, 8). Tests (3) are running separately; 5 and 9 are blocked here (see the end).

Status of everything below: **written, not built.** The Sketchbook, boards and swarm live in ~/roster, which this session can't reach.

---

## Move 1 — Line states get operational rules

Every score line carries exactly one state. Each state now has required fields and one check.

| State | Required fields | Check the loop runs | Source |
|---|---|---|---|
| **Fixed** | value · *purpose* (one clause: what this line is for) · set by (you / brief / Library / rule) | A performer output that breaks it is a defect, unless the line's purpose is not served by it — then flag the line, not the performer. | Fuller (purpose decides the rule); Lawson (who set it) |
| **Band** | low · high · unit or description of the range · set by | Each output is inside or outside. **Stack check:** for lines that act on the same region (e.g. type size, spacing and line length in the hero), test them together on the rendered page; a page can pass every band and fail the stack. | GD&T tolerance stack-up |
| **Open** | the question · *good if…* clause (already built, v38) · **trigger**: the event that would lose an option if it stays open (e.g. "before components are picked", "before round 3") | When the trigger is reached, the line must move to band, fixed, or a dated "stays open because…". An open line past its trigger without that note is flagged. | Poppendieck, last responsible moment |
| **Default** | the default value · origin (Library pick, model habit, house style) | **Penalty default:** where the default is a known house habit, set it to something nobody would want, so a performer that keeps it has to say so. Every kept default shows up as a named question in STATE.md "Waiting on you". | Ayres & Gertner |
| **Refused** | what is refused · **what replaces it** · date | A refusal without a replacement is not accepted (see move 4). | Stokes; Rainer/Dogme as counter-examples |

**Moving between states**
- The normal path across rounds is **open → band → fixed** (set-based narrowing). A round may narrow lines; it doesn't commit early to a point.
- **Unfixing is a recorded move**, never a silent edit: a STATE.md line saying which line, the old state, the new state, and why (Nomic).
- A performer surprise that you keep becomes an open line with a *good if…* clause, not an exception.

**Where it lives:** states on score lines in the Sketchbook (decided Oct 21: boards set values only). Boards don't change.

---

## Move 2 — Score novelty and typicality as two numbers

Replace the single "house habits, fewer is better" score with two numbers per page:

- **Typicality** — how close the page is to the common pattern for this brief: the share of countable house habits present, plus similarity to the centroid of all pages for this brief.
- **Novelty** — how far the page is from the other pages in its round and from the Library: mean distance to its nearest neighbours.

Read them together, never as one total. The target is the region Hekkert et al. found people like: **novel while still typical**. Both low means plain. High typicality with low novelty is the house look. High novelty with low typicality is off-brief.

Consequence: the plain "all-three" arm (median 1 habit, 17/17 white pages) stops scoring as a win. It scores low typicality *and* low novelty.

Open (needs a decision later): the distance measure. The tests running now use TF-IDF over visible text plus section order. An image-based measure would be better for visual habits, which is where the two checkers disagreed (κ 0.00–0.27).

---

## Move 4 — Constraints come in pairs, with a date

- Every ban names its replacement: "no X — instead Y", with Y specific (Stokes: preclude the reliable move, promote a named substitute).
- Every ban and replacement carries the **date it was written** and a **review date** (default: 30 days). A banned look's replacement spreads and becomes the next default (Simmel).
- Pure refusal lists are retired. Dogme 95, Rainer's No Manifesto and the plain arm all show that refusals alone make a new uniform.
- The "named defaults" list (namedef: naming alone left the median at 4 of 8) becomes a list of pairs.

---

## Move 6 — Critique is cross-family, blind, and advisory

- **Cross-family:** no judge rates work from its own model family (Panickssery et al.: self-recognition goes with self-preference).
- **No single shared judge:** use at least two families per verdict (Kleinberg & Raghavan: one shared, more accurate judge can lower overall decision quality).
- **Blind and locked:** authors hidden, order shuffled, first reaction locked before the outcome is shown (already adopted for the swarm).
- **Advisory (Braintrust):** critic output is labelled *notes*. Critics propose; the owner decides. No critic output lands as a change.
- **Order (Lerman):** meaning first, then the performer's questions, then neutral questions, then opinions.

---

## Move 8 — Attention budget per round

- **Default: 10 minutes of your attention per round.** This is a placeholder. Give me your number and it becomes fixed.
- Every check shows its estimated cost (already on the map). A new check that would push the round over budget must name the check it replaces.
- With every costed check adopted, the map's own estimate is 10–16 minutes, so at 10 minutes at least one existing check has to go.

---

## Blocked here

- **Move 5 (G-study of the 60 swarm sessions):** the session data is in ~/roster/ux-swarm, which isn't in this container. The analysis is about 40 lines of script once the data is available.
- **Move 9 (copy round-3 files to ~/roster):** same reason. Files to copy are in this session's scratchpad: r3/, round3-full-list.md, gaps-and-open-items.md, accepted-moves-spec.md, tests/.
- **Base-model arm of move 3:** none of OpenRouter's 469 models is a base (pretrained, non-aligned) model. It needs a provider that serves one.
