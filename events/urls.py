from django.urls import path, include

from .views.event_create import event_create
from .views.event_detail import EventDetail
from .views.event_go import EventGo
from .views.event_interest import EventInterest
from .views.event_like import EventLike
from .views.events import EventsListingView

app_name = 'events'
urlpatterns = [
    path('', EventsListingView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event detail'),
    path('event/<int:pk>/like', EventLike.as_view(), name='event like'),
    path('event/<int:pk>/interested', EventInterest.as_view(), name='event interest'),
    path('event/<int:pk>/going', EventGo.as_view(), name='event going'),
    path('event/create/', event_create, name='event create'),
]