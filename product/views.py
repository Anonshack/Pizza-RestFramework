from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import (
    Pizza,
    Order,
    Settings,
    Category,
)
from django_filters import (
    FilterSet,
    DateFilter,
    NumberFilter,
)
from .serializers import (
    PizzaSerializer,
    CategorySerializer,
    SettingsSerializer,
    OrderSerializer,
)


class OrderFilter(FilterSet):
    min_price = NumberFilter(field_name="total_price", lookup_expr="gte")
    max_price = NumberFilter(field_name="total_price", lookup_expr="lte")
    start_date = DateFilter(field_name="created", lookup_expr="gte")
    end_date = DateFilter(field_name="created", lookup_expr="lte")


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all().order_by('created')
    serializer_class = PizzaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name_uz', 'definition_uz']
    ordering_fields = ['name_uz', 'definition_uz', 'price']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('created')
    serializer_class = CategorySerializer


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ['phone']
    ordering_fields = ['created']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
