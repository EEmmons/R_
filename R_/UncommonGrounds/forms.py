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
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Location

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

class LocationAddForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Enter the name of location")
    description = forms.CharField(max_length=1000, help_text="Brief description of location")
#     image = forms.ImageField()
#     tags = forms.ModelMultipleChoiceField()

    class Meta:
        model = Location
        fields = ("name", "description")

    def clean_d(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        r = Location.objects.filter(name=name)
        if r.count():
            raise ValidationError("A location with that name already exists. Please change location name.")
        return name, description

    def save(self, commit=True):
        location = super(LocationAddForm, self).save(commit=False)
        location.name = self.cleaned_data["name"]
        location.description = self.cleaned_data["description"]

        if commit:
            location.save()
        return location
