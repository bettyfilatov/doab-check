"""doab_check URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('providers/', views.ProvidersView.as_view(), name='providers'),
    path('providers/<str:provider>/', views.ProviderView.as_view(), name='provider'),
]