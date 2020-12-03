from django.urls import path, include
from .views import SignUp, SignIn, UserDetail, redirect_user, user_create_profile, user_edit_profile, ProfileDetail

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', ProfileDetail.as_view(), name='user-profile'),  # view other users profile
    path('profile/edit/', user_edit_profile, name='user-edit-profile'),
    path('profile/create/', user_create_profile, name='user-create-profile'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
]