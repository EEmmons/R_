from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Location, Profile, Tag

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
    # contributor = User.objects.get(name=User.request.user.name)
    tag_list = Tag.objects#.filter(tag_name__exact='park')
    tags = forms.ModelMultipleChoiceField(queryset=tag_list)#, choices=tag_list)

    ratings = forms.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    popularity = forms.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    image = forms.ImageField()


    class Meta:
        model = Location
        fields = ("name", "description", 'tags', 'ratings', 'popularity', 'image')

    def clean_name(self):
        name = self.cleaned_data['name']


        r = Location.objects.filter(name__exact=name)
        if r.count():
            raise ValidationError("A location with that name already exists. Please change location name.")

        return name


class UserProfileForm(ModelForm):

    # def clean_profile_image(self):
    #     data = self.cleaned_data['profile_image']
    #     # filename = Profile.objects.filter(profile_image=profile_image)
    #     # if filename.invalid():
    #     #     raise  ValidationError("Profile image already exists")
    #     return data

    # def save(self, commit=True):
    #     profile = super(UserProfileForm, self).save(commit=False)
    #     profile.profile_image = self.cleaned_data["profile_image"]
    #     if commit:
    #         profile.save()
    #     return profile

    class Meta:
        model = Profile
        fields = ["profile_image"]
