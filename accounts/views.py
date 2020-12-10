from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    success_url = reverse_lazy('user-create-profile')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        user.set_password(user.password)
        user.save()
        login(self.request, user)
        return valid


class SignIn(LoginView):
    model = User
    template_name = 'accounts/signin.html'

    def get_success_url(self):
        redirect_url = self.request.POST.get('return_url')
        return redirect_url if redirect_url else reverse_lazy('events:home')


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


