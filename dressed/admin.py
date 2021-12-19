from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from embed_video.admin import AdminVideoMixin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['name', 'video', 'about']


@admin.register(Product)
class ProductAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['id','category', 'name_collection', 'slug', 'miniimage','video','description','time','draft' ]
    prepopulated_fields = {'slug': ('name_collection',)}

    def miniimage(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=90")
    miniimage.__name__ = "Міні-зображення"

@admin.register(Imagecollection)
class ImagecollectionAdmin(admin.ModelAdmin):
    list_display = ['id','title','collectionpresent','miniimage', 'video', 'money','draft','created','updated']

    def miniimage(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=90")
    miniimage.__name__ = "Міні-зображення"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','slug','about','money','image','online','alive']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Imagecourse)
class Imagecourse(admin.ModelAdmin):
    list_display = ['id','miniimage','course','created']

    def miniimage(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=90")
    miniimage.__name__ = "Міні-зображення"
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','full_height','neck_girth','chest_girth','chest_height','center_chest','back_width','shoulder_long','long_sleeves','arm_girth','wrist_girth','waist_circumference','length_front_waist','long_back_waist','long_waist_knee','hip_girth','thigh_girth','knee_girth']

@admin.register(CollectionUser)
class CollectionUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'clothingparameters', 'order', 'miniimage', 'video', 'ordernumber', 'material', 'document', 'created']

    def miniimage(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=90")
    miniimage.__name__ = "Міні-зображення"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone_number','massege', 'miniimage','cat','agreement']

    def miniimage(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=90")
    miniimage.__name__ = "Міні-зображення"

@admin.register(OrderTeach)
class FormTeachAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number','massege','created','course','agreement']
