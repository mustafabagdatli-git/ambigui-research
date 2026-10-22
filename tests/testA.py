import json,random,re,os,sys
from concurrent.futures import ThreadPoolExecutor
from orc import chat,COST
BRIEF="Design the landing page for Tidepool, a tool that helps small teams plan their week together. Return one self-contained HTML file with inline CSS. No external images."
MODELS=["anthropic/claude-haiku-5.5","openai/gpt-6-luna","z-ai/glm-5.3-flashx"]
os.makedirs('A',exist_ok=True)
def html_of(t):
    m=re.search(r"```(?:html)?\s*(.*?)```",t,re.S)
    return m.group(1) if m else t
def direct(model,i):
    out,fin=chat(model,[{"role":"user","content":BRIEF}])
    return {"arm":"direct","model":model,"i":i,"finish":fin,"html":html_of(out)}
def vs(model,i):
    p=BRIEF+"\n\nBefore building, list 5 genuinely different design directions for this page, each with the probability (0-1, summing to 1) that you would pick it. Return JSON only: [{\"direction\": \"...\", \"probability\": 0.x}, ...]"
    out,fin=chat(model,[{"role":"user","content":p}],max_tokens=8000)
    try:
        dirs,_=json.JSONDecoder().raw_decode(out[out.index('['):]); w=[max(float(d.get('probability',0)),0) for d in dirs]
    except Exception: return {"arm":"vs","model":model,"i":i,"finish":"parse_error","raw":out,"html":""}
    rnd=random.Random(f"{model}{i}"); pick=rnd.choices(dirs,weights=w if sum(w)>0 else None)[0]
    out2,fin2=chat(model,[{"role":"user","content":BRIEF+"\n\nBuild it in this design direction:\n"+pick['direction']}])
    return {"arm":"vs","model":model,"i":i,"finish":fin2,"dirs":dirs,"pick":pick,"html":html_of(out2)}
import glob
bad=set()
for p in glob.glob('A/*.json'):
    r=json.load(open(p))
    if r['finish']!='stop': bad.add((r['arm'],r['model'],r['i']))
jobs=[(direct if a=='direct' else vs,m,i) for a,m,i in sorted(bad)]
print('rerunning',len(jobs))
with ThreadPoolExecutor(12) as ex:
    res=list(ex.map(lambda j:j[0](j[1],j[2]),jobs))
for r in res:
    json.dump(r,open(f"A/{r['arm']}_{r['model'].split('/')[1]}_{r['i']}.json","w"))
print("done",len(res),"cost $%.3f"%COST[0]); 
from collections import Counter;print(Counter((r['arm'],r['finish']) for r in res))
