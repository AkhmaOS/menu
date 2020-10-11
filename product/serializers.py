from django.http import request
from rest_framework import serializers

from product.models import Product, Image, Category


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['title', 'image']


class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'image']


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_product')

    class Meta:
        model = Category
        fields = ['id', 'title', 'products']

    def get_product(self, category):
        qs = Product.objects.filter(is_active=True, category=category)
        serializer = ProductSerializer(instance=qs, many=True)
        return serializer.data
