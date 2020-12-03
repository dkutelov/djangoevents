from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userPhotoURL = CloudinaryField('image')
    about = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username}'
