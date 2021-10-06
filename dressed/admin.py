from django.contrib import admin

from .models import Category, Product, Imagecollection

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name_collection', 'slug', 'image','description' ]
    prepopulated_fields = {'slug': ('name_collection',)}

@admin.register(Imagecollection)
class ImagecollectionAdmin(admin.ModelAdmin):
    list_display = ['title','collectionpresent','image']
