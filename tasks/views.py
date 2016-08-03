from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def tasks_list(request):
    """Display list of tasks"""
    return render(request, 'tasks/list.html', {})


@login_required
def task_view(request, task_id):
    """Main views of one task"""
    print "showing task: ", task_id
    return render(request, 'tasks/task.html', {})

