from django.urls import path

from . import views

urlpatterns = [
    path('<int:pagesize>', views.AlbumListView.as_view(), name='list_album'),
    path('detail/<int:album_id>', views.AlbumDetailView.as_view(), name='show_album')
]
