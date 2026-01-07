from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Item(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/', null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # This handles the "State will Change" from your Update sheet
    status = models.CharField(max_length=50, default='Pending') 
    # This handles the "Cash/UPI" from your Checkout sheet
    payment_method = models.CharField(max_length=20) 
    created_at = models.DateTimeField(auto_now_add=True)