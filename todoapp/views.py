from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todoapp.models import Todo
from django.http import HttpResponseRedirect
from . import models


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todoapp/index.html', {"todo_items": todo_items})


@csrf_exempt
def add_todo(request):
    print(request.POST)
    current_date = timezone.now()
    content = request.POST.get("content")
    # print(added_date, content)
    models.Todo.objects.create(added_date=current_date, text=content)
    # print(created_objects)
    # len = T odo.objects.all().count()
    # print(len)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
