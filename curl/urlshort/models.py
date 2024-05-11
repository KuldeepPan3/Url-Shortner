from django.db import models

# Create your models here.
class UrlModel(models.Model):
    longurl = models.CharField(max_length=300)
    shorturl = models.CharField(max_length=7)
    count = models.IntegerField(default=0)

    def __str__(self) :
        return self.shorturl