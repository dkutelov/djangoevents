from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView

from accounts.models import Profile
from accounts.forms import UserSignupForm, UserSignInForm, UserProfileForm


def redirect_user(request):
    print(request.user)
    url = f'/accounts/profile/{request.user.id}'
    return redirect(url)


class UserDetail(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('accounts:user-create-profile')
        return render(request, self.template_name, {'form': form})


class SignIn(CreateView):
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
                # return redirect('events:home')
        return render(request, self.template_name, {'form': form})


# class UserCreateProfile(CreateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'accounts/profile-create.html'


@login_required
def user_create_profile(request):
    user = request.user
    # instance = get_object_or_404(UserProfile, user=user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(f'/accounts/profile/{user.id}')
    form = UserProfileForm()
    return render(request, 'accounts/profile-create.html', {'form': form})


# TODO create template
@login_required
def user_edit_profile(request):
    user = request.user
    instance = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/profile/edit')  # profile edit page
    form = UserProfileForm()
    return render(request, 'accounts/profile-create.html', {'form': form})


class ProfileDetail(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
