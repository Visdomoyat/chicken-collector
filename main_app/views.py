from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello world</h1>')

def about(request):
    return render(request, 'main_app/about.html')