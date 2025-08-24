from django.db import models
from django.utils import timezone
from django.conf import settings

class CommonModelInfo(models.Model):
    # slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True , null = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True , blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True