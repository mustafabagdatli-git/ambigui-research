import os,json,time,urllib.request,threading
KEY=os.environ['OPENROUTER_API_KEY']; LOCK=threading.Lock(); COST=[0.0]
LOG=open('calls.jsonl','a')
def chat(model,messages,max_tokens=24000,temperature=1.0,tries=4):
    body={"model":model,"messages":messages,"max_tokens":max_tokens,"temperature":temperature,"usage":{"include":True}}
    if "glm" in model or "deepseek" in model: body["reasoning"]={"max_tokens":4000}
    for t in range(tries):
        try:
            req=urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",data=json.dumps(body).encode(),
              headers={"Authorization":"Bearer "+KEY,"Content-Type":"application/json"})
            r=json.load(urllib.request.urlopen(req,timeout=600))
            ch=r['choices'][0]; c=r.get('usage',{}).get('cost',0) or 0
            with LOCK:
                COST[0]+=c; LOG.write(json.dumps({"model":model,"finish":ch.get('finish_reason'),"usage":r.get('usage')})+"\n"); LOG.flush()
            return ch['message'].get('content') or "", ch.get('finish_reason')
        except Exception as e:
            err=str(e); time.sleep(4*(t+1))
    return "", "error:"+err
