from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login_view(request):

    if request.method == "POST":
        data = request.POST

        user = authenticate(
            username=data.get('user'),
            password=data.get('password')
        )

        if user:
            login(request, user=user)

        return redirect('uwierzytelnienie:home')

    return render(
        request,
        'uwierzytelnienie/login.html'
    )


def home(request):
    if request.method=="POST":
        logout(request)

        redirect('uwierzytelnienie:home')

    return render(
        request,
        'uwierzytelnienie/home.html',
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('uwierzytelnienie:login-view')

    form = UserCreationForm()

    return render(
        request,
        'uwierzytelnienie/register.html',
        context={
            'form': form,
        }
    )
