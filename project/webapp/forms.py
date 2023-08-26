from django import forms
from webapp.models import Picture, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['photo', 'signature', 'is_private']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'description', 'is_private']
