from rest_framework.views import APIView
from rest_framework.response import Response

from news.models import AnonymousArticle
from api.serializers import AnonymousArticleSerializer

class AnonymousArticleList(APIView):
    def get(self, request):
        questions = AnonymousArticle.objects.all()[:20]
        data = AnonymousArticleSerializer(questions, many=True).data
        return Response(data)
