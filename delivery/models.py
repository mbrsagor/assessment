from django.db import models
from user.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Service(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Format(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CreateOrder(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_order')
    services = models.ManyToManyField(Service, related_name='OrderServices')
    notes = models.TextField(blank=True, default='')
    download_link = models.URLField(max_length=555)
    is_complete = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()

    def __str__(self):
        return self.user.username
