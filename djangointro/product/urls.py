from django.urls import path

from .views import (
    product_detail_view,
    product_create_view,
    product_dynamic_view,
    product_dynamic_delete,
    product_list_view
)

app_name = "products"

urlpatterns = [
    path('', product_detail_view),
    path('<int:my_id>/', product_dynamic_view, name = 'product_detail'),
    path('<int:my_id>/delete', product_dynamic_delete, name = 'product'),
    path('list', product_list_view, name = 'product'),
    path('create', product_create_view),
]
