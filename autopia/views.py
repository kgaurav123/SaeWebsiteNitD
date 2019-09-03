from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AutopiaForm

def autopia(request):
    form = AutopiaForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        institution = form.cleaned_data['institution']
        article = form.cleaned_data['article']
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'autopia/autopia.html',{'form': form})

