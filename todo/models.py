from django.db import models
from acc.models import User

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    check = models.BooleanField(default=False)
    cheer = models.ManyToManyField(User, blank=True)
    cDate = models.DateTimeField()

    def __str__(self):
        return f"{self.writer} : {self.todo}"

    
# 버튼을 누르면 비공개 가능?