from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article, Event


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
    queryset = Article.objects.filter(status=1)
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
    queryset = Event.objects.filter(status=1)
    template_name = "events/events.html"


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
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()
    return render(
        request,
        "articles/article_detail.html",
        {"article": article,
        "comments": comments,
        "comment_count": comment_count,}
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
    queryset = Event.objects.filter()
    event = get_object_or_404(queryset, slug=slug)
    reviews = event.reviews.all().order_by("-created_on")
    review_count = event.reviews.filter(approved=True).count()
    print("These are the review objects: ", reviews)
    return render(
        request,
        "events/event_detail.html",
        {"event": event,
        "reviews": reviews,
        "review_count": review_count,
        },
    )