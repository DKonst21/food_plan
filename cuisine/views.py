from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def auth_user(request):
    return render(request, 'auth.html')


def register_user(request):
    return render(request, 'registration.html')
