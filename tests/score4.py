# usage: python3 score4.py [labels_dir]  — labels_dir holds labels/pNN.json from ArtifactData out_dir
import json,sys,os,random
K=json.load(open('LABEL_KEY.json'));R=json.load(open('G3_rendered.json'));G=json.load(open('G4_gemini.json'))
V=["V1","V2","V3","V4","V5"];ids=sorted(K)
chk={p:{v:("yes" if R[K[p]].get(v) else "no") for v in V} for p in ids}
gem={p:G[p]['ans'] for p in ids}
def kappa(a,b):
    pr=[(x,y) for x,y in zip(a,b) if x in("yes","no") and y in("yes","no")]
    if not pr:return None,0
    n=len(pr);po=sum(x==y for x,y in pr)/n;pa=sum(x=="yes" for x,_ in pr)/n;pb=sum(y=="yes" for _,y in pr)/n
    pe=pa*pb+(1-pa)*(1-pb);return (None if pe==1 else (po-pe)/(1-pe)),n
def ci(a,b,B=2000):
    g=random.Random(7);ks=[]
    for _ in range(B):
        ix=[g.randrange(len(a)) for _ in a];k,_=kappa([a[i] for i in ix],[b[i] for i in ix])
        if k is not None:ks.append(k)
    ks.sort();return ks[int(.025*len(ks))],ks[int(.975*len(ks))]
def table(X,Y,lx,ly):
    print(f"\n{lx} vs {ly}");out={}
    for v in V:
        a=[X[p][v] for p in ids];b=[Y[p][v] for p in ids];k,n=kappa(a,b)
        agree=sum(x==y for x,y in zip(a,b))
        if k is None:print(f"  {v}: kappa undefined (no variation), raw agreement {agree}/20");out[v]=None;continue
        lo,hi=ci(a,b);print(f"  {v}: kappa {k:+.2f} [{lo:+.2f}, {hi:+.2f}]  n={n}  raw agreement {agree}/20");out[v]=(k,lo,hi)
    return out
table(chk,gem,"rendered checker","gemini")
if len(sys.argv)>1:
    d=sys.argv[1];H={}
    for p in ids:
        f=os.path.join(d,'labels',p+'.json')
        if os.path.exists(f):H[p]=json.load(open(f))
    print(f"\nhuman labels found for {len(H)}/20 pages")
    if len(H)==20:
        c=table(H,chk,"YOU","rendered checker");g=table(H,gem,"YOU","gemini")
        print("\nP4a (checker kappa >= 0.6 on >=4 of 5):",sum(1 for x in c.values() if x and x[0]>=.6),"of 5")
        print("P4b (checker beats gemini on >=3 of 5):",sum(1 for v in V if c[v] and g[v] and c[v][0]>g[v][0]),"of 5")
        print("unsure counts:",{v:sum(H[p].get(v)=="unsure" for p in ids) for v in V})
