from django.contrib import admin
from .models import Task
# Register your models here.@admin.register(Task)
@admin.register(Task)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "assigned_to")
    list_filter = ("status", "assigned_to")
    search_fields = ("status", "assigned_to")
