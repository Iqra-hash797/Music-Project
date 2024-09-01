from django.contrib import admin

# Register your models here.
from home.models import Song,Topsongs

admin.site.register(Song)
admin.site.register(Topsongs)