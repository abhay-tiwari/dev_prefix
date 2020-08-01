from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    body = models.TextField()
    summary = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500)
    