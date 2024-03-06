from django.contrib import admin
from .models import Article, Event, Comment, Review


# Register your models here.
#admin.site.register(About)
admin.site.register(Article)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Review)