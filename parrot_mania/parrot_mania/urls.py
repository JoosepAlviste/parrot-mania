from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = [
    url(r'^api/', include('parrot_mania.rest.urls')),
    url(r'^adminpanel/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    handler500 = 'parrot_mania.views.server_error'
    handler404 = 'parrot_mania.views.page_not_found'

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass


urlpatterns += [
    url(r'^$', RedirectView.as_view(url=settings.SITE_URL, permanent=False), name='app-redirect')
]
