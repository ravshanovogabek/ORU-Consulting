from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email")  # Admin ro‘yxatda telefon va email ko‘rinadi
    search_fields = ("phone_number", "email")  # Qidiruv
