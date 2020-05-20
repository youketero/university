"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from photologue.sitemaps import PhotoSitemap, GallerySitemap

from university import settings
from information_block.views import handler404


handler404 = handler404

sitemaps = {'photologue_galleries': GallerySitemap,
            'photologue_photos': PhotoSitemap,
            }


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include("information_block.urls")),
    url(r'^', include("login.urls")),
    url(r'^', include("library.urls")),
    url(r'^', include("structure.urls")),
    url(r'^', include("learning.urls")),
    url(r'^', include("entrance.urls")),
    url(r'^', include("gallery.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

]\
    + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)