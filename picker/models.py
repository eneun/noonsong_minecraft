from django.db import models

# Create your models here.
class Number(models.Model):
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)