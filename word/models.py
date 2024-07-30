from django.db import models

from django.conf import settings

class CommonModelInfo(models.Model):
    # slug = models.SlugField(unique=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)
    last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
        
class Words(models.Model):
    image = models.ImageField(upload_to='images/dynamic/words/')
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    image = models.ImageField(upload_to='images/dynamic/words/category/')
    category_title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Alphabet_image(models.Model):
    image = models.ImageField(upload_to='images/dynamic/words/category/alphabet/')



class Alphabets(models.Model):
    title = models.CharField(max_length=2)
    
class Alphabets_item(CommonModelInfo):
    alphabet_item_title = models.CharField(max_length=2)
    alphabets = models.ForeignKey(Alphabets , on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    alphabet_image = models.ForeignKey(Alphabet_image , on_delete=models.CASCADE)
    words = models.ForeignKey(Words , on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    

    
    
    
