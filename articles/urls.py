from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path("about/", include("about.urls"), name="about-urls"),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
]