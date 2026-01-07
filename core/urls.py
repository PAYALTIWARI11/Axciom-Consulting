from django.urls import path
from . import views # <--- This dots refers to your views.py

urlpatterns = [
    path('', views.portal, name='portal'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('status/', views.order_status, name='order_status'),
]