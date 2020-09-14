from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    body = models.CharField(max_length=200)