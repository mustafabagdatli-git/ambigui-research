import json,glob,statistics as st,random
from habits import habits
R=json.load(open('G3_rendered.json'))
rows=[]
for f in sorted(glob.glob('G3all/*.json')):
    n=f.split('/')[1];b,m,_=n[:-5].split('_');h=habits(json.load(open(f))['html']);v=R[n]
    vis={k:bool(v.get(k)) for k in ['V1','V2','V3','V4','V5']}
    rows.append(dict(b=b,m=m,cnt=sum(h.values()),h=h,vis=sum(vis.values()),v=vis))
names={"B0":"Tidepool (planner)","B1":"plumber, Leeds","B2":"children's museum","B3":"open-source DB","B4":"poetry press","B5":"sexual-health clinic","B6":"skate shop"}
print(f"{'brief':24}{'median countable/8':>20}{'median visual/5':>17}")
for b in sorted(names):
    g=[r for r in rows if r['b']==b];print(f"{names[b]:24}{st.median(r['cnt'] for r in g):>14}{st.median(r['vis'] for r in g):>16}")
print("\nbriefs with median countable >= 4:",sum(st.median(r['cnt'] for r in rows if r['b']==b)>=4 for b in names),"of 7")
def decomp(key):
    y=[r[key] for r in rows];gm=st.mean(y);sst=sum((x-gm)**2 for x in y)
    def ss(f):
        out=0
        for lv in {r[f] for r in rows}:
            g=[r[key] for r in rows if r[f]==lv];out+=len(g)*(st.mean(g)-gm)**2
        return out
    sm,sb=ss('m'),ss('b');cells={};[cells.setdefault((r['m'],r['b']),[]).append(r[key]) for r in rows]
    scell=sum(len(g)*(st.mean(g)-gm)**2 for g in cells.values());inter=scell-sm-sb
    return sm/sst,sb/sst,inter/sst,(sst-scell)/sst
for key,lab in (('cnt','countable habits'),('vis','visual habits')):
    pm,pb,pi,pr=decomp(key);print(f"{lab:17} performer {pm:.0%} · brief {pb:.0%} · performer×brief {pi:.0%} · run-to-run {pr:.0%}")
# bootstrap for performer vs brief share (countable)
g=random.Random(4);diffs=[]
orig=rows[:]
for _ in range(1000):
    rows=[g.choice(orig) for _ in orig]
    try:pm,pb,_,_=decomp('cnt');diffs.append(pm-pb)
    except Exception:pass
rows=orig;diffs.sort();print("performer minus brief share (countable), 95%% CI [%.2f, %.2f]"%(diffs[25],diffs[975]))
print("\nper-habit rate by brief (countable + visual):")
keys=list(rows[0]['h'])+['V1','V2','V3','V4','V5']
print('habit'.ljust(13)+''.join(b.rjust(6) for b in sorted(names)))
for k in keys:
    print(k.ljust(13)+''.join(f"{sum((r['h'].get(k) if k in r['h'] else r['v'][k]) for r in rows if r['b']==b)/len([r for r in rows if r['b']==b]):6.0%}" for b in sorted(names)))
json.dump(rows,open('G3_scored.json','w'))