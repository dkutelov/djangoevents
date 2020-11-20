from django.contrib.auth.models import User
from django.db import models

from events.models import Event


class Comment(models.Model):
    text = models.TextField(max_length=250)
    created_at = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.text}'
