from django import forms
from .models import Snippets

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippets
        fields = '__all__'