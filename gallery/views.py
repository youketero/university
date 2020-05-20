from django.shortcuts import render

# Create your views here.
from photologue.models import Gallery, Photo


def galery(request):
    gallery1 = Gallery.objects.all()
    return render(request, "gallery/gallery.html", locals())


def show_galery(request, header_foto):
    show_galery = Photo.objects.filter(title__startswith=header_foto)
    return render(request, 'gallery/galery_type.html', locals())