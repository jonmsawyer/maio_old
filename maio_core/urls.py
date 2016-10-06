"""maio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from maio_core import views

urlpatterns = ([
    url(r'^get/(?P<tn>tn)/(?P<id>[a-zA-Z0-9-]{36})?', views.get_file, name='get_tn'),
    url(r'^get/(?P<id>[a-zA-Z0-9-]{36})?', views.get_file, name='get_file'),
    url(r'^videos/$', views.videos_index, name='videos_index'),
    url(r'^audio/$', views.audio_index, name='audio_index'),
    url(r'^images/rate/(?P<id>[a-zA-Z0-9-]{36})/(?P<rating>[0-5])/?', views.images_rate, name='images_rate'),
    url(r'^images/view/(?P<id>[a-zA-Z0-9-]{36})?', views.images_view, name='images_view'),
    url(r'^images/unset_random/$', views.images_unset_random, name='images_unset_random'),
    url(r'^images/getrandomnext/(?P<id>[a-zA-Z0-9-]{36})', views.images_getrandom_next, name='images_getrandom_next'),
    url(r'^images/getrandomprev/(?P<id>[a-zA-Z0-9-]{36})', views.images_getrandom_prev, name='images_getrandom_prev'),
    url(r'^images/getnext/(?P<id>[a-zA-Z0-9-]{36})', views.images_getnext, name='images_getnext'),
    url(r'^images/getprev/(?P<id>[a-zA-Z0-9-]{36})', views.images_getprev, name='images_getprev'),
    url(r'^images/getthis/(?P<id>[a-zA-Z0-9-]{36})', views.images_getthis, name='images_getthis'),
    url(r'^images/$', views.images_index, name='images_index'),
    url(r'^$', views.home, name='home'),
], 'app')

