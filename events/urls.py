from django.urls import path, include

from .views.event_comment import EventComment
from .views.event_create import EventCreateView
from .views.event_delete import EventDeleteView

from .views.event_detail import EventDetail
from .views.event_edit import EventEditView
from .views.event_engage import EventGo, EventInterest, EventLike
from .views.events import EventListView
from .views.events_list_admin import EventAdminListView

app_name = 'events'
urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event detail'),
    path('event/<int:pk>/like', EventLike.as_view(), name='event like'),
    path('event/<int:pk>/interested', EventInterest.as_view(), name='event interest'),
    path('event/<int:pk>/going', EventGo.as_view(), name='event going'),
    path('event/<int:pk>/comment/<int:parent_id>', EventComment.as_view(), name='event comment'),
    path('event/create/', EventCreateView.as_view(), name='event create'),
    path('event/<int:pk>/edit/', EventEditView.as_view(), name='event edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event delete'),
    path('admin-list/', EventAdminListView.as_view(), name='events admin')
]