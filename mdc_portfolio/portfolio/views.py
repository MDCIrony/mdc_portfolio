from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class PrincipalView(TemplateView):
    template_name = 'portfolio/index.html'#html