# Generated by Django 4.2.2 on 2023-06-27 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('vibe', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=140)),
                ('song_name', models.CharField(max_length=140)),
                ('album', models.CharField(max_length=140)),
                ('playlist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify_homepage_dummy.playlist')),
            ],
        ),
    ]
