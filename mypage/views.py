from django.shortcuts import redirect, render
from acc.models import User
from board.models import Board
from .models import Scrap, Memo
from django.utils import timezone


# Create your views here.

def index(request):
    b = Board.objects.all()
    s = Scrap.objects.all()
    m = Memo.objects.all()
    s = s.order_by('-stime')
    m = m.order_by('-mtime')
    context = {
        "myb" : b,
        "scrap" : s,
        "memo" : m,
    }
    return render(request, "mypage/index.html", context)

def scrap(request, bpk):
    #print(dir(request))
    #print(request.path)
    user = request.user
    surl = bpk
    com = request.POST.get("comment")
    s = Scrap(user=user, site_url=surl, comment=com, stime=timezone.now())
    s.save()
    return redirect("mypage:index")

# pagination 기능 추가하기

def memoadd(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        con = request.POST.get("content")
        m = Memo(user=request.user, subject=sub, content=con, mtime=timezone.now())
        m.save()
        return redirect("mypage:index")
    return render(request, "mypage/memoadd.html")

def memodetail(request, mpk):
    m = Memo.objects.get(id=mpk)
    if request.user.username == m.user.username:
        context={
            "memo" : m,
        }
    else:
        return render(request, "error/forbidden.html")
    return render(request, "mypage/memodetail.html", context)

def memomodify(request, mpk):
    m = Memo.objects.get(id=mpk)
    context = {
        "memo" : m,
    }
    if request.method == "POST":
        m.subject = request.POST.get("subject")
        m.content = request.POST.get("content")
        m.save()
        return redirect("mypage:memodetail", mpk=mpk)
    return render(request, "mypage/memomodify.html", context)

