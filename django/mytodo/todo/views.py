from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

# Create your views here.
# def todo_list(request):
#     todos = Todo.objects.filter(complete = False)
#     return render(request,'todo/todo_list.html',{'todos':todos})
    
def todo_post(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request,'todo/todo_post.html',{'form':form})
    else :
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            print(type(form))
            print(type(todo))
            todo.save()
            # save로는 파일 저장이 안된다.
            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            #default_storage = /media.
            Todo.objects.filter(id=todo.id).update(imagefile=upload)
            #신규로 저장한 todo의 id를 참조해서 imagefile 의 값을 update한다
            # new_Todo.save()
            return redirect('todo:todo_list')
        
    
def todo_detail(request,pk):
   todo = Todo.objects.get(id = pk)
   return render(request, 'todo/todo_detail.html',{'todo':todo})
    
def todo_edit(request,pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method=='GET':
        form = TodoForm(instance=todo)
    else:
        form = TodoForm(request.POST,instance = todo)
        if form.is_valid():
            td = form.save(commit=False)
            td.save()
            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            #default_storage = /media.
            Todo.objects.filter(id=todo.id).update(imagefile=upload)
            return redirect('todo:todo_detail',pk = todo.pk)
        
     
    return render(request, 'todo/todo_edit.html',{'form':form})
    1        
        
       
        
    
    
def done_list(request):
    todos = Todo.objects.filter(complete = True)
    return render(request, 'todo/done_list.html',{'todos':todos})
    
    
def todo_done(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')

def todo_delete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('todo:todo_list')


def todo_list(request):
    todos = Todo.objects.filter(complete = False)
    paginator = Paginator(todos,5)
    page_num = request.GET.get('page','1')
    page_obj = paginator.get_page(page_num)
    print(page_obj.paginator.num_pages)
    return render(request,'todo/todo_list.html',{'todos':page_obj})