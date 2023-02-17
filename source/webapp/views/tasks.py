from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import DeleteView, UpdateView
from webapp.models import TODO


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'detailed_description': request.POST.get('detailed_description'),
        'status': request.POST.get('status'),
        'completion_date': request.POST.get('completion_date')
    }
    task = TODO.objects.create(**task_data)
    return redirect('detail_task', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })

class TaskDeleteView(DeleteView):
    model = TODO
    template_name = 'delete_task.html'
    success_url = '/'


class TaskUpdateView(UpdateView):
    model = TODO
    fields = [
        'title',
        'description',
        'detailed_description',
        'status',
        'completion_date'
    ]
    template_name = 'update_task.html'
    success_url = '/'
