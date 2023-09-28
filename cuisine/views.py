from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm


def index(request):
    auth = False

    if request.user.is_authenticated:
        auth = True

    return render(request, 'index.html', {'auth': auth})


def logout_view(request):
    logout(request)
    return redirect('index')


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
            login(request, user)
            return redirect('lk')
        else:
            return render(request, 'registration.html', {'form': form})


def subscribe(request):
    return render(request, 'order.html')


@login_required(login_url='/auth')
def show_user_page(request):
    return render(request, 'lk.html')
