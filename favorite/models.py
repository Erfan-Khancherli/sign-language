from django.db import models

from word.common import CommonModelInfo
from word.models import Words
from django.conf import settings

class Favorite(CommonModelInfo):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL , related_name='favorites_created')
    word = models.ForeignKey(Words ,on_delete = models.CASCADE ,null=True, blank = True,related_name='favorites_received')