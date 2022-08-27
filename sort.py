# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys

import json
s= {"id" : 1, "name" : "value2", "age" : 29}
# Expected Output:

# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }
a=json.dumps(s,sort_keys=True,indent=4)
print(a)
