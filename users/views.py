from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .models import Projects
from .forms import NewProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProjectCreate(LoginRequiredMixin, FormView):
    model = Projects
    template_name = 'users/create.html'
    form_class = NewProjectForm

    def form_valid(self,form):
        Projects.objects.create(**form.cleaned_data)
        return redirect('index')

class UserProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'
    extra_context = {'projects' : Projects.objects.all()}

def deleteProject(request, id):
    classroom = Projects.objects.get(id=id)
    classroom.delete()
    return redirect('index')
    