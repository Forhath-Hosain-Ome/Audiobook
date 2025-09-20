from django import forms
from reader.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'pdf', 'img']
