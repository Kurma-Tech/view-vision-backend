from django.contrib import admin


from .models import Business, User

admin.site.register(User)
admin.site.register(Business)