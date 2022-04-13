from django.urls import path
from App import views

urlspatterns=[
    path('user/',views.userApi),
    path('user/<int:id>/',views.userApi)
]