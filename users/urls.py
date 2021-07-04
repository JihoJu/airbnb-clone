from os import name
from django.urls import path
from django.urls.base import reverse_lazy
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "verify/<str:key>/", views.complete_verification, name="complete-verification"
    ),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path(
        "update-password/",
        views.UpdatePasswordView.as_view(success_url=reverse_lazy("core:home")),
        name="password",
    ),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("switch-hosting/", views.switch_hosting, name="switch-hosting"),
]
