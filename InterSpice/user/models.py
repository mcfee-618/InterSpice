from django.db import models

# Create your models here.
import os.path
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from django.conf import settings
from django.utils import timezone

class UserProfile(models.Model):
    
    cover = models.ImageField(null=True)
    content = RichTextField(unique=True, max_length=1000, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self) -> str:
        return self.content[:20]