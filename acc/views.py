from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def index(request):
    return render(request, "acc/index.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        nn = request.POST.get("nickname")
        em = request.POST.get("email")
        co = request.POST.get("comment")
        pi = request.FILES.get("picture")
        User.objects.create_user(username=un, password=pw, nickname=nn, email=em, comment=co, picture=pi)
        return redirect("acc:index")

    return render(request, "acc/signup.html")

def userlogin(request):
    if request.method =="POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
        return redirect("acc:index")
    return render(request, "acc/userlogin.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def profile(request):
    return render(request, "acc/profile.html")

def usermod(request):
    if request.method == "POST":
        un1 = request.user.username
        u = User.objects.get(username=un1)
        un2 = request.POST.get("username")
        pw = request.POST.get("password")
        nn = request.POST.get("nickname")
        em = request.POST.get("email")
        co = request.POST.get("comment")
        pi = request.FILES.get("picture")
        u.username = un2
        u.nickname = nn
        u.email = em
        u.comment = co
        if pw:
            u.set_password(pw)
        if pi:
            u.picture = pi
        u.save()
        user = authenticate(username=un2, password=pw)
        login(request, user)
        return redirect("acc:profile")
    return render(request, "acc/usermod.html")

def userdel(request):
    u = User.objects.get(username=request.user.username)
    u.delete()
    return redirect("acc:index")