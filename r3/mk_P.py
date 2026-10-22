import json
E=[]
def a(id,label,year,thread,detail,links,opened,cc,impl):
    E.append(dict(id=id,label=label,year=year,thread=thread,detail=detail,links=links,lane="P",opened=opened,claim_check=cc,implication=impl))
a("gerstner","Programmes for solutions, Gerstner","1964","same",
 "Gerstner's subtitle is 'Instead of solutions for problems, programmes for solutions': no problem has one absolute solution, so describing the problem is part of the solution and designing means picking determining elements and combining them.",
 ["knobs","swatch","signature"],
 "full text (excerpt) — https://jonathanzong.com/assets/jzong-gerstner.pdf; publisher blurb books.google.co.uk",
 "narrower: the quote and 'design as selection and combination of determining elements' are in the text I read; 'morphological box' did not appear in the excerpt, so it is left out.",
 "A score should state its determining elements as choices to combine, which is what the knobs on the drum machine and paired constraints already do.")
a("goodman_lang","Score and compliance, Goodman","1968","observe",
 "In Goodman's account a musical work is the class of performances that comply with the score, but only where the notation is strict: a single wrong note makes it another work, while tempo and cadenza stay open to the performer.",
 ["check2","capture","diff"],
 "secondary — https://plato.stanford.edu/entries/goodman-aesthetics/ (Stanford Encyclopedia); Hernadi abstract doi.org/10.2307/3333090",
 "narrower: autographic/allographic and 'a work is the class of performances compliant with the score' confirmed, but compliance is strict only for the notational part; a painting has no score at all. SEP stresses identity is separate from value.",
 "Only the score lines that are truly checkable (present or absent on the rendered page) can be graded as compliance; the rest of a score needs a different check than yes or no.")
a("iser","Gaps the reader fills, Iser","1971","diverge",
 "Iser holds that no tale can be told in its entirety, so every text has gaps; each reader fills them in their own way, which lets one text support several realizations that no single reading exhausts.",
 ["divdec","sampled","agreeno"],
 "secondary — Iser, 'The Reading Process: A Phenomenological Approach' excerpt (are.na PDF); foreword to Aspects of Narrative (1971) on ebin.pub confirms the Iser essay",
 "narrower: gaps and reader-filling confirmed in Iser's own later essay, which cites the 1971 'Indeterminacy and the Reader's Response' (Aspects of Narrative, pp. 1-45). I did not open that 1971 essay itself; Iser there also notes Ingarden treated some hiatuses as flaws.",
 "Where performers fill a gap differently, that gap is a place the score left open, which is why divergence can name decisions; it cannot tell a deliberate gap from an accidental one.")
a("ingarden","Places of indeterminacy, Ingarden","1931","diverge",
 "Ingarden sees a literary work as a schema with places of indeterminacy, such as what a character had for breakfast; readers partly fill these in, giving many legitimate concretizations, some more faithful to the work than others.",
 ["statesgap","divdec","signature"],
 "secondary — https://plato.stanford.edu/entries/ingarden/ (Stanford Encyclopedia)",
 "confirmed for the idea and for 'concretization'; I did not see the German term or the 1931 date in the source, so those rest on memory. SEP adds that some concretizations fit the work better, so not every filling is equal.",
 "A line left open on a score is a deliberate indeterminacy, and the Sketchbook should mark it as open rather than leave it to look like an omission.")
a("keats","Negative capability, Keats","1817","diverge",
 "Keats names negative capability as being 'in uncertainties, Mysteries, doubts, without any irritable reaching after fact & reason', a quality he credits to Shakespeare and denies to Coleridge, who could not rest in half-knowledge.",
 ["statesgap","agreeno","oneq"],
 "full text (letter excerpt) — https://keatslettersproject.com/correspondence/keats-negative-capability-and-the-pantomime/ ; https://www.lyriktheorie.uni-wuppertal.de/lyriktheorie/texte/1817_keats1.html",
 "confirmed: wording matches the letter to George and Tom Keats of 21-27 Dec 1817 (the 'Dec 1817' date is right; the exact day varies by edition: 22nd or 27th).",
 "Some lines should be allowed to stay open on purpose; the loop should not force a fix on a decision the owner has not made.")
