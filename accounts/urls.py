from django.urls import path, include
from .views import SignUp, SignIn, ProfileDetail, ProfileEditView, UserProfileList, ProfileCreateView
from .receivers import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='user-profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='user-edit-profile'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('user-list/', UserProfileList.as_view(), name='user list'),
    path('profile/create/', ProfileCreateView.as_view(), name='user-create-profile'),
]

