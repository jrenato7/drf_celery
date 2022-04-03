from django.contrib import admin

from .models import ErrorLog, Event


class ErrorLogModelAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'message']


class EventModelAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'category', 'name', 'timestamp']


admin.site.register(ErrorLog, ErrorLogModelAdmin)
admin.site.register(Event, EventModelAdmin)
