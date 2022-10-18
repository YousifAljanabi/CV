from django.contrib import admin

from .models import User, UserType, Skill, Job, WorkType, EmploymentType, Category
# Register your models here.

admin.register(User)
admin.register(UserType)
admin.register(Skill)
admin.register(Job)
admin.register(WorkType)
admin.register(EmploymentType)
admin.register(Category)