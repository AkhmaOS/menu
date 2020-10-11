from django.db import models


class Product(models.Model):
    title = models.CharField('товар', max_length=256)
    description = models.TextField('описание товара')
    price = models.CharField('цена', max_length=256)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Категория', max_length=256)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField('название', max_length=256)
    image = models.ImageField('изображение', upload_to='product/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')

    def __str__(self):
        return self.title
