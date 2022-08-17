from django.contrib import admin

from .models import Stream, StreamDevice, StreamUser

# Register your models here.

admin.site.register(Stream)
admin.site.register(StreamDevice)
admin.site.register(StreamUser)
