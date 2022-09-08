# Generated by Django 4.0.7 on 2022-09-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_selection', '0015_alter_course_dept_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_slot',
            name='end',
            field=models.CharField(choices=[('9.5', '9.5'), ('11.5', '11.5'), ('15', '15'), ('17', '17'), ('19', '19')], default='9.5', max_length=10),
        ),
        migrations.AlterField(
            model_name='time_slot',
            name='start',
            field=models.CharField(choices=[('8', '8'), ('10', '10'), ('13.5', '13.5'), ('15.5', '15.5'), ('17.5', '17.5')], default='8', max_length=10),
        ),
    ]