# Generated by Django 4.1.9 on 2024-04-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0037_alter_programcourse_credit_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programcourse',
            name='credit_hour',
            field=models.PositiveIntegerField(default=3, null=True),
        ),
    ]
