import json,base64,re,sys
from concurrent.futures import ThreadPoolExecutor
from orc import chat,COST
M="google/gemini-3.8-flash"
Q=[("V1","Serif headline","The main headline is set in a serif typeface (letters have small strokes at their ends, as in Georgia or Times)."),
("V2","Set-apart word","Part of the headline — a word or phrase — is styled differently from the rest: italic, another colour, another font, an underline, or a gradient."),
("V3","Small label above the headline","A small piece of text sits just above the headline: uppercase, letter-spaced, or inside a pill or badge."),
("V4","Text left, visual right","The headline and copy sit on the left, with a large visual on the right (image, illustration, product mock-up or card)."),
("V5","Warm off-white background","The main page background is a warm off-white: cream, paper or beige. Not pure white, cool grey, a colour, or dark.")]
P=("This is a screenshot of the first screen (1280×800) of a landing page. Judge only what is visible. "
   "Headline means the largest text that states what the page is about. Answer each question yes, no or unsure "
   "(unsure only when it is really a toss-up).\n\n"+"\n".join(f"{k} — {t}: {d}" for k,t,d in Q)+
   '\n\nReturn JSON only: {"V1":"yes|no|unsure","V2":...,"V3":...,"V4":...,"V5":...}')
def ask(path):
    b=base64.b64encode(open(path,'rb').read()).decode()
    msg=[{"role":"user","content":[{"type":"text","text":P},{"type":"image_url","image_url":{"url":"data:image/jpeg;base64,"+b}}]}]
    for t in range(3):
        o,f=chat(M,msg,max_tokens=4000,temperature=0)
        try: return {"ans":json.loads(re.search(r"\{.*\}",o,re.S).group(0)),"finish":f}
        except Exception: pass
    return {"ans":None,"finish":f,"raw":o[:500]}
items={f"p{i:02d}":f"../label/shots/p{i:02d}.jpg" for i in range(1,21)}
items.update({c:f"CTRLshots/{c}.jpg" for c in ("pos","neg","dark")})
with ThreadPoolExecutor(8) as ex: res=dict(zip(items,ex.map(ask,items.values())))
json.dump(res,open('G4_gemini.json','w'),indent=1)
for k,v in res.items(): print(k,v['finish'],v['ans'])
print("cost $%.3f"%COST[0])
