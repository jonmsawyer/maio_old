from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maio.views.home', name='home'),
    # url(r'^maio/', include('maio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^get/(?P<tn>tn)/(?P<id>[a-zA-Z0-9-]{36})?', 'app.views.get_file', name='get_tn'),
    url(r'^get/(?P<id>[a-zA-Z0-9-]{36})?', 'app.views.get_file', name='get_file'),
    url(r'^videos/$', 'app.views.videos_index', name='videos_index'),
    url(r'^audio/$', 'app.views.audio_index', name='audio_index'),
    url(r'^images/rate/(?P<id>[a-zA-Z0-9-]{36})/(?P<rating>[0-5])/?', 'app.views.images_rate', name="images_rate"),
    url(r'^images/view/(?P<id>[a-zA-Z0-9-]{36})?', 'app.views.images_view', name="images_view"),
    url(r'^images/unset_random/$', 'app.views.images_unset_random', name="images_unset_random"),
    url(r'^images/getrandomnext/(?P<id>[a-zA-Z0-9-]{36})', 'app.views.images_getrandom_next', name="images_getrandom_next"),
    url(r'^images/getrandomprev/(?P<id>[a-zA-Z0-9-]{36})', 'app.views.images_getrandom_prev', name="images_getrandom_prev"),
    url(r'^images/getnext/(?P<id>[a-zA-Z0-9-]{36})', 'app.views.images_getnext', name="images_getnext"),
    url(r'^images/getprev/(?P<id>[a-zA-Z0-9-]{36})', 'app.views.images_getprev', name="images_getprev"),
    url(r'^images/getthis/(?P<id>[a-zA-Z0-9-]{36})', 'app.views.images_getthis', name="images_getthis"),
    url(r'^images/$', 'app.views.images_index', name='images_index'),
    url(r'^$', 'app.views.home', name='home'),
)
