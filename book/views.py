from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, \
    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
    UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.decorators import authentication_classes, permission_classes, api_view

from .models import Book, Category
from .serializers import CategorySerializer, BookSerializer
from .permissions import SomePermission


# class CategoryGenericViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin,
#                              DestroyModelMixin, RetrieveModelMixin):
class CategoryGenericViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication, ]
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAdminUser, ]
    permission_classes = [SomePermission, ]


class BookGenericViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class CategoryCreateAPIView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryListAPIView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryUpdateAPIView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryRetrieveAPIView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryDestroyAPIView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# # ПРИМЕР ИСПОЛЬЗОВАНИЯ @api_view @authentication_classes @permission_classes
# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated, ])
# def category_list(request):
#     pass
