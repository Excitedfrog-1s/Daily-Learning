from . import models
from django.shortcuts import render


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'article': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
