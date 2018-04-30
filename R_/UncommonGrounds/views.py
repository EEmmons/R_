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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

# Create your views here.


@csrf_exempt
def discover(request):
    """
    View function for home page of site.
    """


    # Generate counts of the main objects
    unfiltered_list = Location.objects.all()
    highest_rated  = None
    highest_rating = 0
    for location in unfiltered_list:
        if location.ratings > highest_rating:
            highest_rated = location
            highest_rating = location.ratings

    most_popular = None
    highest_popularity = 0
    for location in unfiltered_list:
        if location.popularity > highest_popularity:
            most_popular = location
            highest_popularity = location.popularity

    most_recent = unfiltered_list[0]
    latest_date = unfiltered_list[0].added
    for location in unfiltered_list:
        add = location.added
        add2 = unfiltered_list[0].added
        if location.added > latest_date:
            most_recent = location
            latest_date = location.added

    random = unfiltered_list[randint(0, len(unfiltered_list)-1)]
    while random == highest_rated or random == most_popular or random == most_recent:
        random = unfiltered_list[randint(0, len(unfiltered_list)-1)]

    location_list = []

    test = None
    if request.method == 'GET':
        search = request.GET.get("search")
        if search is None:
            search = ""
        # test = "TEST"
        words = search.lower().split(" ")
        for word in words:
            for location in unfiltered_list:
                locationWords = []
                t = location.tags.all()
                n = location.name.lower().split(" ")
                d = location.description.lower().split(" ")
                locationWords += list(location.tags.all())
                locationWords += location.name.lower().split(" ")
                locationWords += location.description.lower().split(" ")
                if word in locationWords:
                    location_list += [location]

        # location


        template = loader.get_template('discover.html')
        context = {'location_list': location_list,
                   'highest_rated': highest_rated,
                   'most_popular': most_popular,
                   'most_recent': most_recent,
                   'random': random,
                   'test': test}

        num_tags = Tag.objects.all().count()

        # Render the HTML template index.html with the data in the context variable
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('discover.html')
        context = {'location_list': location_list,
                   'highest_rated': highest_rated,
                   'most_popular': most_popular,
                   'most_recent': most_recent,
                   'random': random,
                   'test': test}
        return HttpResponse(template.render(context, request))
    # if post request came
    # words = None
    # if request.method == 'POST':
    #     # getting values from post
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #
    #     words = name.split(" ")
    #     # adding the values in a context variable
    #     context = {
    #         # 'name': name,
    #         # 'email': email,
    #         # 'phone': phone,
    #         'words': words
    #     }
    #
    #     # getting our showdata template
    #     template = loader.get_template('showdata.html')
    #
    #     # returing the template
    #     return HttpResponse(template.render(context, request))
    # else:
    #     # if post request is not true
    #     # returing the form template
    #     template = loader.get_template('index.html')
    #     return HttpResponse(template.render())

@csrf_exempt
def discover_search(request):
    """
    View function for home page of site.
    """


    # Generate counts of the main objects
    unfiltered_list = Location.objects.all()
    highest_rated  = None
    highest_rating = 0
    for location in unfiltered_list:
        if location.ratings > highest_rating:
            highest_rated = location
            highest_rating = location.ratings

    most_popular = None
    highest_popularity = 0
    for location in unfiltered_list:
        if location.popularity > highest_popularity:
            most_popular = location
            highest_popularity = location.popularity

    most_recent = unfiltered_list[0]
    latest_date = unfiltered_list[0].added
    for location in unfiltered_list:
        add = location.added
        add2 = unfiltered_list[0].added
        if location.added > latest_date:
            most_recent = location
            latest_date = location.added

    random = unfiltered_list[randint(0, len(unfiltered_list)-1)]
    while random == highest_rated or random == most_popular or random == most_recent:
        random = unfiltered_list[randint(0, len(unfiltered_list)-1)]

    location_list = []

    if request.method == 'GET':
        search = request.GET.get("search")
        if search is None:
            search = ""
        # = ""
        words = search.lower().split(" ")
        for word in words:
            for location in unfiltered_list:
                locationWords = []
                t = location.tags.all()
                n = location.name.lower().split(" ")
                d = location.description.lower().split(" ")
                locationWords += list(location.tags.all())
                locationWords += location.name.lower().split(" ")
                locationWords += location.description.lower().split(" ")
                if word in locationWords:
                    location_list += [location]

        # location


        template = loader.get_template('UncommonGrounds/location_list.html')
        context = {'location_list': location_list,
                   'highest_rated': highest_rated,
                   'most_popular': most_popular,
                   'most_recent': most_recent,
                   'random': random,
                   }

        num_tags = Tag.objects.all().count()

        # Render the HTML template index.html with the data in the context variable
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('discover.html')
        context = {'location_list': location_list,
                   'highest_rated': highest_rated,
                   'most_popular': most_popular,
                   'most_recent': most_recent,
                   'random': random,
                   'test': test}
        return HttpResponse(template.render(context, request))

from UncommonGrounds.forms import UserCreateForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import LocationAddForm
from .models import Location
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin

def addUser(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your UncommonGrounds account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #new_user = form.save()
            messages.success(request, 'Account created successfully. Please verify and activate your account through your email')
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


# def user_autocomplete(request):
#     if request.is_ajax():
#         query = request.GET.get('term', '')
#         users = Profile.objects.filter(user.username__icontains=query)
#         results = []
#         for u in users:
#             user_json = u.name
#             results.append(user_json)
#         data = json.dumps(results)
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)



@login_required
def addLocation(request):

    if request.method == 'POST':
        form = LocationAddForm(request.POST, request.FILES)

        if form.is_valid():
            new_loc = form.save(commit=True)
            new_loc.contributor = request.user.profile
            new_loc.save()
            messages.success(request, 'Location added successfully')
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = LocationAddForm()

    return render(request, 'UncommonGrounds/location_form.html', {'form': form})

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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        # return redirect('home')
        return HttpResponseRedirect("/UncommonGrounds/account_activated/")
    else:
        return HttpResponse('Activation link is invalid!')

def confirmed(request):
    return render(
        request,
        'UncommonGrounds/account_activation_successful.html',
        )

#profile page using user name as url
@login_required
def profile_page(request, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        user = request.user

    return render(request, 'UncommonGrounds/profile.html', {'profile_user': user})

from .forms import UserProfileForm
#user profile form
@login_required
def edit_profile(request, username):
    profile = Profile.objects.get(user=request.user)
    form = UserProfileForm(request.POST, request.FILES, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
        else:
            print (form.errors)
    else:
        form = UserProfileForm()

    return render(request, 'UncommonGrounds/edit_profile.html', {'form': form})

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['profile_image']
    success_url = '../'
