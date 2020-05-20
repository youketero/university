from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import logout

import gallery
import gallery.views

urlpatterns = [
    url(r'^galery/$', gallery.views.galery, name='galery'),
    url(r'^galery/(?P<header_foto>.*)/$', gallery.views.show_galery, name="foto_gallery"),
]
