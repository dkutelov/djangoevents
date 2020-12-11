from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic.base import View

from events.models import Event, Interested, Going, Like


class EventEngage(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/accounts/signin/'
    event = None

    def test_func(self):
        event_id = self.kwargs['pk']
        event = Event.objects.get(pk=event_id)
        return event.hosted_by != self.request.user

    def get(self, request, pk):
        event = Event.objects.get(pk=pk)

        if event.hosted_by == request.user:
            return redirect(f'/event/{pk}')

        self.event = event


class EventLike(EventEngage):
    def get(self, request, pk):
        super().get(request, pk)
        like = Like.objects.filter(user_id=request.user.id, event=pk).first()

        if like:
            like.delete()
        else:
            like = Like(user=request.user, event=self.event)
            like.save()

        return redirect(f'/event/{pk}/')


class EventInterest(EventEngage):
    def get(self, request, pk):
        super().get(request, pk)
        interested = Interested.objects.filter(user_id=request.user.id, event=pk).first()

        if interested:
            interested.delete()
        else:
            interested = Interested(user=request.user, event=self.event)
            interested.save()

            going = Going.objects.filter(user_id=request.user.id, event=pk).first()
            if going:
                going.delete()

        return redirect(f'/event/{pk}/')


class EventGo(EventEngage):
    def get(self, request, pk):
        super().get(request, pk)
        going = Going.objects.filter(user_id=request.user.id, event=pk).first()

        if going:
            going.delete()
        else:
            going = Going(user=request.user, event=self.event)
            going.save()
            interested = Interested.objects.filter(user_id=request.user.id, event=pk).first()

            if interested:
                interested.delete()

        return redirect(f'/event/{pk}/')

