from django.shortcuts import redirect, render
from .models import Todo
from acc.models import User
from django.utils import timezone

# Create your views here.

def index(request):
    d = Todo.objects.all()
    d = d.order_by('-cDate')
    context = {
        "todo" : d,
    }
    return render(request, "todo/index.html", context)

def check(request, dpk):
    d = Todo.objects.get(id=dpk)
    if request.user.username == d.writer:
        d.check = True
        d.save()
    return redirect("todo:index")

def uncheck(request, dpk):
    d = Todo.objects.get(id=dpk)
    if request.user.username == d.writer:
        d.check = False
        d.save()
    return redirect("todo:index")

def delete(request, dpk):
    b = Todo.objects.get(id=dpk)
    if request.user.username == b.writer:
        b.delete()
    return redirect("todo:index")

def create(request):
    if request.method == "POST":
        td = request.POST.get("todo")
        wri = request.user.username
        Todo(todo=td, writer=wri, cDate=timezone.now()).save()
    return redirect("todo:index")

def cheer(request, dpk):
    b = Todo.objects.get(id=dpk)
    if not request.user in b.cheer.all():
        b.cheer.add(request.user)
    return redirect("todo:index")

def uncheer(request, dpk):
    b = Todo.objects.get(id=dpk)
    if request.user in b.cheer.all():
        b.cheer.remove(request.user)
    return redirect("todo:index")