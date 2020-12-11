from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField

from accounts.models import Profile


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'John Doe'})
        self.fields['email'].widget.attrs.update({'placeholder': 'johndoe@mail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': '8+ characters'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat password'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# TODO city and description validation
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


