# Generated by Django 3.0.4 on 2020-05-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information_block', '0004_auto_20200519_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image_head',
            field=models.ImageField(default='#', upload_to=''),
        ),
    ]
