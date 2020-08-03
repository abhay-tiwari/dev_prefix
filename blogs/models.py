from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)
    posts_count = models.IntegerField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    body = models.TextField()
    summary = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    publish_date = models.DateTimeField(blank=True, default=datetime.now())
    read_duration = models.IntegerField(default=0)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment {} by {}'.format(self.content, self.author_name)
