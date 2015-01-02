from django.db import models

# Create your models here.

class Editor(models.Model):
    name = models.CharField(max_length=20);
    status= models.BooleanField(default=False);
    
    
class Author(models.Model):
    name = models.CharField(max_length=20);
    surname = models.CharField(max_length=20);
    status = models.BooleanField(default=False);

    
class Category(models.Model):
    name = models.CharField(max_length=20);
    status = models.BooleanField(default=False);
    
    
class Book(models.Model):
    title = models.CharField(max_length=30);
    pages = models.PositiveIntegerField();
    front = models.ImageField();
    price = models.FloatField();
    authors = models.ManyToManyField(Author);
    editors = models.ManyToManyField(Editor);
    categories = models.ManyToManyField(Category);
    status = models.BooleanField(default=False);