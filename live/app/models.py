from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    # verification_code = models.CharField(max_length=100, blank=True, null=True)
    last_login=models.DateTimeField(null=True,blank=True)
    # otp = models.CharField(max_length=6, blank=True, null=True)  # Add OTP field
   