# Generated by Django 3.0.4 on 2020-06-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0005_auto_20200524_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrance_specialization',
            name='foto',
            field=models.ImageField(default='#', upload_to='entrance/specialization'),
        ),
    ]