import json
dict={
    "name":"pavani",
    "age":"21",
    "topic":"json",
}
string=json.dumps(dict)
print(string)
print(type(string))
