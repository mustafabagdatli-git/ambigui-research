// Rendered checker: visual habits read from the page as drawn (computed style, geometry, pixels). Deterministic.
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');
const SERIF=/(serif|georgia|times|garamond|baskerville|playfair|fraunces|newsreader|instrument serif|dm serif|lora|merriweather|cormorant|crimson|spectral|literata|bodoni|didot|caslon|recoleta|tiempos|canela|domaine|libre caslon|source serif|pt serif|noto serif|charter|iowan|cambria|palatino|book antiqua|young serif|gelasio|bitter|zilla|roboto serif|ibm plex serif|eb garamond|cardo|vollkorn|alegreya(?! sans)|petrona|fraunces)/i;
async function check(page){return page.evaluate(()=>{
  const h1=document.querySelector('h1');const vw=innerWidth,vh=innerHeight;const out={has_h1:!!h1};
  if(!h1)return out;
  const cs=getComputedStyle(h1), r=h1.getBoundingClientRect();
  out.h1font=cs.fontFamily; out.h1size=parseFloat(cs.fontSize);
  // V2 set-apart word
  const kids=[...h1.querySelectorAll('*')].filter(k=>k.textContent.trim().length>0&&k.textContent.trim().length<0.75*h1.textContent.trim().length);
  out.V2=kids.some(k=>{const c=getComputedStyle(k);return c.fontStyle==='italic'||c.color!==cs.color||c.fontFamily!==cs.fontFamily||(c.backgroundImage!=='none'&&/gradient/.test(c.backgroundImage));});
  // V3 label above: nearest text element just above the h1, small, caps or letter-spaced
  let best=null;
  for(const el of document.querySelectorAll('body *')){if(el===h1||el.contains(h1)||h1.contains(el))continue;
    const t=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim(); if(t.length<2||t.length>70)continue;
    const b=el.getBoundingClientRect(); if(b.height===0||b.width===0)continue;
    const gap=r.top-b.bottom; if(gap<-4||gap>90)continue; if(b.right<r.left-20||b.left>r.right)continue;
    const c=getComputedStyle(el), fsz=parseFloat(c.fontSize); if(fsz>0.55*out.h1size)continue;
    const caps=c.textTransform==='uppercase'||(t===t.toUpperCase()&&/[A-Z]/.test(t)), ls=parseFloat(c.letterSpacing)||0;
    const pill=(c.borderRadius&&parseFloat(c.borderRadius)>8&&c.backgroundColor!=='rgba(0, 0, 0, 0)');
    if(caps||ls>0.4||pill){if(!best||gap<best.gap)best={gap,t};}}
  out.V3=!!best; out.V3t=best?best.t:'';
  // V4 copy left, visual right in the first screen
  const cx=(r.left+r.right)/2; let vis=false;
  if(cx<vw*0.55&&r.top<vh){for(const el of document.querySelectorAll('body *')){if(el.contains(h1)||h1.contains(el))continue;
      const b=el.getBoundingClientRect(); if(b.width*b.height<0.08*vw*vh)continue; if(b.left<r.right-40||b.left<vw*0.4)continue;
      if(b.top>r.bottom+250||b.bottom<r.top-250||b.top>vh)continue; vis=true;break;}}
  out.V4=vis; return out;});}
(async()=>{const dir=process.argv[2], out=process.argv[3];const files=fs.readdirSync(dir).filter(f=>f.endsWith('.json'));
  const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1280,height:800}});const res={};
  for(const f of files){const p=await ctx.newPage();const r=JSON.parse(fs.readFileSync(path.join(dir,f)));
    try{await p.setContent(r.html||'',{waitUntil:'load',timeout:20000});}catch(_){}
    await p.waitForTimeout(500);let o={};try{o=await check(p);}catch(e){o={err:String(e)}}
    // V1 serif from the font stack
    if(o.h1font){const fams=o.h1font.split(',').map(x=>x.trim().replace(/["']/g,'').toLowerCase());const gen=fams.find(x=>x==='serif'||x==='sans-serif'||x==='monospace'||x==='system-ui');
      o.V1=gen==='serif'||(!gen&&SERIF.test(fams[0]))||(gen!=='sans-serif'&&gen!=='system-ui'&&SERIF.test(fams[0]));if(gen==='sans-serif'||gen==='system-ui')o.V1=false;}
    // V5 warm paper: sample background pixels along the left margin of the first screen
    try{const buf=await p.screenshot({type:'png'});const png=await p.evaluate(async b64=>{const im=new Image();im.src='data:image/png;base64,'+b64;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);
        const px=[];for(const y of [120,300,500,700])for(const x of [8,20,1260]){const d=g.getImageData(x,y,1,1).data;px.push([d[0],d[1],d[2]]);}return px;},buf.toString('base64'));
      const key=c=>c.join(','), cnt={};png.forEach(c=>cnt[key(c)]=(cnt[key(c)]||0)+1);const mode=Object.entries(cnt).sort((a,b)=>b[1]-a[1])[0][0].split(',').map(Number);
      const [R,G,B]=mode.map(v=>v/255),mx=Math.max(R,G,B),mn=Math.min(R,G,B),L=(mx+mn)/2,S=mx===mn?0:(L>0.5?(mx-mn)/(2-mx-mn):(mx-mn)/(mx+mn));
      let H=0;if(mx!==mn){H=mx===R?((G-B)/(mx-mn))%6:mx===G?(B-R)/(mx-mn)+2:(R-G)/(mx-mn)+4;H*=60;if(H<0)H+=360;}
      o.bg=mode;o.V5=L>0.82&&H>=25&&H<=60&&S>=0.12&&!(mode.every(v=>v>=250));}catch(e){o.V5err=String(e)}
    res[f]=o;await p.close();}
  fs.writeFileSync(out,JSON.stringify(res,null,1));await b.close();
  const keys=['V1','V2','V3','V4','V5'];const n=Object.keys(res).length;console.log(n,'pages');keys.forEach(k=>console.log(k,Object.values(res).filter(o=>o[k]).length));})();
