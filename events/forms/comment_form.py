from django import forms
from django.core.validators import MinLengthValidator


class CommentForm(forms.Form):
    text = forms.CharField(
        max_length=300,
        required=True,
        validators=[MinLengthValidator(2, message='Comment should be min 2 characters long.')],
        widget=forms.Textarea(
            attrs={
                'class': 'form-textarea',
                'placeholder': 'Comment should be min 2 character and max 300 characters.'
            }
        )
    )
