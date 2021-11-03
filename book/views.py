from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Book


# Create your views here.

def index(request):
    b = Book.objects.all()
    context = {
        "book" : b,
    }
    return render(request, "book/index.html", context)

def create(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        surl = request.POST.get("surl")
        Book(user=request.user, site_name=sname, site_url=surl, ctime=timezone.now()).save()
        return redirect("book:index")
    return redirect("book:index")

def check(request, bpk):
    b = Book.objects.get(id=bpk)
    if b.impo == False:
        b.impo = True
        b.save()
    return redirect("book:index")

def uncheck(request, bpk):
    b = Book.objects.get(id=bpk)
    if b.impo == True:
        b.impo = False
        b.save()
    return redirect("book:index")

def delete(request, bpk):
    b = Book.objects.get(id=bpk)
    if request.user:
        b.delete()
    return redirect("book:index")