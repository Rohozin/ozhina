from django.conf import settings
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


class Category (models.Model):
    name = models.CharField(max_length=100,
                                db_index=True,
                                verbose_name='Category'
                                )
    slug = models.SlugField(max_length=100,
                                unique=True
                                ) 
    class Meta:
            
            ordering = ('name',)
            verbose_name = 'category'
            verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Presentation (models.Model):
    name = models.CharField (max_length=50,
                                unique=True,
                                verbose_name='Name'
                                )
    video = EmbedVideoField (blank=True, 
                                null=True
                                )
    about = models.TextField (blank=True,
                                verbose_name='Description'
                                )

class Product (models.Model):
    category = models.ForeignKey (Category,
                                    related_name='products' ,
                                    on_delete=models.CASCADE,
                                    verbose_name='Category'
                                    )
    name_collection = models.CharField (max_length=200,
                                        unique=True,
                                        verbose_name='Name'
                                        )
    slug = models.SlugField (max_length=200,
                                unique=True
                                )
    image = models.ImageField (upload_to='data/clothes/product/',
                                blank=True,
                                verbose_name='Presentation image'
                                )
    video = EmbedVideoField (blank=True, 
                                null=True
                                )
    description = models.TextField (blank=True,
                                    verbose_name='Description'
                                    )
    draft = models.BooleanField (default=False, 
                                    help_text= "публиковать/ скрыть", 
                                    verbose_name= 'Hide'
                                    )
    time = models.TextField (max_length=3, 
                                blank=True,
                                verbose_name='Hours of consultations for 1 model'
                                )
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
    title               = models.CharField (max_length=90,
                                verbose_name= 'Name of the creator'
                                )
    url = models.SlugField (max_length=90,
                                unique=True,
                                null=True
                                )
    collectionpresent   = models.ForeignKey (Product, 
                                            related_name = 'imagecollection', 
                                            on_delete=models.CASCADE
                                            )
    image               = models.ImageField (upload_to='data/clothes/imagecollection/',
                                blank=True,
                                verbose_name='vertical 16: 9 or square image'
                                )
    video               = EmbedVideoField (blank=True, 
                                            null=True
                                            )
    draft               = models.BooleanField (default=False, 
                                    help_text= "публиковать/ скрыть", 
                                    verbose_name= 'Hide'
                                    )
    money               = models.DecimalField (max_digits=10, 
                                    decimal_places=2,
                                    blank=True, 
                                    null=True,
                                    verbose_name='Price per model'
                                    )
    file        = models.FileField(upload_to="data/user/file_imagecollection/", null=True, blank=True)
    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'imagecollection'
        verbose_name_plural = 'imagecollections'

    def __str__(self):
    		return self.title


class Profile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.TextField (max_length=27, blank=True,verbose_name='Phone')
    full_height = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Full height')
    neck_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Neck girth')                 
    chest_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Chest girth')
    chest_height = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Chest height')
    center_chest = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='The center of the chest')
    back_width = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Back width')
    shoulder_long = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Shoulder length')
    long_sleeves = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Sleeve length')
    arm_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Forearm girth')
    wrist_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Brush girth')
    waist_circumference = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Waist circumference')
    length_front_waist = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Length in front to the waist')
    long_back_waist = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='The length of the back to the waist')
    long_waist_knee = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Length from waist to knee')
    hip_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Thigh circumference')
    thigh_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Scope tightened')
    knee_girth = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True,verbose_name='Knee girth')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Order (models.Model):
    name            = models.TextField  (max_length=50,
                                        blank=True,
                                        null=True,
                                        verbose_name='Name'
                                        )
    phone_number    = models.CharField (max_length=25,
                                        blank=True, 
                                        null=True,
                                        verbose_name='Phone number'
                                        )
    image           = models.ImageField (upload_to='data/clothes/order/',
                                        blank=True,
                                        verbose_name='Download image'
                                        )
    massege         = models.TextField (max_length=1000,
                                        blank=True,
                                        null=True,
                                        verbose_name='Your wishes')
    created         = models.DateTimeField (auto_now_add=True)
    cat             = models.ForeignKey (Category,
                                            on_delete=models.CASCADE,
                                            verbose_name='Clothing category'
                                            )
    agreement       = models.BooleanField(verbose_name='I accept the Terms of Service and Privacy Policy',
                                            default=True
                                            )
    def __str__(self):
        return self.name        

