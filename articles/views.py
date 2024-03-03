from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

# Create your views here.


def test(request):
    return HttpResponse("Hello, world, this is a test")
    

class ArticleList(ListView):
    queryset = Article.objects.filter(status=1, is_article=0)
    template_name = "articles/articles.html"



class EventList(ListView):
    queryset = Article.objects.filter(status=1, is_article=1)
    template_name = "articles/events.html"



"""
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})
"""