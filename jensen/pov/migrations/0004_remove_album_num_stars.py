# Generated by Django 4.1.1 on 2022-09-28 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pov', '0003_alter_album_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='num_stars',
        ),
    ]
