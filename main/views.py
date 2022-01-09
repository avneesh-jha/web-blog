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
    

def create_article(request):
    #print(request.POST)
    authors=models.Author.objects.all()
    context={
        'authors':authors
    }

    if request.method=="POST":
        article_data ={
            'content': request.POST['content'],
            'title': request.POST['title'],
            }
        article=models.Article.objects.create(**article_data)
        author_data=models.Author.objects.filter(pk=request.POST['author'])
        article.authors.set(author_data)
        #author=models.Author.objects.filter(pk=request.POST['author'])
        #article.authors.set(author)
        
        context["success"]=True
        

    
    return render(request,'main\create_article.html',context)




def add_author(request):
    #print(request.POST)
    authors=models.Author.objects.all()
    context={
        'authors':authors
    }

    if request.method=="POST":
        author_data ={
            'name': request.POST['name'],
            
            }
        author=models.Author.objects.create(**author_data)
       # author_data=models.Author.objects.filter(pk=request.POST['author'])
        #article.authors.set(author_data)
        #author=models.Author.objects.filter(pk=request.POST['author'])
        #article.authors.set(author)
        
        context["success"]=True
        

    
    return render(request,'main\_author.html', context)



