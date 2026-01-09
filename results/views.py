from django.shortcuts import render
from .models import Result

def results(request):
    results = Result.objects.all()
    return render(request, 'results/results.html', {'results': results})
