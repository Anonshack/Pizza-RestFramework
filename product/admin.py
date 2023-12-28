from django.contrib import admin
from .models import Pizza, Category, Settings, Order
# Register your models here.
models = [Pizza, Category, Settings, Order]
for i in models:
    admin.site.register(i)
