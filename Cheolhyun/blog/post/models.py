from django.db import models

# Create your models here.

class Post(models.Model):
    create = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)