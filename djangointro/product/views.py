from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import ProductForm, RawProductForm
from .models import Product


# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     mycontext = {
#         "form" : form
#     }
#     return render(request, "products/product_form.html", mycontext)

# def product_create_view(request):
#     if request.method == 'POST':
#         print(request.POST.get('title'))
#     mycontext = {}
#     return render(request, "products/product_form.html", mycontext)

def product_list_view(request):
    objs = Product.objects.all()
    context = {
        "objs" : objs
    }
    return render(request, "products/product_list.html", context)

def product_dynamic_delete(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    if request.method == "POST" :
        print("--> delete : ", my_id)
        obj.delete()
        return redirect("../../")
    context = {}
    return render(request, "products/product_delete.html", context)

def product_dynamic_view(request, my_id):
    #obj = Product.objects.get(id = my_id)
    obj = get_object_or_404(Product, id = my_id)
    # try:
    #     obj = Product.objects.get(id = my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "object" : obj
    }
    return render(request, "products/product_details.html", context)


def product_create_view(request):
    initial_data = {
        'title' : 'initail title'
    }
    #to edit an exist product just get the product
    #obj = Product.objects.get(id = 1)
    #than add instance = obj argument to ProfuctForm 
    form = ProductForm(request.POST or None, initial = initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    mycontext = {
        'form' : form
    }
    return render(request, "products/product_form.html", mycontext)

def product_detail_view(request):
    obj = Product.objects.get(id = 2)
    mycontext = {
        'object' : obj
    }
    return render(request, "products/product_details.html", mycontext)