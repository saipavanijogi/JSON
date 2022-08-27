# Access the value of key2 from the following JSON
# import json
# sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2
# Expected Output:
# value2

import json
samplejson = """{"key1": "value1", "key2": "value2"}"""
f=json.loads(samplejson)
# for i in f:
#     x=f["key2"]
# print(x)
print(f['key2'])