# Generated by Django 2.2.2 on 2019-11-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itmusic', '0006_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='playlist',
        ),
        migrations.AddField(
            model_name='music',
            name='playlist',
            field=models.ManyToManyField(null=True, to='itmusic.Playlist'),
        ),
    ]
