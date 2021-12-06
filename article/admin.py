from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comment, Post, Category, Link

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Link)


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'timestamp', 'can_comment', 'category', 'is_private')

    list_filter = ('category', 'is_private')

    list_per_page = 10


class PostAdminForm(forms.ModelForm):
    title = forms.CharField(max_length=60, required=True)
    body = forms.CharField(required=True, widget=CKEditorWidget())
    timestamp = forms.DateTimeField(required=True)
    can_comment = forms.IntegerField(max_value=1, min_value=0, required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    is_private = forms.BooleanField(required=True)

    class Meta:
        model = Post
        fields = '__all__'


admin.site.register(Post, PostAdmin)
