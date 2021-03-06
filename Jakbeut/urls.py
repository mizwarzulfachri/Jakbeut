"""Jakbeut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App.views import (
    index, 
    ceramah, 
    tambah_ceramah 
)
from accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ceramah/', ceramah, name='view_ceramah'),
    path('ceramah/tambah/', tambah_ceramah, name='tambah_ceramah'),
    path('home/', index, name='home'),
    path('login/', login_view, name='view_login'),
]
