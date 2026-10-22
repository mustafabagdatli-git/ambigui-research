const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const key=JSON.parse(fs.readFileSync('LABEL_KEY.json'));const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1280,height:800}});
for(const [id,f] of Object.entries(key)){const p=await ctx.newPage();const r=JSON.parse(fs.readFileSync('G3all/'+f));
 try{await p.setContent(r.html,{waitUntil:'load',timeout:20000});}catch(_){} await p.waitForTimeout(800);
 await p.screenshot({path:'../label/shots/'+id+'.jpg',type:'jpeg',quality:72});await p.close();}
await b.close()})();
