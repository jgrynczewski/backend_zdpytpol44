from django.shortcuts import render
from django.shortcuts import redirect

from form_app6.models import Task


def register(request):
    task = request.POST.get('task')
    if task:
        Task.objects.create(text=task)

        return redirect('form_app6:tasks-list')

    return render(
        request,
        'form_app6/register.html',
    )


def tasks_list(request):

    tasks = Task.objects.all()

    return render(
        request,
        'form_app6/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )