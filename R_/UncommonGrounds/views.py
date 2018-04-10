from django.shortcuts import render
from .models import Location, Tag, Comment, Profile
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.


def discover(request):
    """
    View function for home page of site.
    """

    # Generate counts of the main objects
    location_list = Location.objects.all()
    num_tags = Tag.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'discover.html',
        context = {'location_list':location_list}
    )

def profile(request):
    favorites_list = Profile.objects.all()

    return render(
	    request,
	    'UncommonGrounds/profile.html',
        context = {'favorites_list':favorites_list}
	)

def users(request):
    return render(
	    request,
	    'UncommonGrounds/user_list.html',
	)

from UncommonGrounds.forms import UserCreateForm
from django.contrib.auth import login
from django.contrib import messages

def addUser(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect("/accounts/login/")
            # redirect, or however you want to get to the main view
    else:
        form = UserCreateForm()

    return render(request, 'UncommonGrounds/add_user.html', {'form': form}) 

def about(request):
    return render(
	    request,
	    'UncommonGrounds/about.html',
	    )

def login(request):
    return render(
	    request,
	    'UncommonGrounds/login.html',
	    )

# @login_required
# def add_profile(request):
#     if request.method == 'GET':
#         form = ProfileForm()
#     else:
#         user=Profile.object.get(pk=request.profile.id)
#         form=ProfileForm(request.POST, request.FILES)
#         pic=Profile(profile_image=request.FILES['profile_image'])
#         print ("......image.....", pic.profile_image)
#         pic.save()

#         return redirect('/profile/')
#     return render(request, 'profile.html', {'form':form})

class LocationListView(generic.ListView):
    model = Location

class LocationDetailView(generic.DetailView):
    model = Location

class TagListView(generic.ListView):
    model = Tag

class CommentListView(generic.ListView):
	model = Comment

class UserListView(generic.ListView):
	model = User

class ProfileListView(generic.ListView):
	model = Profile
