# Generated by Django 4.0.7 on 2022-08-16 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_selection', '0011_alter_course_dept_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unit_selection.departemant'),
        ),
    ]
