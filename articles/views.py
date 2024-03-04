from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article


# Create your views here.


class ArticleList(ListView):
    """
    Display a list of :model:`article.Article` filtered by is_article =1.

    **Context**

    ``article``
        An instance of :model:`article.Article`.

    **Template:**

    :template:`article/articles.html`
    """
    queryset = Article.objects.filter(status=1, is_article=1)
    template_name = "articles/articles.html"


class EventList(ListView):
    """
    Display a list of :model:`article.Article` filtered by is_article =0.

    **Context**

    ``article``
        An instance of :model:`article.Article`.

    **Template:**

    :template:`article/events.html`
    """
    queryset = Article.objects.filter(status=1, is_article=0)
    template_name = "articles/events.html"


def article_detail(request, slug):
    """
    Display an individual :model:`article.Post`.

    **Context**

    ``article``
        An instance of :model:`article.Post`.

    **Template:**

    :template:`article/article_detail.html`
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "articles/article_detail.html",
        {"article": article},
    )

def event_detail(request, slug):
    """
    Display an individual :model:`article.Post`.

    **Context**

    ``article``
        An instance of :model:`article.Post`.

    **Template:**

    :template:`article/article_detail.html`
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "articles/event_detail.html",
        {"article": article},
    )