from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article, Event


# Create your views here.


class ArticleList(ListView):
    """
    Display a list of :model:`article.Article`

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
    Display a list of :model:`event.Events`

    **Context**

    ``event``
        An instance of :model:`event.Event`.

    **Template:**

    :template:`events.html`
    """
    queryset = Event.objects.filter(status=1)
    template_name = "articles/events.html"


def article_detail(request, slug):
    """
    Display an individual :model:`article.Post`.

    **Context**

    ``article``
        An instance of :model:`article.Post`.

    **Template:**

    :template:`article_detail.html`
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
    Display an individual :model:`event.Post`.

    **Context**

    ``event``
        An instance of :model:`event.Post`.

    **Template:**

    :template:`event_detail.html`
    """
    
    queryset = Event.objects.filter()
    event = get_object_or_404(queryset, slug=slug)
    print("Retrieved event:", event)
    reviews = event.review.all().order_by("-created_on")
    print("Retrieved reviews:", reviews)
    review_count = event.review.filter(approved=True).count()
    print("These are the review objects: ", reviews)
    return render(
        request,
        "articles/event_detail.html",
        {"event": event,
        "reviews": reviews,
        "review_count": review_count,
        },
    )

