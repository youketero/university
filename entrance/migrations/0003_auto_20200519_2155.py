# Generated by Django 3.0.4 on 2020-05-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0002_auto_20200324_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrance_specialization_way',
            name='duration_of_study',
            field=models.IntegerField(default=1.0),
        ),
    ]
