from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return render(request, 'main/list.html', {"ls":ls})

def home(request):
    return render(request, 'main/home.html', {})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(title=n)
            t.save()
        return HttpResponseRedirect('/%i' % t.id)
    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {"form": form}) 