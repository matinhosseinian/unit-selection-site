# Generated by Django 4.0.7 on 2022-08-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_selection', '0006_course_exam_date_course_exam_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='exam_day',
        ),
        migrations.AddField(
            model_name='course',
            name='exam_time',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
