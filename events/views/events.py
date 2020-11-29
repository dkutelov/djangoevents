from django.views.generic import ListView

from events.forms.filter_form import FilterForm
from events.forms.search_form import SearchForm
from events.models import Event
from events.views.utils import extract_filter_values


class EventsListingView(ListView):
    model = Event
    template_name = 'events/index.html'
    context_object_name = 'events'
    order_by_asc = True
    order_by = 'date'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        # self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'date' if self.order_by == FilterForm.ORDER_ASC else '-date'
        #TODO filter date today +
        #TODO filter category, city
        #TODO sort by date, price
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
        })
        context['search_form'] = SearchForm(initial={
            'text': self.contains_text
        })
        return context
