from django.urls import reverse
from django.shortcuts import render
import stripe
from django.conf import settings

from events.models import Event


def payment(request, pk):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    event = Event.objects.get(pk=pk)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HxZtvAFQOjrfmLHzifQv42H',
            'quantity': 1
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('cancel'))
    )

    context = {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'event': event
    }

    return render(request, 'payment/payment.html', context)


def thanks(request):
    return render(request, 'payment/success.html')


def cancel(request):
    pass
