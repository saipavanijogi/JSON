import json
dic={
    "name":"sushma",
    "colour":"red",
    "age":"21",
    
}
#with open("list.json","w") as f:
 #   json.load(list,f)
    
with open("list.json","w") as f:
    json.dump(dic,f,indent=4)
