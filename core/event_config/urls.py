from django.contrib import admin
from django.urls import path, include # <--- 1. Check this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # <--- 2. Check this line
]