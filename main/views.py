from django.shortcuts import render
from rest_framework .generics import ListAPIView

#TODO: список категорий
#TODO: КРАД постов
#TODO: картинки в постах
#TODO: комменты
#TODO: подключить Твилио
#TODO: авторизация
#TODO: избранное, лайки
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.models import Category, Post, Comment
from main.permissions import IsAuthor
from main.serializers import CategorySerializer, PostSerializer, PostListSerializer, CommentSerializer


class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = PostListSerializer
        return serializer_class

    def get_permissions(self):
        #создавать пост может залогиненый юзер
        if self.action == 'create':
            return [IsAuthenticated()]
        #изменять или удалять только автор
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]

        #просматривать мгут все

        pass


class CommentViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


