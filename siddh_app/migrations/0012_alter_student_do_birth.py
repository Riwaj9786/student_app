# Generated by Django 4.1.9 on 2024-04-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0011_student_registration_number_alter_faculty_faculty_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='do_birth',
            field=models.DateField(),
        ),
    ]
