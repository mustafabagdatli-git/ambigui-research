const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1280,height:800}});fs.mkdirSync('shots120',{recursive:true});
for(const f of fs.readdirSync('G3all')){const p=await ctx.newPage();const r=JSON.parse(fs.readFileSync('G3all/'+f));
 try{await p.setContent(r.html||'',{waitUntil:'load',timeout:20000});}catch(_){} await p.waitForTimeout(600);
 await p.screenshot({path:'shots120/'+f.replace('.json','.png')});await p.close();}
await b.close()})();
