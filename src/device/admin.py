from django.contrib import admin

from .models import Device, DeviceType, UserDevice


admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(UserDevice)