from django.db import models
from acc.models import User
from django.utils.timezone import datetime

# Create your models here.

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_url = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    stime = models.DateTimeField()
    
    def __str__(self):
        return self.comment
    
    
class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    mtime = models.DateTimeField()
    impo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.subject