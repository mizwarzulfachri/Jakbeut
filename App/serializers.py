from rest_framework import serializers
from App.models import User, Ceramah

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('UserID','UserName','UserEmail','UserPassword','UserPhone','UserAddress','UserCountry','JoinedDate')

class CeramahSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ceramah
        fields = ('Judul', 'Deskripsi', 'Tanggal', 'Waktu', 'Images', 'Link')