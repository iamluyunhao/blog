from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from backweb.models import Article, Category

from rest_framework import mixins, viewsets

from web.article_filter import ArticleFilter
from web.article_serializer import ArticleSerializer


class ArticleView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_class = ArticleFilter


def index(request):
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
        category = Category.objects.all()
        articles = Article.objects.all()
        paginator = Paginator(articles, 8)
        page = paginator.page(page_num)
        id = page[0].id
        return render(request, 'web/index.html', {'page': page, 'id': id, 'category': category})


def list(request):
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
        category = Category.objects.all()
        articles = Article.objects.all()
        paginator = Paginator(articles, 8)
        page = paginator.page(page_num)
        id = page[0].id
        return render(request, 'web/list.html', {'page': page, 'id': id, 'category': category})


def category_list(request, g_id):
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
        c_gory = Category.objects.filter(id=g_id)
        category = Category.objects.all()
        articles = Article.objects.filter(category=g_id)
        paginator = Paginator(articles, 8)
        page = paginator.page(page_num)
        id = page[0].id
        c_gory = c_gory[0].name
        return render(request, 'web/category_list.html', {'page': page, 'id': id, 'category': category, 'c_gory': c_gory})


def about(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'web/about.html', {'category': category})


def info(request, id):
    if request.method == 'GET':
        category = Category.objects.all()
        article = Article.objects.get(pk=id)
        return render(request, 'web/info.html', {'article': article, 'category': category})