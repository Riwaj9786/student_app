# Generated by Django 4.1.9 on 2024-04-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0006_alter_registration_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registration_number',
            field=models.CharField(default='', editable=False, max_length=15, unique=True),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
