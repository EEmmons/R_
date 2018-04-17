from django.shortcuts import render
from .models import Location, Tag, Comment, Profile
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import *
from django.urls import reverse
import datetime
from random import randint
import json

# Create your views here.


def discover(request):
    """
    View function for home page of site.
    """

    # Generate counts of the main objects
    location_list = Location.objects.all()
    highest_rated  = None
    highest_rating = 0
    for location in location_list:
        if location.ratings > highest_rating:
            highest_rated = location
            highest_rating = location.ratings

    most_popular = None
    highest_popularity = 0
    for location in location_list:
        if location.popularity > highest_popularity:
            most_popular = location
            highest_popularity = location.popularity

    most_recent = location_list[0]
    latest_date = location_list[0].added
    for location in location_list:
        add = location.added
        add2 = location_list[0].added
        if location.added > latest_date:
            most_recent = location
            latest_date = location.added

    random = location_list[randint(0, len(location_list)-1)]
    while random == highest_rated or random == most_popular or random == most_recent:
        random = location_list[randint(0, len(location_list)-1)]



    num_tags = Tag.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'discover.html',
        context = {'location_list':location_list,
                   'highest_rated':highest_rated,
                   'most_popular': most_popular,
                   'most_recent':  most_recent,
                   'random': random}
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
from .forms import LocationAddForm

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

def location_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        locations = Location.objects.filter(name__icontains=query)
        results = []
        for loc in locations:
            place_json = loc.name
            results.append(place_json)
        data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


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

@login_required
def addLocation(request):

    if request.method == 'POST':
        form=LocationAddForm(request.POST)

        if form.is_valid():
            new_loc = form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = LocationAddForm()

    return render(request, 'UncommonGrounds/add_location.html', {'form': form})

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
