from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local Apps
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
]
