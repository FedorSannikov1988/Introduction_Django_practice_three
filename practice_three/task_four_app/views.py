from django.shortcuts import render
from task_four_app.models import Article, Author, Comment


def get_all_articles(request):

    articles = Article.objects.all()

    context = {
        "title": "Все статьи из базы данных",
        "articles": articles
    }

    return render(request, "get_all_articles.html", context)


def get_all_articles_author_name(request, author_name: str):

    author = Author.objects.filter(name=author_name).first()

    articles = None

    if author:

        articles = \
            Article.objects.filter(author=
                                   author).order_by('date_publication').all()

    context = {
        "title": "Все статьи автора",
        "author_name": author_name,
        "articles": articles
    }

    return render(request, "get_all_articles_author_name.html", context)


def see_article_by_id(request, id_article: int):

    article = \
        Article.objects.get(pk=id_article)

    article.number_views += 1
    article.save()

    comments = \
        Comment.objects.filter(article=article).order_by('-date_change').all()

    context = {
        "article": article,
        "comments": comments,
    }

    return render(request, "see_article_by_id.html", context)
