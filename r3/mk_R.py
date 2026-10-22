import json
R=[]
def a(id,label,year,thread,detail,links,opened,cc,imp):
    R.append(dict(id=id,label=label,year=year,thread=thread,detail=detail,links=links,lane="R",opened=opened,claim_check=cc,implication=imp))
a("kleinberg","Algorithmic monoculture, Kleinberg & Raghavan","2021","same",
"Kleinberg and Raghavan model many decision-makers relying on one algorithm and show that, even without shocks and even when it is more accurate for any one agent alone, the group's overall decision quality can fall.",
["allclaude","signature","unsaid"],"abstract and significance statement — https://www.pnas.org/doi/10.1073/pnas.2018340118",
"confirmed","Three performers sharing one model or one score can look more reliable while the round as a whole loses range, so a shared stronger performer is not a free gain.")
a("bommasani","Outcome homogenization, Bommasani et al.","2022","same",
"Bommasani and colleagues find that sharing training data reliably makes the same individuals fail across decision-makers; sharing a foundation model gave mixed results, depending heavily on how the model was adapted.",
["lookholds","signature","allclaude"],"abstract — https://arxiv.org/abs/2211.13972",
"narrower: training-data sharing reliably homogenizes outcomes; for shared foundation models the paper reports mixed results that depend on the adaptation method, not a flat 'shared components lead to the same failures'.",
"If two performers share a base model but differ in setup, the same pages may still fail the same way, so check how each was adapted before counting them as independent.")
a("panickssery","Self-recognition and self-preference, Panickssery, Bowman & Feng","2024","blind",
"LLM judges score their own outputs higher while human annotators rate them equal, and they can tell their own text from others'. Fine-tuning shows a linear link between self-recognition and the strength of self-preference.",
["rejudge","blindfirst","swap"],"abstract — https://arxiv.org/abs/2404.13076",
"narrower: out of the box the models show non-trivial self-recognition; the linear correlation comes from fine-tuning experiments, and the paper also reports controlled experiments against confounders.",
"A critic from the same family as a performer may favour its work, so hide authorship and prefer a critic from another family when scores are locked.")
a("simmel","Imitation and distinction, Simmel","1904","same",
"Simmel writes that the latest fashion touches only the upper classes; as soon as lower classes copy a style, the upper classes turn away from it and adopt a new one, so the game goes on.",
["plainuni","unsaid","lookholds"],"full text — http://www.modetheorie.de/fileadmin/Texte/s/Simmel-Fashion_1904.pdf",
"confirmed","The season's default look is a mark of what has become common; a line that bans it will need renewing as the replacement itself spreads, so a banned list should be dated.")
a("salganik","MusicLab, Salganik, Dodds & Watts","2006","blind",
"In an artificial music market of 14,341 participants, stronger social influence raised both inequality and unpredictability of success. Quality counted only partly: the best songs rarely did poorly and the worst rarely did well, but anything between was possible.",
["blindfirst","arena","makers"],"abstract — https://www.science.org/doi/10.1126/science.1121066",
"confirmed","Showing a performer or critic earlier results before it judges can lock in an early winner, which is why scores are given blind and in shuffled order.")
a("zajonc","Mere exposure, Zajonc","1968","same",
"Zajonc argues that mere repeated exposure to a stimulus makes attitudes toward it more favourable. He reviews four kinds of evidence and notes the effect looks logarithmic in frequency and should be larger for novel objects than familiar ones.",
["avgtaste","lookholds","unsaid"],"abstract and conclusion — https://web.mit.edu/curhan/www/docs/Articles/biases/9_J_Personality_Social_Psychology_1_%28Zajonc%29.pdf",
"confirmed (log-frequency and novelty points added from the conclusion; Zajonc himself says the account books cannot yet be closed)",
"Seeing the same house style on every board may raise its appeal to the judge, so a reviewer who has looked at many pages needs an unfamiliar reference to calibrate against.")
a("sibley","Aesthetic concepts, Sibley","1959","observe",
"Sibley holds that aesthetic terms such as balanced or serene are not condition-governed: no set of non-aesthetic features logically warrants applying them, so one has to look and see for oneself.",
["capture","whocounts","namedef"],"secondary — https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/sibley-frank-1923-1996 and https://plato.stanford.edu/entries/aesthetic-concept/",
"confirmed (Stanford Encyclopedia notes later critics say some aesthetic ascriptions are condition-governed and the thesis does not by itself define the aesthetic)",
"A checklist of countable items cannot certify that a page is balanced or calm, so a person still has to look at the rendered page, with the count shown beside it.")
a("campbell_bvsr","Blind variation and selection, Campbell and Simonton","1960","diverge",
"Campbell framed creative thought as variation plus selective retention. Simonton's study of ten psychologists found a constant probability of success per work, but Simonton himself later says that rule is not Campbell's claim and does not test the theory.",
["divdec","signature","plan"],"abstract of Simonton 1986 (https://doi.org/10.2190/kb7e-a45m-x8x7-dqj4) and Simonton 2022 review (https://www.tandfonline.com/doi/full/10.1080/10400419.2022.2059919); Campbell 1960 abstract not read",
"narrower: the equal-odds ratio is Simonton's addition, supported in a ten-psychologist career study, and Simonton later warns it is not a direct test of Campbell's theory. Campbell 1960 itself was not opened.",
"More performers per score means more variants to select from, but selection is the part that needs a judge; do not read output volume as a quality guarantee.")
a("march91","Exploration and exploitation, March","1991","same",
"In March's model, slower socialization into the organizational code keeps diversity longer and gives higher equilibrium knowledge; moderate turnover helps by bringing in less socialized people, whose value comes from their diversity, not their knowledge.",
["signature","knobs","allclaude"],"abstract and model results (PDF) — https://strategy.sjsu.edu/www.stable/pdf/March,%20J.%20G.%20%281991%29.%20Organization%20Science%202%281%29%2071-87.pdf",
"confirmed (abstract also says fast adaptive processes are effective in the short run but self-destructive in the long run; the turnover benefit is conditional on fast socialization or turbulence)",
"A library that every performer learns from quickly will converge; keep some performers on a fresh or unlearned start so the shared code keeps something to learn from.")
a("lazer","Network structure of exploration, Lazer & Friedman","2007","diverge",
"In a simulation of agents copying the more successful, an efficient network gave better short-run but worse long-run results on complex problems; inefficient networks kept diversity, and moderate connectedness did best at intermediate times.",
["divdec","plan","diagram"],"abstract — https://doi.org/10.2189/asqu.52.4.667 (also PDF at nsr.asc.upenn.edu)",
"narrower: the less connected network wins only in the long run, loses in the short run, and at intermediate times an inverted-U favours moderate connection; it is a simulation, not field data.",
"Letting performers see each other's work early speeds agreement and costs range; show the diff after each has produced a first pass, not before.")
a("daft_lengel","Uncertainty and equivocality, Daft & Lengel","1986","diverge",
"Daft and Lengel define uncertainty and equivocality as two forces behind organizational information processing, and conclude that a major managerial problem is lack of clarity, not lack of data.",
["sampled","agreeno","oneq"],"abstract — https://pubsonline.informs.org/doi/10.1287/mnsc.32.5.554",
"narrower: the abstract supports the uncertainty/equivocality split and the 'clarity, not data' point; the claim that rich media suit equivocal tasks is the paper's body argument and was not read here.",
"When performers diverge it may be an ambiguous brief, not missing facts, so the fix is a question to the operator, not more material.")
a("star","Boundary objects, Star & Griesemer","1989","human",
"Star and Griesemer, studying Berkeley's Museum of Vertebrate Zoology, say boundary objects are adaptable to different viewpoints and robust enough to keep identity across them; they name four types: repositories, ideal types, coincident boundaries and standardized forms.",
["prov","oneq","diff"],"abstract and introduction — https://doi.org/10.1177/030631289019003001 and https://ics.uci.edu/~corps/phaseii/StarGriesemer-BoundaryObjects-SSS.pdf",
"narrower: the abstract says 'adaptable' and 'robust enough to maintain identity'; the exact 'plastic enough to adapt to local needs' wording was not seen in the text opened.",
"STATE.md and the score can serve as a boundary object between operator, performers and critics: one shared record each reads differently, with the same identity.")
a("garbagecan","Garbage can model, Cohen, March & Olsen","1972","diverge",
"Cohen, March and Olsen describe organized anarchies with unclear preferences, unclear technology and fluid participation, as choices looking for problems, solutions looking for issues and decision makers looking for work, then simulate the process.",
["divdec","oneq","yes"],"abstract and opening of the paper — https://doi.org/10.2307/2392088 and https://fbaum.unc.edu/teaching/articles/Cohen_March_Olsen_1972.pdf",
"narrower: the abstract lists choices, issues, solutions and decision makers; the 'independent streams' framing and the model's five measures were not read in the body.",
"A loop with loose preferences and changing participants will attach solutions to whichever question is open, so each open decision needs a named question before a performer is pointed at it.")
a("weick","Loose coupling, Weick","1976","human",
"Weick proposes that organizational elements are often tied together frequently but loosely, rather than by dense tight linkages, and argues the idea explains many odd observations in educational organizations. He later links it to self-determination and local adaptation.",
["monitor","subtract","oneq"],"abstract and Citation Classic note — https://doi.org/10.2307/2391875 and https://garfield.library.upenn.edu/classics1989/A1989T566900001.pdf",
"narrower: loose coupling confirmed from the 1976 abstract; equivocality reduction from The Social Psychology of Organizing / Sensemaking was not opened and is unverified.",
"Keep performers, critics and the operator loosely coupled through a few fixed artifacts, so one can change without forcing the others to.")
a("pickering","Mangle of practice, Pickering","1995","human",
"Pickering describes practice as an open-ended interplay of human and material agency, a dance of agency, worked out through resistance and accommodation, with outcomes that emerge in time and cannot be predicted in advance.",
["prov","knobs","standins"],"secondary — Pickering's own account in https://monoskop.org/images/c/c5/Pickering_Andrew_2002_Cybernetics_and_the_Mangle_Ashby_Beer_and_Pask.pdf, Olohan's summary at https://doi.org/10.7202/1038682ar, and the Chicago press blurb",
"confirmed (the phrase 'dance of agency' is Pickering's; the resistance and accommodation wording comes from a secondary summary, not the book)",
"A rendered page that fails to do what the score asked is the material pushing back; the performer's change in response is the useful record, so log both.")
a("malafouris","Material engagement theory, Malafouris","2013","human",
"Malafouris proposes Material Engagement Theory, which adds materiality, meaning things, artifacts and material signs, into the account of cognition, and treats things as cognitive extensions of the body rather than the mind being all in the head.",
["prov","rung","capture"],"publisher description — https://mitpress.mit.edu/9780262019194/how-things-shape-the-mind/",
"narrower: the publisher text supports 'things as cognitive extensions' and adding materiality to cognition; 'cognition extends into material' is a fair paraphrase but the book's chapters were not read.",
"Working on real material, such as rendered pages and a placeholder register, shapes the maker's thinking, so juniors and agents who never touch the material may not build the same judgement.")
import json
json.dump(R,open("/tmp/claude-0/-home-user/0abab622-a16f-58a8-b39c-750f5ad86b9b/scratchpad/r3/out_R.json","w"),indent=1)
print(len(R))
