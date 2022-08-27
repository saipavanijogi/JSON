import json
a={
    "name":"pavani",
    "age":"21",
    "topic":"json",
}
with open("eqn2.json","w") as f:
    json.dump(a,f ,indent=4)
