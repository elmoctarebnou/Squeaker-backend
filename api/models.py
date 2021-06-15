
from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name =  models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=300)


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField()


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE) 
    content = models.TextField()
    date = models.DateTimeField()



















