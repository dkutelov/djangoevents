from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from accounts.models import Profile


def all_events(request):
    return render(request, 'events/events.html')


def event_detail(request, event_id):
    pass


@login_required
def event_create(request):
    current_profile = Profile.objects.get(user=request.user)
    print(current_profile.userPhotoURL.url)
    context = {
        'profile': current_profile
    }
    return render(request, 'events/create-event.html', context)
