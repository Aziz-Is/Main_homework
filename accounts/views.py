from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['has error'] = True
    return render (request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')

def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        my_form = RegisterForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('login')
    else:
        my_form = RegisterForm()
    return render(request, 'register.html', {'form': my_form})

