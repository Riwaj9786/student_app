# Generated by Django 4.1.9 on 2024-04-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0026_alter_programcourse_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programcourse',
            name='semester',
            field=models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII')], default=None, max_length=5, null=True),
        ),
    ]
