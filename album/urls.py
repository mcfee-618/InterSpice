from django.urls import path

from . import views

urlpatterns = [
    path('<int:pagesize>', views.list_album, name='list_album'),
    path('show/<int:album_id>', views.show_album, name='show_album')
]
