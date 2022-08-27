import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
with open("a.json","w") as f:
    json.dump(a,f,)
