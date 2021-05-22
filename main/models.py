from django.db import models
from uuid import uuid4
import os
from django.conf import settings
from django_resized import ResizedImageField

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    quandity = models.PositiveIntegerField()
    image = ResizedImageField(size=[5000,3000],upload_to="images/")

    def __str__(self):
        return self.name

    @property
    def get_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)
    
