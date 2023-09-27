from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def auth_user(request):
    return render(request, 'auth.html')


def register_user(request):
    return render(request, 'registration.html')


def subscribe(request):
    return render(request, 'order.html')


@login_required(login_url='/auth')
def show_user_page(request):
    return render(request, 'lk.html')
