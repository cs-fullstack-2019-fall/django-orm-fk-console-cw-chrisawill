
# Create your models here.
from django.db import models
from django.utils import timezone

class Author(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)


class Post(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=200)
    Date_Posted = models.DateTimeField(default=timezone.now)
