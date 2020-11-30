from django.shortcuts import redirect
from django.views.generic.base import View

from events.models import Event, Interested, Going


class EventInterest(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)

        if event.hosted_by.id == request.user.id:
            return redirect(f'/event/{pk}')

        interested = Interested.objects.filter(user_id=request.user.id, event=pk).first()

        if interested:
            interested.delete()
        else:
            interested = Interested(user=request.user, event=event)
            interested.save()
            going = Going.objects.filter(user_id=request.user.id, event=pk).first()

            if going:
                going.delete()

        return redirect(f'/event/{pk}/')
