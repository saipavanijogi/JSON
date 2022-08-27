import json
a={
 "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
user=input("enter the name"":")
user1=int(input("enter the number"))
for i in a:
    if a[i][user]==a[i][user]:
        c=a[i][user]
        e=int(c)
        s=e-user1
        d={}
        dic={}
    for key in a :
        for value in a[key]:
            d[value]=a[key][value]
            if value==user:
                d[value]=s
                dic[key]=d
# print(dic)
with open("pavani.json","w")as f:
    json.dump(dic,f,indent=4)
# file = open("pavani.json", "w")
# json.dump(dic, file, indent = 6)
# file.close()
   
    
    


                    
                
                
                
            
            
        
        
        
    
    
    