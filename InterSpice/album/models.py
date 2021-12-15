from django.db import models


class Album(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now=True)
    tag = models.CharField(max_length=200, null=True, blank=True)
    is_private = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name}:{str(self.pub_date)}"


class Photo(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    source = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='album', null=True)
