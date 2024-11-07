from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cus_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def cus_logout(request):
    logout(request)
    return redirect('/')

def products(request):

    products = Product.objects.all()
    return render(request, 'shop.html',{'products':products})

def shop_detail(request):
    return render(request, 'shop-detail.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')

def testimonial(request):
    return render(request,'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
