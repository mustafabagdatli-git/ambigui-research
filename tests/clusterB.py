import json,random
from concurrent.futures import ThreadPoolExecutor
from orc import chat
rows=json.load(open('B_rows.json'))
ph=sorted({p.strip().lower() for r in rows for p in r['feats'] if isinstance(p,str)})
print(len(ph),'phrases')
def ask(q,opener,mt=12000):
    for t in range(4):
        o,f=chat("deepseek/deepseek-v4.1-flash",[{"role":"user","content":q}],max_tokens=mt,temperature=0)
        try: return json.JSONDecoder().raw_decode(o[o.index(opener):])[0]
        except Exception: print('retry',f,flush=True)
samp=random.Random(5).sample(ph,min(400,len(ph)))
labels=ask("These are design features found in landing-page plans. Propose 60 to 90 canonical feature labels (2-5 words each) that together cover them, each label one distinct design feature. Return a JSON array of strings only.\n"+json.dumps(samp),'[')
print(len(labels),'labels',flush=True)
def mapb(b):
    return ask("Assign each phrase to the single best label from this fixed list; if none fits, use \"OTHER: <new 2-5 word label>\".\nLabels: "+json.dumps(labels)+"\nPhrases: "+json.dumps(b)+"\nReturn JSON only: {\"phrase\": \"label\", ...} covering every phrase.",'{') or {}
bs=[ph[i:i+60] for i in range(0,len(ph),60)]
with ThreadPoolExecutor(12) as ex: maps=list(ex.map(mapb,bs))
mp={};miss=0
for b,m in zip(bs,maps):
    for p in b:
        if p in m: mp[p]=m[p]
        else: miss+=1; mp[p]="UNMAPPED:"+p
json.dump({"labels":labels,"map":mp},open('B_featmap.json','w')); print('unmapped',miss)
