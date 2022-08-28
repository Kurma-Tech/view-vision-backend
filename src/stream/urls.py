from django.urls import path

from .views import StreamView
from .api import StreamAPI

urlpatterns = [
    path("", StreamView.as_view()),
    path("<int:id>", StreamView.as_view()),
    path("streamapi/<int:id>", StreamAPI.as_view())
]