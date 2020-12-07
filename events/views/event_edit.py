from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group

from events.forms.event_create import CreateEventForm
from events.models import Event


class EventEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/edit-event.html'
    context_object_name = 'event'

    def form_valid(self, form):
        form.instance.hosted_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        event = self.get_object()
        return f'/event/{event.id}'

    def test_func(self):
        event = self.get_object()
        user = self.request.user
        group = Group.objects.get(name='Admins')
        is_admin = group in user.groups.all()
        is_author = event.hosted_by == user
        return is_author or is_admin
