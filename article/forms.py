from django import forms
from .models import Comment
class CommentPostForm(forms.ModelForm):
   class Meta:
       # 指明数据模型来源
       model = Comment
       # 定义表单包含的字段
       fields = ('author', 'email', "body" )