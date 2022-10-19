from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test', csrf_exempt(views.test), name="test"),
    path('login', views.user_login, name="login"),
    path('signup', views.signup, name="signup"),
    path('signup/seeker', views.create_seeker, name="create_seeker"),
    path('signup/employer', views.create_employer, name="create_employer"),
    path('create_account', views.create_account, name="create_account"),
    path('job_details', views.job_details, name="job_details"),
    path('companyProfile', views.companyProfile, name="companyProfile"),
]
