from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def cookies(request):
    print(request.COOKIES)
    res = HttpResponse("OK")
    res.set_cookie('title', 'Bosh')
    res.set_cookie('ciasteczko2', 10, max_age=1000)

    return res