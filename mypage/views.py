from django.shortcuts import render
from acc.models import User
from board.models import Board

# Create your views here.

def index(request):
    b = Board.objects.all()
    context = {
        "myb" : b
    }
    return render(request, "mypage/index.html", context)