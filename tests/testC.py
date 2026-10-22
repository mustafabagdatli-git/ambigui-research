import json,base64,random,os
from concurrent.futures import ThreadPoolExecutor
from orc import chat
ids=json.load(open('C/targets.json')); targets=ids[:12]; foils=ids[12:]
JUDGES=["openai/gpt-6-luna","google/gemini-3.8-flash","anthropic/claude-haiku-5.5"]
P="You lead a 6-person product team and are deciding whether to try a new tool for planning your team's week. "
def img(i): return {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,"+base64.b64encode(open(f"C/{i}.jpg","rb").read()).decode()}}
def single(j,t,rep):
    c=[{"type":"text","text":P+"Here is the landing page for Tidepool. Rate 1-10 how much it makes you want to try it. List every problem you see, one short line each. Say whether you would reject this design outright. Return JSON only: {\"rating\": int, \"problems\": [str], \"reject\": bool}"},img(t)]
    return c,None
def trio(j,t,rep):
    r=random.Random(f"{j}{t}{rep}"); fs=r.sample([f for f in foils if f.split('_')[1]!=t.split('_')[1]],2)
    order=[t]+fs; r.shuffle(order); labs="ABC"
    c=[{"type":"text","text":P+"Here are three alternative landing-page designs for the same product, Tidepool, labelled A, B and C in order. For EACH design: rate 1-10 how much it makes you want to try the tool, list every problem you see (one short line each), and say whether you would reject that design outright. Return JSON only: {\"A\": {\"rating\": int, \"problems\": [str], \"reject\": bool}, \"B\": {...}, \"C\": {...}}"}]
    for k,i in zip(labs,order): c+= [{"type":"text","text":"Design "+k+":"},img(i)]
    return c,labs[order.index(t)]
def run(job):
    cond,j,t,rep=job; c,lab=(single if cond=="single" else trio)(j,t,rep)
    for k in range(3):
        o,f=chat(j,[{"role":"user","content":c}],max_tokens=8000,temperature=1.0)
        try:
            d=json.JSONDecoder().raw_decode(o[o.index('{'):])[0]; d=d[lab] if lab else d
            return dict(cond=cond,judge=j,target=t,rep=rep,rating=d['rating'],problems=len(d['problems']),reject=bool(d['reject']),slot=lab)
        except Exception as e: err=(f,o[:200])
    return dict(cond=cond,judge=j,target=t,rep=rep,error=str(err))
jobs=[(c,j,t,r) for c in("single","trio") for j in JUDGES for t in targets for r in range(2)]
with ThreadPoolExecutor(12) as ex: res=list(ex.map(run,jobs))
json.dump(res,open('C_results.json','w')); print(len(res),sum('error' in r for r in res),'errors')
