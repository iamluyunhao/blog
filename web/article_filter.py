from rest_framework import filters
import django_filters
from backweb.models import Article


class ArticleFilter(filters.FilterSet):
    keyword = django_filters.CharFilter('title', lookup_expr='contains')

    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'content', 'category']
