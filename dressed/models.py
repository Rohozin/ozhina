from django.conf import settings
from django.db import models

from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse

from embed_video.fields import EmbedVideoField

class Category (models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name='Категорія')
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
    category = models.ForeignKey (Category,
                                    related_name='products' ,
                                    on_delete=models.CASCADE,verbose_name='Категорія')
    name_collection = models.CharField (max_length=200,
                                        unique=True,verbose_name='Найменування')
    slug = models.SlugField (max_length=200,
                                unique=True)
    image = models.ImageField (upload_to='product',
                                blank=True,verbose_name='Презентаційне зображення')
    video = EmbedVideoField (blank=True, null=True,)
    description = models.TextField (blank=True,verbose_name='Опис')
    draft = models.BooleanField (default=False, help_text= "публиковать/ скрыть")
    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now=True)
    
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
    title = models.CharField (max_length=30,verbose_name= 'Ім*я створювача,сьогоднішня дата ')
    collectionpresent = models.ForeignKey (Product, related_name = 'imagecollection', on_delete=models.CASCADE)
    image = models.ImageField (upload_to='imagecollection/',blank=True,verbose_name='Зображення ветрикального формату 16:9 або квадрат')
    draft = models.BooleanField (default=False, help_text= "публиковать/ скрыть")
    money = models.DecimalField (max_digits=10, decimal_places=2,blank=True, null=True,verbose_name='Ціна за модель')
    format_file = models.TextField (max_length=5,
                                        blank=True,verbose_name='Формат електронного документу')
    time = models.TextField (max_length=3, blank=True,verbose_name='Години консультацій за 1 модель')

    class Meta:
        ordering = ['-title']
        verbose_name = 'imagecollection'
        verbose_name_plural = 'imagecollections'

    def __str__(self):
    		return self.title

# CART
class Cart(models.Model):
	cart_id = models.CharField(max_length=250, blank=True)
	date_added = models.DateField(auto_now_add=True)
	class Meta:
		ordering = ['date_added']
		db_table = 'Cart'

	def __str__(self):
		return self.cart_id

class CartItem(models.Model):
	imagecollection = models.ForeignKey(Imagecollection, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
	quantity = models.IntegerField()
	active = models.BooleanField(default=True)

	class Meta:
		db_table = 'CartItem'

	def sub_total(self):
		return self.imagecollection.money * self.quantity

	def __str__(self):
		return self.imagecollection



class Profile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone_number = models.CharField (max_length=25,verbose_name='Контактний номер')
    city = models.TextField(max_length=100,blank=True,verbose_name='Ваше місто')
    hair = models.TextField(max_length=100,blank=True,verbose_name='Колір волосся')
    full_height = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Повний зріст')
    neck_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват шиї')                 
    chest_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват грудей')
    chest_height = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Висота грудей')
    center_chest = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Центр грудей')
    back_width = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Ширина спинки')
    shoulder_long = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Довжина плеча')
    long_sleeves = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Довжина рукава')
    arm_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват руки (плеча)')
    wrist_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват кисті')
    waist_circumference = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват талії')
    length_front_waist = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Довжина переду до талії')
    long_back_waist = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Довжина спини до талії')
    long_waist_knee = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Довжина від талії до коліна')
    hip_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват стегон')
    thigh_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват стегна')
    knee_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Обхват коліна')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Course (models.Model):
    name = models.CharField(max_length=50,verbose_name='Наіменування курсу')
    slug = models.SlugField(max_length=50,
                                unique=True)
    about = models.TextField(max_length=500,verbose_name='Опис')
    image = models.ImageField(upload_to="course",
                                blank=True,verbose_name='Презентаційне зображення')
    lessons_circle = models.DecimalField(max_digits=10, decimal_places=1,verbose_name='Занять у 1 курсі')
    #Цыклы занятий
    circle = models.DecimalField(max_digits=10, decimal_places=1,verbose_name='Кількість курсів')
    #Количество часов
    time = models.TextField(max_length=51,verbose_name='Годин на 1 день')
    online = models.TextField(max_length=10,
                                        blank=True,verbose_name='Онлайн')
    alive = models.TextField(max_length=10,
                                        blank=True,verbose_name='Зустрічи')

    class Meta:   
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def get_url(self):
        return reverse('course_list', args=[self.slug])

    def __str__(self):
    		return self.name
    
