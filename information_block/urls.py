from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import logout

import information_block.views

urlpatterns = [
    url(r'^$', information_block.views.home, name="home"),
    url(r'^article/(?P<article_title>.*)/$', information_block.views.show_articles, name='article'),
    url(r'^anonce/$', information_block.views.anonce1, name="anonce"),
    url(r'^anonce/(?P<anonce_id>.*)/$', information_block.views.anonce_detail, name='anonce_detail'),
    url(r'^news/$', information_block.views.news, name="news"),
    url(r'^partner/$', information_block.views.partneru, name="partner"),
    url(r'^contact/$', information_block.views.contact, name="contact"),
    url(r'^info/$', information_block.views.info, name="info"),
    url(r'^info_for_students/$', information_block.views.info_for_students, name="info_for_students"),
    url(r'^info_for_students_detailed/(?P<info_title>.*)/$', information_block.views.info_detailed, name="info_for_students_detailed"),
    url(r'^search_result/$', information_block.views.search.as_view(), name="search"),
]
