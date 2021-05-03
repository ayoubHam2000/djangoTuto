from django.urls import path

from .views import home, todolist, create

app_name = "index"

urlpatterns = [
    path('list/<int:id>', todolist, name = 'todolist'),
    path('', home, name = 'home'),
    path('create', create, name = 'create'),
]
