from django.contrib import admin

from .models import Category, Product, Imagecollection, Profile

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

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number','city','full_height','neck_girth','chest_girth','chest_height','center_chest','back_width','shoulder_long','long_sleeves','arm_girth','wrist_girth','waist_circumference','length_front_waist','long_back_waist','long_waist_knee','hip_girth','thigh_girth','knee_girth']
