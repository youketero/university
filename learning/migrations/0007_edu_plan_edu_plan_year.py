# Generated by Django 3.0.4 on 2020-10-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_auto_20200606_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='edu_plan',
            name='edu_plan_year',
            field=models.IntegerField(default='2000', max_length=4),
        ),
    ]
