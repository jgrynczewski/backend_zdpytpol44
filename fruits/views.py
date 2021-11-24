from django.shortcuts import render

# Create your views here.
def index(request):
    fruits = [
        'ananas',
        'cytryna',
        'pomarancza',
        'jablko',
    ]

    return render(
        request,
        'fruits/index.html',
        context={
            'fruits': fruits,
        }
    )
