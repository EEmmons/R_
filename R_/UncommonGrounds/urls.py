from django.urls import path
from . import views


urlpatterns = [

	path('', views.discover, name='discover'),
	path('locations/', views.LocationListView.as_view(), name='locations'),
	path('locations/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
	path('users/', views.UserListView.as_view(), name='users'),
	path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
	path('tags/', views.TagListView.as_view(), name='tags'),
	path('comments/', views.CommentListView.as_view(), name='comments'),
]
