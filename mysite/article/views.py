from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Article


@cache_page(60 * 15)
def show_article(request, id: int):
    article = Article.objects.get(id=id)
    context = {"article": article}
    return render(request, "article.html", context)
