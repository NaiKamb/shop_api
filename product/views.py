from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductDetailSerializer, ProductListSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from review.serializers import RatingSerializer
from review.models import Rating
from rest_framework.response import Response
from rest_framework.decorators import action
from review.serializers import LikeSerializer, DislikeSerializer, FavoritsSerializer
from review.models import Like, Dislike, Favorites
from rest_framework.response import Response
import django_filters

class PermissionMixin:
    def get_permissions(self):
        if self.action in ('create','update', 'partial_update', 'destroy'):
            permissions = [IsAuthenticated]
            
        else: 
            permissions = [AllowAny]
            
        return [permission() for permission in permissions]
        # return super().get_permissions() #используем, если миксин наследуется от BasePermission

class CategoryView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price', 'in_stock']
    ordering_filter = ['category', 'price'] 
    
    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = LikeSerializer(data= request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(product=product, author=user)
                like.delete()
                message = 'Unliked'
            except Like.DoesNotExist:
                Like.objects.create(product=product, author=user)
                message = 'Liked'
            return Response(message, 200)
        
    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def dislike(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = DislikeSerializer(data= request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                dislike = Dislike.objects.get(product=product, author=user)
                dislike.delete()
                message = 'Undisliked'
            except Dislike.DoesNotExist:
                Dislike.objects.create(product=product, author=user)
                message = 'Disliked'
            return Response(message, 200)
    
        
    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def favorits(self, request, pk=None):
        product= self.get_object()
        user = request.user
        serializer = FavoritsSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                favorite = Favorites.objects.get(product=product, author = user)
                favorite.delete()
                message = 'Deleted from favorite'
            except Favorites.DoesNotExist:
                Favorites.objects.create(product=product, author = user)
                message = 'Added to favorites'
            return Response(message, 200)

     
