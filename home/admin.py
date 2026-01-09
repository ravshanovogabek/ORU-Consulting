from django.contrib import admin
from .models import HomeBanner, SocialMediaCard, SiteSettings


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')


@admin.register(SocialMediaCard)
class SocialMediaCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'bg_color', 'text_color')
    search_fields = ('name', 'link')
    list_filter = ('bg_color', 'text_color')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
