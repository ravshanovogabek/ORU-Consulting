from .models import SiteSettings, SocialMediaCard

def site_settings(request):
    return {
        'site': SiteSettings.objects.first(),
        'social_cards': SocialMediaCard.objects.all()
    }
