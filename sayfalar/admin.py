from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','content','date_posted','author']
    list_display_links = list_display
    search_fields = list_display
    list_filter=['date_posted','author']
    class Meta:
        model=Post