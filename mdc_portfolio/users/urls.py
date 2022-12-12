from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('create/', views.ProjectCreate.as_view(), name = 'create' ),
    path('', views.UserProjectView.as_view(), name = 'index')
]