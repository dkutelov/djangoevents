from django.shortcuts import redirect
from django.views.generic.base import View

from events.models import Like, Event


class EventLike(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)

        if event.hosted_by.id == request.user.id:
            return redirect(f'/event/{pk}')
        # TODO is logged in

        like = Like.objects.filter(user_id=request.user.id, event=pk).first()

        if like:
            like.delete()
        else:
            like = Like(user=request.user, event=event)
            like.save()

        return redirect(f'/event/{pk}/')
