from django.db import models
from acc.models import User

# Create your models here.

class Topic(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    voter = models.ManyToManyField(User, blank=True)
    content = models.TextField()
    cDate = models.DateTimeField()

    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) > 30:
            return self.content[:30] + "..."
        return self.content

    
class Choice(models.Model):
    top = models.ForeignKey(Topic, on_delete=models.CASCADE)
    select = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="vote/%y")
    voter = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.top} : {self.select}"

    def getpic(self):
        if self.pic:
            return self.pic.url 
        return "/media/noimg.png"

