from django.contrib import admin
from .models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created")
    list_filter = ("created",)
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
