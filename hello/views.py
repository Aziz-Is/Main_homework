from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Tracker
from .forms import MyForm
from django.db.models import Q
from django.utils.http import urlencode
from .forms import Search
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(ListView):
    model = Tracker
    template_name = "index.html"
    context_object_name = "trackers"
    paginated_by = 10

    def get(self,request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request,*args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Tracker.objects.filter()
        return Tracker.objects.all().order_by("-updated_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] =self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            print(query)
            context['query'] = query
        return  context

    def get_search_form(self):
        return Search(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data("search")



class MainpageView(TemplateView):
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tracker.objects.all()
        print(context)
        return context


class DetailView(TemplateView):
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Tracker.objects.get(pk=context['pk'])
        print(context)
        return context

class AddView(LoginRequiredMixin, TemplateView):
    template_name = 'add.html'
    form = MyForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_form'] = self.form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            types = form.cleaned_data.pop('tracker_type')
            new_tracker = Tracker.objects.create(summary=form.cleaned_data['summary'], description=form.cleaned_data['description'],
                                   status=form.cleaned_data['status'])
            new_tracker.tracker_type.set(types)
            return redirect('home')
        return render(request, 'add.html', {'my_form': form})

class UpdateView(TemplateView):
    template_name = 'add.html'
    form = MyForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Tracker.objects.get(pk=context['pk'])
        context['my_form'] = self.form(initial={'summary':obj.summary, 'description': obj.description, 'status':obj.status, 'type':obj.tracker_type.all()})
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            obj = Tracker.objects.get(pk=kwargs['pk'])
            obj.summary = form.cleaned_data['summary']
            obj.description = form.cleaned_data['description']
            obj.status = form.cleaned_data['status']
            obj.tracker_type.set(types)
            obj.save()
            return redirect('home')
        return render(request, 'add.html',{'my_form':form})

class DeleteView(TemplateView):
    template_name = 'delete.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Tracker.objects.get(pk=context['pk'])
        context['task'] = obj
        return context
    def post(self, request, *args, **kwargs):
        obj = Tracker.objects.get(pk=kwargs['pk'])
        if obj:
            obj.delete()
            return redirect('home')
        return render (request,'delete.html', {'task':obj})