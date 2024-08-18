from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    
    
    STATUS = (('Guest', 'Гостьовий аккаунт'),
            ('User', 'Користувач'),
            ('Admin', 'Адміністратор'))
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=20, choices=STATUS, default="Guest")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title