from django.shortcuts import render
from django.http import HttpResponse
from .models import Chicken


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'main_app/about.html')


class Chicken:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
chickens = [
    Chicken('Nugget', 'Plymouth Rock', 'Nugget is a friendly chicken', 2),
    Chicken('Fluffy', 'Plymouth Rock', 'Fluffy is a fluffy chicken', 1),
    Chicken('Bella', 'Plymouth Rock', 'Bella is a beautiful chicken', 3),
]

def chickens_index(request):
    return render(request, 'chickens/index.html', {
        'chickens': chickens
    })
