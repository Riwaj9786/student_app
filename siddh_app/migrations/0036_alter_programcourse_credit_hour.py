# Generated by Django 4.1.9 on 2024-04-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0035_alter_programcourse_credit_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programcourse',
            name='credit_hour',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]