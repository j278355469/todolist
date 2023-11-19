from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.


def todo(request):
    # all,filter,get

    user = request.user
    todos = None
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)

    return render(request, "todo/todo.html", {"todos": todos})


def viewtodo(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/viewtodo.html', {"todo": todo})
