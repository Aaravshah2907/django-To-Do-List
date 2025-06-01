from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    
    if ls in request.user.todolists.all():
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
    return render(request, 'main/view.html', {})

def home(request):
    return render(request, 'main/home.html', {})

@login_required  # Ensures only logged-in users can create lists
def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(title=n, user=request.user)
            t.save()
            return redirect(f'/{t.id}')  # or use reverse() for named URLs
        # If form is invalid, fall through to re-render the form with errors
    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {"form": form})

@login_required
def view(request):
    print("Current user:", request.user)
    lists = ToDoList.objects.filter(user=request.user)
    print("Lists found:", lists)
    return render(request, 'main/view.html', {'lists': lists})