from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from . models import *


# Create your views here.
def home(request):
    return render (request, 'pages/index.html')

def product(request):
    if 'name' in request.GET:
        name = request.GET['name']
        productList = Product.objects.filter(name=name)
    else:
        productList = Product.objects.all()
    categoryList = Category.objects.all()
    return render (request, 'pages/product.html', {'productList':productList, 'categoryList':categoryList})

def productDetail(request, slug,id):
    product = Product.objects.get(slug = slug, id = id)
    return render (request, 'pages/productDetail.html', {'product':product})

def cart(request):
    return render (request, 'pages/cart.html')

def login(request):
    return render (request, 'pages/login.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render (request, 'pages/register.html',{'form': form})