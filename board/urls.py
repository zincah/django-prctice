from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<bpk>', views.detail, name="detail"),
    path('create_rep/<bpk>', views.create_rep, name="create_rep"),
    path('delete_rep/<bpk>/<rpk>', views.delete_rep, name="delete_rep"),
    path('create', views.create, name="create"),
    path('delete/<bpk>', views.delete, name="delete"),
    path('modify/<bpk>', views.modify, name="modify"),
    path('addlike/<bpk>', views.addlike, name="addlike"),
    path('dellike/<bpk>', views.dellike, name="dellike"),

]
