import random
import datetime
import uuid
from dateutil.relativedelta import relativedelta
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from environs import Env
from yookassa import Configuration, Payment

from .forms import RegisterForm, SubscriptionForm
from .models import Dish


def index(request):
    auth = False

    if request.user.is_authenticated:
        auth = True

    recipes_keys = list(Dish.objects.values_list('pk', flat=True))
    print(recipes_keys)
    random_keys = random.sample(recipes_keys, 5)
    recipes = Dish.objects.filter(pk__in=random_keys)
    context = {
        'auth': auth,
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


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
    env = Env()
    env.read_env()
    shop_id = env.str('SHOP_ID')
    shop_key = env.str('SHOP_KEY')
    Configuration.account_id = shop_id
    Configuration.secret_key = shop_key

    if request.method == 'GET':
        form = SubscriptionForm()
        return render(request, 'order.html', {'form': form})

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        date_now = datetime.date.today()
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.ends_at = date_now + relativedelta(months=int(subscription.period))
            subscription.user = User.objects.get(username=request.user.username)
            subscription.save()

            payment = Payment.create({
                "amount": {
                    "value": "100.00",
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://www.example.com/return_url"
                },
                "capture": True,
                "description": "Оплата подписки FoodPlan"
            }, uuid.uuid4())
            return redirect(payment.confirmation.confirmation_url)
        return render(request, 'order.html', {'form': form})


@login_required(login_url='/auth')
def show_user_page(request):
    return render(request, 'lk.html')


def show_recipe_card(request, slug):
    recipe = Dish.objects.get(slug=slug)
    context = {'recipe': recipe}
    return render(request, 'card2.html', context)
