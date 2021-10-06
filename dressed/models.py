from django.db import models
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


