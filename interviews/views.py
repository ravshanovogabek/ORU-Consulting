from django.shortcuts import render
from .models import Interview

def interviews(request):
    videos = Interview.objects.all()
    return render(request, 'interviews/interviews.html', {'videos': videos})
