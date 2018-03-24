from django.contrib import admin

# Register your models here.
from .models import User, Location, Tag, Comment

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Comment)
