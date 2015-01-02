from django import forms
from models import *

class EditorForm(forms.Form):
    class Meta:
        model = Editor
        exclude = ('status',)