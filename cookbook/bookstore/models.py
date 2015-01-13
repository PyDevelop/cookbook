from django.db import models

class Editor(models.Model):
    name = models.CharField(max_length=20,blank=False, unique=True)
    status= models.BooleanField(default=False)
    dependencies= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def has_dependencies(self,pk):
        editor = self.objects.get(id=pk)
        books_related = editor_set.all().count()
        if books_related > 0:
            return True
        else:
            return False
    
class Author(models.Model):
    name = models.CharField(max_length=20);
    surname = models.CharField(max_length=20);
    status = models.BooleanField(default=False)
    dependencies= models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.name,self.surname)
    
    def has_dependencies(self,pk):
        author = self.objects.get(id=pk)
        books_related =author_set.all().count()
        if books_related > 0:
            return True
        else:
            return False
        
class Category(models.Model):
    name = models.CharField(max_length=20);
    status = models.BooleanField(default=False);
    dependencies= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def has_dependencies(self,pk):
        categories = self.objects.get(id=pk)
        books_related = categories_set.all().count()
        if books_related > 0:
            return True
        else:
            return FAlse
        

class Book(models.Model):
    title = models.CharField(max_length=30,unique=True);
    pages = models.PositiveIntegerField();
    front = models.ImageField();
    price = models.FloatField();
    authors = models.ManyToManyField(Author);
    editors = models.ManyToManyField(Editor);
    categories = models.ManyToManyField(Category);
    status = models.BooleanField(default=False);
    
    def __str__(self):
        return self.name
    