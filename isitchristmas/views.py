import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    month = now.month
    day = now.day

    if month == 12 and day == 25:
        is_it_christmas = True
    else:
        is_it_christmas = False

    return render(
        request,
        'isitchristmas/index.html',
        context={
            'is_it_christmas': is_it_christmas,
        }
    )
