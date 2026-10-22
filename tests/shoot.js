const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:2000}});
 const ids=JSON.parse(fs.readFileSync('C/targets.json'));
 for(const id of ids){const r=JSON.parse(fs.readFileSync('A/'+id+'.json'));
  await p.setContent(r.html,{waitUntil:'load',timeout:20000}).catch(()=>{});await p.waitForTimeout(400);
  await p.screenshot({path:'C/'+id+'.jpg',type:'jpeg',quality:70});}
 await b.close()})();
