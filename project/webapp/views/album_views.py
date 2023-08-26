from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Picture, Album, Favorite
from webapp.forms import PhotoForm, AlbumForm


class AlbumView(LoginRequiredMixin, DetailView):
    template_name = 'album/album_view.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture = self.object.pictures.all()
        pictures = picture.filter(is_private=False).order_by('-created_date')
        context['pictures'] = pictures
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = "album/album_create.html"
    model = Album
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.album_author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.pk})


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "album/album_update.html"
    model = Album
    form_class = AlbumForm
    context_object_name = 'album'
    permission_required = 'webapp.change_album'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.pk})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'album/album_delete.html'
    model = Album
    context_object_name = 'album'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user
