from django import forms
from models import *

class EditorForm(forms.Form):
    class Meta:
        model = Editor
        exclude = ('status',)
        
class AuthorForm(forms.Form):
    class Meta:
        model = Author
        exclude = ('status',)
        
    
class CategoryForm(forms.Form):
    class Meta:
        model = Category
        exclude = ('status',)
        
        
class BookForm(forms.Form):
    class Meta:
        model = Book
        exclude = ('status',)
        
        