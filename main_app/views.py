from django.shortcuts import render
from django.http import HttpResponse
from .models import Chicken

def home(request):
    return HttpResponse('<h1>Hello world</h1>')

def about(request):
    return render(request, 'main_app/about.html')

def chickens_index(request):
    chickens = Chicken.objects.all()
    return render(request, 'chickens/index.html', {'chickens' : 'chickens'})