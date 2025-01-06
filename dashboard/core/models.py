from django.db import models

from django.contrib.auth.models import User
class Doctor(models.Model):
    username=models.TextField(max_length=100)
    docid=models.TextField(max_length=100)
    def __str__(self):
        return self.username
class Patient(models.Model):
    username=models.TextField(max_length=100)
    docid=models.IntegerField(default=0)
    def __str__(self):
        return self.username
class Blogs(models.Model):
    Blog_title=models.TextField(max_length=100)
    Blog_content=models.TextField(max_length=500)
    Blog_author=models.TextField(max_length=100)
    def __str__(self):
        return self.Blog_title
    
    ################################################
# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='post_images')
#     comments = models.TextField(max_length=500, blank=True)
#     caption = models.CharField(max_length=100, blank=True)
    
# Create your models here.
