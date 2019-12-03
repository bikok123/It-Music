# Generated by Django 2.2.2 on 2019-11-12 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itmusic', '0002_auto_20191112_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='artist_image/')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itmusic.Artist'),
        ),
    ]