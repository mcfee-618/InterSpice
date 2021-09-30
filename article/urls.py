from django.urls import path

from . import views

urlpatterns = [
    path('post/list/', views.list_post, name='list_post'),
    path('post/show/<int:post_id>', views.show_post, name='list_show'),
]