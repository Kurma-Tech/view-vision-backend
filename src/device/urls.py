from django.urls import path

from .views import DeviceView

urlpatterns = [
    path("", DeviceView.as_view()),
    path("<int:id>", DeviceView.as_view()),
]