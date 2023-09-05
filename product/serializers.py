from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'title', 'image', 'price', 'in_stock']
        
class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'