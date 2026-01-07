from django.contrib import admin
from .models import Vendor, Item, Order

admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Order)