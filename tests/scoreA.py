import json,glob,re,math,statistics as st
from collections import Counter,defaultdict
from bs4 import BeautifulSoup
from habits import habits
rows=[]
for f in sorted(glob.glob('A/*.json')):
    r=json.load(open(f)); h=habits(r['html']); s=BeautifulSoup(r['html'],'html.parser')
    for t in s(['style','script']): t.decompose()
    txt=re.sub(r'\s+',' ',s.get_text(' ')).lower()
    secs=[ (x.name+':'+re.sub(r'\W+',' ',x.get_text(' '))[:30].strip().lower()) for x in s.find_all(['section','header','footer'])]
    rows.append(dict(arm=r['arm'],model=r['model'].split('/')[1],i=r['i'],h=h,score=sum(h.values()),txt=txt,secs=[x.split(':')[0]+':'+' '.join(x.split(':')[1].split()[:2]) for x in secs]))
def tfidf(docs):
    tok=[re.findall(r'[a-z]{3,}',d) for d in docs]; df=Counter(w for t in tok for w in set(t)); N=len(docs)
    vecs=[]
    for t in tok:
        c=Counter(t); v={w:(1+math.log(n))*math.log(N/df[w]) for w,n in c.items()}; nrm=math.sqrt(sum(x*x for x in v.values())) or 1
        vecs.append({w:x/nrm for w,x in v.items()})
    return vecs
def meansim(vs):
    s=[sum(a.get(w,0)*x for w,x in b.items()) for i,a in enumerate(vs) for b in vs[i+1:]]; return st.mean(s)
allv=tfidf([r['txt'] for r in rows])
for r,v in zip(rows,allv): r['v']=v
print("model         arm     median_habits  mean   pairwise_text_sim")
for m in sorted({r['model'] for r in rows}):
    for a in ('direct','vs'):
        g=[r for r in rows if r['model']==m and r['arm']==a]
        print(f"{m:14}{a:8}{st.median([r['score'] for r in g]):>8}   {st.mean([r['score'] for r in g]):5.2f}   {meansim([r['v'] for r in g]):.3f}")
for a in ('direct','vs'):
    g=[r for r in rows if r['arm']==a]; print('POOLED',a,st.median([r['score'] for r in g]),round(st.mean([r['score'] for r in g]),2))
print('\nhabit rates by arm:')
for k in rows[0]['h']:
    print(f"{k:13}",*[f"{a}:{sum(r['h'][k] for r in rows if r['arm']==a)}/30" for a in('direct','vs')])
json.dump([{k:v for k,v in r.items() if k not in('v','txt')} for r in rows],open('A_scored.json','w'))
