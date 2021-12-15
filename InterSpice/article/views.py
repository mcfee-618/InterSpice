import markdown
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from InterSpice.views import BaseView
from .models import Post, Category
from .forms import CommentPostForm
from InterSpice.tags import get_range


class PostListView(BaseView):
    def get(self, request, page=1, category_id=0, *args, **kwargs):
        keyword = request.GET.get("keyword")
        posts = Post.objects
        categories = Category.objects.all()
        if not request.user.is_authenticated:
            posts = posts.filter(is_private=0)
        if category_id:
            posts = posts.filter(category_id=category_id)
        else:
            posts = posts.all()
        if keyword:
            posts = posts.filter(Q(body__contains=keyword) | Q(title__contains=keyword))
        posts = posts.order_by('-timestamp')
        paginator = Paginator(posts, 5)
        pageinfo = paginator.page(page)
        context = {"pageinfo": pageinfo, "categories": categories, "category_id": category_id}
        if keyword:
            context.update({"keyword": keyword})
        return self.render(request, "article/list_post.html", context=context)


class PostDetailView(BaseView):
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, pk=post_id)
        post.body = markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
        
        categories = Category.objects.all()
        comments = post.comment_set.all()
        context = {"post": post, "categories": categories, "comments": comments}
        return self.render(request, "article/detail_post.html", context=context)


class PostAddCommentView(BaseView):
    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, pk=post_id)
        comment_post_form = CommentPostForm(request.POST)
        if comment_post_form.is_valid():
            new_comment = comment_post_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(reverse("article:detail_post", args=[post.id]))
        return redirect(reverse("article:detail_post", args=[1]))
