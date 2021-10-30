from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    comment = models.TextField()
    nickname = models.CharField(max_length=30)
    email = models.EmailField()
    picture = models.ImageField(upload_to="usr")

    def getpic(self):
        if self.picture:
            return self.picture.url
        return "/media/noimg.png" 