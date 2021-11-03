from django.shortcuts import redirect, render
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Board, Reply
from acc.models import User


# Create your views here.

def index(request):
    page = request.GET.get('page', 1)
    b = Board.objects.all()
    b = b.order_by('-pubdate')

    pag = Paginator(b, 6)
    obj = pag.get_page(page)

    context = {
        "blist" : obj,
    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        "bo" : b,
        "rep" : r,
    }
    return render(request, "board/detail.html", context)

def create_rep(request, bpk):
    b = Board.objects.get(id=bpk)
    com = request.POST.get("comment")
    rep = request.user.username
    if com:
        Reply(boa=b, replyer=rep, comment=com, pubdate2=timezone.now()).save()
    return redirect('board:detail', bpk=bpk)   

def delete_rep(request, bpk, rpk):
    r = Reply.objects.get(id=rpk)
    if request.user.username == r.replyer:
        r.delete()
    return redirect('board:detail', bpk=bpk)

def create(request):
    if request.method == "POST":
        wri = request.user.username
        pic = request.FILES.get("picture")
        con = request.POST.get("content")
        Board(picture=pic, writer=wri, content=con, pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(request, "board/create.html")

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user.username == b.writer:
        b.delete()
    return redirect("board:index")

def modify(request, bpk):
    b = Board.objects.get(id=bpk)
    context = {
        "bo" : b,
    }
    if request.method == "POST":
        con = request.POST.get("content")
        b.content = con
        b.pubdate = timezone.now()
        b.save()
        return redirect("board:index")
    return render(request, "board/modify.html", context)

def addlike(request, bpk):
    b = Board.objects.get(id=bpk)
    b.like.add(request.user)
    return redirect("board:detail", bpk=bpk)

def dellike(request, bpk):
    b = Board.objects.get(id=bpk)
    b.like.remove(request.user)
    return redirect("board:detail", bpk=bpk)