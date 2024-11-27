from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import *
from django.contrib import messages


class Task(View):
    template_name = 'tasks/post_task.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request):
        title = request.POST.get('title')
        id_category = int(request.POST.get('category'))
        try:
            category = Category.objects.get(id=id_category)
            Todo.objects.create(title=title, category=category)
        except Category.DoesNotExist :
            messages.error(request, "Echec d'enregistrement")
        except Exception as e:
            messages.error(request, "Une erreur s'est produit dans le système")
        return redirect('tasks:post_task')

def get_tasks(request):
    tasks = Todo.objects.all()
    return render(request, 'components/get_task.html', {'tasks': tasks})