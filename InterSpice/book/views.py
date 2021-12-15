from django.shortcuts import render
from .models import Book, BookCategory
from django.core.paginator import Paginator
from InterSpice.views import BaseView

class BookListView(BaseView):
    
    def get(self, request, page=1, category_id=0):
        book_categories = BookCategory.objects.all()
        books = Book.objects.all()
        if category_id:
            books = books.filter(category_id=category_id)
        books.order_by("-timestamp")
        paginator = Paginator(books, per_page=5)
        pageinfo = paginator.page(page)
        context = {
            "book_categories": book_categories,
            "pageinfo": pageinfo
        }
        return self.render(request, "book/list_book.html", context=context)