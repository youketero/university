# Generated by Django 3.0.4 on 2020-05-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_edu_plan_specialization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu_plan',
            name='specialization_name',
            field=models.TextField(default='default'),
        ),
    ]
