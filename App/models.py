from django.db import models

# Create your models here.

class User(models.Model): 
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    UserEmail = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)
    UserPhone = models.IntegerField(null=True)
    UserAddress = models.CharField(max_length=500)
    UserCountry = models.CharField(max_length=500)
    JoinedDate = models.DateField()

    def _str_(self):
        return self.UserName
    
class Ceramah(models.Model):
    Judul = models.CharField(max_length=100)
    Deskripsi = models.CharField(max_length=800)
    Tanggal = models.DateField(null=False)
    Waktu = models.TimeField(null=False)
    Images = models.ImageField(upload_to = 'static/images/')
    Link = models.URLField()

    def _str_(self):
        return self.Judul