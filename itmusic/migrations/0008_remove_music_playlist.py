# Generated by Django 2.2.2 on 2019-11-18 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itmusic', '0007_auto_20191118_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='playlist',
        ),
    ]
