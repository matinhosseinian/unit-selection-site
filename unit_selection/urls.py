from django.urls import path
from .views import HomePage, AboutPageView, Suggest

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("suggest/", Suggest, name="suggest"),
    path("", HomePage, name="home"),
]
