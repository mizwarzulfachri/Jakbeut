from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        #print(Username, Password)

        user = authenticate(request, username=Username, password=Password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Invalid username or password"))
            return redirect('view_login')
    else:
        return render(request, 'accounts/login.html', {})

def logout_view(request):
    return render(request, 'accounts/logout.html', {})

def register_view(request):
    return render(request, 'accounts/register.html', {})