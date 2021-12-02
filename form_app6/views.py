from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404

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


def update(request, task_id):

    # try:
    #     task = Task.objects.get(id=task_id)
    # except ObjectDoesNotExist:
    #     raise Http404()

    task = get_object_or_404(Task, id=task_id)


    return render(
        request,
        'form_app6/update.html',
        context={
            'task': task,
        }
    )