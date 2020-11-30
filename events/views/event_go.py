from django.shortcuts import redirect
from django.views.generic.base import View

from events.models import Event, Interested, Going


class EventGo(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)

        if event.hosted_by.id == request.user.id:
            return redirect(f'/event/{pk}')

        going = Going.objects.filter(user_id=request.user.id, event=pk).first()

        if going:
            going.delete()
        else:
            going = Going(user=request.user, event=event)
            going.save()
            interested = Interested.objects.filter(user_id=request.user.id, event=pk).first()

            if interested:
                interested.delete()

        return redirect(f'/event/{pk}/')

