from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home' ),
    path('product/', views.product, name = 'product' ),
    path('product-Detail/<slug:slug>/<int:id>', views.productDetail, name = 'productDetail' ),
    path('cart/', views.cart, name='cart' ),
    path( 'login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path( 'logout/',auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('register/', views.register, name='register' )
]
