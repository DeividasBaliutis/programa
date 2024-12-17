from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("programa/", include("programa.urls")),
    path("admin/", admin.site.urls),
]