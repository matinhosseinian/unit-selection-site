from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^_nested_admin/', include('nested_admin.urls')),
    # Local apps
    # path("accounts/", include("accounts.urls")),
    path("", include("unit_selection.urls")),
]
