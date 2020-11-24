from django.urls import path, include
from .views import all_events, event_detail

app_name = 'events'
urlpatterns = [
    path('', all_events, name='home'),
    path('event/<int:pk>/', event_detail, name='event detail'),
]