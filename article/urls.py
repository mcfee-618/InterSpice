from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('post/list/<int:page>/<int:category_id>', views.PostListView.as_view(), name='list_post'),
    path('post/detail/<int:post_id>', views.PostDetailView.as_view(), name='detail_post'),
    path('post/addcomment/<int:post_id>', views.PostAddCommentView.as_view(), name='add_comment'),
]