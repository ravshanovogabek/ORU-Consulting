# apps/documents/views.py
from django.shortcuts import render
from .models import Document

def documents_view(request):
    documents = Document.objects.all()
    return render(request, "documents/documents.html", {"documents": documents})
