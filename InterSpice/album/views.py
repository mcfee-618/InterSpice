from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Album
from InterSpice.views import BaseView

class AlbumListView(BaseView):
    
    def get(self, request, page, *args, **kwargs):
        args = request.GET
        page = int(args['page'])
        query_set = Album.objects.all()
        paginator = Paginator(query_set, pagesize)
        pageinfo = paginator.page(page)
        context = {"pageinfo": pageinfo}
        return self.render(request, "album/list_album.html", context=context)


class AlbumDetailView(BaseView):
    
    def get(self, request, album_id, *args, **kwargs):
        album = get_object_or_404(Album, pk=album_id)
        photos = album.photo_set.all()
        context = {"album": album, "photos": photos}
        return self.render(request, "album/show_album.html", context=context)