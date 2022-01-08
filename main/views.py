from django.db import reset_queries
from django.http import response
from django.shortcuts import get_object_or_404, render
from main import models

# Create your views here.
def index (request):
    latest_articles =models.Article.objects.all().order_by ('-Created_at')[:10]
    context = {
        'latest_articles': latest_articles
    }
    return render(request ,'main\index.html',context)


def article (request,pk):
    article= models.Article.objects.get(pk = pk)
    context={
        'article': article
    }
    return render(request,'main\post.html',context)


def author(request,pk):
    author= get_object_or_404(models.Author,pk=pk)
    context={
        'author': author
    }
    return render(request,'main\writer.html',context)
    