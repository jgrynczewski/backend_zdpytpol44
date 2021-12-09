from django.urls import path

from uwierzytelnienie import views

app_name = 'uwierzytelnienie'

urlpatterns = [
    path('login-view/', views.login_view, name='login-view'),
    path('home/', views.home, name='home'),
]