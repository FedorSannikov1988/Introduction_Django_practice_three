from django.urls import path
from .views import get_all_articles, \
                   get_all_articles_author_name, \
                   see_article_by_id


urlpatterns = [
    path('get_all_articles', get_all_articles, name='get_all_articles'),
    path('get_all_articles_author_name/<str:author_name>/', get_all_articles_author_name, name='get_all_articles_author_name'),
    path('see_article_by_id/<int:id_article>/', see_article_by_id, name='see_article_by_id'),
]
