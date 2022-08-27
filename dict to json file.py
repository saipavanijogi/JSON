# import json
# my={
#     "name":"pavani",
#     "age ":"21",
#     "occuption":"student",
#     }
# a=json.dumps(my)
# with open ("my_.json","w") as f:
#     f.write(a)
#     f.close()
    

a=[1,2,3,4,5]
dic={}
# o/p {0:1,1:2,2:3,3:4,4:5}
dic={}
for i in range (0,len(a)):
    dic[i]=a[i]
print(dic)