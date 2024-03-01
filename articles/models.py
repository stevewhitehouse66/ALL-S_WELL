from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="article_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
        ordering = ["-created_on"]


def __str__(self):
    return f"The title of this post is {self.title}"


def __str__(self):
    return f"{self.title} | written by {self.author}"

class Review(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="review")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()


class Meta:
        ordering = ["created_on"]

def __str__(self):
    return f"Comment {self.body} by {self.author}"


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