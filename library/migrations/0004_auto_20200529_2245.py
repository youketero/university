# Generated by Django 3.0.4 on 2020-05-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200529_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library_author',
            name='last_name',
            field=models.TextField(default='enter last name here'),
        ),
    ]
