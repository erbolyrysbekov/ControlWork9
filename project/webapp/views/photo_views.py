from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Picture, Album, Favorite
from webapp.forms import PhotoForm


class PhotoListViews(LoginRequiredMixin, ListView):
    template_name = 'pictures/pictures_list.html'
    context_object_name = 'pictures'
    model = Picture
    ordering = ['-created_date']

    def get_queryset(self):
        return Picture.objects.filter(Q(is_private=False) & (Q(album__isnull=True) | Q(album__is_private=False)))


class PhotoView(LoginRequiredMixin, DetailView):
    template_name = 'pictures/picture_view.html'
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = Favorite.objects.filter(fav_pic=self.object).values_list('user', flat=True)
        context['users'] = get_user_model().objects.filter(id__in=users)
        return context


class PictureView(View):
    def photo_detail(self, token):
        picture = get_object_or_404(Picture, token=token)
        context = {'picture': picture}

        return render(self, 'pictures/picture_view.html', context)

    def generate_access_link(self, picture_id):
        picture = get_object_or_404(Picture, id=picture_id)
        access_link = picture.generate_access_link()
        return redirect('pictures/picture_view.html', token=str(picture.token))


#
#
class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "pictures/picture_create.html"
    model = Picture
    form_class = PhotoForm

    def form_valid(self, form):
        form.instance.pic_author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:picture_view', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['photo'].queryset = Album.objects.filter(album_author=self.request.user)
        return form


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "pictures/picture_update.html"
    model = Picture
    form_class = PhotoForm
    context_object_name = 'picture'
    permission_required = 'webapp.change_picture'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["photo"].queryset = Album.objects.filter(album_author=self.request.user)
        return form

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:picture_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'pictures/picture_delete.html'
    model = Picture
    context_object_name = 'picture'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user
