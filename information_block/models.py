from django.contrib.auth.models import User
from django.db import models
from photologue.models import Photo
# Create your models here.
class Foto_article(models.Model):
    foto = models.ImageField(upload_to="information_block/foto_article")
    foto_id = models.IntegerField(default=1)
    name_foto = models.TextField(max_length=1000, default="enter short description here")

    def __str__(self):
        return "%s %s " % (self.foto_id, self.name_foto)


class Articles(models.Model):
    header_image = models.ManyToManyField(Foto_article)
    title = models.TextField(default="Enter title here")
    image_head = models.ImageField(default="#",upload_to="information_block/article")
    text = models.TextField()
    date = models.DateField()
    link_facebook = models.TextField(default="Enter link here")
    link_telegram = models.TextField(default="Enter link here")
    link_twitter = models.TextField(default="Enter link here")
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return "%s %s " % (self.date, self.header_image)

    def short_text(self):
        if len(self.text) > 100:
            return self.text[:100] + '...'
        else:
            return self.text


class Partner(models.Model):
    name = models.TextField()
    short_information = models.TextField()
    foto_logo = models.ImageField(upload_to="information_block/partner")
    hyper_link_site = models.TextField(default="http")
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s,%s" % (self.name, self.short_information)


class future_conference_anonce(models.Model):
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()
    location = models.TextField(default="/")
    link_facebook = models.TextField(default="Enter link here")
    link_telegram = models.TextField(default="Enter link here")
    link_twitter = models.TextField(default="Enter link here")
    foto = models.ImageField(default="#",upload_to="information_block/conference")
    partner_id = models.ManyToManyField(Partner)

    def __str__(self):
        return "%s,%s" % (self.title, self.date)


class Info(models.Model):
    title = models.TextField(default="Enter title here")
    image_head = models.ImageField(default="#",upload_to="information_block/info")
    text = models.TextField()
    date = models.DateField()
    link_facebook = models.TextField(default="Enter link here")
    link_telegram = models.TextField(default="Enter link here")
    link_twitter = models.TextField(default="Enter link here")
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()