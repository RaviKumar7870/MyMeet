# Generated by Django 3.2.3 on 2021-05-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20210521_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='end_time',
            field=models.TimeField(blank=True, default='17:00:00', null=True),
        ),
    ]