from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return render(request, 'main/list.html', {"ls":ls})

def home(request):
        return render(request, 'main/home.html', {})