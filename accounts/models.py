from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, password, **kwargs):
        user = self.model( is_superuser=True,  **kwargs)    
        user.password = make_password(password)    
        user.save()    
        return user
    
class Interest(models.Model):
    # user_id= models.ForeignKey(Useraccount,on_delete=models.CASCADE)
    interest = models.CharField(max_length=50)

    def __str__(self):
        return self.interest

class Useraccount(AbstractBaseUser,PermissionsMixin):
        id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
        username=models.CharField(max_length=20,null=True)
        name=models.CharField(max_length=150,null=True,blank=True)
        email = models.EmailField(unique=True,null=True,blank=True)
        password=models.CharField(max_length=150,unique=True,null=True,blank=True)
        otp=models.CharField(max_length=8,null=True,blank=True)
        is_verified=models.BooleanField(null=True,blank=True)
        created_at=models.DateTimeField(null=True,blank=True)
        is_staff=models.BooleanField(default=True,null=True,blank=True)
        user_interest = models.ForeignKey(Interest,on_delete=models.CASCADE,null=True,blank=True)

        objects = CustomUserManager()
    
        USERNAME_FIELD = 'email'
    
        def __str__(self):
            return self.email

        class Meta:
             db_table = 'Accounts'

