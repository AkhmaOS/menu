from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from product.models import Product, Image, Category


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    fields = ('title', 'image', 'image_preview',)
    readonly_fields = ['image_preview', ]

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )
    image_preview.short_description = 'Изображение (просмотр)'



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'image_preview',)
    readonly_fields = ['image_preview', ]

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )

    image_preview.short_description = 'Изображение (просмотр)'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
