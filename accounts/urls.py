from django.urls import path, include
from .views import SignUp, SignIn, UserDetail, redirect_user, UserCreateProfile

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', redirect_user, name='profile'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='user-profile'),
    path('profile/<int:pk>/create', UserCreateProfile.as_view(), name='user-create-profile'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
]