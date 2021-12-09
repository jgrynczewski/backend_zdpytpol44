from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views import View

from viewapp.models import Person
from viewapp.forms import PersonForm

# Widoki generyczne
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

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


# C (CRUD)

# Widok funkcyjny
def create_person(request):
    # form = PersonForm(request.POST or None)

    if request.method == "GET":
        form = PersonForm()

        return render(
            request,
            'viewapp/create-person.html',
            context={
                'form': form,
            }
        )

    elif request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('viewapp:create-person')


# Widok klasowy
class PersonCreateView(View):
    def get(self, request):
        form = PersonForm()

        return render(
            request,
            'viewapp/create-person.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('viewapp:create-person2')


# Widok generyczny
class PersonGenericCreateView(CreateView):
    model = Person
    fields = '__all__'
