# Generated by Django 4.2.4 on 2023-08-26 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Album name')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('album_date', models.DateTimeField(auto_now=True, verbose_name='Album date')),
                ('is_private', models.BooleanField(default=False, verbose_name='Private')),
                ('album_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
                ('signature', models.CharField(max_length=500, verbose_name='Signature')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('is_private', models.BooleanField(default=False, verbose_name='Private')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='webapp.album', verbose_name='Album')),
                ('pic_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fav_albums', to='webapp.album', verbose_name='Fav Album')),
                ('fav_pic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fav_pics', to='webapp.picture', verbose_name='Fav Picture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
