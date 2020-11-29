from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import Profile


@login_required
def event_create(request):
    current_profile = Profile.objects.get(user=request.user)
    print(current_profile.userPhotoURL.url)
    context = {
        'profile': current_profile
    }
    return render(request, 'events/create-event.html', context)