from django.views.generic import ListView
from django.utils import timezone

from events.forms.sort_form import SortForm
from events.forms.filter_form import FilterForm
from events.models import Event
from events.views.utils import extract_filter_values


class EventListView(ListView):
    model = Event
    template_name = 'events/index.html'
    context_object_name = 'events'
    order_by = 'date'
    contains_text = ''
    paginate_by = 12
    current_date = timezone.now()

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'date' if self.order_by == SortForm.ORDER_ASC or \
                             self.order_by == SortForm.ORDER_DATE else '-date'
        return self.model.objects.filter(date__gte=self.current_date)\
            .filter(name__icontains=self.contains_text)\
            .order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = SortForm(initial={
            'order': SortForm.ORDER_DATE,
        })
        context['search_form'] = FilterForm(initial={
            'text': self.contains_text
        })
        return context
