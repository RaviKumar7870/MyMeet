# Generated by Django 3.2.3 on 2021-05-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20210521_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='end_time',
            field=models.TimeField(default='17:00:00'),
        ),
        migrations.AlterField(
            model_name='link',
            name='start_time',
            field=models.TimeField(default='08:00:00'),
        ),
    ]
