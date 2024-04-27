# Generated by Django 4.1.9 on 2024-04-26 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siddh_app', '0016_department_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_id', models.CharField(max_length=12, unique=True)),
                ('program_name', models.CharField(max_length=35)),
                ('courses', models.ManyToManyField(related_name='departments', to='siddh_app.course')),
                ('faculty', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='siddh_app.faculty')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='depart',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='siddh_app.program'),
        ),
    ]