from django.db import models
from django.db.models.base import Model

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=256)
    #articles=models.ManyToManyField('Article')

    def __str__(self):
        return self.name


class Article(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    Created_at=models.DateTimeField(auto_now_add=True)

    authors=models.ManyToManyField('Author')

    def __str__(self):
        return self.title