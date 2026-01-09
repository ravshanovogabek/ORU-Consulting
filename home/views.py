from django.shortcuts import render
from .models import HomeBanner, SocialMediaCard

def home_view(request):
    banner = HomeBanner.objects.first()
    social_cards = SocialMediaCard.objects.all()
    return render(request, 'home/home.html', {'banner': banner, 'social_cards': social_cards})
