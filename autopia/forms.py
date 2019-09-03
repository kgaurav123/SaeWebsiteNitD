from django import forms
from .models import Autopia

class AutopiaForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization/Academic Institutions*'}))
    article = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the article'}))
    class Meta:
        model = Autopia
        fields = ['name','institution','article']
        
