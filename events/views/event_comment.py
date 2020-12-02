from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import View

from comments.models import Comment
from events.forms.comment_form import CommentForm
from events.models import Event


class EventComment(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            event = Event.objects.get(pk=pk)
            comment = Comment(text=form.cleaned_data['text'])
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('events:event detail', pk)
