
from django.conf.urls import url

import library
from library import views

urlpatterns = [
   url(r'^library/$', library.views.library, name="library")
]