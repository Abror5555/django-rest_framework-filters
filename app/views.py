from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from app.models import Post
from app.serialzers import PostSerializers

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','about']