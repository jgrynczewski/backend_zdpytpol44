from django.shortcuts import render
from django.shortcuts import redirect

from formapp.models import Message
from formapp.forms import ContactForm
from formapp.forms import MessageForm

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

    if request.method=="POST":
        form = ContactForm(request.POST)  # bound form - formularz związany
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body'),
                date=data.get('date'),
                time=data.get('time')
            )

            return redirect("formapp:contact2")

    form = ContactForm()  # unbound form - formularz niezwiązany

    return render(
        request,
        'formapp/form2.html',
        context={
            'form': form,
        }
    )


# Formularze modelu
def contact3(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        form.save()

    form = MessageForm()

    return render(
        request,
        'formapp/form3.html',
        context={"form": form}
    )