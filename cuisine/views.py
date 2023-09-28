from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm


def index(request):
    if request.user.is_authenticated:
        auth = True

    return render(request, 'index.html', {'auth': auth})


def auth_user(request):
    return render(request, 'auth.html')


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, 'registration.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('lk')
        else:
            print(form.is_valid())
            messages.error(request, 'Something again went wrong...')
            return render(request, 'registration.html', {'form': form})


def subscribe(request):
    return render(request, 'order.html')


@login_required(login_url='/auth')
def show_user_page(request):
    return render(request, 'lk.html')
