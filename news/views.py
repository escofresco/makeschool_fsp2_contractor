from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .models import AnonymousArticle


class ArticleDetailView(DetailView):
    """Shows a page dispaying a specific article."""
    model = AnonymousArticle

    def get(self, request, slug):
        """Hand down that article."""
        article = self.get_queryset().get(slug__iexact=slug)
        return render(request, "pages/article.html", {"article": article})


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = AnonymousArticle.objects.all()
        return context
