from django.urls import path
from . import views

app_name = "mypage"
urlpatterns = [
    path('', views.index, name="index"),
    path('scrap/<bpk>', views.scrap, name="scrap"),
    path('memoadd', views.memoadd, name="memoadd"),
    path('memodetail/<mpk>', views.memodetail, name="memodetail"),
    path('memomodify/<mpk>', views.memomodify, name="memomodify"),
    path('memodelete/<mpk>', views.memodelete, name="memodelete"),
    path('impo/<mpk>', views.impo, name="impo"),
    path('unimpo/<mpk>', views.unimpo, name="unimpo"),
    path('scrapdel/<spk>', views.scrapdel, name="scrapdel"),
    
] 
