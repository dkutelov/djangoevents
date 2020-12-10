from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils import timezone

from events.models import Event
from shared.views import GroupRequiredMixin


class EventAdminListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/admin-list.html'
    context_object_name = 'events'
    order_by = 'date'
    paginate_by = 12
    current_date = timezone.now()
    groups = ['Admins']

    def get_queryset(self):
        return self.model.objects.filter(date__gte=self.current_date).order_by(self.order_by)
