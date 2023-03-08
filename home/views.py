from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from . models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    productList = Product.objects.all()
    categoryList = Category.objects.all()
    return render (request, 'pages/index.html',{'productList':productList, 'categoryList':categoryList})

def product(request):
    categoryList = Category.objects.all()

    # filter
    ATOZ = request.GET.get('ATOZ')
    # search
    if 'name' in request.GET:
        name = request.GET['name']
        productList = Product.objects.filter( name = name )
    else:
        productList = Product.objects.all()
        # number
        product_paginator = Paginator(productList, 9)

        # page
        page_num = request.GET.get('page')

        productList = product_paginator.get_page(page_num)


    context = {
        # 'count' :  product_paginator.count,
        'productList' : productList,
        'categoryList' : categoryList
    }
    return render (request, 'pages/product.html', context)

def categoryView(request, slug):
    categoryList = Category.objects.all()
    # filter Category
    if Category:
        productList = Product.objects.filter(category_id = slug).order_by('slug')
        context = {'productList': productList,'categoryList':categoryList}
        return render (request, 'pages/product.html', context)
    else:
        productList = Product.objects.all()
    context = {'productList': productList,'categoryList':categoryList}
    return render (request, 'pages/product.html', context)
    

def productDetail(request, slug,id):
    product = Product.objects.get(slug = slug, id = id)
    return render (request, 'pages/productDetail.html', {'product':product})

@login_required
def cart(request):
    order_id = 6
    order  = Order.objects.filter(is_paid = False, user = request.user, id = order_id)
    order_details = OrderDetail.objects.filter(order_id=order_id)
    context = {'order':order, 'order_details':order_details }
    return render (request, 'pages/cart.html', context)

def login(request):
    return render (request, 'pages/login.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login/')
    return render (request, 'pages/register.html',{'form': form})

def remove_cart(request, id):
    try:
        order_detail = OrderDetail.objects.get(id = id)
        order_detail.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_to_cart(request , id):
    product = Product.objects.get(id = id)
    user = request.user
    order , _ = Order.objects.get_or_create(user = user, is_paid = False)

    order_details = OrderDetail.objects.create(order = order, product = product)

    

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))