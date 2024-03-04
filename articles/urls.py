from . import views
from django.urls import path


urlpatterns = [
    path('test', views.test, name='home'),
    path('', views.ArticleList.as_view(), name='home'),
    path('events', views.EventList.as_view(), name='events'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]

