from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import SignupView, LoginTokenView, LogoutTokenView, LogoutView

urlpatterns = [
    # JWT Auth
    path("api/token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/logout/", LogoutView.as_view(), name="token_logout"),
    # Token Auth
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginTokenView.as_view(), name="login"),
    path("logout/", LogoutTokenView.as_view(), name="logout"),
]
