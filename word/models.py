from django.db import models
from django.utils import timezone
from django.conf import settings
# from favorite.models import Favorite
from .common import CommonModelInfo
# class CommonModelInfo(models.Model):
#     # slug = models.SlugField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True , null = True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)

#     class Meta:
#         abstract = True
        
class Category(CommonModelInfo):
    image = models.ImageField(upload_to='images/dynamic/words/category/')
    category_title = models.CharField(max_length=20)
    def __str__(self):
        return self.title





class Words(CommonModelInfo):
    image = models.ImageField(upload_to='images/dynamic/words/')
    title = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    favorite = models.ForeignKey('favorite.Favorite' , null = True , on_delete = models.SET_NULL)
    def __str__(self):
        return self.title
    
# class QuizQuestion(model.Model):
#     question_text = models.TextField()
#     word_id = models.ForeignKey(Words , on_delete = models.CASCADE)

# class Alphabet_image(models.Model):
#     image = models.ImageField(upload_to='images/dynamic/words/category/alphabet/')



# class Alphabets(models.Model):
#     title = models.CharField(max_length=2)
    
# class Alphabets_item(CommonModelInfo):
#     alphabet_item_title = models.CharField(max_length=2)
#     alphabets = models.ForeignKey(Alphabets , on_delete=models.CASCADE)
#     category = models.ForeignKey(Category , on_delete=models.CASCADE)
#     alphabet_image = models.ForeignKey(Alphabet_image , on_delete=models.CASCADE)
#     words = models.ForeignKey(Words , on_delete=models.CASCADE)
#     liked = models.BooleanField(default=False)
    

    
    
    
