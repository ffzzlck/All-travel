from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from apps.home.views import set_language, index
from apps.about.views import about
from apps.contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path('set_language/<str:language>', set_language, name='set-language'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
