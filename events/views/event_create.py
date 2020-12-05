from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from events.forms.event_create import CreateEventForm
from events.models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'events/create-event.html'
    form_class = CreateEventForm
    success_url = reverse_lazy('events:home')

    def form_valid(self, form):
        form.instance.hosted_by = self.request.user
        return super().form_valid(form)
