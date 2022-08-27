# Exercise 5: Access the nested key ‘salary’ from the following JSON
import json

p = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary
# Expected Output:
# 7000
x=json.loads(p)
print(x)
print(x["company"]["employee"]["payble"]["salary"])