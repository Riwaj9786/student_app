# Generated by Django 4.1.9 on 2024-04-25 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0009_remove_student_registration_number_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='siddh_app.student'),
        ),
    ]
