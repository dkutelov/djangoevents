from django.urls import path, include
from .views import SignUp, SignIn, ProfileCreateView, ProfileDetail, ProfileEditView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='user-profile'),  # view other users profile
    path('profile/edit/', ProfileEditView.as_view(), name='user-edit-profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='user-create-profile'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
]