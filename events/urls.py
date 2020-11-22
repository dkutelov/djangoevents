from django.urls import path, include
from .views import all_events, event_detail

urlpatterns = [
    path('events/', all_events, name='events'),
    path('event/<int:pk>/', event_detail, name='event detail'),
]