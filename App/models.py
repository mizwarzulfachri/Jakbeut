from django.db import models

# Create your models here.

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    UserEmail = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)
    UserPhone = models.IntegerField()
    UserAddress = models.CharField(max_length=500)
    UserCountry = models.CharField(max_length=500)
    JoinedDate = models.DateField()
    