a("meyer_style","Style as constrained choice, Meyer","1989","same",
 "Meyer defines style as a replication of patterning, in behaviour or its artifacts, that results from a series of choices made within some set of constraints; most constraints are learned, not newly invented by whoever uses them.",
 ["unsaid","plainuni","avgtaste"],
 "full text (chapter 1) — https://pdfcoffee.com/meyer-leonard-b-style-and-music-cap-1-pdf-free.html ; Dempster & Brown review (Integral)",
 "confirmed, wording matches Meyer's first sentence. Review adds three constraint levels: laws, rules, strategies.",
 "A shared look is what you get when every performer inherits the same constraints and the score is silent, so the first thing to change is the constraints, not the cast.")
a("moholy","Telephone Pictures, Moholy-Nagy","1923","human",
 "MoMA says an enamel factory in Weimar made the three Telephone Pictures to the artist's instructions, and that Moholy-Nagy later wrote that he ordered them by telephone; the three share one composition at large, medium and small scale.",
 ["prov","rung"],
 "secondary — https://www.moma.org/collection/works/147626 (MoMA collection page)",
 "narrower: MoMA dates the works 1923, not 1922, and only reports that he 'later wrote' he phoned the order; its kids label says he 'liked to tell a story'. I found no source here disputing it, so 'disputed' is unconfirmed.",
 "Authorship by specification is a recognised stance, but the Ship check should record whose hand made each part, as the map's provenance marks do.")
a("halprin","RSVP Cycles, Halprin","1969","human",
 "The RSVP Cycles name four parts: Resources, Scores, Valuaction and Performance, in no set order; scores run from open to closed, and the method came out of the Halprins' workshops that mixed dancers, architects and designers.",
 ["pscore","subtract"],
 "secondary — https://en.wikipedia.org/wiki/RSVP_cycles ; https://www.arch.columbia.edu/exhibitions/6-the-halprin-workshops-1966-1971 ; Halprin interview transcript (tclf.org)",
 "confirmed: four components, Lawrence developed it with Anna Halprin, book 1969 (cited 1970 edition). Larry himself calls an open score one that says how to start but not what the solution is.",
 "The loop's resources, score, judgement and performance map onto RSVP directly, so the useful borrowing is its open-to-closed gradient for score lines.")
a("molnar","One percent disorder, Molnar","1974","same",
 "Molnar worked from 1959 as if she were a computer, which she called a machine imaginaire, and introduced strictly limited disorder into rigid order, such as 1% in a square matrix, a dose small enough to read as variation.",
 ["knobs","swatch","signature"],
 "secondary — https://sites.ac-nancy-metz.fr/arts-plastiques/wp-content/uploads/vera-molnar.pdf ; https://pedagogie.ac-rennes.fr/sites/pedagogie.ac-rennes.fr/IMG/pdf/machines_a_dessiner_programme_limitatif.pdf (French teaching dossiers)",
 "confirmed in substance; narrower on dating: one dossier gives 1% de désordre bleu et rouge as 1974-1978, the other gives 1980, so the year is uncertain. Both are teaching dossiers, not Molnar's own text.",
 "A small, named dose of disorder on one score line is a cleaner knob than hoping the cast diverges on its own.")
a("queneau_ex","Same story, 99 ways, Queneau","1947","same",
 "Exercises in Style retells one unexceptional bus incident and a later button-advice scene in ninety-nine styles, so content stays fixed and only the manner moves.",
 ["swatch","signature","unsaid"],
 "secondary — https://www.ndbooks.com/book/exercises-in-style-anniversary/ (publisher) ; https://en.wikipedia.org/wiki/Exercises_in_style",
 "confirmed: 99 retellings of one trivial story (the 65th anniversary edition adds more exercises on top).",
 "Holding the brief fixed and varying only the manner is a ready test for how much of a look belongs to the setup.")
