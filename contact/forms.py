from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail*'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization/Academic Institutions*'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here...'}))
    class Meta:
        model = Message
        fields = ['name','email','institution','message']
        
