from django.urls import path

from api.views import AnonymousArticleList

urlpatterns = [
    path('news/', AnonymousArticleList.as_view(), name='news_list'),
]
