from django.shortcuts import render

# Create your views here.
from library.models import library_book


def library(request):
    books = library_book.objects.all()
    return render(request, "library/library.html", locals())