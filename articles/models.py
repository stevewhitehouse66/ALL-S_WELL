from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
IS_ARTICLE = ((0, "Article"), (1, "Event"))
RATING = ((1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars"))
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="article_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    is_article = models.IntegerField(choices=IS_ARTICLE, default=0)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        if (self.is_article == 0):
            return f"Article: {self.title} | written by {self.author}"
        else:
            return f"Event: {self.title} | posted by {self.author}"
            
class Review(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="review")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=1)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Review {self.body} by {self.author}"


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"    