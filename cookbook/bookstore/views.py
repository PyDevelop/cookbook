from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms import *

# Create your views here.

def principal(request):
    render(request,"principal.html")
    
@login_required    
def administrator(request):
    render(request,"administration.html")
    

#book -editor - category -author


#Category management
    
def addCategory(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New category added successufully"
    else:
        message = form.errors
    return render(request, "addCategory.html",{'form': form, 'message':message})


def deleteCategory(request,pk):
    instance = get_object_or_404(Category,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Category','element':instance})

def confirmDelete(request,pk):
    instance = get_object_or_404(Category,id=pk)
    categories = Category.objects.get(pk=pk)
    categories.update(status=True)
    for i in categories:
        i.save()
        
def listCategories(request):
    categories = Category.objects.all()
    return render(request,"list.html",{'type':'Category','list':categories})


def changeCategory(request,pk):
    if request.method == 'POST':
        category = get_object_or_404(Category,id=pk)
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            message = "changes saved"
        else:
            message = form.errors
    else:
        #deberia redirigir a la pagina de listados

        
# Editor management

def addEditor(request):
    form = EditorForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New editor added successufully"
    else:
        message = form.errors
    return render(request, "addEditor.html",{'form': form, 'message':message})


def deleteEditor(request,pk):
    instance = get_object_or_404(Editor,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Editor','element':instance})

def confirmDelete(request,pk):
    instance = get_object_or_404(Editor,id=pk)
    editors = Editor.objects.get(pk=pk)
    editors.update(status=True)
    for i in editors:
        i.save()
        
def listEditors(request):
    editors = Editor.objects.all()
    return render(request,"list.html",{'type':'Editor','list':editors})


def changeEditor(request,pk):
    if request.method == 'POST':
        editor = get_object_or_404(Editor,id=pk)
        form = CategoryForm(data=request.POST, instance=editor)
        if form.is_valid():
            form.save()
            message = "changes saved"
        else:
            message = form.errors
    else:
        #deberia redirigir a la pagina de listados



#Author management

def addAuthor(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New author added successufully"
    else:
        message = form.errors
    return render(request, "addAuthor.html",{'form': form, 'message':message})


def deleteEditor(request,pk):
    instance = get_object_or_404(Author,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Author','element':instance})

def confirmDelete(request,pk):
    instance = get_object_or_404(Author,id=pk)
    authors = Author.objects.get(pk=pk)
    authors.update(status=True)
    for i in authors:
        i.save()
        
def listAuthors(request):
    authors = Author.objects.all()
    return render(request,"list.html",{'type':'Author','list':authors})


def changeAuthor(request,pk):
    if request.method == 'POST':
        author = get_object_or_404(Author,id=pk)
        form = AuthorForm(data=request.POST, instance=author)
        if form.is_valid():
            form.save()
            message = "changes saved"
        else:
            message = form.errors
    else:
        #deberia redirigir a la pagina de listados

#Book management

def addBook(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New book added successufully"
    else:
        message = form.errors
    return render(request, "addBook.html",{'form': form, 'message':message})


def deleteBook(request,pk):
    instance = get_object_or_404(Book,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Book','element':instance})

def confirmDelete(request,pk):
    instance = get_object_or_404(Book,id=pk)
    books = Book.objects.get(pk=pk)
    books.update(status=True)
    for i in books:
        i.save()
        
def listBooks(request):
    books= Book.objects.all()
    return render(request,"list.html",{'type':'Book','list':books})


def changeBook(request,pk):
    if request.method == 'POST':
        book = get_object_or_404(Book,id=pk)
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            message = "changes saved"
        else:
            message = form.errors
    else:
        #deberia redirigir a la pagina de listados