a("zorn_cobra","Cue cards and rules, Zorn","1984","human",
 "In Cobra, players call cues by gesture, the prompter accepts or declines and holds up the card, and the card names a kind of change, not the music; what happens is left to the performers.",
 ["monitor","oneq","statesgap"],
 "full text (excerpt) — Brackett, 'Some Notes on John Zorn's Cobra' (scispace.com/pdf/some-notes-on-john-zorn-s-cobra-1a4unii54e.pdf); cue sheet on archive.org",
 "narrower: a player makes the call and the prompter can ignore it, so the prompter is a gatekeeper, not a driver. Zorn calls Cobra the most celebrated game piece of 1984; the cue list is a key to cues, not a score of content.",
 "The prompter role fits the STATE.md channel: players raise cues, one agent accepts or declines, and nobody gets to ask twice at once.")
a("conduction","Sign vocabularies, Morris and Thompson","1974","human",
 "Conduction and Soundpainting are the most developed systems of gestures for steering improvisers live: the conductor signs, the ensemble responds, and the conductor answers with new signs; Soundpainting grew to over 200 gestures.",
 ["monitor","oneq"],
 "secondary — Eskildsen review, https://doi.org/10.21083/csieci.v12i1.4164 ; https://www.soundpainting.com/history/",
 "confirmed in outline; the year is Thompson's start of Soundpainting (1974, his own dictionary page). I did not open a source giving the year Morris began Conduction.",
 "A small fixed set of signs, each with a known meaning, is the model for line states: the steering stays live without free text.")
a("commedia","Scenario and lazzi, Commedia","1611","same",
 "A canovaccio lists only acts and scenes, leaving detail to the actors' improvisation and to their lazzi, the jokes and gags they brought; Scala's 1611 collection holds 100 such scenarios.",
 ["libex","diagram","pscore"],
 "secondary — https://en.wikipedia.org/wiki/Canovaccio ; https://lucetadicosimo.com/wp-content/uploads/2017/07/writing-commedia-dell_arte-scenarios-2017.pdf ; Genoa thesis (unige.iris.cineca.it)",
 "narrower: scenario plus lazzi confirmed. The Italian thesis supports 'stock' (the actors draw on a store of tested routines), but I did not find a source stating the set of lazzi was a fixed list.",
 "A Library of tested pieces for the performers to draw on is old practice, with the old risk that everyone reaches for the same joke.")
a("partimento","Stock schemata, Gjerdingen","2007","same",
 "Gjerdingen describes galant music as a seamless chain of stock phrases, or schemata, such as the Romanesca and the Prinner, each defined by melody, bass and metric pattern, and ties them to the Neapolitan partimento teaching tradition.",
 ["libex","signature","unsaid"],
 "secondary — https://en.wikipedia.org/wiki/Galant_Schemata ; Holtmeier review, https://doi.org/10.1017/s1478570611000091 ; schema prototypes appendix (partimenti.org)",
 "narrower: schemata and their link to partimento confirmed; 'bass-line exercises' for training improviser-composers is not stated in the passages I read (the review only places the rule of the octave, cadences and sequences at the centre of the tradition).",
 "A shared stock of patterns gives a recognisable period style without any one source copied, so a house look can be measured by which schemata recur.")
a("conddesign","Rules as constraints, Conditional Design","2008","diverge",
 "The Conditional Design manifesto says the process is the product and that rules are constraints: 'avoid arbitrary randomness', and 'difference should have a reason'.",
 ["divdec","signature","knobs"],
 "full text — https://conditionaldesign.org/manifesto/ ; https://en.wikipedia.org/wiki/Conditional_Design_Manifesto",
 "narrower: authors, 2008 and process/logic/input confirmed; the manifesto does not mention drawing games, though the group's workshop list includes conditional drawing titles.",
 "A difference between performers only counts as a decision if there is a reason for it on the score.")
