from django.conf.urls import url

import entrance
from entrance import views

urlpatterns = [
    url(r'^vstup/$', entrance.views.vstup, name="vstup"),
    url(r'^vstup/(?P<id>.*)/$', entrance.views.vstup_info, name="vstup_info"),
]