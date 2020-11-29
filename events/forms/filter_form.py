from django import forms


class FilterForm(forms.Form):
    ORDER_DATE = 'by_date'
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_DATE, 'By date'),
        (ORDER_ASC, 'ascending'),
        (ORDER_DESC, 'descending'),
    )

    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': "dropdown-select-navigation"})
    )
