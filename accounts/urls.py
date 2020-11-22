from django.urls import path, include
from .views import SignUp, SignIn, UserDetail, redirect_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', redirect_user, name='profile'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='user-profile'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
]