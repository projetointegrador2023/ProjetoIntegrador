from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro', include('registro.urls')),
    path('', RedirectView.as_view(url='/admin')),
    path('accounts/', include('django.contrib.auth.urls')),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
