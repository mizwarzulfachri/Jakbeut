from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

from App.models import User, Ceramah
from App.forms import FormCeramah
from App.serializers import UserSerializer, CeramahSerializer

def index(request):
    return render(request, 'index.html')

def ceramah(request):
    ceramah = Ceramah.objects.all()
    context = {
        'ceramah': ceramah,
    }
    return render(request, 'ceramah.html', context)

def tambah_ceramah(request, *args, **kwargs):
    if request.POST:
        form = FormCeramah(request.POST, request.FILES)
        for field in form:
            print("Field Error: ", field.name, field.errors)
        print(request.FILES)
        if form.is_valid():
            form.save()
            form = FormCeramah()
            pesan = "Data disimpan berhasil"

            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah_ceramah.html', context)
        else:
            form = FormCeramah()
            pesan = "Gagal disimpan"
            context = {
                'form': form,
                'pesan': pesan,
            }
    else:
        form = FormCeramah()
        

        context = {
            'form': form,
        }
    return render(request, 'tambah_ceramah.html', context)