from django.contrib.auth import views as auth_views
from django.urls import path
from cuisine import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.register_user, name='registration'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('lk', views.show_user_page, name='lk'),
    path('logout', views.logout_view, name='logout'),
    path('auth', auth_views.LoginView.as_view(template_name='auth.html', next_page='lk'), name='auth'),
]
