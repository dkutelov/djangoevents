from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photoURL = models.URLField(blank=True)
    about = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)


