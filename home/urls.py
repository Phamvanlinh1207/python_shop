from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.home ),
    path('product/', views.product, name = 'product' ),
    path('productDetail/<int:id>/', views.productDetail, name = 'productDetail' ),
    path('cart/', views.cart, name='cart' )
]
