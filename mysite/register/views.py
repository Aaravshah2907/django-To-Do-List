from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save and get the user instance
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate and log in the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/view")
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})