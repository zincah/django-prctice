from django.shortcuts import redirect, render
from acc.models import User
from board.models import Board
from .models import Scrap
from django.utils import timezone


# Create your views here.

def index(request):
    b = Board.objects.all()
    s = Scrap.objects.all()
    s = s.order_by('-stime')
    context = {
        "myb" : b,
        "scrap" : s,
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
