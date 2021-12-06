from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from form_app6.models import Task


def register(request):  # Create
    task = request.POST.get('task')
    if task:
        Task.objects.create(text=task)

        return redirect('form_app6:tasks-list')

    return render(
        request,
        'form_app6/register.html',
    )


def tasks_list(request):  # Read

    tasks = Task.objects.all()

    return render(
        request,
        'form_app6/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )


def update(request, task_id):  # Update

    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        updated_task = request.POST.get('task')
        if updated_task:
            task.text = updated_task
            task.save()

        return redirect('form_app6:tasks-list')

    return render(
        request,
        'form_app6/update.html',
        context={
            'task': task,
        }
    )


@require_http_methods(["POST"])
def delete(request, task_id):  # Delete

    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()

    return redirect('form_app6:tasks-list')
