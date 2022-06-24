from django.db import models

# Create your models here.

class Register(models.Model):
    Name=models.CharField(max_length=20)
    Seat=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)