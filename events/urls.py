from django.urls import path, include

from .views.event_create import event_create
from .views.event_detail import event_detail
from .views.events import EventsListingView

app_name = 'events'
urlpatterns = [
    path('', EventsListingView.as_view(), name='home'),
    path('event/<int:pk>/', event_detail, name='event detail'),
    path('event/create/', event_create, name='event create'),
]