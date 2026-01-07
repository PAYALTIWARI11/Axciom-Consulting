from django.shortcuts import render, redirect
from .models import Item, Order

def portal(request):
    items = Item.objects.all()
    return render(request, 'portal.html', {'items': items})

def view_cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def order_status(request):
    orders = Order.objects.all()
    return render(request, 'order_status.html', {'orders': orders})

