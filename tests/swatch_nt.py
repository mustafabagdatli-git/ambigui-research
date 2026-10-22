import json,glob,re,math,random,statistics as st
from bs4 import BeautifulSoup
from habits import habits
rows=[]
for f in sorted(glob.glob('A/*.json')):
    r=json.load(open(f)); s=BeautifulSoup(r['html'],'html.parser')
    for t in s(['style','script']): t.decompose()
    rows.append(dict(arm=r['arm'],model=r['model'].split('/')[1],txt=re.sub(r'\s+',' ',s.get_text(' ')).lower(),h=habits(r['html'])))
toks=[re.findall(r'[a-z]{3,}',x['txt']) for x in rows];from collections import Counter
df=Counter(w for t in toks for w in set(t));N=len(rows)
def vec(t):
    c=Counter(t);v={w:(1+math.log(n))*math.log(N/df[w]) for w,n in c.items() if df[w]<N};nr=math.sqrt(sum(x*x for x in v.values())) or 1;return {w:x/nr for w,x in v.items()}
for r,t in zip(rows,toks): r['v']=vec(t)
cos=lambda a,b:sum(a.get(w,0)*x for w,x in b.items())
def hj(a,b):
    A={k for k,v in a.items() if v};B={k for k,v in b.items() if v};return len(A&B)/len(A|B) if A|B else 1
def boot(xs,k=4000):
    g=random.Random(9);bs=sorted(st.mean(g.choices(xs,k=len(xs))) for _ in range(k));return bs[int(.025*k)],bs[int(.975*k)]
print("=== SWATCH (direct arm, one brief): spread = 1 - similarity ===")
D=[r for r in rows if r['arm']=='direct']
within=[];between=[]
for i,a in enumerate(D):
    for b in D[i+1:]:
        (within if a['model']==b['model'] else between).append((1-cos(a['v'],b['v']),1-hj(a['h'],b['h'])))
for name,idx in (("text",0),("habits",1)):
    w=[x[idx] for x in within];b=[x[idx] for x in between]
    print(f"{name:7} within-performer spread {st.mean(w):.3f} {tuple(round(x,3) for x in boot(w))} | between-performer {st.mean(b):.3f} {tuple(round(x,3) for x in boot(b))} | ratio within/between {st.mean(w)/st.mean(b):.2f}")
for m in sorted({r['model'] for r in D}):
    g=[r for r in D if r['model']==m];w=[1-cos(a['v'],b['v']) for i,a in enumerate(g) for b in g[i+1:]]
    print(f"   {m:18} within text spread {st.mean(w):.3f}")
print("\n=== NOVELTY + TYPICALITY (all 60 pages) ===")
cent={}
for r in rows:
    for w,x in r['v'].items(): cent[w]=cent.get(w,0)+x/N
cn=math.sqrt(sum(x*x for x in cent.values()));cent={w:x/cn for w,x in cent.items()}
for r in rows:
    r['typ']=cos(r['v'],cent)
    sims=sorted((cos(r['v'],o['v']) for o in rows if o is not r),reverse=True)
    r['nov']=1-st.mean(sims[:3])
    r['hab']=sum(r['h'].values())
print("arm/model            typicality  novelty  habits")
for a in ('direct','vs'):
    for m in sorted({r['model'] for r in rows}):
        g=[r for r in rows if r['arm']==a and r['model']==m]
        print(f"{a:6} {m:18} {st.mean(r['typ'] for r in g):.3f}      {st.mean(r['nov'] for r in g):.3f}    {st.mean(r['hab'] for r in g):.1f}")
def corr(x,y):
    mx,my=st.mean(x),st.mean(y);return sum((a-mx)*(b-my) for a,b in zip(x,y))/math.sqrt(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))
print("corr(typicality, habits) %.2f | corr(novelty, habits) %.2f | corr(typicality, novelty) %.2f"%(corr([r['typ'] for r in rows],[r['hab'] for r in rows]),corr([r['nov'] for r in rows],[r['hab'] for r in rows]),corr([r['typ'] for r in rows],[r['nov'] for r in rows])))
