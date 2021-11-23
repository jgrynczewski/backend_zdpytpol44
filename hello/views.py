from django.shortcuts import HttpResponse
from django.shortcuts import render


def hello_view(request):
    return HttpResponse("<!DOCTYPE html><html><head><title>Hello</title></head><body><h1>Hello, world!</h1></body></html>")


def hello2_view(request):
    return render(request, 'hello.html')


def adam_view(request):
    return HttpResponse("Witaj, Adam!")


def ewa_view(request):
    return HttpResponse("Witaj, Ewa!")


def name_view(request, name):
    from markupsafe import escape
    print(escape(name))
    return HttpResponse(f"Witaj, {escape(name)}!")


def name_view2(request, name):
    return render(
        request,
        'name.html',
        context={
            'name': name
        }
    )
