from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('signup/seeker', views.createSeeker, name="createSeeker"),
    path('signup/employer', views.createEmployer, name="createEmployer"),
    path('createAccount', views.createAccount, name="createAccount"),
    path('jobDetails', views.jobDetails, name="jobDetails"),
    path('companyProfile', views.companyProfile, name="companyProfile"),
    


]
