from django.urls import path
from .views import ProductListCreate, CustomerListCreate, OrderListCreate

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
]