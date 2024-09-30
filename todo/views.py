from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TodoModelForm

def Index(request):
    form = TodoModelForm()

    return render( request, "todo/index.html", {"form" : form} ) 
    # return HttpResponse( "hello world" )


def Add(request):
    if request.method == "POST":
        form = TodoModelForm( request.POST )
        if form.is_valid():
            form.save()

            return redirect("index")
        
# def add(request):
#     title = request.POST['title']
#     Todo.objects.create(title=title)

#     return redirect('todos:index')

# def delete(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     todo.delete()

#     return redirect('todos:index')

# def update(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     isCompleted = request.POST.get('isCompleted', False)
#     if isCompleted == 'on':
#         isCompleted = True
    
#     todo.isCompleted = isCompleted

#     todo.save()
#     return redirect('todos:index')