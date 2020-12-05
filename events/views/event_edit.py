from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from events.forms.event_create import CreateEventForm
from events.models import Event


class EventEditView(UpdateView):
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

    # def get(self, request, pk):
    #     if not has_access_to_modify(self.request.user, self.get_object()):
    #         return render(request, 'permission_denied.html')
    #     instance = Furniture.objects.get(pk=pk)
    #     form = CreateFurnitureForm(request.POST or None, instance=instance)
    #     return render(request, 'furniture_create.html', {'form': form})