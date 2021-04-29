from django.urls import path


from .views import (
    CourseView,
    CourseListView,
    CourceCreateView,
    CourceUpdateView,
    CourceDeletView
)

app_name = "cources"

urlpatterns = [
    path("", CourseListView.as_view(), name = 'cources_list'),
    path("create/", CourceCreateView.as_view(), name = 'cources_create'),
    path("<int:id>/update", CourceUpdateView.as_view(), name = 'cources_update'),
    path("<int:id>/delete", CourceDeletView.as_view(), name = 'cources_delete'),
    path("<int:id>/", CourseView.as_view(template_name = 'cources/cources_detail.html'), name = 'cources_detail'),
]