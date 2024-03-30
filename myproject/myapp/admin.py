from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'stack', 'team_lead']
    list_filter = ['stack', 'team_lead']
    search_fields = ['name', 'surname']

admin.site.register(Employee, EmployeeAdmin)