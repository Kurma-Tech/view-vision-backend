from django.urls import path


from .views import ChannelsView, ServerView, DeviceChannel


urlpatterns = [
    path("", ServerView.as_view()),
    path("<int:id>", ServerView.as_view()),
    path("channel", DeviceChannel.as_view()),
    path("channel/<int:id>", DeviceChannel.as_view()),
    path("channel/channelView", ChannelsView.as_view())
]