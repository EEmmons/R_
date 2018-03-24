from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='index'),
	path('locations/', views.LocationListView.as_view(), name='locations'),
	path('users/', views.UserListView.as_view(), name='users'),
	path('tags/', views.TagListView.as_view(), name='tags'),
	path('comments/', views.CommentListView.as_view(), name='comments'),
]