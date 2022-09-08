from django.urls import path

from .views import SignupPageView, UserLoginView, UserLogout

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogout, name="logout"),
]