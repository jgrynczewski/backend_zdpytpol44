from django.shortcuts import render
from django.shortcuts import redirect

from form_app5.models import Task


def register(request):
    return render(
        request,
        'form_app5/register.html',
    )


def tasks_list(request):

    task = request.POST.get('task')

    with open('tasks.txt', 'a+') as f:
        if task:
            # Create
            Task.objects.create(text=task)
            return redirect('form_app5:tasks-list')

    # Read
    tasks = Task.objects.all()

    return render(
        request,
        'form_app5/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )