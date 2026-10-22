import json,numpy as np
E=json.load(open('emb120.json'));fs=E['files'];n=len(fs)
B=np.array([f.split('_')[0] for f in fs]);M=np.array([f.split('_')[1] for f in fs])
S={r_:None for r_ in []}
rows={}
for r in json.load(open('G3_scored.json')):pass
rng=np.random.default_rng(3)
def ss_groups(D2,lab):
    t=0
    for g in np.unique(lab):
        ix=np.where(lab==g)[0];t+=D2[np.ix_(ix,ix)].sum()/(2*len(ix))
    return t
def partition(D2,B,M):
    sst=D2.sum()/(2*len(B))
    cell=np.array([b+'|'+m for b,m in zip(B,M)])
    w_b=ss_groups(D2,B);w_m=ss_groups(D2,M);w_c=ss_groups(D2,cell)
    sb=sst-w_b;sm=sst-w_m;sc=sst-w_c
    return sm/sst,sb/sst,(sc-sm-sb)/sst,w_c/sst
for name in ('dino','clip'):
    X=np.array(E[name]);Xp=X[:n];C=X[n:]
    D2=((Xp[:,None]-Xp[None])**2).sum(-1);D=np.sqrt(D2)
    pm,pb,pi,pr=partition(D2,B,M)
    perm_b=[];perm_m=[]
    for _ in range(999):
        p=rng.permutation(n);a=partition(D2,B[p],M);perm_b.append(a[1]);c=partition(D2,B,M[p]);perm_m.append(c[0])
    boot=[]
    for _ in range(1000):
        ix=rng.integers(0,n,n);a=partition(D2[np.ix_(ix,ix)],B[ix],M[ix]);boot.append(a[0]-a[1])
    boot=np.sort(boot)
    print(f"\n== {name}")
    print(f"performer {pm:.0%} · brief {pb:.0%} · performer×brief {pi:.0%} · run-to-run {pr:.0%}")
    print(f"permutation p: brief {np.mean(np.array(perm_b)>=pb):.3f}, performer {np.mean(np.array(perm_m)>=pm):.3f}; shuffled-label brief share median {np.median(perm_b):.0%}")
    print(f"performer minus brief share, 95% CI [{boot[25]:.2f}, {boot[975]:.2f}]")
    np.fill_diagonal(D,np.inf);nn=D.argmin(1)
    print(f"nearest neighbour same brief {np.mean(B[nn]==B):.0%} (chance ~{np.mean([(np.sum(B==b)-1)/(n-1) for b in B]):.0%}), same performer {np.mean(M[nn]==M):.0%} (chance ~33%)")
    np.fill_diagonal(D,0)
    # swatch rule per brief
    out=[]
    for b in np.unique(B):
        ix=np.where(B==b)[0];w=[];bt=[]
        for i in ix:
            for j in ix:
                if i<j:(w if M[i]==M[j] else bt).append(D[i,j])
        out.append((b,np.mean(w),np.mean(bt)))
    print("swatch within/between performer, per brief:"," ".join(f"{b} {w/bt:.2f}" for b,w,bt in out))
    # novelty vs typicality within brief
    T=[];N=[]
    for b in np.unique(B):
        ix=np.where(B==b)[0];cen=Xp[ix].mean(0)
        for i in ix:
            T.append(-np.linalg.norm(Xp[i]-cen));d=sorted(D[i,j] for j in ix if j!=i);N.append(np.mean(d[:3]))
    print(f"typicality vs novelty r = {np.corrcoef(T,N)[0,1]:+.2f}")
    # controls: pos vs neg distance relative to page distances
    dpn=np.linalg.norm(C[0]-C[1]);dnd=np.linalg.norm(C[1]-C[2]);pairs=D[np.triu_indices(n,1)]
    print(f"controls: pos–neg {dpn:.3f}, neg–dark {dnd:.3f}; page pairs median {np.median(pairs):.3f}, 5th–95th pct {np.percentile(pairs,5):.3f}–{np.percentile(pairs,95):.3f}")
    json.dump({"T":T,"N":N},open(f'nt_{name}.json','w'))
# Mantel: embedding distance vs habit distance
H=json.load(open('G3_scored.json'))
import glob
order=sorted(glob.glob('G3all/*.json'));assert [o.split('/')[1].replace('.json','.png') for o in order]==fs
hv=np.array([[r['h'][k] for k in r['h']]+[r['v'][k] for k in r['v']] for r in H],float)
Dh=np.abs(hv[:,None]-hv[None]).sum(-1);iu=np.triu_indices(n,1)
for name in ('dino','clip'):
    X=np.array(E[name])[:n];D=np.sqrt(((X[:,None]-X[None])**2).sum(-1))
    print(f"Mantel r ({name} vs 13-habit distance): {np.corrcoef(D[iu],Dh[iu])[0,1]:+.2f}")
