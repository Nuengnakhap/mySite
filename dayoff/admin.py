from django.contrib import admin
# Register your models here.
from dayoff.models import DayOff

class DayOffAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'type', 'reason', 'date_start', 'date_end', 'approve_status']
    list_editable = ['approve_status']
    list_filter = ['created_by', 'date_start', 'date_end', 'approve_status']
    list_per_page = 20

admin.site.register(DayOff, DayOffAdmin)