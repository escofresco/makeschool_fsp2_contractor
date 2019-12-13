from rest_framework.serializers import ModelSerializer

from news.models import AnonymousArticle

class AnonymousArticleSerializer(ModelSerializer):
    class Meta:
        model = AnonymousArticle
        fields = '__all__'
