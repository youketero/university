# Generated by Django 3.0.4 on 2020-06-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_auto_20200606_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure_laboratory',
            name='foto',
            field=models.ImageField(upload_to='structure/laboratory'),
        ),
        migrations.AlterField(
            model_name='structure_person',
            name='foto',
            field=models.ImageField(default='#', upload_to='structure_person'),
        ),
        migrations.AlterField(
            model_name='stucture_cathed',
            name='foto',
            field=models.ImageField(upload_to='structure/cathed'),
        ),
    ]
