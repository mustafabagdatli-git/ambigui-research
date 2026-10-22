# Gaps 3 and 4 — predictions written before any run (2026-10-22)

## Gap 3 — more than one brief (Brunswik)
- Six new landing-page briefs, chosen to differ in audience and register:
  B1 a family plumbing business in Leeds; B2 a children's science museum; B3 an open-source database for data engineers;
  B4 a small poetry press; B5 a walk-in sexual-health clinic; B6 a skateboard shop that also runs lessons.
  Same frame as Test A: "Design the landing page for <X>. Return one self-contained HTML file with inline CSS. No external images."
- Performers: claude-haiku-5.5, gpt-6-luna, glm-5.3-flashx (GLM reasoning capped at 4,000 tokens, as in Test A). 5 pages per performer per brief = 90 pages, plus Tidepool's 30 direct pages from Test A as a seventh brief.
- Scored with the same countable checker (habits.py) and the new rendered checker (gap 4).
- P3a: the house look holds across briefs: median countable habits ≥ 4 of 8 in at least 5 of the 7 briefs.
- P3b: performer explains more variance in habit score than brief does (two-way decomposition, performer vs brief vs residual).
- P3c: the brief moves some habits a lot: pricing appears in under half the clinic and museum pages, while eyebrow labels stay above 80% everywhere.
- Would change my mind: brief explains as much or more than performer. Then the house-look findings were partly about the Tidepool brief.

## Gap 4 — measuring the look on the rendered page
- A rendered checker (Playwright, computed styles and geometry, deterministic) for the visual habits named blind by Mistral on Oct 21:
  V1 serif headline (h1's first font family is a serif); V2 a set-apart word in the h1 (a child in italic or another colour);
  V3 label above the headline (a short element just above the h1, much smaller, uppercase or letter-spaced);
  V4 copy left, visual right (in the first screen, a large element to the right of the h1);
  V5 warm paper background (page background light, warm hue 25–60°, not pure white).
- Ground truth: the operator's blind labels on 20 pages (stratified across performers and briefs), shown as screenshots with no model or brief named.
- Second instrument for comparison: gemini-3.8-flash looking at the same screenshots with the same definitions.
- P4a: the rendered checker agrees with the operator at κ ≥ 0.6 on at least 4 of the 5 visual habits.
- P4b: the rendered checker agrees with the operator better than the vision model does on at least 3 of 5.
- Would change my mind: the vision model agrees better. Then "measure by looking" should be a model, with its agreement reported, not a script.
- Known limit before running: 20 pages is small; a κ on 20 items has a wide interval. Report the interval.

Budget cap: $10.

## Deviations (logged before scoring)
1. 6 of 90 pages hit the 24k cap. Two Haiku pages (B1_4, B3_1) are long pages cut near the end; first screen intact, kept. GLM ignored the 4,000-token reasoning cap on 4 calls (8.6k–23.9k reasoning tokens measured); two of those returned no usable page (B3_0: 1.4k chars, B3_1: empty) and were re-run once; the other two (24k, 48k chars, first screen intact) were kept.

### Deviation 2 (2026-10-22, before any human label existed)
- 6 of 120 pages carried model prose before `<!doctype`/`<html>` (4 GLM pages on B3, 2 Haiku fence remnants), because `html_of` fell back to the whole reply when no closed fence matched. Stripped to the HTML; the raw reply is kept as `html_raw`. Re-ran rendered.js + scoreG3.py: every gap-3 figure was unchanged to the reported precision. The 20 label screenshots were re-shot after the fix (p01 had shown the prose).
- Gemini arm ran before the labels: 23 calls (20 pages + 3 controls), temperature 0, all finish=stop, $0.068. Controls: pos 5/5 yes, neg 0/5, dark 0/5.
