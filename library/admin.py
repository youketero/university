from django.contrib import admin

# Register your models here.
from library.models import library_author, library_book

admin.site.register(library_book)
admin.site.register(library_author)