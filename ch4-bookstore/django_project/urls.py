from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path("anything-but-admin/", admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local Apps
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
] +  static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
