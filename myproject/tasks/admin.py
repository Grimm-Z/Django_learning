from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Publication)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "data")
    list_filter = ("name", "data")
    search_fields = ("name", "description", "data")

@admin.register(Commentary)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "data")
    list_filter = ("name", "data")
    search_fields = ("name", "text", "data")