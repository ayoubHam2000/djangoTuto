from django.http import HttpResponse
from django.shortcuts import render

#request in the first was in args
#HttpResponse("<h1>Hello World</h1>") 
#print(request.user)

def home_view(request, *args, **kwargs):    
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "this is about me",
        "title" : "Title",
        "number" : 123,
        "list" : [1, 2, 3, 4],
        "html" : "<h1>Html text with safe filter </h1>"
    }
    return render(request, "about.html", my_context)

