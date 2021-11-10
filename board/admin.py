from django.contrib import admin
from .models import Board, Reply, Scrap

# Register your models here.

admin.site.register(Board)
admin.site.register(Reply)
admin.site.register(Scrap)