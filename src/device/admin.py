from django.contrib import admin

from .models import Server, DeviceType, UserServer, Device


# admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(UserServer)

class ServerAdmin(admin.ModelAdmin):
    list_display = ("server","server_name","user_name", "address","port")
   
    def server(self, obj):
        return obj.combined_fields()
    
admin.site.register(Server,  ServerAdmin)

admin.site.register(Device)      
        