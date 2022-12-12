from django.shortcuts import render, redirect
from django.views.generic import FormView
from .models import Projects
from .forms import NewProjectForm

# Create your views here.
class ProjectCreate(FormView):
    model = Projects
    template_name = 'users/create.html'
    form_class = NewProjectForm

    def form_valid(self,form):
        Projects.objects.create(**form.cleaned_data)
        return redirect('index')