from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Post, Category

@require_http_methods(["GET"])
def list_post(request):
    args = request.GET
    page = int(args.get("page", 1))
    posts = Post.objects.all().order_by('-timestamp')
    categorys = Category.objects.all()
    paginator = Paginator(posts, 10)
    pageinfo = paginator.page(page)
    context = {"pageinfo": pageinfo, "categories": categorys}
    return render(request, "article/list_post.html", context=context)


def show_post(request):
    pass

