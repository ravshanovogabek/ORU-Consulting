from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'university', 'created_at')
    search_fields = ('full_name', 'university')
    list_filter = ('university',)
