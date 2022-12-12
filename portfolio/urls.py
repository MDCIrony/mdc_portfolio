from django.urls import path
from . import views

urlpatterns = [
    path('', views.PrincipalView.as_view(), name = 'index'),
]