class CollectionUser(models.Model):
    user            = models.ForeignKey(User,
                                            related_name='collection_user',
                                                on_delete=models.CASCADE
                                                )
    category = models.ForeignKey (Category,
                                    related_name='category' ,
                                    on_delete=models.CASCADE,
                                    verbose_name='Category',
                                    null=True,
                                    )
    clothingparameters = models.TextField(verbose_name='Clothing parameters',
                                            null=True,
                                            help_text="parameters: pg96,gk107"
                                            )
    order           = models.ForeignKey(Order, 
                                            related_name = 'order', 
                                            on_delete=models.CASCADE
                                            )
    image           = models.ImageField (upload_to='data/user/img_user_collection/',
                                            blank=True
                                            )
    video           = EmbedVideoField (blank=True, 
                                            null=True
                                            )
    ordernumber     = models.PositiveIntegerField (verbose_name="Number order", 
                                                    default=0, 
                                                    help_text="id_orderform"
                                                    )
    material        = models.TextField(max_length= 600,
                                            verbose_name='Materials for model'
                                            )
    document        = models.FileField(upload_to="data/user/documents_collection/", null=True, blank=True)
    created         = models.DateTimeField (auto_now_add=True)

    class Meta:   
        ordering = ['-video']
        verbose_name = 'user_collection'
        verbose_name_plural = 'user_collections'

    def __str__(self):
        return self.clothingparameters

class Course (models.Model):
    name            = models.CharField(max_length=50,
                                        verbose_name='Name of the course'
                                        )
    slug            = models.SlugField(max_length=50,
                                        unique=True)
    about           = models.TextField(max_length=500,
                                        verbose_name='Description'
                                        )
    money           = models.DecimalField (max_digits=10, 
                                        decimal_places=2,
                                        blank=True, 
                                        null=True,
                                        verbose_name='Price for 1 lessons'
                                        )
    image           = models.ImageField(upload_to="data/learn/course",
                                        blank=True,
                                        verbose_name='Presentation image'
                                        )
    online          = models.TextField(max_length=10,
                                        blank=True,
                                        verbose_name='Online'
                                        )
    alive           = models.TextField(max_length=10,
                                        blank=True,
                                        verbose_name='Alive'
                                        )
    is_published    = models.BooleanField(default=True, verbose_name="Публикация")

    class Meta:   
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
    		return self.name


    
class Imagecourse(models.Model):
    image           = models.ImageField (upload_to="data/learn/studentimage",
                                        blank=True,
                                        verbose_name='Studentimage'
                                        )
    course          = models.ForeignKey (Course,
                                            related_name='course' ,
                                            on_delete=models.CASCADE,
                                            verbose_name='Course'
                                            )
    created         = models.DateTimeField (auto_now_add=True)

    class Meta:
        ordering = ['-created']


class OrderTeach (models.Model):
    name            = models.TextField  (max_length=50,
                                            blank=True,
                                            null=True,
                                            verbose_name='Name'
                                            )
    phone_number    = models.CharField (max_length=25,
                                            blank=True, 
                                            null=True,
                                            verbose_name='Phone number'
                                            )
    massege         = models.TextField (max_length=500,
                                            blank=True,
                                            null=True,
                                            verbose_name='What do you expect from the course'
                                            )
    created         = models.DateTimeField (auto_now_add=True)
    course          = models.ForeignKey (Course,
                                            on_delete=models.CASCADE,
                                            verbose_name='Course'
                                            )
    agreement       = models.BooleanField(verbose_name='I accept the Terms of Service and Privacy Policy',
                                            default=True
                                            )                                   
    def __str__(self):
        return self.name        
