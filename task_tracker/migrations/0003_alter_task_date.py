# Generated by Django 4.1.4 on 2022-12-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0002_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]