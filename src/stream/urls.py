from django.urls import path

from .views import StreamView

urlpatterns = [
    path("", StreamView.as_view()),
    path("<int:id>", StreamView.as_view())
    # path("<int:id>", DeviceView.as_view()),
]