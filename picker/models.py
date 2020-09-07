from django.db import models

# Create your models here.
class Number(models.Model):
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)