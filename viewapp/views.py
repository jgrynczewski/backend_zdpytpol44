from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404

from viewapp.models import Person

# Widoki generyczne
from django.views.generic import TemplateView
from django.views.generic import DetailView


# function-based view (widok funkcyjny)
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view (widok klasowy)
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# Widok funkcyjny
def template_hello(request):
    return render(
        request,
        'viewapp/hello.html',
    )


# Widok klasowy
class HelloClassView(View):
    def get(self, request):
        return render(
            request,
            'viewapp/hello.html'
        )


# Generic view - Widok generyczny
class HelloGenericView(TemplateView):
    template_name = 'viewapp/hello.html'


# Widok funkcyjny
def template_hello2(request):
    name = "Adam"

    return render(
        request,
        'viewapp/hello2.html',
        context={
            "name": name
        }
    )

# Widok klasowy
class HelloClassView2(View):
    def get(self, request):
        name = "Adam"

        return render(
            request,
            'viewapp/hello2.html',
            context={
                "name": name
            }
        )


# Widok generyczny
class HelloGenericView2(TemplateView):
    template_name = "viewapp/hello2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Adam"
        return context


# Widok funkcyjny
def person_detail(request, id):
    person = get_object_or_404(Person, id=id)

    return render(
        request,
        'viewapp/person_detail.html',
        context = {
            "person": person
        }
    )


# Widok klasowy
class PersonView(View):
    def get(self, request, id):
        person = get_object_or_404(Person, id=id)

        return render(
            request,
            'viewapp/person_detail.html',
            context={
                "person": person
            }
        )


# Widok generyczny
class PersonDetailView(DetailView):
    model = Person
