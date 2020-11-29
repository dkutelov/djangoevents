from django.contrib import admin

from events.models import Event, Like

admin.site.register(Event)
admin.site.register(Like)
