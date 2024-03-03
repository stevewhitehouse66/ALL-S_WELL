from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Article

# Create your views here.


def test(request):
    return HttpResponse("Hello, world, this is a test")
    

class ArticleList(ListView):
    template_name = "articles.html"
    paginate_by = 6
    

    def get_queryset(self):
        return Article.objects.filter(Q(status=1) & Q(is_article=1))

class EventList(ListView):
    template_name = "articles.html"
    paginate_by = 1

    def get_queryset(self):
        return Article.objects.filter(Q(status=1) & Q(is_article=0))

"""def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})
"""