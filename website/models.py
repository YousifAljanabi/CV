from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(TimeStamps):
    name = models.CharField(max_length=32)


class User(AbstractUser, TimeStamps):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    user_type = models.ForeignKey('UserType', on_delete=models.DO_NOTHING, related_name='users', blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    cv_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill)


class UserType(TimeStamps):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, created_at: {self.created_at}, updated_at: {self.updated_at}'


class Job(TimeStamps):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    company = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='published_jobs', blank=True,
                                null=True)
    salary = models.FloatField()
    work_type = models.ForeignKey('WorkType', on_delete=models.DO_NOTHING, related_name='jobs', blank=True, null=True)
    employment_type = models.ForeignKey('EmploymentType', on_delete=models.DO_NOTHING, related_name='jobs', blank=True,
                                        null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='jobs', blank=True, null=True)
    status = models.PositiveSmallIntegerField(default=0)
    deadline = models.DateTimeField()
    required_skills = models.ManyToManyField(Skill)
    applicants = models.ManyToManyField(User)


class WorkType(TimeStamps):
    name = models.CharField(max_length=32)


class EmploymentType(TimeStamps):
    name = models.CharField(max_length=32)


class Category(TimeStamps):
    name = models.CharField(max_length=32)
