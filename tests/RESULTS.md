# Accepted-move tests — results (Oct 21, 2026)

Predictions: PREREG.md (sha256 8b87f89c…, written before any call). Deviations are logged at its end. 862 calls, **$2.47** in total (cap $15). Model-only, one brief ("Tidepool"), three cheap performers (claude-haiku-5.5, gpt-6-luna, glm-5.3-flashx). The habit checker is new, written this session; its numbers are not comparable to the Oct 20/21 medians.

## Test A — Verbalized Sampling (60 pages)

| model | arm | median habits (0–8) | mean | mean pairwise text similarity |
|---|---|---|---|---|
| claude-haiku-5.5 | direct | 6 | 6.30 | 0.246 |
| claude-haiku-5.5 | VS | 6 | 5.70 | 0.147 |
| glm-5.3-flashx | direct | 5 | 4.80 | 0.106 |
| glm-5.3-flashx | VS | 4.5 | 4.40 | 0.075 |
| gpt-6-luna | direct | 4 | 4.20 | 0.194 |
| gpt-6-luna | VS | 4 | 3.60 | 0.169 |
| **pooled** | direct → VS | **5 → 4** | 5.10 → 4.57 | |

- **A1 (median down ≥1, pooled and in ≥2 of 3 models): FAILED as stated.** The pooled median fell 5 → 4, but per model it fell by 0, 0.5 and 0. Means fell 0.4–0.6 in all three models.
- **A2 (pages less alike in ≥2 of 3 models): HELD in 3 of 3** (0.246→0.147, 0.106→0.075, 0.194→0.169). No interval computed: n = 10 per cell, so treat this as a direction.
- **Where the movement was:** serif headline 24/30 → 16/30, FAQ 11 → 7. The near-universal habits didn't move: eyebrow label 28 → 29, emphasised word in the h1 30 → 29, numbered steps 29 → 27.
- **The finding I didn't predict:** in 27 of 30 VS lists, the model's *own top direction* is "warm editorial / serif / paper", with on average 42% of its stated probability. The models know their mode. Sampling from their stated distribution builds it less often (18 of 30 picks) than direct prompting does (serif 24/30).
- Checker validity: controls behave (a bare h1 scores 0; an `<em>` in the h1 scores emphasis), and a hand look at 8 pages confirmed `class="eyebrow"` labels and `<em>` words in the h1s.

## Test B — Library example timing (120 plans)

| arm | planted features copied (0–4) | 95% CI | flawed 45-word headline copied | house habits in plan |
|---|---|---|---|---|
| none | 0.13 | [0.03, 0.27] | 0/30 | 5.50 |
| early | 1.53 | [0.93, 2.17] | 5/30 | 4.27 |
| late | 1.97 | [1.43, 2.47] | 3/30 | 4.50 |
| repeated | 1.57 | [1.00, 2.13] | 9/30 | 4.27 |

- **B1 (every example arm copies more than none; late ≥ early): HELD.** Late's lead over early is inside the intervals.
- **B2 (early/repeated add uncommon features, late doesn't): NOT READABLE.** The feature clustering failed as an instrument: 1,435 phrases ended in 970 labels, so about 11 of 15 features per plan count as "uncommon" in every arm (10.7–11.6, overlapping intervals). This is a measurement failure, not evidence of no effect.
- **B3 (flaw copied < 0.15 per plan in every arm): FAILED.** Early 0.17, repeated 0.30, late 0.10.
- **Models differ by an order of magnitude.** Planted features copied, early arm: GLM 3.5, Haiku 1.1, Luna 0.0. Late: GLM 3.0, Haiku 2.6, Luna 0.3. One averaged number hides this.
- **Against Oct 20's libex** (0.30 planted features per plan): this test shows 1.5–2. The setups differ (here: "a page from our Library", a revise step, four strong features), so this doesn't overturn libex, but it does say the copying rate depends heavily on how the example is framed.
- Side effect: seeing any example cut house habits in the plan (5.5 → 4.3).

## Test C — one page vs three (144 judgments)

| judge | condition | rating (1–10) | problems listed | rejected |
|---|---|---|---|---|
| claude-haiku-5.5 | single | 4.38 | 15.2 | 0/24 |
| claude-haiku-5.5 | trio | 6.42 | 7.0 | 3/24 |
| gemini-3.8-flash | single | 4.88 | 6.9 | 4/24 |
| gemini-3.8-flash | trio | 5.67 | 4.2 | 8/24 |
| gpt-6-luna | single | 6.17 | 6.3 | 0/24 |
| gpt-6-luna | trio | 6.50 | 3.6 | 4/24 |

Paired single − trio rating: **−1.06, 95% CI [−1.53, −0.60]** (36 target×judge pairs). Haiku −2.04 [−2.75, −1.25]; Gemini −0.79 [−1.54, −0.08]; Luna −0.33 [−0.88, 0.25].

- **C1 (single rated ≥0.5 higher): FAILED, and reversed.** Model judges rate a lone page *lower*, the opposite of Tohidi's people. Clear in Haiku and Gemini; Luna's interval crosses zero.
- **C2: split.** Rejections were rarer when the page was alone (4/72 vs 15/72), matching Tohidi. More problems were listed when alone, but that count is confounded: a judge rating three pages divides one answer between them.
- **Reading:** a model judge given one page behaves like a critic hunting for faults, and given three like a chooser. Both a lone page and a set of three give a biased number. For the swarm, show alternatives when the question is *which design*, and don't compare ratings across the two setups.

## What this changes

1. **VS is a cheap knob with a small, real effect on sameness, not a fix.** Keep it as a performer option. The stronger signal is that models can *name* their house direction: ask for the list, then refuse the top item (a paired constraint, move 4).
2. **Library examples: framing and model matter more than timing.** Show examples only through a model that argues with them (Luna here), or mark their features as "not to copy". Measure copying per model, never pooled.
3. **Swarm ratings: never compare a single-page score with a multi-page score.** Pick one setup per question. The one place model judges matched people was rejections.

## Not done
- **Base-model arm:** no base model on OpenRouter.
- **G-study and copying files to ~/roster:** not reachable from here.
- **Stranger round:** excluded by you.
- **Uncommon-features measure:** needs a better instrument, either a fixed feature taxonomy written before the run or image embeddings.
