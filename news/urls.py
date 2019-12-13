from django.urls import path

from .views import ArticleDetailView, HomeView
urlpatterns = [

    # home page
    path("", HomeView.as_view(), name="home"),

    # article slug
    path("<str:slug>/",
         ArticleDetailView.as_view(),
         name="news-article-details-page")
]
