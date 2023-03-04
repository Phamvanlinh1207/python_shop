from django.shortcuts import render
from django.http import HttpResponse

from . models import *


# Create your views here.
def home(request):
    return render (request, 'pages/index.html')

def product(request):
    productList = Product.objects.all()
    return render (request, 'pages/product.html', {'productList':productList})

def productDetail(request, id):
    product = Product.objects.get(id = id)
    return render (request, 'pages/productDetail.html', {'product':product})

def cart(request):
    return render (request, 'pages/cart.html')