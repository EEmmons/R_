from django.urls import path
from . import views
from UncommonGrounds.views import *

urlpatterns = [

	path('discover/', views.discover, name='discover'),
	path('about/', views.about, name='about'),
	path('', views.discover, name='discover'),
	path('addUser/', views.addUser, name='addUser'),
	path('locations/', views.discover_search, name='locations'),
	path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
	path('profiles/', views.ProfileListView.as_view(), name='profiles'),
	path('tags/', views.TagListView.as_view(), name='tags'),
	path('comments/', views.CommentListView.as_view(), name='comments'),
	path('location/create/', views.addLocation, name='location_form'),
	path('location-autocomplete/', location_autocomplete, name='location-autocomplete'),
	path('user-autocomplete/', user_autocomplete, name='user-autocomplete'),
	#path('profile/', views.RedirectView.as_view(url="{% url 'user_profile' user.username %}", permanent=False), name='active_user_profile')
	path('<username>/', views.profile_page, name='user_profile'),
	path('<username>/edit/<int:pk>', views.ProfileUpdate.as_view(), name='edit_profile'),
]

from django.conf.urls import url
urlpatterns += [
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	path('account_activated/', views.confirmed, name='confirmed')
]
