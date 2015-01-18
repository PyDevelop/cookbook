from django.forms import ModelForm
from bookstore.models import *

class EditorForm(ModelForm):
    class Meta:
        model = Editor
        exclude = ('status','dependencies',)
        
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ('status','dependencies',)
        
    
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ('status','dependencies',)
        
        
class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('status','dependencies',)
        
        