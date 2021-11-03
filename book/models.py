from django.db import models
from acc.models import User

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=30)
    site_url = models.TextField()
    impo = models.BooleanField(default=False)
    ctime = models.DateTimeField()

    def __str__(self):
        return self.site_name

    def surl(self):
        if len(self.site_url) > 50:
            return self.site_url[:50] + "..."
        return self.site_url

