from django.contrib import admin

from .models import ErrorLog, Event


class ErrorLogModelAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'message']


admin.site.register(ErrorLog, ErrorLogModelAdmin)
admin.site.register(Event)
