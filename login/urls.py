
from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^register/$', views.MyRegisterFormView.as_view(), name="register"),
    url(r'^login/$', views.MyLoginFormView.as_view(), name="login1"),
    #url(r'^password_reset/$', views.MyPasswordResetView.as_view(),name='password_reset_form')
]