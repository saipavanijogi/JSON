
import json
dic={}
with open("abhi.txt") as file:
    for i in file :
        key,desc=i.strip().split(None,1)
    
        dic[key]=desc.strip()
with open("sush.json","w")as f:
    json.dump(dic,f,indent=6)   
        
