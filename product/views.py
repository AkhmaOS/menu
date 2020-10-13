from rest_framework import generics

from product.models import Category
from product.serializers import CategorySerializer


class ProductByCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
