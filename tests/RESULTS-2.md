# Gap 3 and gap 4: results (Oct 22, 2026)

Predictions: PREREG-2.md (sha256 ea686084…, written before any call). Deviations are logged at its end.

## Gap 3: does the house look follow the performer or the brief?

7 briefs × 3 performers × 5 pages = 105 new pages, plus 15 Tidepool pages from Test A, giving 120. Cost $0.84.

| brief | median countable habits (of 8) | median visual habits (of 5) |
|---|---|---|
| Tidepool (planner) | 5 | 4 |
| plumber, Leeds | 4 | 4 |
| children's science museum | 2 | 3 |
| open-source database | 2 | 3 |
| poetry press | 3 | 5 |
| sexual-health clinic | 4 | 4 |
| skate shop | 3 | 3 |

How the variance splits:

| habits | performer | brief | performer×brief | run-to-run |
|---|---|---|---|---|
| countable | 16% | 46% | 14% | 24% |
| visual | 7% | 32% | 16% | 44% |

For countable habits, performer share minus brief share is −0.30 (95% CI [−0.47, −0.13]).

- **P3a (median ≥4 in ≥5 of 7 briefs): FAILED.** It held in 3 of 7.
- **P3b (performer explains more than brief): FAILED, reversed.** The brief explains about three times as much.
- **P3c: PARTIAL.** Some habits hold whatever the brief:
  - label above the headline (V3): 73–100% in every brief
  - set-apart word in the headline (V2): 67–100%
  - copy left, visual right (V4): 80–100%

  Others follow the brief:
  - numbered steps: 97% on Tidepool, 7–27% elsewhere
  - serif headline: 0% on the museum, 100% on the poetry press
  - pricing: 0% on the database
- **What this changes:** the earlier single-brief findings overstated how fixed the house look is. The part that holds across briefs is a *layout skeleton* (label, headline with one set-apart word, copy left and visual right), not a typeface or a palette. Constraints aimed at the house look should target that skeleton.

## Gap 4: measure the house look visually, against your blind labels

- **Rendered-DOM checker** (rendered.js, V1–V5): it reads the real computed styles at 1280×800. Controls: pos 5/5, neg 0/5, dark 0/5.
- **Second instrument:** gemini-3.8-flash looking at the same screenshots, with the same wording you see. Controls: pos 5/5, neg 0/5, dark 0/5.

Agreement between the two instruments (κ, bootstrap 95% CI, n = 20):

| habit | κ | 95% CI | raw agreement |
|---|---|---|---|
| V1 serif headline | 1.00 | [1.00, 1.00] | 20/20 |
| V2 set-apart word | 0.61 | [−0.07, 1.00] | 18/20 |
| V3 label above headline | 1.00 | [1.00, 1.00] | 20/20 |
| V4 copy left, visual right | 1.00 | [1.00, 1.00] | 20/20 |
| V5 warm off-white background | 0.78 | [0.43, 1.00] | 17/20 |

