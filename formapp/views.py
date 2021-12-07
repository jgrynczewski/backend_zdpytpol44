from django.shortcuts import render
from django.shortcuts import redirect

from formapp.models import Message
from formapp.forms import ContactForm

# Formularz HTML
def contact1(request):
    if request.method == "POST":

        data = request.POST

        Message.objects.create(
            name = data.get('name'),
            email = data.get('email'),
            category = data.get('category'),
            subject = data.get('subject'),
            body = data.get('body'),
            date = data.get('date'),
            time = data.get('time')
        )

        return redirect('formapp:contact1')

    return render(
        request,
        'formapp/form1.html',
    )


# Formularz Django
def contact2(request):

    form = ContactForm()

    return render(
        request,
        'formapp/form2.html',
        context={
            'form': form,
        }
    )