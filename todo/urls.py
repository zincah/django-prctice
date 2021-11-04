from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name="index"),
    path('check/<dpk>', views.check, name="check"),
    path('uncheck/<dpk>', views.uncheck, name="uncheck"),
    path('delete/<dpk>', views.delete, name="delete"),
    path('create', views.create, name="create"),
    path('cheer/<dpk>', views.cheer, name="cheer"),
    path('uncheer/<dpk>', views.uncheer, name="uncheer")

]
