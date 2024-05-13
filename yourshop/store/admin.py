from django.contrib import admin
from .models import Banners, Products, Orders, Categorys, ProductImage, Sizes

@admin.register(Banners)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'active',
        'image',
        'link',
    )

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # количество дополнительных пустых форм для загрузки изображений

@admin.register(Sizes)
class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'size',
    )

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'category',
    )
    filter_horizontal = ('sizes',)

    inlines = [ProductImageInline]  # добавляем встраиваемый класс для загрузки изображений

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'products',
        'quantity',
        'total_price',
        'status',
        'created_at',
    )

@admin.register(Categorys)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'image',
        'main_image'
    )
