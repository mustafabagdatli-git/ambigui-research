import json,os,re
from concurrent.futures import ThreadPoolExecutor
from orc import chat,COST
BRIEF="Design the landing page for Tidepool, a tool that helps small teams plan their week together."
TASK=" Return a build plan, not code: list every section top to bottom, and for each give layout, visual treatment (palette, type, imagery) and copy approach. Be concrete. About 300 words."
EX=("Here is a landing page from our Library that a past round produced for a different product (a shared shopping-list app):\n"
"- A vertical week-timeline runs down the left side as a sidebar, with each day as a node.\n"
"- A hand-drawn arrow annotation points from the headline to the main screenshot.\n"
"- Palette: deep forest green with coral accents.\n"
"- A customer pull quote is set in a monospace typeface.\n"
"- Hero headline: 'Bring every member of your household together around one living list that updates instantly, remembers what you buy every week, and quietly takes the guesswork out of the trip to the store so nobody ever forgets the milk again.'\n")
MODELS=["anthropic/claude-haiku-5.5","openai/gpt-6-luna","z-ai/glm-5.3-flashx"]
os.makedirs('B',exist_ok=True)
def run(model,arm,i):
    pre=EX+"\n" if arm in("early","repeated") else ""
    m1=[{"role":"user","content":pre+BRIEF+TASK}]
    d,f1=chat(model,m1,max_tokens=16000)
    rev="Now revise your plan to make it stronger. Return the full revised plan."
    if arm in("late","repeated"): rev=EX+"\n"+rev
    d2,f2=chat(model,m1+[{"role":"assistant","content":d},{"role":"user","content":rev}],max_tokens=16000)
    r={"model":model,"arm":arm,"i":i,"draft":d,"final":d2,"finish":[f1,f2]}
    json.dump(r,open(f"B/{arm}_{model.split('/')[1]}_{i}.json","w")); return r
jobs=[(m,a,i) for m in MODELS for a in("none","early","late","repeated") for i in range(10)]
with ThreadPoolExecutor(12) as ex: res=list(ex.map(lambda j:run(*j),jobs))
from collections import Counter
print("done",len(res),"cost $%.3f"%COST[0],Counter(tuple(r['finish']) for r in res))
