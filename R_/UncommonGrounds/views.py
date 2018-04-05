from django.shortcuts import render
from .models import Location, User, Tag, Comment
from django.views import generic

# Create your views here.


def discover(request):
    """
    View function for home page of site.
    """

    # Generate counts of the main objects
    location_list = Location.objects.all()
    num_users = User.objects.all().count()
    num_tags = Tag.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'discover.html',
        context = {'location_list':location_list}
    )

def profile(request):
    profile_favorites = User.favorites

    return render(
        request,
        'UncommonGrounds/profile.html',
        context = {'profile_favorites':profile_favorites}
    )

def addUser(request):
    return render(
        request,
        'UncommonGrounds/add_user.html',
    )

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


class LocationListView(generic.ListView):
    model = Location

class LocationDetailView(generic.DetailView):
    model = Location

class UserListView(generic.ListView):
    model = User

class UserDetailView(generic.DetailView):
    model = User

class TagListView(generic.ListView):
    model = Tag

class CommentListView(generic.ListView):
	model = Comment
