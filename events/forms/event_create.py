from cloudinary.forms import CloudinaryFileField
from django import forms

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
        exclude = ('hosted_by',)
        labels = {
            'name': 'Name of your event',
            'description': 'Short description of your event',
            'event_photo': 'Inspiring photo for your event'
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker', 'id': 'datetime'})
        }
# class CreateFurnitureForm(forms.ModelForm):
#
#     make = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     model = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     description = forms.CharField(required=True ,widget=forms.Textarea(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     price = forms.IntegerField(required=True,
#                             validators=[MinValueValidator(10)],
#                             widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'type': 'number'
#         }
#     ))
#     image_url = forms.URLField(required=True, widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     material = forms.ModelChoiceField(queryset=Material.objects.all(),
#                                       widget=forms.Select(
#                                           attrs={
#                                               'class': 'form-control'
#                                           }
#                                       ))
#
#
#     class Meta:
#         model = Furniture
#         fields = ('id', 'make', 'model', 'description', 'price', 'image_url', 'material')