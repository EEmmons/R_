from django.urls import path
from . import views
from UncommonGrounds.views import *

urlpatterns = [

	path('discover/', views.discover, name='discover'),
	path('about/', views.about, name='about'),
	path('', views.discover, name='discover'),
	path('profile/', views.profile, name='profile'),
	path('addUser/', views.addUser, name='addUser'),
	path('locations/', views.LocationListView.as_view(), name='locations'),
	path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
	path('profiles/', views.ProfileListView.as_view(), name='profiles'),
	path('tags/', views.TagListView.as_view(), name='tags'),
	path('comments/', views.CommentListView.as_view(), name='comments'),
	path('addLocation/', views.addLocation, name='addLocation',),
	path('location-autocomplete/', location_autocomplete, name='location-autocomplete')
]
