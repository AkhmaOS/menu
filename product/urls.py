from django.urls import path

from product.views import ProductByCategoryView

urlpatterns = [
    path('products/', ProductByCategoryView.as_view(), name='product-serializers'),
]