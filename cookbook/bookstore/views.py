from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bookstore.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from bookstore.models import *

# Create your views here.

def principal(request):
    return render(request,"principal.html")
    
@login_required    
def administrator(request):
    return render(request,"administration.html")
    

#book -editor - category -author


#Category management
    
def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('principal'))
    else:
        form = CategoryForm()
    return render_to_response("addCategory.html",{'formulario': form, 'type':'Category','action':'add'},context_instance=RequestContext(request))
    
    
def deleteCategory(request):
    lista = Category.objects.all()
    return render(request,"deleteCategory.html",{'type':'Category','lista':lista})

def confirmDelete(request):
    lista = request.POST.getlist('selected')
    return render(request,"confirmation.html",{'type':'Category','lista':lista})
    
        
def listCategories(request):
    categories = Category.objects.all()
    return render(request,"listCategories.html",{'type':'Category','list':categories})


def changeCategory(request,pk):
    category = get_object_or_404(Category,id=pk)
    if request.method == 'POST':
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            message = "changes saved"
            return HttpResponseRedirect(reverse('listCategories'))
        else:
            message = form.errors 
    else:
        form =CategoryForm(instance=category)
    return render(request,"change.html",{'instance':category.pk,'form':form, 'type':'Category', 'action':'Change'})

        
# Editor management

def addEditor(request):
    form = EditorForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New editor added successufully"
    else:
        message = form.errors
    return render(request, "addEditor.html",{'form': form, 'message':message,'action':'add','type':'Editor'})


def deleteEditor(request,pk):
    instance = get_object_or_404(Editor,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Editor','element':instance,'action':'Delete Confirmation'})
'''
def confirmDelete(request,pk):
    instance = get_object_or_404(Editor,id=pk)
    editors = Editor.objects.get(pk=pk)
    editors.update(status=True)
    for i in editors:
        i.save()
'''        
def listEditors(request):
    editors = Editor.objects.all()
    return render(request,"listEditors.html",{'type':'Editor','list':editors,'action':'List'})


def changeEditor(request,pk):
    if request.method == 'POST':
        editor = get_object_or_404(Editor,id=pk)
        form = EditorForm(data=request.POST, instance=editor)
        if form.is_valid():
            form.save()
            message = "changes saved"
        else:
            message = form.errors
    else:
        form = EditorForm(instance=editor)
    return render(request,"change.html",{'form':form,'action':'Change','type':'Editor'})



#Author management

def addAuthor(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New author added successufully"
    else:
        message = form.errors
    return render(request, "addAuthor.html",{'form': form, 'message':message,'action':'add','type':'Author'})


def deleteAuthor(request,pk):
    instance = get_object_or_404(Author,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Author','element':instance,'action':'Delete confirmation'})
'''
def confirmDelete(request,pk):
    instance = get_object_or_404(Author,id=pk)
    authors = Author.objects.get(pk=pk)
    authors.update(status=True)
    for i in authors:
        i.save()
'''        
def listAuthors(request):
    authors = Author.objects.all()
    return render(request,"listAuthors.html",{'type':'Author','list':authors,'action':'List'})


def changeAuthor(request,pk):
    author = get_object_or_404(Author,id=pk)
    if request.method == 'POST':       
        form = AuthorForm(data=request.POST, instance=author)
        if form.is_valid():
            form.save()
            message = "changes saved"
            return HttpResponseRedirect(reverse('authors'))
            message = form.errors
    else:
        message = "update the info"
        form= AuthorForm(instance=author)
    return render(request,"changeAuthor.html",{'type':'Author','action':'Change','form':form,'message':message,'instance':author.pk})

#Book management

def addBook(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "New book added successufully"
    else:
        message = form.errors
    return render(request, "addBook.html",{'form': form, 'message':message,'action':'add','type':'Book'})


def deleteBook(request,pk):
    instance = get_object_or_404(Book,id=pk)
    #podria poner elementos como si tiene dependencias o no, bien podria ser un metodo de clase
    return render(request,"confirmation.html",{'type':'Book','element':instance,'action':'Delete confirmation'})

'''
def confirmDelete(request,pk):
    instance = get_object_or_404(Book,id=pk)
    books = Book.objects.get(pk=pk)
    books.update(status=True)
    for i in books:
        i.save()
'''        
def listBooks(request):
    books= Book.objects.all()
    return render(request,"list.html",{'type':'Book','list':books,'action':'List'})


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
        form = BookForm(instance=book)
    return render(request,"change.html",{'type':'Book', 'action':'Change','form':form})


def ajaxRequest(request):
    if request.method == 'POST':
        key = request.POST['id']
        category = Category.objects.get(id=key)
        data = serializers.serialize('json',categories,fields=('name',))
        return HttpResponse(data,mimetype='application/json')