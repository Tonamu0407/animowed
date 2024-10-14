from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
	return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Invalid email or password.")   
    return render(request, 'login.html')

def signup(request):
	return render(request,'signup.html')

def oshi(request):
	return render(request,'oshi.html')

def hxh(request):
	return render(request,'hxh.html')

def eva(request):
	return render(request,'eva.html')

def stone(request):
	return render(request,'stone.html')

def note(request):
	return render(request,'note.html')