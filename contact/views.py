from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MessageForm

def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        institution = form.cleaned_data['institution']
        message = form.cleaned_data['message']
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'contact/contact.html',{'form': form})
