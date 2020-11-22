from django.shortcuts import render


# Create your views here.
def all_events(request):
    return render(request, 'events/events.html')


def event_detail(request, event_id):
    pass