from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waller.views.home', name='home'),
    # url(r'^waller/', include('waller.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'waller.views.home'),
    url(r'^news/', 'waller.views.news'),
    url(r'^about/$', 'waller.views.about'),
    url(r'^products/$', 'waller.views.products'),
    url(r'^photos/$', 'waller.views.photos', {'slug': None}),
    url(r'^photos/(?P<slug>.+)/$', 'waller.views.photos'),
)
