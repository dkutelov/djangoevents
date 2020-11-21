from django.urls import path, include
from .views import SignUp, UserDetail, redirect_user

urlpatterns = [
    path('profile/', redirect_user, name='profile'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
]