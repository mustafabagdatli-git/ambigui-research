# Countable house-habit checker, written this session (NOT the kit's checker in ~/roster).
import re
from bs4 import BeautifulSoup
SERIF=re.compile(r"serif",re.I); SANS=re.compile(r"sans-serif",re.I)
def text(el): return re.sub(r"\s+"," ",el.get_text(" ",strip=True)) if el else ""
def habits(html):
    s=BeautifulSoup(html,"html.parser"); low=html.lower(); body=text(s.body or s).lower()
    h1=s.find("h1"); h={}
    # 1 eyebrow: a short text element right before the h1 within the same parent
    eb=False
    if h1:
        prev=h1.find_previous_sibling()
        if prev is not None and 0<len(text(prev))<=40 and prev.name not in("h1","nav","header","img","svg"): eb=True
    h["eyebrow"]=eb
    h["pricing"]=bool(re.search(r"\bpricing\b|/\s?mo(nth)?\b|per month|\$\d+\s*/",body))
    h["testimonials"]=bool(re.search(r"testimonial|what (our )?(teams|customers|users) (say|are saying)|loved by",low)) or len(s.find_all("blockquote"))>=2
    h["logo_strip"]=bool(re.search(r"trusted by|used by (teams|companies)|teams at|loved by teams",body))
    h["faq"]=bool(re.search(r"\bfaq\b|frequently asked",body)) or len(s.find_all("details"))>=3
    h["steps"]=bool(re.search(r"how it works|step 1|step one|\b01\b.{0,80}\b02\b.{0,80}\b03\b",body))
    # serif headline: any font-family declaration on h1/headings/display classes containing serif but not sans-serif
    css=" ".join(t.get_text() for t in s.find_all("style"))
    serif=False
    for m in re.finditer(r"([^{}]+)\{([^}]*)\}",css):
        sel,decl=m.group(1).lower(),m.group(2).lower()
        if re.search(r"\bh1\b|display|headline|hero|--font-(display|head|serif)",sel+decl):
            fm=re.search(r"font-family\s*:\s*([^;]+)",decl)
            if fm and SERIF.search(fm.group(1)) and not SANS.search(fm.group(1).split(",")[-1]): serif=True
        fm=re.search(r"--font-(display|head\w*|serif)\s*:\s*([^;]+)",decl)
        if fm and SERIF.search(fm.group(2)) and not SANS.search(fm.group(2).split(",")[-1]) and "h1" in css.lower(): serif=True
    h["serif_head"]=serif
    h["h1_emphasis"]=bool(h1 and h1.find(["em","i","span"]))
    return h
