# Generated by Django 2.2.2 on 2019-11-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itmusic', '0005_auto_20191117_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_image/'),
        ),
    ]
