import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from App.models import User
from App.serializers import UserSerializer

# Create your views here.

@csrf_exempt
def userApi(request,id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successful",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserID = user_data["UserID"])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update Successful",safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        user = User.objects.get(UserID=id)
        user.delete()
        return JsonResponse("Delete Successful",safe=False)