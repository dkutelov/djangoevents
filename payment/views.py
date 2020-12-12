from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    #create in terminal with stripe CLI stripe listen --forward-to localhost:8000/payment/stripe_webhook/
    endpoint_secret = 'whsec_xaiaGQm9xSrIT3laff4VEfsysBNHmObe'
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)