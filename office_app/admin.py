from django.contrib import admin
from .models import Department,Role,Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "location"]

class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name","dept","salary","bonus","role","phone","hire_date"]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Employee,EmployeeAdmin)
