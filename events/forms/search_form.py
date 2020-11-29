from django import forms


class SearchForm(forms.Form):
    text = forms.CharField(
        label='Looking for',
        widget=forms.TextInput(attrs={'placeholder': 'Event name'}),
        required=False,
    )
