from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('book_info/list/<int:page>/<int:category_id>/', views.BookListView.as_view(), name='list_book'),
]