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
