from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.user_login, name="login"),
    path('signup', views.signup, name="signup"),
    path('signup/seeker', views.create_seeker, name="create_seeker"),
    path('signup/employer', views.create_employer, name="create_employer"),
    path('create_account', views.create_account, name="create_account"),
    path('job_details', views.job_details, name="job_details"),
    path('companyProfile', views.companyProfile, name="companyProfile"),
    path('job_search', views.job_search, name="job_search"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('jobs_list', views.jobs_list, name="jobs_list"),
    path('employee_list', views.employee_list, name="employee_list"),
]
