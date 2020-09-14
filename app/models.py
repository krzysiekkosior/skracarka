from django.db import models

# Create your models here.

class Link(models.Model):
    target = models.TextField()
    count = models.IntegerField(default=0)
    last_visited = models.DateTimeField(auto_now=True)
