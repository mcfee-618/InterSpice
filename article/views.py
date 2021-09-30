from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post, Category

@require_http_methods(["GET"])
def list_post(request):
    args = request.GET
    page = int(args.get("page", 1))
    posts = Post.objects.all().order_by('-timestamp')
    categories = Category.objects.all()
    paginator = Paginator(posts, 10)
    pageinfo = paginator.page(page)
    context = {"pageinfo": pageinfo, "categories": categories}
    return render(request, "article/list_post.html", context=context)

@require_http_methods(["GET"])
def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    comments = post.comment_set.all()
    context = {"post": post, "categories": categories, "comments": comments}
    return render(request, "article/show_post.html", context=context)
