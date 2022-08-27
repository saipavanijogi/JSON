# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

# samplejson = {"key1": "value1", "key2": "value2"}
# Expected Output:

# {
#  "key1" = "value2",
#  "key2" = "value2",
#  "key3" = "value3"
# }
import json
s = {"key1": "value1", "key2": "value2"}
s['key3']='value3'
print(json.dumps(s, indent=4, separators=(". ", " = ")))
