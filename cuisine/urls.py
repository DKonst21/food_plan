from django.urls import path
from cuisine import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth_user, name='auth'),
    path('registration', views.register_user, name='registration'),
]
