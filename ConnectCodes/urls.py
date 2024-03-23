from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/',include("api.urls")),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('room/', include('rooms.urls')),
    path('profile/', include('accounts.urls')),
    path("accounts/", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

