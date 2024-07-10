from rest_framework import serializers
from ..models import Category, Product

class ProductSerializer(serializers.Serializer):
    
    class Meta: 
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.Serializer):
    product = ProductSerializer(many = True, read_only = True)
    class Meta:
        model = Category
        fields = "__all__"


