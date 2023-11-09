from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Product
from .serializer import ProductSerializer
from .permission import IsOwnerOrAuthor
from django_filters.rest_framework import DjangoFilterBackend


class StandartPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandartPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', )
    filterset_fields = ('category', )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [IsAuthenticated(), IsOwnerOrAuthor()]
        return [IsAuthenticatedOrReadOnly(), ]
