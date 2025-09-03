from django.contrib import admin

from .models import Department, HOD, Professor, Students

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(HOD)
class HODAdmin(admin.ModelAdmin):
    list_display = ('name', 'Department', 'phone')
    search_fields = ('name', 'Department__name', 'phone')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'Department', 'Subject')
    search_fields = ('name', 'phone', 'Department__name', 'Subject')

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'Register_ID', 'Department', 'HOD')
    search_fields = ('name', 'Register_ID', 'Department__name', 'HOD__name')

