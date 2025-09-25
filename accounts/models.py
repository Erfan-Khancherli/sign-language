from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from django.core import validators

class CustomUserManager(BaseUserManager):
    def create_user(self , phone_number , first_name , last_name,password = None):
        if not phone_number:
            raise ValueError("User must have an phone_number")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        user = self.model()
        user.phone_number = phone_number
        user.first_name = first_name
        user.last_name  = last_name
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save()
        return user
    def create_superuser(self, phone_number, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an phone_number")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        user = self.model()
        user.phone_number = phone_number
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    
class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=11 , unique=True,
          validators=[
              validators.RegexValidator(
                  r"^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$",
                  ("Enter a valid phone number"),
                  "invalid",
              ),
          ],
          error_messages={
              "invalid": "Enter a valid phone number",
          },
      )
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()
    def __str__(self):
        return "{}".format(self.first_name)

