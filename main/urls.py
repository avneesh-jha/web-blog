from django.urls import path
from main import views
from django.conf import urls

urlpatterns=[
    path('' , views.index, name = 'index'),
    path('article/<int:pk>', views.article, name ='get_article'),
    path ('author/<int:pk>' , views.author, name='get_author'),
    path ('article' , views.create_article, name='create_article'),
    path ('author' , views.add_author, name='add_author')
]

