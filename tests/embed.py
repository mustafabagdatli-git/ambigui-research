import os,json,numpy as np,torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModel
import open_clip
torch.set_num_threads(4)
fs=sorted(os.listdir('shots120'));ims=[Image.open('shots120/'+f).convert('RGB') for f in fs]
ctrl=[Image.open(f'CTRLshots/{c}.jpg').convert('RGB') for c in ('pos','neg','dark')]
dp=AutoImageProcessor.from_pretrained("facebook/dinov2-small");dm=AutoModel.from_pretrained("facebook/dinov2-small").eval()
cm,_,cpre=open_clip.create_model_and_transforms("ViT-B-32",pretrained="laion2b_s34b_b79k");cm.eval()
def dino(xs):
    out=[]
    for i in range(0,len(xs),8):
        with torch.no_grad(): o=dm(**dp(images=xs[i:i+8],do_center_crop=False,size={"height":224,"width":350},return_tensors="pt"))
        out.append(o.last_hidden_state[:,0])
    return torch.cat(out).numpy()
def clip(xs):
    with torch.no_grad(): return torch.cat([cm.encode_image(torch.stack([cpre(x.resize((224,224),Image.BICUBIC)) for x in xs[i:i+16]])) for i in range(0,len(xs),16)]).numpy()
E={"files":fs}
for name,fn in (("dino",dino),("clip",clip)):
    e=fn(ims+ctrl);e=e/np.linalg.norm(e,axis=1,keepdims=True);E[name]=e.tolist();print(name,e.shape)
print(dp(images=ims[:1],do_center_crop=False,size={'height':224,'width':350},return_tensors='pt')['pixel_values'].shape)
json.dump(E,open('emb120.json','w'))
