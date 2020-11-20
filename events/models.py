from django.db import models

from django.contrib.auth.models import User

from accounts.models import Profile
from events.enums import EventTypesEnum


class Event(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(blank=False)
    type = models.CharField(max_length=100,
                            choices=((event_type.name, event_type.value) for event_type in EventTypesEnum),
                            default='unknown')
    city = models.CharField(max_length=100, blank=False)
    venue = models.CharField(max_length=150, blank=False)
    venue_lat = models.FloatField(default=0)
    venue_lng = models.FloatField(default=0)
    ticket_price = models.PositiveIntegerField(default=0)
    hosted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interested = models.ManyToManyField(Profile, related_name='interested')
    going = models.ManyToManyField(Profile, related_name='going')
    likes = models.ManyToManyField(Profile, related_name='like')

    def __str__(self):
        return f'{self.name} - {self.date} - {self.get_type_display()}'


class EventPhoto(models.Model):
    photoURL = models.URLField(blank=False)
    event = models.ForeignKey(Profile, on_delete=models.CASCADE)

