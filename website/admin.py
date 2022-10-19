from django.contrib import admin

# Register your models here.
from .models import User, UserType, Skill, Job, WorkType, EmploymentType, Category


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class EmploymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


admin.site.register(User)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(EmploymentType, EmploymentTypeAdmin)
admin.site.register(Category)
