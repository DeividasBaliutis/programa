from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("programa/", include("programa.urls")),
    path("admin/", admin.site.urls),
    path('', RedirectView.as_view(url='programa/', permanent=True)),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)