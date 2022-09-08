# Generated by Django 4.0.7 on 2022-08-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_selection', '0005_alter_time_slot_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exam_date',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='exam_day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یکشنبه', 'یکشنبه'), ('دوشنبه', 'دوشنبه'), ('سشنبه', 'سشنبه'), ('چهارشنبه', 'چهارشنبه')], default='شنبه', max_length=10),
        ),
    ]
