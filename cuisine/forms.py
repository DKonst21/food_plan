from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Subscription


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['period', 'meal_types', 'allergy_types']
