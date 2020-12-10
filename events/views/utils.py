from events.forms.sort_form import SortForm


def extract_filter_values(params):
    order = params['order'] if 'order' in params else SortForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }