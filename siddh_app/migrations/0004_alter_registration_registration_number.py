# Generated by Django 4.1.9 on 2024-04-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0003_alter_student_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registration_number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
