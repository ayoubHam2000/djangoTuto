from django.shortcuts import render, get_object_or_404, redirect

from django.views import View

from .models import Cource

from .form import CourceModelFrom

class CourseObjectMixin(object):
    model = Cource

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Cource, id = id)
        return obj        

class CourceDeletView(CourseObjectMixin, View):
    template_name = 'cources/cources_delete.html'

    # using CourseObjectMixin
    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Cource, id = id)
    #     return obj
    
    def get(self, request, id = None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Cource, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)            
            
    def post(self, request, id = None, *args, **kwargs):
        context = {}
        obj = get_object_or_404(Cource, id=id)
        obj.delete()
        return redirect('/cources/')

class CourceUpdateView(View):
    template_name = 'cources/cources_update.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Cource, id = id)
        return obj
            
        
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourceModelFrom(instance=obj)
            context['form'] = form
            context['object'] = obj

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourceModelFrom(request.POST, instance=obj)
            if form.is_valid:
                form.save()
                form = CourceModelFrom()
            context['form'] = form
            context['object'] = obj

        return render(request, self.template_name, context)

class CourceCreateView(View):
    template_name = 'cources/cources_create.html'

    def get(self, request, *args, **kwargs):
        form = CourceModelFrom()
        context = {"form" : form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = CourceModelFrom(request.POST)
        if form.is_valid:
            form.save()
            form = CourceModelFrom()

        context = {"form" : form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'cources/cources_list.html'

    def getqueryset(self):
        return Cource.objects.all()

    def get(self, request, *args, **kwargs):
        context = {'object' : self.getqueryset() }
        return render(request, self.template_name, context)

class CourseView(View):
    template_name = "cources/cources_detail.html"

    def get(self, request, id = None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Cource, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)


