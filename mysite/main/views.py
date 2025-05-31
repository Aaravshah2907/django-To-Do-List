from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    
    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get('c' + str(item.id)) == 'clicked':
                    item.completed = True
                else:
                    item.completed = False
                item.save()
        elif request.POST.get("newItem"):
            text = request.POST.get("new")
            if len(text) > 2:
                ls.item_set.create(text=text, completed=False)
            else:
                print("Invalid input") 
    
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