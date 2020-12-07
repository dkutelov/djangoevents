from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from events.models import Event


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/delete-event.html'
    success_url = reverse_lazy('events:home')

    def test_func(self):
        event = self.get_object()
        user = self.request.user
        group = Group.objects.get(name='Admins')
        is_admin = group in user.groups.all()
        is_author = event.hosted_by == user
        return is_author or is_admin

