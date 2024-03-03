from . import views
from django.urls import path


urlpatterns = [
    path('test', views.test, name='home'),
    path('', views.ArticleList.as_view(), name='home'),
    path('events', views.ArticleList.as_view(), name='events'),
]

