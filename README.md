# Ambigui research (Oct 21–22, 2026)

Tests and reading behind the Ambigui score loop. Model-only unless a file says otherwise. Every test wrote its predictions first (sha256 recorded) and logged deviations.

Live pages (private claude.ai artifacts):
- Research Relationship Map: https://claude.ai/artifact/FZiTPybP8DerPuAwBxi5MC (copy in `artifacts/research-map.html`)
- Score Sketchbook v39, with line states: https://claude.ai/artifact/RX2ARngg2vy8FwWhxyQ5jE (copy in `artifacts/score-sketchbook-v39.html`)
- Blind labelling page: https://claude.ai/artifact/3A5NY8wCZ7ubnip5ppzNiZ (source in `artifacts/labelling/`)

## Read first
| file | what |
|---|---|
| `tests/RESULTS.md` | Accepted-move tests A/B/C: Verbalized Sampling, Library example timing, one page vs three |
| `tests/RESULTS-2.md` | Gap 3 (seven briefs: the brief moves the look ~3× the performer), gap 4 (visual checker vs your blind labels), image embeddings |
| `tests/PREREG.md`, `tests/PREREG-2.md` | Predictions written before any call, plus deviations |
| `accepted-moves-spec.md` | Line states, novelty + typicality, paired dated constraints, critique rules, attention budget |
| `gaps-and-open-items.md`, `round3-full-list.md` | Open items; the 123 round-3 works, fact-checked |
| `r3/` | Round-3 lane outputs and verification JSONs |

## Reproduce
Needs `OPENROUTER_API_KEY` for anything that calls a model, Node 22 + Playwright (Chromium), Python 3 with numpy/Pillow; embeddings also need `torch torchvision transformers open_clip_torch` (CPU is enough).
```bash
cd tests
python3 testG3.py                         # 105 pages, ~$0.80
node rendered.js G3all G3_rendered.json   # visual habits V1–V5 from computed styles
python3 scoreG3.py                        # variance split + per-habit rates
node shootall.js && python3 embed.py && python3 embstats.py   # embeddings, $0
python3 vision.py                         # Gemini arm, ~$0.07
python3 score4.py human                   # kappa vs your labels (human/labels/pNN.json)
```
`LABEL_KEY.json` maps p01–p20 to the source pages; it was hidden from the labelling page.
