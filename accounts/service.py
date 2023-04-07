from .models import Useraccount
from django.db.models import Q

def user_exist(email):
    email_c=Useraccount.objects.filter(Q(email=email))
    print("email_c -----------",email_c)
    if len(email_c) == 0 :
        return False
    else:
        return True   

def user_validation(email,password):
    email=email
    obj=Useraccount.objects.filter(Q(email=email) & Q(password=password)).values()
    # user= Useraccount.objects.filter(email=email).values_list('is_verified')
    if len(obj)==0:
        return False
    else:
        # if user[0][0] == True:
            return True
        

def user_verification(email):
    user= Useraccount.objects.filter(email=email).values_list('is_verified')
    if user[0][0] == True:
        return True
    else:
        return False
    
def getintrest(data,intrest):
    data=data
    intrest= intrest

    print("----------------- its data ",data)
    print("----------------- its interest ",intrest)
    # for i in data:
    #     print(i.get("intrest"))