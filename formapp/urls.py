from django.urls import path

from formapp import views

app_name = 'formapp'

urlpatterns = [
    path('contact1/', views.contact1, name='contact1'),
    path('contact2/', views.contact2, name='contact2')
]