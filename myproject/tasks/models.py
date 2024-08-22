from django.db import models
from django.utils import timezone
# Create your models here.


class Commentary(models.Model):
    name = models.CharField(max_length=25, default="Anonym")
    text = models.TextField(default="Yeah, yeah, very intersting.")
    data = models.DateField(default=timezone.now)

class Publication(models.Model):
    name = models.CharField(max_length=25, default="Test_name")
    description = models.TextField(default="Blah blah blah")
    data = models.DateField(default=timezone.now)
    commentaries = models.ManyToManyField(Commentary)