from ckeditor_uploader import fields
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=True, null=True)
    
    class Meta:
        managed = False
        
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("list_post")
         


class Post(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    can_comment = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    is_private = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __str__(self) -> str:
        return f"{str(self.category)}_{self.title}"
        

class Comment(models.Model):
    author = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    from_admin = models.IntegerField(blank=True, null=True)
    reviewed = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    replied = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = False
    
    def __str__(self) -> str:
        return self.body

 
        