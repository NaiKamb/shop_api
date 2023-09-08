from django.shortcuts import render
from .models import Like, Dislike, Comment, Rating
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import CommentSerializer, RatingSerializer #, LikeSerializer
from rest_framework.response import Response
from rest_framework.permissions import  AllowAny, IsAuthenticated
from .permissions import IsAuthorOrReadonly

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ('update', 'partial_update', 'destroy'):
            permissions = [IsAuthorOrReadonly]    
        else: 
            permissions = [AllowAny]
            
        return [permission() for permission in permissions]

class CommentView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class RatingView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = RatingSerializer
    
    
