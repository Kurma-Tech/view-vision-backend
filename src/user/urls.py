from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import SimpleRouter


from src.user import views
from src.user import apis
# from .views import UserView


auth_urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    # path(
    #     # "refresh/", TokenRefreshView.as_view(), name="token_refresh"
    # ),
    # path("", UserView.as_view(), name="User View"),
    path("register/", apis.RegistrationView.as_view(), name="registration"),
     path("registerBusiness/", apis.BusinessRegestrationView.as_view(), name="business_registration"),
]

urlpatterns = [
    path("auth/", include(auth_urlpatterns)),
]