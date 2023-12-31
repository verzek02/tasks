from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

