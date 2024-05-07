from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager
from utils.user_role import UserRole


class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=14, unique=True)
    estd = models.CharField(max_length=120, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_email = models.EmailField(max_length=120, blank=True, null=True)
    tread_license = models.CharField(max_length=120, blank=True, null=True)
    role = models.IntegerField(choices=UserRole.get_choices(), default=UserRole.CUSTOMER.value)
    company_logo = models.ImageField(upload_to='company/logo/%m/%y', blank=True, null=True)
    company_cover_photo = models.ImageField(upload_to='company/cover/%m/%y', blank=True, null=True)
    address = models.TextField(blank=True, null=True, default='')
    device_token = models.CharField(max_length=100, blank=True, null=True, default='')
    avatar = models.ImageField(upload_to='avatar/%m/%y', blank=True, null=True)
    # Default fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    @property
    def get_photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/images/avatar.svg"

    @property
    def uuid(self):
        return f"DM{self.id}"

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'full_name']
    objects = UserManager()
