from . models import *
def getprofile(data):
    data= data
    for i in data:
        print(i.get("category"))
        cat = i.get("category")
       
        cat_name=[]
       
        for j in range(0,cat+1):
            if j ==cat:
                name= Category.objects.get(id=j).name
                cat_name.append(name)
                i["category"]= cat_name   

                                        
     
    return data
