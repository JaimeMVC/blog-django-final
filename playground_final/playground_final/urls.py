from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),           # Home, about, posts
    path('accounts/', include('accounts.urls')),  # Login, perfil, registro
    path('messenger/', include('messenger.urls')), # Mensajes
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
