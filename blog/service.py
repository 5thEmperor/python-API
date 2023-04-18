from . models import *
def getprofile(data):
    data= data
    for i in data:
        print(i.get("category"))
        cat = i.get("category")
        tag = i.get("tags")
        cat_name=[]
        tag_name=[]
        for j in range(0,cat+1):
            if j ==cat:
                name= Category.objects.get(id=j).name
                cat_name.append(name)
                i["category"]= cat_name

        for k in range(0,len(tag)+1):
            if k in tag:
                name= Tag.objects.get(id=k).name
                tag_name.append(name)
                i["tags"]= tag_name

    return data
