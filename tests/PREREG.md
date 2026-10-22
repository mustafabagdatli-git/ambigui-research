# Accepted-move tests — predictions written before any run
Written 2026-10-21, before any call below was made. Model-only. No person involved.

Shared setup
- Brief (new, one only): "Design the landing page for Tidepool, a tool that helps small teams plan their week together. Return one self-contained HTML file with inline CSS. No external images."
- Performers: anthropic/claude-haiku-5.5, openai/gpt-6-luna, z-ai/glm-5.3-flashx (same three as the Oct 20 outside-review tests).
- Judge for text features: deepseek/deepseek-v4.1-flash, blind to arm.
- House-habit checker: a NEW script written in this session (not the kit's checker, which lives in ~/roster and is not reachable). Countable habits only, because visual habits had kappa 0.00–0.27 between checkers on Oct 21: eyebrow label above the h1, pricing section, testimonials, logo/"trusted by" strip, FAQ, numbered how-it-works steps, serif headline font, emphasised word inside the h1. Score 0–8.
- Known limits before running: one brief; three cheap models; plans not pages in Test B; my own checker, so numbers are not comparable to the Oct 20/21 medians.

Test A — Verbalized Sampling (accepted move 3a; the base-model arm is DROPPED: no base model on OpenRouter, 469 models listed)
- Arms: DIRECT (one call: build the page) vs VS (call 1: list 5 distinct directions for this page with the probability you would pick each; one direction sampled by those stated probabilities; call 2: build that direction).
- n = 10 pages per model per arm = 60 pages.
- Prediction A1: VS lowers the median habit score by at least 1 (of 8), pooled and in at least 2 of 3 models.
- Prediction A2: VS raises diversity: mean pairwise similarity of pages (TF-IDF cosine over visible text + section order) is lower under VS in at least 2 of 3 models.
- Would change my mind: A1 and A2 both fail, i.e. asking for a distribution changes what models say but not what they build.

Test B — Library example timing (accepted move 3b; Kulkarni et al. 2012)
- Example: a written description of a past page with 4 planted features (vertical week-timeline sidebar; hand-drawn arrow annotation; deep green + coral palette; pull quote set in monospace) and 1 planted flaw (a 45-word hero sentence).
- Arms (all two calls: draft plan, then revise plan): NONE (no example, plain revise), EARLY (example before the draft), LATE (example only at the revise step), REPEATED (example before the draft and again at revise).
- n = 10 per model per arm = 120 final plans. Judge counts planted features present (0–4), flaw present, house habits present, and lists the plan's distinct features.
- Prediction B1 (conformity, Kulkarni): every example arm copies more planted features than NONE; LATE copies at least as many as EARLY.
- Prediction B2 (novelty, Kulkarni): EARLY and REPEATED have more uncommon features (features found in <10% of all 120 plans) than NONE; LATE does not.
- Prediction B3: flaw copying stays under 0.15 per plan in every arm (Oct 20 libex: models argued with the flaw).
- Would change my mind: LATE beats EARLY on uncommon features, i.e. timing matters the other way for models.

Test C — One page vs three (accepted move 3c; Tohidi et al. 2006)
- Targets: 12 DIRECT pages from Test A (4 per model), rendered and screenshotted at 1280x2000.
- Judges (vision): openai/gpt-6-luna, google/gemini-3.8-flash, anthropic/claude-haiku-5.5, each as a small-team lead deciding whether to try the tool.
- SINGLE: target alone; rate 1–10, list problems, say whether you'd reject it. TRIO: target plus two other pages, order shuffled; same questions per page; target's answers kept.
- n = 12 targets x 3 judges x 2 conditions x 2 repeats = 144 judgments.
- Prediction C1: SINGLE rates the target at least 0.5 points higher than TRIO, in at least 2 of 3 judges.
- Prediction C2: SINGLE lists fewer problems; rejections are rarer in SINGLE than TRIO.
- Would change my mind: no difference, i.e. model raters aren't inflated by a lone page the way people were — then the swarm can keep showing one page.

Budget cap: $15 for all three tests. Stop and report if exceeded.

## Deviations, logged during the run (2026-10-21, before any result was scored)
1. z-ai/glm-5.3-flashx spent ~24,000 tokens reasoning and returned no page in all 10 DIRECT and all 10 VS cells (finish_reason=length). Fix: OpenRouter `reasoning.max_tokens=4000` for GLM only; those 20 cells re-run. A call limit, not a model result. Test B (plans) was unaffected: all 120 finished with stop.
2. One Haiku VS cell failed to parse because Haiku wrote the page after the JSON list. Parser changed to read the first JSON array only; that cell re-run.
3. The base-model arm was dropped before running (no base model on OpenRouter).
