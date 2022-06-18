from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "cp_name"]


@admin.register(Job_Posting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ["id", "jp_position", "jp_compensation"]
