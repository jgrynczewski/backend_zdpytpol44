from django.shortcuts import render

TASKS = []

def register(request):
    return render(
        request,
        'form_app2/register.html'
    )


def tasks_list(request):
    task = request.GET.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app2/tasks_list.html',
        context={
            'tasks': TASKS
        }
    )
