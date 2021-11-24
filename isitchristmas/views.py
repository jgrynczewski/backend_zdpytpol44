import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    month = now.month
    day = now.day

    is_it_christmas = False
    if (month == 11 and day == 24):
        is_it_christmas = True

    return render(
        request,
        'isitchristmas/index.html',
        context={
            'is_it_christmas': is_it_christmas,
        }
    )
