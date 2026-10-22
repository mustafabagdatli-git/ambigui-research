import json
E=[]
def a(id,label,year,thread,detail,links,opened,cc,impl):
    E.append(dict(id=id,label=label,year=year,thread=thread,detail=detail,links=links,lane="S",opened=opened,claim_check=cc,implication=impl))
a("venturi","Both-and, Venturi","1966","diverge",
"Venturi writes 'I prefer both-and to either-or', wants richness of meaning over clarity, praises the ambiguous over the articulated, and says of oversimplified buildings 'Less is a bore.' He argues inclusion is a harder unity than exclusion.",
["divdec","signature","sampled"],"full text excerpt (MoMA sample PDF of the book) — https://www.moma.org/d/pdfs/W1siZiIsIjIwMTkvMDcvMDEvOHI4MnI1aW1qcV9XZWJTYW1wbGVfQ29tcGxleGl0eV9Wb2xfMWFuZDIucGRmIl1d/WebSample_Complexity_Vol_1and2.pdf and Buszek excerpt",
"confirmed: 'both-and' over 'either-or', ambiguity and 'Less is a bore' are all in the text; 'Less is a bore' is a reply to Mies's 'less is more', not a standalone slogan.",
"Two performers differing on a line can be kept as both-and on the score, but only where Venturi's condition holds: the whole must still read as one truth, so a kept difference needs a stated reason.")
a("aravena","Half a house, Aravena / Elemental","2004","human",
"Elemental was given about $7,500 per unit for 93 families on their own Iquique site. It built one concrete segment of each house beside an empty segment of equal size, and residents finished the rest as their incomes allowed.",
["prov","oneq","statesgap"],"secondary — MoMA 'Small Scale, Big Change' project page and Wikipedia (Quinta Monroy)",
"narrower: built half is right, but dates differ by source (MoMA 2003-05, Elemental 2003-04, Wikipedia says completed 2003); the half left open was a choice made because the budget could not fund a full house, and the openings were sized to guide the families.",
"A 'fixed' line is the built half and an 'open' line the half left for the owner; the loop should say which half each part is, and size the open half so it can be filled without breaking the fixed one.")
a("brand_pace","Layers change at different rates, Brand","1994","level",
"Brand's six shearing layers (site, structure, skin, services, space plan, stuff) change at different rates, which is why buildings tear at themselves. His pace layers run from fashion and art through commerce, infrastructure, governance and culture to nature, fast layers innovating and slow ones stabilizing.",
["subtract","statesgap","standins"],"full text — How Buildings Learn chapter excerpt (are.na PDF), longnow.org pace-layers page and JoDS essay by Brand (2018)",
"narrower: the shearing-layers idea is Frank Duffy's (four S's), which Brand expanded to six; pace layering is Brand's own and the six-level list is in the Clock of the Long Now material (Long Now dates it 01998, book 1999). I opened excerpts, not the books.",
"Library, board, score and STATE.md move at different speeds; keep fast things (performer output) from rewriting slow ones (fixed lines), and give each layer its own review rate.")
a("supernormal","Super Normal, Fukasawa & Morrison","2006","level",
"Morrison says Super Normal began as a noticing that some mostly anonymous objects outperform others in long everyday use; he calls the Super Normal object the result of long evolution of everyday forms, and a certain lack of noticeability a requirement.",
["plainuni","subtract","avgtaste"],"full text — Jasper Morrison's essay and exhibition page (jaspermorrison.com)",
"narrower: 'celebrating ordinary objects' is close, but Morrison's point is that they perform well in long use and do not draw attention; the term came from Fukasawa in conversation, and the 2006 exhibition was at Axis Gallery, Tokyo.",
"A plain, unnoticed result is not automatically the default look; judge pages by long-use performance on the score, and treat a deliberate quiet as a decision rather than an absence.")
a("mullerb","Grid as ordering system, Müller-Brockmann","1981","same",
"Müller-Brockmann calls the grid an ordering system and a working instrument for faster, more confident design. He says reducing visual elements and fitting them to a grid gives clarity and credibility, and ties the grid to an attitude of objectivity over subjectivity.",
["knobs","unsaid","plainuni"],"full text excerpt — book text on archive.org; publisher page niggli.ch",
"confirmed: the 1981 book names the grid an 'ordering system' for the designer (also in 3-D and exhibition work). Note the stated aim goes further than order, to a democratic, objective ethos.",
"A grid is a constraint the designer chooses, so shared grid tokens make pages look alike on purpose; if the loop fixes a grid, mark it fixed on the score line so sameness there is a decision.")
a("vignelli","A few typefaces, Vignelli","2010","same",
"Vignelli's 1991 exhibition showed years of work in only four typefaces (Garamond, Bodoni, Century Expanded, Helvetica), to prove 'it's not the type but what you do with it that counts.' He calls discipline a set of self-imposed rules within which we operate.",
["plainuni","knobs","unsaid"],"secondary + quoted primary — Fonts In Use quoting The Vignelli Canon; viki.wiki summary of the Canon (RIT PDF itself not opened)",
"narrower: few typefaces, discipline and timelessness are all in the Canon, but the Canon itself says he can add another half dozen, and the quotes are via secondary pages. Fonts In Use dates the book 2009–10; the map's 2010 is the commonly cited print year.",
"A small, declared typeface set is a legitimate fixed line, not a flaw: the sameness to worry about is the unchosen default, so require the score to say which type is fixed and why.")
a("dynid","Identity as a generator, MIT Media Lab & Casa da Música","2011","diverge",
"MIT Media Lab's identity by TheGreenEyl and E Roon Kang is an algorithm giving over 40,000 logos, one per community member, under rules that keep it coherent. Sagmeister's 2007 Casa da Música identity derives variants from six building profiles and 17 planes.",
["divdec","signature","knobs"],"secondary — E Roon Kang's and TheGreenEyl's project pages, ICON magazine, Sagmeister Inc. page, Cooper Hewitt collection record",
"narrower: both are real. MIT's date varies (Kang says 2010 unveiling, TheGreenEyl 2011) and so does the count (40,000 vs 45,000). The Casa da Música date, 2007, matches the Cooper Hewitt record and 2007 press.",
"Variation is cheap to generate and only meaningful when a rule limits it; give performers a seeded variant space and read the spread as a map of which decisions the score left open.")
a("suits","Voluntary obstacles, Suits","1978","human",
"Suits defines playing a game as 'the voluntary attempt to overcome unnecessary obstacles'. The long form has a goal, rules that forbid the more efficient means, and a lusory attitude: accepting the rules just because they make the activity possible.",
["subtract","monitor","knobs"],"secondary — Wikipedia 'Lusory attitude', Hurka's chapter on Suits, and a York University book review quoting p.43",
"confirmed: quote and 1978 date match; 'lusory attitude' is Suits's term for accepting the rules for the sake of the activity.",
"A constraint on a performer is only play if accepted for the activity; state each fixed line as a rule that serves the work, and keep it removable if nobody can say what it makes possible.")
a("caillois","Paidia to ludus, Caillois","1958","human",
"Caillois sorts games into agon (competition), alea (chance), mimicry (role) and ilinx (vertigo). He places them between paidia, spontaneous play, and ludus, play bound by explicit rules. French edition 1958, English 1961.",
["subtract","divdec","statesgap"],"secondary — Wikipedia 'Man, Play and Games'",
"narrower: the four categories and the paidia/ludus pair are confirmed from a secondary page only; I did not open the book, and Wikipedia presents paidia and ludus as two types where Caillois treats them as ends of a range.",
"A score line can sit between loose and rule-bound; open lines are paidia and fixed lines ludus, and rounds could go from the first to the second as decisions settle.")
a("costikyan","Eleven uncertainties, Costikyan","2013","diverge",
"Costikyan argues games need uncertainty to hold interest, and lists eleven forms, among them performative uncertainty, solver's uncertainty, randomness, analytic complexity, hidden information and narrative anticipation. Most games combine two.",
["divdec","signature","agreeno"],"secondary — Analog Game Studies review (Torner 2014), publisher blurb (Google Books) and Costikyan's site",
"confirmed: a taxonomy of eleven forms per the review; I did not open the book and did not check that review's labels against the text.",
"Divergence among performers could be sorted by kind of uncertainty (taste, solving, hidden brief), because only some kinds are open decisions for the operator.")
a("nomic","Rules as a move, Suber","1982","diverge",
"Suber's Nomic is a game in which changing the rules is a move. It has an initial set of immutable and mutable rules, and an immutable rule can be changed only after it is transmuted into a mutable one; first published in Scientific American, June 1982.",
["divdec","statesgap","rung"],"full text — Suber's 'Nomic: A Game of Self-Amendment' (Earlham) and Activities Index entry for June 1982",
"confirmed: the line 'a game in which changing the rules is a move' is in Suber's text; he also says no rule is absolutely immutable.",
"Fixed lines should be amendable by an explicit step, like transmutation, never silently; add a move on the score to unfix a line, recorded in STATE.md.")
a("akrich","De-scription, Akrich","1992","human",
"Akrich says designers inscribe their picture of users and the world into an object as a 'script'. Users may not take the part, or may define quite different roles; de-scription is analysing that gap between imagined and real user.",
["prov","oneq","standins"],"full text excerpt — chapter in Shaping Technology/Building Society (MIT Press, 1992), via fulcrum.org, plus reading notes",
"narrower: 'script' and 'inscribe' are in her words, and users may take other roles; 'follow, adapt or resist' is a fair paraphrase, not her wording. The chapter studies technology transfer cases such as a photoelectric lighting kit.",
"Each score carries a hidden script about who uses the page; test it against real users, since stand-in rounds only show the script back.")
a("bricoleur","Bricoleur vs engineer, Lévi-Strauss","1962","history",
"Lévi-Strauss says the bricoleur does many tasks but makes do with 'whatever is at hand', a finite, heterogeneous stock kept because it may come in handy, where the engineer has tools conceived for the project. He admits the engineer also questions his means.",
["libex","matpack","diagram"],"full text excerpt — The Savage Mind, English translation (MIT-hosted PDF and Columbia quote page)",
"confirmed: the passage is quoted as given; the book is French 1962, English translation 1966. He adds that the distinction is less clear-cut than it looks.",
"A Library is a bricoleur's stock: pieces valued for possible use, not made for one brief; keep them half-specialized and tag each part with where it came from.")
a("fox","Training for uncertainty, Fox","1957","human",
"Fox, observing medical students at Cornell, described three kinds of uncertainty: incomplete mastery of existing knowledge, limits of medical knowledge, and the difficulty of telling the two apart. Students developed ways of coping with it.",
["prov","monitor","statesgap"],"secondary — Fox's own 1980 retrospective in Milbank Quarterly quoting her 1957 text (pp. 208–9); Hastings Center essay",
"confirmed: all three kinds match, including 'difficulty in distinguishing' own ignorance from the field's limits; opened her later paper quoting the 1957 chapter, not the chapter itself.",
"Debriefs and score lines should say whether a gap is the performer's limit or the brief's; where it can't be told, mark the line open rather than blaming either.")
a("horvitz","Mixed-initiative principles, Horvitz","1999","human",
"Horvitz lists twelve principles for mixing automation with direct manipulation, including considering uncertainty about the user's goals, inferring ideal action from costs and benefits, and using dialog to resolve key uncertainties. His LookOut system sets two thresholds, one for dialog and one for action.",
["oneq","monitor","yes"],"full text — Horvitz, CHI 1999 paper PDF (erichorvitz.com)",
"confirmed: twelve numbered principles are listed; (2), (4) and (5) match the claim, and the dialog-versus-action thresholds come from the LookOut example.",
"Decide whether an agent acts, asks or does nothing by the cost of a wrong guess; ask one question only where an error costs more than interrupting.")
a("amershi","Human-AI guidelines, Amershi et al.","2019","human",
"Amershi and colleagues propose 18 guidelines for human-AI interaction, refined through several rounds of evaluation, including a user study in which 49 design practitioners tested them on 20 AI-infused products.",
["monitor","oneq","subtract"],"abstract — Microsoft Research page and ACM abstract (CHI 2019)",
"confirmed: 18 guidelines, validated by a study with 49 practitioners across 20 products; also noted CHI 2019 Honorable Mention.",
"Use the guidelines as a checklist on the STATE.md channel and Sketchbook, e.g. scoping services when in doubt, but remember 'validated' means practitioners judged relevance.")
a("klein_team","Automation as team player, Klein et al.","2004","human",
"Klein and colleagues say joint activity needs four things: a Basic Compact to work together, mutual predictability, mutual directability and common ground. The Compact must be continuously renewed, and anyone dropping out must signal it.",
["monitor","oneq","yes"],"full text — IEEE Intelligent Systems 2004 article (IHMC PDF)",
"confirmed: four requirements named as stated; the paper then states ten challenges for automation.",
"The loop needs a visible compact: who does what, what each agent will do next, how the operator redirects, and a signal when a performer cannot finish.")
a("stigmergy","Traces in a shared medium, Grassé & Heylighen","2016","diverge",
"Grassé coined stigmergy in 1959 for insects coordinating through what earlier work left behind. Heylighen defines it as indirect coordination in which the trace of an action left on a medium stimulates the next action, with no planning or direct messages.",
["divdec","statesgap","oneq"],"full text — Heylighen, Cognitive Systems Research 38 (2016) PDF (VUB)",
"confirmed: Grassé 1959 and the trace-in-medium definition are in the paper; year 2016 is the journal issue (online Dec 2015).",
"STATE.md, the score and the page itself can be the medium: each agent leaves a trace the next reads, with line states as the visible marks.")
a("blackboard","Blackboard, Erman et al. (Hearsay-II)","1980","diverge",
"In Hearsay-II, independent knowledge sources communicate through a global database, the blackboard, where each posts hypotheses with credibility ratings at levels such as word and syllable. A hypothesis can trigger other sources.",
["divdec","sampled","statesgap"],"abstract + full text excerpt — ACM Computing Surveys 12(2), 1980 (UMass PDF)",
"narrower: sources do communicate through the blackboard, but the system also has a scheduler choosing which source runs, so independence is not the whole picture; I read excerpts only.",
"A shared board with levels and a credibility mark per entry is a close model for line states, with a scheduler (the operator) deciding which entry to work next.")
a("lerman","Critical Response Process, Lerman","1990","blind",
"Lerman devised the process in 1990: responders state meaning, the artist asks questions, responders ask neutral questions, then give opinions only with the artist's permission ('I have an opinion about ___, would you like to hear it?').",
["blindfirst","subtract","makers"],"secondary — lizlerman.com process page and Purdue OWL summary",
"narrower: 1990 and the four steps are confirmed on her site; the 2003 book date was not checked, and the facilitator role comes with it.",
"Critique rounds can hold the performer as questioner and ask permission before opinions; neutral questions about a page come before any verdict.")
a("braintrust","Braintrust, Catmull","2014","human",
"Catmull says the Braintrust is made of people who understand storytelling and has no authority: the director need not follow any suggestion. Its notes aim to surface the true causes of problems, not to demand a remedy.",
["makers","subtract","rung"],"full text — Creativity, Inc. chapter excerpt and Fast Company/Collider quoting it; HBR 2008 article not seen",
"confirmed: 'The Braintrust has no authority' and the director's freedom to ignore suggestions are Catmull's words; it meets every few months per film.",
"A critic that proposes but cannot mandate keeps the performer or operator as owner; mark critique output as notes, never as changes landed.")
json.dump(E,open("out_S.json","w"),indent=1)
