# Generated by Django 4.1.9 on 2024-04-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0002_alter_student_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
