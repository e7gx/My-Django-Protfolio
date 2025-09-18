from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    RELATION_CHOICES = [
        ('friend', 'Friend'),
        ('employee', 'Recruitment Employee'),
        ('other', 'Other'),
        ('family', 'Family'),
        ('colleague', 'Colleague'),
        ('client', 'Client'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES)

    def __str__(self):
        return f"{self.user.username} Profile"