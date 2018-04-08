# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# import datetime #for checking renewal date range.
# from django.forms import ModelForm
# from .models import Profile

# class RenewBookModelForm(ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['profile_image',]
#         labels = { 'profile_image': _('Profile Image'), }
#         help_texts = { 'profile_image': _('Upload a photo.'), } 

# class ProfileForm(forms.Form):
#   profile_image = forms.ImageField()