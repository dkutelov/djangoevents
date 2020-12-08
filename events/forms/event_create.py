from cloudinary.forms import CloudinaryFileField
from django import forms
from django.core.exceptions import ValidationError

from events.models import Event


class CreateEventForm(forms.ModelForm):
    event_photo = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 400,
            'height': 400,
            'folder': 'events/event-photos'
        }
    )

    class Meta:
        model = Event
        fields = ('event_photo', 'name', 'description', 'type', 'date', 'city', 'venue', 'venue_address',
                  'venue_lat', 'venue_lng', 'ticket_price')
        labels = {
            'name': 'Name of your event',
            'description': 'Short description of your event',
            'date': 'Date of the event'
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker', 'id': 'datetime'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'})
        }

    def clean(self):
        if len(self.cleaned_data['city']) < 2:
            raise ValidationError('City name should be 2 characters and more')

        if len(self.cleaned_data['name']) < 3:
            raise ValidationError('Event name should be 3 characters and more')

        if len(self.cleaned_data['venue']) < 2:
            raise ValidationError('City name should be 2 characters and more')

        ticket_price = self.cleaned_data['ticket_price']
        if not isinstance(ticket_price, int) or ticket_price < 0:
            raise ValidationError('Ticket price must be zero or positive number')

        venue_lat = self.cleaned_data['venue_lat']
        venue_lng = self.cleaned_data['venue_lng']
        if venue_lat != 0 or venue_lng != 0:
            if not isinstance(venue_lat, float) and venue_lat >= 0:
                raise ValidationError('Venue latitude must be zero or positive number')
            if not isinstance(venue_lng, float) and venue_lng >= 0:
                raise ValidationError('Venue latitude must be zero or positive number')

