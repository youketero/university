# Generated by Django 3.0.4 on 2020-10-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_stucture_cathed_foto_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='stucture_cathed',
            name='education',
            field=models.TextField(default='enter eduation here'),
        ),
    ]
