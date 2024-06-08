from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from shop.serializers import CategorySerializer, ProductSerializer, ProductImageSerializer
from shop.models import Category, Product, ProductImage


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

    filter_fields = (
        'name', 
    )
    search_fields = (
        '^name', 
    )


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'

    filter_fields = (
        'name', 
    )
    search_fields = (
        '^name', 
    )


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'


class ProductImageList(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    name = 'productimage-list'
    
    filter_fields = (
        'label', 
    )
    search_fields = (
        '^label', 
    )

class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    name = 'productimage-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'categories': reverse(CategoryList.name, request=request),
                'products': reverse(ProductList.name, request=request),
                'product-images': reverse(ProductImageList.name, request=request),

            }
        )
