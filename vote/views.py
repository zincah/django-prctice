from django.http import request
from django.shortcuts import redirect, render
from .models import Topic, Choice
from acc.models import User
from django.utils import timezone


# Create your views here.

def index(request):
    t = Topic.objects.all()
    t = t.order_by('-cDate')
    context = {
        "topic" : t
    }
    return render(request, "vote/index.html", context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    u = User.objects.get(username=t.writer)
    c = t.choice_set.all()
    context = {
        "topic" : t,
        "pic" : u.getpic(),
        "choice" : c,
    }
    return render(request, "vote/detail.html", context)

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        s = request.POST.get("select")
        c = Choice.objects.get(id=s)
        c.voter.add(request.user)
    return redirect("vote:detail", tpk=tpk)

def cancel(request, tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    c = t.choice_set.all()
    for i in c:
        if request.user in i.voter.all():
            i.voter.remove(request.user)
    return redirect("vote:detail", tpk=tpk)
    
def create(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        wri = request.user.username
        con = request.POST.get("content")
        t = Topic(subject=sub, writer=wri, content=con, cDate=timezone.now())
        t.save()
        sel = request.POST.getlist("select")
        pic = request.FILES.getlist("picture")
        
        for i,j in zip(sel, pic):
            print(i, j)
            Choice(top=t, select=i, pic=j).save()
        return redirect("vote:index")
    return render(request, "vote/create.html")

def delete(request, tpk):
    t = Topic.objects.get(id=tpk)
    t.delete()
    return redirect("vote:index")