import json,glob,random,re
from concurrent.futures import ThreadPoolExecutor
from orc import chat
J="deepseek/deepseek-v4.1-flash"
Q='''You are auditing a landing-page build plan. Answer from the plan text only. Return JSON only:
{"planted":{"timeline_sidebar":bool,"handdrawn_arrow":bool,"green_coral":bool,"mono_pullquote":bool},
 "long_hero":bool,
 "habits":{"eyebrow_label":bool,"pricing":bool,"testimonials":bool,"logo_strip":bool,"faq":bool,"numbered_steps":bool,"serif_headline":bool,"product_mockup":bool},
 "features":[short noun phrases, 8 to 15, one per distinct design feature of THIS plan, e.g. "dark mode toggle", "illustrated mascot"]}
Definitions: timeline_sidebar = a vertical week/day timeline running down the side; handdrawn_arrow = a hand-drawn/sketched arrow or annotation; green_coral = palette of deep/forest green with coral accents; mono_pullquote = a quote set in a monospace typeface; long_hero = the hero headline itself is over 30 words; eyebrow_label = small label/kicker above the main headline; product_mockup = a screenshot/mock UI of the product.
PLAN:
'''
files=sorted(glob.glob('B/*.json')); random.Random(7).shuffle(files)
def j(f):
    r=json.load(open(f))
    for t in range(3):
        o,fin=chat(J,[{"role":"user","content":Q+r['final']}],max_tokens=6000,temperature=0)
        try: return f,json.JSONDecoder().raw_decode(o[o.index('{'):])[0]
        except Exception: pass
    return f,None
with ThreadPoolExecutor(16) as ex: out=dict(ex.map(j,files))
json.dump(out,open('B_judged.json','w')); print(sum(v is None for v in out.values()),'failed of',len(out))
