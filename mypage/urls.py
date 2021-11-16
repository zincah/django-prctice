from django.urls import path
from . import views

app_name = "mypage"
urlpatterns = [
    path('', views.index, name="index"),
    path('scrap/<bpk>', views.scrap, name="scrap"),
    path('memoadd', views.memoadd, name="memoadd"),
    path('memodetail/<mpk>', views.memodetail, name="memodetail"),
    path('memomodify/<mpk>', views.memomodify, name="memomodify"),
    
    
] 
