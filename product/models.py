from django.db import models
import uuid
from django.db import models


class Pizza(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name_uz = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)
    definition_uz = models.TextField(null=True, blank=True)
    definition_en = models.TextField(null=True, blank=True)
    definition_ru = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='bottles', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='pizzas')

    def __str__(self):
        return self.name_uz or self.name_ru or self.name_en


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name_uz = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz or self.name_ru or self.name_en


class Settings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    total = models.IntegerField(default=1)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pizza.name_uz

