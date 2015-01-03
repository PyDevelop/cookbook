from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def principal(request):
    render(request,"principal.html")
    
@login_required    
def administrator(request):
    render(request,"administration.html")
    