from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns = patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
