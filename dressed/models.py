from django.contrib.auth.models import User
from django.db import models

from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Category (models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
            
            ordering = ('name',)
            verbose_name = 'category'
            verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name



class Product (models.Model):
    category = models.ForeignKey(Category,
                                    related_name='products' ,
                                    on_delete=models.CASCADE)
    name_collection = models.CharField(max_length=200,
                                        unique=True)
    slug = models.SlugField(max_length=200,
                                unique=True)
    image = models.ImageField(upload_to='product',
                                blank=True)
    description = models.TextField(blank=True)
    draft = models.BooleanField (default=False, help_text= "публиковать/ скрыть")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.TextField(max_length=7,
                                        unique=True)
    format_file = models.TextField(max_length=5,
                                        blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name_collection', )
        index_together = (('id', 'slug'),)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
    		return self.name_collection


class Imagecollection (models.Model):
    title = models.CharField (max_length=30)
    collectionpresent = models.ForeignKey (Product, related_name = 'imagecollection', on_delete=models.CASCADE)
    image = models.ImageField (upload_to='imagecollection/',blank=True)
    draft = models.BooleanField (default=False, help_text= "публиковать/ скрыть")

    class Meta:
        ordering = ['-title']
        verbose_name = 'imagecollection'
        verbose_name_plural = 'imagecollections'

    def __str__(self):
    		return self.title

class Profile (models.Model):
    user = models.OneToOneField(User,blank=True,on_delete=models.CASCADE)
    phone_number = models.CharField (max_length=25)
    city = models.TextField(max_length=100,blank=True)
    full_height = models.DecimalField(max_digits=10, decimal_places=2, help_text= "полный рост")
    neck_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват шеи")                 
    chest_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват груди")
    chest_height = models.DecimalField(max_digits=10, decimal_places=2, help_text= "высота груди")
    center_chest = models.DecimalField(max_digits=10, decimal_places=2, help_text= "центр груди")
    back_width = models.DecimalField(max_digits=10, decimal_places=2, help_text= "ширина спинки")
    shoulder_long = models.DecimalField(max_digits=10, decimal_places=2, help_text= "длина плеча")
    long_sleeves = models.DecimalField(max_digits=10, decimal_places=2, help_text= "длинна рукава")
    arm_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват руки (плеча)")
    wrist_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват кисти")
    waist_circumference = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват талии")
    length_front_waist = models.DecimalField(max_digits=10, decimal_places=2, help_text= "длинна переда до талии")
    long_back_waist = models.DecimalField(max_digits=10, decimal_places=2, help_text= "длинна спины к талии")
    long_waist_knee = models.DecimalField(max_digits=10, decimal_places=2, help_text= "длинна от талии до колена")
    hip_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват бедер")
    thigh_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват бедра")
    knee_girth = models.DecimalField(max_digits=10, decimal_places=2, help_text= "обхват колена")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Course (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,
                                unique=True)
    about = models.TextField(max_length=500)
    image = models.ImageField(upload_to="course",
                                blank=True)
    lessons_circle = models.DecimalField(max_digits=10, decimal_places=1)
    #Цыклы занятий
    circle = models.DecimalField(max_digits=10, decimal_places=1)
    #Количество часов
    time = models.TextField(max_length=51)
    online = models.TextField(max_length=10,
                                        blank=True)
    alive = models.TextField(max_length=10,
                                        blank=True)

    class Meta:   
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def get_url(self):
        return reverse('course_list', args=[self.slug])

    def __str__(self):
    		return self.name
    
