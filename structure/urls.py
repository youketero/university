
from django.conf.urls import url

import structure
from structure import views

urlpatterns = [
    url(r'^structure/$', structure.views.structure, name='cathed'),
    url(r'^teacher/(?P<teacher>.*)/$', structure.views.teacher, name="teacher"),
    url(r'^structure/(?P<cathed_name>.*)/$', structure.views.cathed_b, name='cathed_name'),
    #url(r'^password_reset/$', views.MyPasswordResetView.as_view(),name='password_reset_form')
]