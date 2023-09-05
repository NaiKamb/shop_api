from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductDetailSerializer, ProductListSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminUser]
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer
    
    # def get_permissions(self):
    #     if self.action in ['create','update', 'partial_update', 'destroy']:
    #         self.permission_classes = [IsAdminUser]
                    
    #     elif self.action in ['list', 'retrieve']:
    #         self.permission_classes = [AllowAny]
        
    #     return super().get_permissions()
     
