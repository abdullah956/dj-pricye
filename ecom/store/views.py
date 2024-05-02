from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def home(request) :
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})
    #request , page , {}
    #just like the controllers fucntions in laravel
def about(request) :
    return render(request,'about.html',{})
def login_user(request) :
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user :
            login(request,user)
            messages.success(request,("You have been Logged in!"))
            return redirect('home')
        else:
            messages.success(request,("Error Try Again!"))
            return redirect('login')
    else :
        return render(request,'login.html',{})
def logout_user(request) :
    logout(request)
    messages.success(request,("You have been Logged out!"))
    return redirect('home')