from django.shortcuts import render

def index(request):
    return render(request,'index/home.html')
def events(request):
    return render(request,'index/events.html',{})
def allteam(request):
    return render(request,'index/allteam.html',{})
