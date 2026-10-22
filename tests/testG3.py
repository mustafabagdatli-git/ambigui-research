import json,os,re
from concurrent.futures import ThreadPoolExecutor
from orc import chat,COST
BRIEFS={"B1":"a family plumbing business in Leeds","B2":"a children's science museum","B3":"an open-source database for data engineers",
"B4":"a small poetry press","B5":"a walk-in sexual-health clinic","B6":"a skateboard shop that also runs lessons"}
MODELS=["anthropic/claude-haiku-5.5","openai/gpt-6-luna","z-ai/glm-5.3-flashx"]
os.makedirs('G3',exist_ok=True)
def html_of(t):
    m=re.search(r"```(?:html)?\s*(.*?)```",t,re.S); return m.group(1) if m else t
def run(b,m,i):
    fn=f"G3/{b}_{m.split('/')[1]}_{i}.json"
    if os.path.exists(fn):return json.load(open(fn))
    o,f=chat(m,[{"role":"user","content":f"Design the landing page for {BRIEFS[b]}. Return one self-contained HTML file with inline CSS. No external images."}])
    r={"brief":b,"model":m,"i":i,"finish":f,"html":html_of(o)}; json.dump(r,open(fn,"w")); return r
jobs=[(b,m,i) for b in BRIEFS for m in MODELS for i in range(5)]
with ThreadPoolExecutor(12) as ex: res=list(ex.map(lambda j:run(*j),jobs))
from collections import Counter
print("done",len(res),"cost $%.3f"%COST[0],Counter((r['model'].split('/')[1],r['finish']) for r in res))
