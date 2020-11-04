# Generated by Django 3.0.4 on 2020-10-22 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0011_auto_20201004_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='structure_cv_files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_name', models.FileField(default='#', upload_to='')),
                ('person_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.structure_person')),
            ],
        ),
    ]
