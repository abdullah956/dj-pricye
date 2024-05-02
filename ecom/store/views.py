from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

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


def register_user(request):
	form = SignUpForm() #form object from views
	if request.method == "POST": # if they actually filled form
		form = SignUpForm(request.POST) # add the data
		if form.is_valid(): # if form field are filled correctly
			form.save() #save
			username = form.cleaned_data['username'] #clean
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You Have Registered Successfully!"))
			return redirect('home')
		else: #if the form data is not filled correctly
			messages.success(request, ("Error Try Again!"))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})
