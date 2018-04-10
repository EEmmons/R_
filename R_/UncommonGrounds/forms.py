#from django import forms
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# import datetime #for checking renewal date range.
#from django.forms import ModelForm
#from .models import Profile

# class RenewBookModelForm(ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['profile_image',]
#         labels = { 'profile_image': _('Profile Image'), }
#         help_texts = { 'profile_image': _('Upload a photo.'), } 

# class ProfileForm(forms.Form):
#   profile_image = forms.ImageField()

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Enter email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user