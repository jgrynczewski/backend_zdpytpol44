from django.shortcuts import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<!DOCTYPE html><html><head><title>Hello</title></head><body><h1>Hello, world!</h1></body></html>")


def hello2(request):
    return render(request, 'hello.html')
