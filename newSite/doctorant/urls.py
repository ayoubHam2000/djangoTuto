from django.urls import path

from .views import (
    home,
    create
)

app_name = 'doctorant'

urlpatterns = [
    path('', home, name = 'home'),
    path('create', create, name = 'create'),
]