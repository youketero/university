from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class library_author(models.Model):
    first_name = models.TextField(default="enter first name here")
    last_name = models.TextField(default="enter last name here")

    def __str__(self):
        return "%s,%s" % (self.first_name, self.last_name)


class library_book(models.Model):
    name = models.TextField(default="enter name of the book")
    author_id = models.ManyToManyField(library_author)
    foto = models.ImageField(upload_to='information_block/static/img', default="#")
    link_for_download = models.FileField(default="enter hyper link here", upload_to="information_block/static/docs")
    published_in = models.DateField()
    type_of_book = models.TextField(default="enter type of book")
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)