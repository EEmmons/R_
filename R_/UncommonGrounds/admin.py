from django.contrib import admin

# Register your models here.
from .models import Location, Tag, Comment, Profile

admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Profile)
