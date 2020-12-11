from django import forms

from events.enums import EventTypesEnum
from events.models import Event

city_choices = [(0, 'By city')] + [(city['city'], city['city'])for city in Event.objects.all().values("city").distinct()]
type_choices = [(0, 'By type')] + [(event_type.name, event_type.value) for event_type in EventTypesEnum]
type_choices = [type for type in type_choices if type[0] != "UNKNOWN"]


class FilterForm(forms.Form):
    text = forms.CharField(
        label='Looking for',
        widget=forms.TextInput(attrs={'placeholder': 'Event name', 'class': 'filter-text'}),
        required=False,
    )
    type = forms.ChoiceField(
        choices=type_choices,
        widget=forms.Select(
            attrs={
                'class': 'filter-select'
            }
        )
    )
    city = forms.ChoiceField(
        choices=city_choices,
        widget=forms.Select(
            attrs={
                'class': 'filter-select'
            }
        )
    )

