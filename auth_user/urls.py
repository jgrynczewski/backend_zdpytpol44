from django.urls import path

from auth_user import views

app_name = 'auth_user'

urlpatterns = [
    path('cookies/', views.cookies, name='cookies'),
]