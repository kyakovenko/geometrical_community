__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from cms.sitemaps import CMSSitemap
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include, url, patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}})
)

urlpatterns += i18n_patterns('',

    # Examples:
    # url(r'^$', 'geometry.views.home', name='home'),
    # url(r'^geometry/', include('geometry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)
