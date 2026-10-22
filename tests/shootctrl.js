const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1280,height:800}});fs.mkdirSync('CTRLshots',{recursive:true});
for(const f of fs.readdirSync('CTRL')){const p=await ctx.newPage();const r=JSON.parse(fs.readFileSync('CTRL/'+f));await p.setContent(r.html,{waitUntil:'load'});await p.waitForTimeout(300);
await p.screenshot({path:'CTRLshots/'+f.replace('.json','.jpg'),type:'jpeg',quality:72});await p.close()}await b.close()})();
