# apps/documents/urls.py
from django.urls import path
from .views import documents_view

urlpatterns = [
    path('', documents_view, name='documents'),
]
