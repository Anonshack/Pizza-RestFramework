from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register("pizzas", PizzaViewSet)
router.register("categories", CategoryViewSet)
router.register("settings", SettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view())
]
