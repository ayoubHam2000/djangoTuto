from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = "blog"

urlpatterns = [
    path("", ArticleListView.as_view(), name = 'article_list'),
    path("<int:my_id>", ArticleDetailView.as_view(), name = 'article_detail'),
    path("create/", ArticleCreateView.as_view(), name = 'article_create'),
    path("<int:my_id>/update/", ArticleUpdateView.as_view(), name = 'article_update'),
    path("<int:my_id>/delete/", ArticleDeleteView.as_view(), name = 'article_delete'),
]