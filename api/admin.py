from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmi(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'city']
