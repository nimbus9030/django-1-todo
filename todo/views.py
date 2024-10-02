from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TodoModelForm
from .models import Todo

def Index(request):
    form = TodoModelForm()
    todo_list = Todo.objects.all()
    print( todo_list )

    return render( request, "todo/index.html", {"form" : form, "list" : todo_list} ) 
    # return HttpResponse( "hello world" )


def Add(request):
    if request.method == "POST":
        form = TodoModelForm( request.POST )
        if form.is_valid():
            form.save()

            return redirect("index")

def Delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('index')


def Update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('index')