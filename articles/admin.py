from django.contrib import admin
from .models import Article, Comment, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('is_article','title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status','is_article',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
   

# Register your models here.

admin.site.register(Comment)
admin.site.register(Review)