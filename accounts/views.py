from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from accounts.models import Profile
from accounts.forms import UserSignupForm, UserSignInForm, UserProfileForm
from shared.views import GroupRequiredMixin


class UserDetail(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'accounts/signup.html'

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('user-create-profile')
        return render(request, self.template_name, {'form': form})


class SignIn(View):
    model = User
    template_name = 'accounts/signin.html'

    @staticmethod
    def get_redirect_url(params):
        redirect_url = params.get('return_url')
        return redirect_url if redirect_url else 'events:home'

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
                login(request, user)
                redirect_url = self.get_redirect_url(request.POST)
                return redirect(redirect_url)
        return render(request, self.template_name, {'form': form})


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


class ProfileEditView(LoginRequiredMixin, FormView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return f'/accounts/profile/{self.request.user.id}'

    def get_form(self, form_class=UserProfileForm):
        try:
            profile = Profile.objects.get(user=self.request.user)
            return form_class(instance=profile, **self.get_form_kwargs())
        except Profile.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ProfileDetail(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class UserProfileList(GroupRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profiles.html'
    context_object_name = 'profiles'
    paginate_by = 12
    groups = ['Admins']


class OtherProfileEditView(GroupRequiredMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = UserProfileForm
    groups = ['Admins']


