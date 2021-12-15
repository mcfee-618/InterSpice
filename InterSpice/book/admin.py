from django.contrib import admin
from django.db.models import fields
from .models import Book, BookCategory

admin.site.register(BookCategory)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    fields = ["name", "introduction", "cover", "link", "status"]
    
    list_display = ['name']
