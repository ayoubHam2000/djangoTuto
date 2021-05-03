from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item

from .forms import CreateNewList

def home(request):
    theList = ToDoList.objects.get(id = 1)
    context = {"ls" : theList}
    return render(request, 'mainApp/home.html', context)

def todolist(request, id):
    theList = ToDoList.objects.get(id = id)
    context = {"ls" : theList}

    if request.method == "POST":
        if request.POST.get("save"):
            for item in theList.item_set.all():
                x = request.POST.get(  f'c{item.id}'  )
                if x == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif request.POST.get("newItem") :
            newItemName = request.POST.get("new")
            if len(newItemName) > 2:
                theList.item_set.create(text = newItemName, complete = False)
            else:
                print("Invalide")
    return render(request, 'mainApp/list.html', context)


def create(request):
    if request.method == "POST":
        form = CreateNewList()
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
    else:
        form = CreateNewList()
    context = {
        "form" : form,
    }
    return render(request, 'mainApp/create.html', context)