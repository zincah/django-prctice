from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('check/<bpk>', views.check, name="check"),
    path('uncheck/<bpk>', views.uncheck, name="uncheck"),
    path('delete/<bpk>', views.delete, name="delete"),
]
