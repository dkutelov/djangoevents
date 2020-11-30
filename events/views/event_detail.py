from django.views.generic import DetailView

from events.models import Event


class EventDetail(DetailView):
    model = Event
    template_name = 'events/event-detail.html'
    context_object_name = 'event'
    is_host = False
    liked = False
    interested = False
    going = False

    def dispatch(self, request, *args, **kwargs):
        event_id = self.kwargs['pk']
        event = Event.objects.get(pk=event_id)
        self.is_host = self.request.user.id == event.hosted_by.id
        self.liked = event.like_set.filter(user_id=request.user.id).exists()
        self.interested = event.interested_set.filter(user_id=request.user.id).exists()
        self.going = event.going_set.filter(user_id=request.user.id).exists()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_host'] = self.is_host
        context['liked'] = self.liked
        context['interested'] = self.interested
        context['going'] = self.going
        return context
