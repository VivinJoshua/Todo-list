from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import todoItem

def todoview(request):
    # return HttpResponse('Hello welcome')
    all_item=todoItem.objects.all();
    return render(request,'todo.html',{'all_value':all_item})

def addtodo(request):
    val=todoItem(content=request.POST['content'])
    val.save()
    return HttpResponseRedirect('/todo/')

def deletetodo(request,todo_id):
    val=todoItem.objects.get(id=todo_id)
    val.delete()
    return HttpResponseRedirect('/todo/')
