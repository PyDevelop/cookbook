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
    return render(request, "addCategory.html",  )
        
    