# Generated by Django 3.2.3 on 2021-05-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_alter_link_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='end_time',
            field=models.TimeField(default='17:00:00'),
        ),
    ]