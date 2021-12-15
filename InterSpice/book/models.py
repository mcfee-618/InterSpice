from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


    
class BookCategory(models.Model):

    name = models.CharField(unique=True, max_length=30, blank=True, null=False)
    
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    
    status_choices = (
        (0, '未阅'),
        (1, '已阅'),
    )

    name = models.CharField(unique=True, max_length=100, blank=True, null=False)

    introduction = RichTextUploadingField(blank=True, null=True, config_name="my-custom-toolbar")

    cover = models.ImageField(null=True, upload_to="book")

    link = models.CharField(max_length=255, blank=True, null=False)

    status = models.IntegerField(null=False, choices=status_choices)
    
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    category = models.ForeignKey(BookCategory, models.DO_NOTHING, default=None, related_name="books")
    
    def __str__(self) -> str:
        return self.name
