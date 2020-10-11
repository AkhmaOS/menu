from rest_framework import generics

from product.models import Product, Image, Category
from product.serializers import ProductSerializer, CategorySerializer


class ProductByCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(products__is_active=True)
