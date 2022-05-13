from ast import Mod
from email.mime import image
from multiprocessing import context
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255, default='Enter your name here')
    email = models.EmailField(default='@gmail.com')
    phone = models.CharField(max_length=15, default="+91")
    city = models.CharField(max_length=255, default= 'Mumabi')
    country = models.CharField(max_length=255, default= 'India')
    message = models.TextField(null=False, blank=False, default='Start writing your message here...')
    time_of_message = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Message from, {self.name} & meassage is {self.message}'
class Category(models.Model):
    category = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Category :{self.category}'
class Post(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.FileField(default='media/no_img.png', upload_to='BlogImages')
    links = RichTextField()
    content = RichTextField() 
    created_on = models.DateTimeField(auto_now_add=True)
    references = models.CharField(max_length=255)
    code = RichTextField()
    blog_written_by = models.CharField(max_length=255, default='Mubashir Mustafa') 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, help_text= 'Check for publish your post online')
    def __str__(self):
        return f'Title : {self.title}, {self.category}'
    