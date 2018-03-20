from django.contrib import admin

# Register your models here.
from .models import User, Location, Tag

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Tag)
