from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group

from accounts.models import Profile
from accounts.forms import UserSignupForm, UserProfileForm
from shared.views import GroupRequiredMixin


class UserDetail(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('events:home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignIn(LoginView):
    model = User
    template_name = 'accounts/signin.html'

    def get_success_url(self):
        redirect_url = self.request.POST.get('return_url')
        return redirect_url if redirect_url else reverse_lazy('events:home')


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = UserProfileForm
    groups = ['Admins']

    def get_success_url(self):
        return f'/accounts/profile/{self.get_object().id}'

    def test_func(self):
        profile = self.get_object()
        user = self.request.user
        is_author = profile.user == user
        group = Group.objects.get(name='Admins')
        is_admin = group in user.groups.all()
        return is_author or is_admin


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'


class UserProfileList(GroupRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profiles.html'
    context_object_name = 'profiles'
    groups = ['Admins']


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'accounts/profile-create.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('events:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return f'/accounts/profile/{self.request.user.id}'
