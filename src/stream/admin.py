from django.contrib import admin

from .models import Stream, StreamServer, StreamUser

# Register your models here.

admin.site.register(Stream)
admin.site.register(StreamServer)
admin.site.register(StreamUser)
