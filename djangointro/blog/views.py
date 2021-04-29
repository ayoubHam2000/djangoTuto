from django.shortcuts import render,get_object_or_404, redirect

from .models import Article

from .forms import ArticleModelForm

from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    #override the pk id into my_id
    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id = id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id = id_)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()

    def get_success_url(self):
        return reverse("blog:article_list")

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id = id_)

