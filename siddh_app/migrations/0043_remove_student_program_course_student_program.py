# Generated by Django 4.1.9 on 2024-04-28 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0042_mark_semester_remove_student_program_course_program_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='program_course',
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='siddh_app.program'),
        ),
    ]
