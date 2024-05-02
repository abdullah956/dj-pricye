from django.shortcuts import render
from .models import Product
def home(request) :
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})
    #request , page , {}
    #just like the controllers fucntions in laravel
def about(request) :
    return render(request,'about.html',{})