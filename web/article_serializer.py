from rest_framework import serializers

from backweb.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'desc', 'content', 'icon']