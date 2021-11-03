from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from InterSpice.views import BaseView
from .models import Post, Category
from InterSpice.tags import get_range

class PostListView(BaseView):

    def get(self, request, page=1, category_id=0, *args, **kwargs):
        posts = Post.objects
        if category_id:
            posts = posts.filter(category_id=category_id)
        else:
            posts = posts.all()
        posts = posts.order_by('-timestamp')
        categories = Category.objects.all()
        paginator = Paginator(posts, 5)
        pageinfo = paginator.page(page)
        context = {"pageinfo": pageinfo, "categories": categories, "category_id": category_id}
        return self.render(request, "article/list_post.html", context=context)

class PostDetailView(BaseView):
    
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, pk=post_id)
        categories = Category.objects.all()
        comments = post.comment_set.all()
        context = {"post": post, "categories": categories, "comments": comments}
        return self.render(request, "article/detail_post.html", context=context)
