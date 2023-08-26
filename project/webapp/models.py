from django.contrib.auth import get_user_model
from django.db import models

CHOICES = ['public']


# Create your models here.
class Picture(models.Model):
    photo = models.ImageField(verbose_name='Photo', upload_to='img')
    signature = models.CharField(verbose_name='Signature', max_length=500)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    pic_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pictures',
                                   verbose_name='Author')
    album = models.ForeignKey('webapp.Album', related_name='pictures', on_delete=models.CASCADE, verbose_name='Album',
                              null=True, blank=True)
    is_private = models.BooleanField(default=False, verbose_name='Private')

    def __str__(self):
        return f'{self.signature}'


class Album(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Album name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='description')
    album_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='albums',
                                     verbose_name='Author')
    album_date = models.DateTimeField(auto_now=True, verbose_name='Album date')
    is_private = models.BooleanField(default=False, verbose_name='Private')

    def __str__(self):
        return f'{self.name}'

    class Favorite(models.Model):
        user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='users',  verbose_name='User')
        fav_pic = models.ForeignKey('webapp.Picture', on_delete=models.CASCADE, null=True, blank=True, related_name='fav_pics', verbose_name='Fav Picture')
        fav_album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, null=True, blank=True, related_name='fav_albums', verbose_name='Fav Album')

        def __str__(self):
            return f'{self.user}{self.fav_pic}{self.fav_album}'