- This is far above the 0.00–0.27 between the countable checker and the text judge earlier. It is **not validity**: both instruments use one set of definitions, and they may share its blind spots.
- **P4a and P4b wait on your labels** (blind labelling page: https://claude.ai/artifact/3A5NY8wCZ7ubnip5ppzNiZ). Scoring: `python3 score4.py <dir>`.
- **Expect the human κ to be lower.** The research expects κ around 0.3–0.4 on looser UI judgements (UICrit, UIClip). There is no published κ for named style habits.
- **Not done (superseded below for embeddings):**
  - ~~Image embeddings: "no torch and no GPU"~~. Wrong: CPU torch installed in 1 minute and embedding 120 pages takes 28 s. See the addendum.
  - A typicality score against a human-made reference corpus: no corpus has been picked yet.

## Addendum: image embeddings (Oct 22, same session)

All 120 first screens (1280×800 PNG) were embedded with two image models on CPU in 28 s. No API calls, $0.
- **DINOv2-small:** full frame at 224×350. The default preprocessing center-crops to a square, which would cut off the left and right edges where "copy left, visual right" lives. Caught before reading any result.
- **OpenCLIP ViT-B/32 (laion2b):** full frame squashed to 224×224.

Variance split computed from pairwise distances (PERMANOVA-style), with 999 permutations and a 1000× bootstrap:

| instrument | performer | brief | performer×brief | run-to-run | performer − brief, 95% CI |
|---|---|---|---|---|---|
| countable habits (code) | 16% | 46% | 14% | 24% | [−0.47, −0.13] |
| visual habits (rendered checker) | 7% | 32% | 16% | 44% | — |
| DINOv2 | 8% | 36% | 16% | 40% | [−0.34, −0.24] |
| OpenCLIP | 5% | 33% | 14% | 48% | [−0.33, −0.27] |

- **Control (two arms that must differ):** with brief labels shuffled, the brief share drops to 5% (median of 999 permutations; p < 0.001 for brief and for performer).
- **Brief > performer replicates on four instruments**, two of which read pixels and know nothing about the habit list.
- **The performer is small in share but easy to recognise.** A page's nearest neighbour comes from the same performer 83% (DINO) or 90% (CLIP) of the time, against 33% by chance. Within each brief, a performer's pages are closer to each other than to other performers' pages: within/between ratio 0.72–0.88 (DINO), 0.75–0.95 (CLIP). Performers leave a fingerprint, but the brief sets most of the look.
- **Embeddings see more than the habit list.** Mantel r between embedding distance and 13-habit distance is 0.21 (DINO) and 0.31 (CLIP). The habit list captures a minority of what makes two pages look alike.
- **Novelty vs typicality still collapses: r = −0.88 (DINO), −0.87 (CLIP), the same as TF-IDF (−0.87).** So the fault is the definition, not the instrument. Measured within one set of pages, "near the centroid" and "near your neighbours" are almost the same fact in any space. Typicality needs an external reference: real human sites for the same kind of business. Novelty should stay measured against the round.

## Gap 4 scored against your blind labels (Oct 22, 01:3x UTC)

20 pages, one rater (you), no "unsure" used. Cohen's κ with bootstrap 95% CI:

| habit | you vs rendered checker | you vs Gemini | raw agreement (checker) |
|---|---|---|---|
| V1 serif headline | **0.90** [0.69, 1.00] | 0.90 | 19/20 |
| V2 set-apart word | 0.32 [−0.14, 1.00] | 0.32 | 17/20 |
| V3 label above headline | **1.00** [1.00, 1.00] | 1.00 | 20/20 |
| V4 copy left, visual right | **0.64** [0.00, 1.00] | 0.64 | 19/20 |
| V5 warm off-white background | 0.55 [0.12, 0.89] | 0.54 | 16/20 |

- **P4a (checker κ ≥ 0.6 on ≥4 of 5): FAILED, 3 of 5.**
- **P4b (checker beats Gemini on ≥3 of 5): FAILED, 1 of 5.** The two instruments tie on 4 habits and differ by 0.01 on the fifth. Against your eye they are interchangeable.
- **Usable as automated measures:** serif headline and label above the headline. Copy-left/visual-right qualifies with a caveat: only 1 disagreement in 20, but the CI reaches 0 because "no" is rare.
- **Not usable yet:** set-apart word and warm background.
  - Set-apart word: 3 disagreements, in both directions.
  - Warm background: you said yes on 4 pages where the checker said no. On 3 of them the dominant pixel colour is neutral white, so a whole-screen colour fix changed nothing (still κ 0.55; exploratory, on these same 20 pages). On p10 the background is dark teal, which the definition excludes. So either your "warm" means something the definition doesn't say (warm accents? overall feel?) or p10 was a slip. That's a definition question, not a checker bug.
- **Caveats:** one rater and n = 20, so the intervals are wide. No re-test of your own consistency.
