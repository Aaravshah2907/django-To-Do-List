from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.title)

