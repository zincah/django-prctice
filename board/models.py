from datetime import datetime
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from acc.models import User

# Create your models here.

class Board(models.Model):
    picture = models.ImageField(upload_to="boa")
    writer = models.CharField(max_length=30)
    content = models.TextField()
    pubdate = models.DateTimeField()
    like = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.writer

    def summary(self):
        if len(self.content) > 30:
            return self.content[:30] + "..."
        return self.content

    def wri_pic(self):
        u = User.objects.get(username=self.writer)
        return u.getpic()

    # js 로 누르면 다 보이게 해주는 것도 될까?

class Reply(models.Model):
    boa = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer= models.CharField(max_length=20)
    comment = models.TextField()
    pubdate2 = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.replyer

class Scrap(models.Model):
    bo = models.ForeignKey(Board, on_delete=models.CASCADE)
    scrap = models.ManyToManyField(User, blank=True)