a("doit","Instructions realised by others, do it","1993","diverge",
 "do it began in 1993 in Paris from a talk between Obrist, Boltanski and Lavier, starting with twelve artist instructions; by 2013 it held instructions from over 400 artists, realised differently at each venue.",
 ["divdec","diff","signature"],
 "secondary — https://www.e-flux.com/announcements/31773/do-it ; https://www.e-flux.com/projects/66684/do-it",
 "confirmed: 1993, the three founders and the twelve instructions are in the e-flux notice; 'over 400' is its 2013 figure.",
 "A set of short instructions realised at several venues is a standing example of what the same score gives across performers.")
a("fluxus","Event scores, Brecht and Ono","1964","history",
 "Brecht reduced the event score to a bare minimum of language, sometimes one word, and left interpretation to the person enacting it; Ono's Grapefruit collects such instructions, one asking people to touch each other.",
 ["plainlines","pscore","namedef"],
 "secondary — https://www.moma.org/magazine/articles/407 (MoMA); Fluxus Foundation essay fluxusfoundation.com; Finberg dissertation (escholarship.org)",
 "narrower: short text instructions confirmed; Grapefruit's date varies, 1964 in MoMA and Finberg, while the Fluxus Foundation essay gives a 1965 Tokyo limited edition of 500 copies.",
 "Plain short lines can carry a whole piece, which agrees with the finding that plain statements move choices as much as quotes.")
a("johnstone","Offers and blocking, Johnstone","1979","human",
 "Johnstone calls anything an actor does an offer, which can be accepted or blocked; scenes build when both accept, and he says improvisers should assume an offer was already made.",
 ["yes","oneq"],
 "secondary — Impro excerpts, https://pwn.ersh.io/notes/keith_johnstone-impro/keith_johnstone-impro.pdf ; Routledge front matter (taylorfrancis.com)",
 "confirmed: offers, blocking and status are in the text (status is the book's first section). First published by Faber in 1979.",
 "An agent trained to accept every offer is the 'optimises for yes' risk in the map, so the channel needs a way to refuse that is not blocking.")
a("renga","Linked verse and the folded page, Renga","1980","blind",
 "A 1980 review notes that renga poets built one work under strict rules for linking verses, with no folded paper, while the Surrealist exquisite corpse hid each contribution; the Academy of American Poets puts the hiding as its one hard rule.",
 ["blindfirst","swap","rejudge"],
 "secondary — Christopher Reid, LRB 1980, https://www.lrb.co.uk/the-paper/v02/n09/christopher-reid/consequences ; https://poets.org/glossary/exquisite-corpse",
 "corrected: the claim that renga poets saw only the previous verse is not supported by what I opened; the review says renga had strict rules and no folding. Only the exquisite corpse is confirmed as hidden from the others.",
 "Hiding what others did is a deliberate rule, and it fits blind-first judgment; renga is the opposite case, a chain where each link is seen.")
json.dump(E,open("/tmp/claude-0/-home-user/0abab622-a16f-58a8-b39c-750f5ad86b9b/scratchpad/r3/out_P.json","w"),indent=1,ensure_ascii=False)
ids=set("unsaid matpack namedef plainuni lookholds blindname whocounts statesgap capture check2 ground quote logfacts card freeze video blindfirst swap rejudge arena makers m56 diagram libex signature swatch flatten avgtaste knobs allclaude interview label10 dated behav plainlines pscore echo still dirlevel goal swing aa standins divdec sampled agreeno specgap diff plan subtract prov rung monitor oneq yes".split())
th={"observe","blind","same","history","level","diverge","human"}
for e in E:
    assert e["thread"] in th and all(l in ids for l in e["links"]),e["id"]
    print(e["id"],len(e["detail"].split()))
print(len(E))
