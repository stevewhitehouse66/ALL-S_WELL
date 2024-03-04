from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('events', views.EventList.as_view(), name='events'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
]

