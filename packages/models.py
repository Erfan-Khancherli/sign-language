from django.db import models

from word.common import CommonModelInfo
from word.models import Category
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class Packages(CommonModelInfo):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name

class PackageCategory(CommonModelInfo):
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class UserPackage(CommonModelInfo):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    payment_id = models.CharField(max_length=50, null=True, blank=True)