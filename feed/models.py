from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)