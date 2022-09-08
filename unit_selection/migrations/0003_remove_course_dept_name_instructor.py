# Generated by Django 4.0.7 on 2022-08-16 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_selection', '0002_remove_course_code_section_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='dept_name',
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_selection.departemant')),
            ],
        ),
    ]
