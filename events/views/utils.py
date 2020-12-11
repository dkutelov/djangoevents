from events.forms.sort_form import SortForm


def extract_filter_values(params):
    order = params['order'] if 'order' in params else SortForm.ORDER_ASC
    text = params['text'] if 'text' in params and params['text'] != '' else None

    city = params['city'] if 'city' in params and params['city'] != "0" else None
    event_type = params['type'] if 'type' in params and params['type'] != "0" else None

    return {
        'order': order,
        'text': text,
        'city': city,
        'type': event_type,
    }