from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defualt.jpg', upload_to='profile_pics')
# Create your models here.

    def __str__(self):
        return f'{self.user.username} Profile'
