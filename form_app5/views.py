from django.shortcuts import render
from django.shortcuts import redirect


def register(request):
    return render(
        request,
        'form_app5/register.html',
    )


def tasks_list(request):

    task = request.POST.get('task')

    with open('tasks.txt', 'a+') as f:
        if task:
            f.write(task + "\n")
            return redirect('form_app5:tasks-list')

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        'form_app5/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )