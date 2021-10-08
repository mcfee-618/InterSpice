from django.urls import path

from . import views

urlpatterns = [
    path('post/list/<int:page>/<int:category_id>', views.PostListView.as_view(), name='list_post'),
    path('post/detail/<int:post_id>', views.PostDetailView.as_view(), name='detail_post'),
]