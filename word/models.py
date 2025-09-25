from django.db import models
from django.utils import timezone
from django.conf import settings
from .common import CommonModelInfo

class Category(CommonModelInfo):
    image = models.ImageField(upload_to='images/dynamic/words/category/') 
    category_title = models.CharField(max_length=20 , unique = True)
    def __str__(self):
        return self.category_title

class Words(CommonModelInfo):
    image = models.ImageField(upload_to='images/dynamic/words/')
    title = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    favorite = models.ForeignKey('favorite.Favorite' , null = True , on_delete = models.SET_NULL)
    def __str__(self):
        return self.title