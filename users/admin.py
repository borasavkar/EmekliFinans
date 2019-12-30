from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','image']
    list_display_links = list_display
    search_fields = list_display
    list_filter=['user']
    class Meta:
        model=Profile
