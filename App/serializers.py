from rest_framework import serializers
from App.models import User

class UserSerializer(serializers.ModelSerializer):
    class User:
        models = User
        fields = ('UserID','UserName','UserEmail','UserPassword','UserPhone','UserAddress','UserCountry','JoinedDate')