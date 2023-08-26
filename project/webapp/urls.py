from django.urls import path
from webapp.views import PhotoListViews, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView
from webapp.views.album_views import AlbumView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListViews.as_view(), name='index'),
    path('picture/<int:pk>/', PhotoView.as_view(), name='picture_view'),
    path('picture/create/', PhotoCreateView.as_view(), name='picture_create'),
    path('picture/<int:pk>/update/', PhotoUpdateView.as_view(), name='picture_update'),
    path('picture/<int:pk>/delete/', PhotoDeleteView.as_view(), name='picture_delete'),

    path('album/<int:pk>/', AlbumView.as_view(), name='album_view'),
    path('album/create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
