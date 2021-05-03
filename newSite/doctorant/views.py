from django.shortcuts import render

from .models import Doctorant, Conference


def home(request):
    docs = Doctorant.objects.all()
    context = {
        "docs" : docs
    }
    return render(request, 'doctorant/home.html', context)

def create(request):
    context = {}
    return render(request, 'doctorant/create.html', context)
