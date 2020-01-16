from django.db import models
from django.utils import timezone


class Blog(models.Model):
    publish_date = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
