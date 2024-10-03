from django.views.generic import TemplateView
from django.urls import path


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class RulesPageView(TemplateView):
    template_name = "pages/rules.html"


app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("rules/", RulesPageView.as_view(), name="rules"),
]
