# Generated by Django 3.0.4 on 2020-10-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0007_stucture_cathed_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stucture_cathed',
            name='description',
            field=models.TextField(default='empty'),
        ),
        migrations.AlterField(
            model_name='stucture_cathed',
            name='education',
            field=models.TextField(default='empty'),
        ),
        migrations.AlterField(
            model_name='stucture_cathed',
            name='history',
            field=models.TextField(default='empty'),
        ),
    ]
