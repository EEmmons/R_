from django.shortcuts import render
from .models import Location, User, Tag, Comment
from django.views import generic

# Create your views here.


def discover(request):
    """
    View function for home page of site.
    """

    # Generate counts of the main objects
    num_locations = Location.objects.all().count()
    num_users = User.objects.all().count()
    num_tags = Tag.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'discover.html',
        context = {'num_locations':num_locations,'num_users':num_users,'num_tags':num_tags}
    )

def profile(request):
    profile_favorites = User.favorites

    return render(
        request,
        'profile.html',
        context = {'profile_favorties':profile_favorites}
    )

def addLocation(request):
    return render(
        request,
        'add_location.html',
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
