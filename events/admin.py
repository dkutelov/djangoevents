from django.contrib import admin

from events.models import Event, Like, Interested, Going

admin.site.register(Event)
admin.site.register(Like)
admin.site.register(Interested)
admin.site.register(Going)
