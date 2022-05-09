from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# from django.http import HttpResponse
from .models import User


def index(request):
    return render(request, 'index.html')

def login(request):
    login = User.objects.all()
    context = {
        'title': 'User Login',
        'login': login,
    }
    return render(request, 'login.html', context)


#def detail_blog(request, slug):
    # detail = Blog.objects.filter(slug=slug).first()
    # context = {
        # 'title': detail.title,
        # 'detail': detail,
    # }
    # return render(request, 'blog/detail.html', context)
