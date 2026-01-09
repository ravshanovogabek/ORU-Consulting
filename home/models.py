from django.db import models

class HomeBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Izoh matni")
    background_image = models.ImageField(upload_to='home_banners/', verbose_name="Fon rasmi")

    def __str__(self):
        return self.title

class SocialMediaCard(models.Model):
    name = models.CharField(max_length=100, verbose_name="Platforma nomi (masalan: Instagram)")
    icon = models.ImageField(upload_to='social_icons/', verbose_name="Ikonka (rasm)")
    link = models.URLField(verbose_name="Havola")
    bg_color = models.CharField(max_length=50, verbose_name="Fon rangi (masalan: bg-pink-500 yoki bg-gradient-to-r from-rose-500 to-pink-500)")
    text_color = models.CharField(max_length=50, default="text-white", verbose_name="Matn rangi (masalan: text-white)")

class SiteSettings(models.Model):
    title = models.CharField(max_length=255, default="StudyToKorea")
    name = models.CharField(max_length=100, default="StudyToKorea")
    favicon = models.ImageField(upload_to='icons/', blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    footer_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.name
