from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny
from .models import Post,User
from .serializers import PostSerializers, CreateNewUser
from .permissions import IsUserOrReadOnly



class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsUserOrReadOnly,)


class PostDestroy(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsUserOrReadOnly,IsAdminUser)


class User(generics.CreateAPIView):
    queryset = User.objects.all
    serializer_class = CreateNewUser
    permission_classes = (AllowAny,)