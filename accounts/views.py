from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView

from accounts.models import Profile
from accounts.forms import UserSignupForm


def redirect_user(request):
    url = f'/furniture/'
    return HttpResponseRedirect(url)


class UserDetail(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = '/furniture/'
    template_name = 'accounts/signup.html'

