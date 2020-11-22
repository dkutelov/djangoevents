from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from accounts.models import Profile
from accounts.forms import UserSignupForm, UserSignInForm


def redirect_user(request):
    url = f'/events/'
    return HttpResponseRedirect(url)


class UserDetail(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = '/profile/'
    template_name = 'accounts/signup.html'
    # if user:
    #     return HttpResponseRedirect(f'/profile/{user.id}')


class SignIn(CreateView):
    model = User
    template_name = 'accounts/signin.html'

    def get(self, request, *args, **kwargs):
        form = UserSignInForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                return HttpResponseRedirect('/events')
        return render(request, self.template_name, {'form': form})
