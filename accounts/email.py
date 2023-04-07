from django.core.mail import send_mail
import random
from django .conf import settings
from .models import Useraccount

def send_otp(email):
    subject='Your account verification email'
    otp=random.randint(1000,9999)
    message=f'Your Otp is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj=Useraccount.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save()