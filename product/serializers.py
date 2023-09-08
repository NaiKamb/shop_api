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
        
    def validate_price(self, price): #валидация всегда создается в сериализаторах
        if price <=0:
            raise ValidationError('Стоимость не может быть 0 или меньше')
        return price