# Generated by Django 3.0.4 on 2020-03-24 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='edu_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_plan_doc', models.FileField(upload_to='web/static/docs')),
                ('cource', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='subject_edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_name', models.TextField(default='enter name of subject here')),
                ('code', models.TextField(default='OK 1')),
                ('count_credits', models.IntegerField(default='2')),
                ('form_control', models.TextField(default='Іспит')),
                ('cathed_specialization', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.stucture_cathed')),
            ],
        ),
        migrations.CreateModel(
            name='edu_prog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.TextField(default='Українська')),
                ('credit_sum', models.IntegerField(default=240)),
                ('specialization_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning.edu_plan')),
                ('subject_edu_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning.subject_edu')),
            ],
        ),
    ]
