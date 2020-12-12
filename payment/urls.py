from django.urls import path
from . import views

urlpatterns = [
    path('make/<int:pk>/', views.payment, name='make payment'),
    path('thanks/', views.thanks, name='thanks'),
    path('cancel/', views.cancel, name='cancel'),
]
