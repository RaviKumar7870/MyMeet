# Generated by Django 3.2.3 on 2021-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_name', models.CharField(max_length=100)),
                ('meeting_link', models.URLField(max_length=100)),
                ('start_time', models.TimeField(default='08:00:00')),
                ('end_time', models.TimeField(default='17:00:00')),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
            ],
        ),
    ]
