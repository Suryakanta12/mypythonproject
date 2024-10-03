from rest_framework import serializers,viewsets
from .models import Product, Customer, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'
