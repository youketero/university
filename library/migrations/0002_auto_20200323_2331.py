# Generated by Django 3.0.4 on 2020-03-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library_book',
            name='foto',
            field=models.ImageField(default='#', upload_to='information_block/static/img'),
        ),
        migrations.AlterField(
            model_name='library_book',
            name='link_for_download',
            field=models.FileField(default='enter hyper link here', upload_to='information_block/static/docs'),
        ),
    ]
