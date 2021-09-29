from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Album


@require_http_methods(["GET"])
def list_album(request, pagesize):
    args = request.GET
    page = int(args['page'])
    query_set = Album.objects.all()
    paginator = Paginator(query_set, pagesize)
    pageinfo = paginator.page(page)
    context = {"pageinfo": pageinfo}
    return render(request, "album/list_album.html", context=context)


@require_http_methods(["GET"])
def show_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    photos = album.photo_set.all()
    context = {"album": album, "photos": photos}
    return render(request, "album/show_album.html", context=context)