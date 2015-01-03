from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email,password):
        user = self.model(username=username,email=email,password=password)
        return user
    
    def create_superuser(self,username,email,password):
        user = self.model(username=username,email=email,password=password)
        user.is_admin=True
        user.save()
        return user


class usuario(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30,blank = True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    password=models.CharField(max_length=8)
    direccion = models.CharField(max_length=50,blank=True)
    codigo_postal = models.CharField(max_length=10,blank=True)
    telefono = models.PositiveIntegerField()
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['username','email','password']
    
    objects= UsuarioManager()
    


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