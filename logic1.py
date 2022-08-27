# Convert the following dictionary into JSON format
# Expected Output:{"key1" : "value1", "key2" : "value2"}

import json
x= {
    "key1" : "value1", 
    "key2" : "value2",
}
# out_file=open("output.json","w")
print(json.dumps(x))


