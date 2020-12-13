from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField

from accounts.models import Profile


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class UserProfileForm(forms.ModelForm):
    userPhotoURL = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 400,
            'height': 400,
            'folder': 'events/user-photos'
        }
    )

    class Meta:
        model = Profile
        exclude = ('user', )
        labels = {
            'userPhotoURL': 'Upload you photo',
            'about': 'Introduce yourself to potential friends',
            'city': 'Your city'
        }
        widgets = {
            'about': forms.Textarea(attrs={'class': 'form-textarea'})
        }


class ResetPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailField(max_length=200))


